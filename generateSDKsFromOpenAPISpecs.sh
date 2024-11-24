#!/bin/bash

#
# Copyright (c) 2024. wink.travel. All rights Reserved.
# Responsibility:
# Generates python SKD's for each listed OpenAPI spec
#

# Exit immediately if a command exits with a non-zero status
set -e

# Determine environment (dev, staging, or production)
env="${1:-production}"

# Set base URLs based on the environment
case "$env" in
  dev)
    wink_url="https://dev-api.wink.travel:8443"
    integrations_url="https://dev-integrations.wink.travel:8445"
    ;;
  staging)
    wink_url="https://staging-api.wink.travel"
    integrations_url="https://staging-integrations.wink.travel"
    ;;
  *)
    wink_url="https://api.wink.travel"
    integrations_url="https://integrations.wink.travel"
    ;;
esac

# Function to read the current version
get_current_version() {
  if [ -f VERSION ]; then
    cat VERSION
  else
    echo "0.0.1"  # Default if VERSION file is missing
  fi
}

# Function to update the VERSION file
update_version_file() {
  local new_version="$1"
  echo "$new_version" > VERSION
}

# Get current version
current_version=$(get_current_version)

# Get the new version number
new_version=$(npx git-changelog-command-line \
  --print-next-version \
  --major-version-pattern BREAKING \
  --minor-version-pattern feat)

echo "Current version: $current_version"
echo "New version: $new_version"

# Add the new version to VERSION file.
update_version_file $new_version

# Function to generate SDK from OpenAPI spec
generate_sdk() {
  local api_url="$1"
  local package_name="$2"
  local project_name="$3"
  local package_url="$4"

  echo "Generating $package_name..."

  # Health check
  if ! curl -s -I "$api_url" | grep -qi "Content-Type:.*application/json"; then
    echo "Invalid URL or content type for $api_url"
    exit 1
  fi

  additional_props="projectName=$project_name,packageName=$package_name,packageVersion=$new_version,packageUrl=$package_url"
  
  # Generate the SDK
  openapi-generator generate \
    -g python \
    --artifact-id $package_name \
    --artifact-version $new_version \
    --git-host github.com \
    --git-user-id wink-travel \
    --git-repo-id wink-sdk-python \
    --http-user-agent wink-sdk-python \
    -i "$api_url" \
    -o "$project_name" \
    -t ".openapi-generator/templates/" \
    --additional-properties="$additional_props"

  # Add the license file
  cp LICENSE $project_name/LICENSE

  echo "SDK generation for $package_name complete"
}

# Function to convert API names to snake_case for package names
to_snake_case() {
  local input="$1"
  # Replace hyphens with underscores
  input="${input//-/_}"
  # Convert to lowercase
  echo "${input,,}"
}

# Generate SDK configs and SDK's
generate_all() {
  local baseUrl="$1"
  shift  # Shift the arguments so that "$@" contains only the APIs
  local apis=("$@")  # Capture all remaining arguments as an array

  for api in "${apis[@]}"; do
    api_url="$baseUrl/v3/api-docs/$api"
    package_name="wink_sdk_$(to_snake_case $api)"
    project_name="wink-sdk-$api"
    package_url="https://github.com/wink-travel/wink-sdk-python.git"

    generate_sdk "$api_url" "$package_name" "$project_name" "$package_url"
  done
}

# List of APIs using wink_url
wink_apis=(
  "affiliate"
  "affiliate-browse"
  "affiliate-inventory"
  "affiliate-sales-channel"
  "affiliate-winklinks"
  "analytics"
  "booking"
  "engine-client"
  "extranet-booking"
  "extranet-distribution"
  "extranet-experiences"
  "extranet-facilities"
  "extranet-monetize"
  "extranet-property"
  "extranet-property-register"
  "inventory"
  "lookup"
  "notification"
  "ping"
  "reference"
  "travel-agent"
  "user-settings"
)

# List of APIs using integrations_url
integrations_apis=(
  "channel-manager"
)

# Generate SDKs for APIs using wink_url
generate_all "$wink_url" "${wink_apis[@]}" 

# Generate SDKs for APIs using integrations_url
generate_all "$integrations_url" "${integrations_apis[@]}" 

echo "All SDKs generated successfully."

echo $new_version
