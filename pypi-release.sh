#!/bin/bash

#
# pypi-release.sh
#
# Uploads all SDKs in subfolders to PyPI.
#

# Exit immediately if a command exits with a non-zero status
set -e

###############################################################################
# Configuration
###############################################################################

# PyPI Configuration
PYPI_REPO_URL="https://upload.pypi.org/legacy/"  # Use TestPyPI for testing

# SDK Directories
SDK_BASE_DIR="."                     # Base directory containing SDK subfolders
SDK_PREFIX="wink-sdk-"                # Prefix to identify SDK subfolders

###############################################################################
# Functions
###############################################################################

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

# Function to build and upload SDK to PyPI
build_and_upload_sdk() {
  local sdk_dir="$1"

  echo "Processing SDK: $sdk_dir"

  # Navigate to the SDK directory
  cd "$sdk_dir"

  # Check for setup.py
  if [ -f "setup.py" ]; then
    build_command="python setup.py sdist bdist_wheel"
    upload_command="twine upload --repository-url $PYPI_REPO_URL dist/*"
  else
    echo "No setup.py found in $sdk_dir. Skipping PyPI upload."
    cd -
    return
  fi

  echo "Building the package in $sdk_dir..."
  # Install build tools if not already installed
  pip install --upgrade pip setuptools wheel twine build

  # Build the distribution packages
  $build_command

  echo "Uploading the package to PyPI for $sdk_dir..."
  # Upload using twine
  $upload_command || { echo "Failed to upload $sdk_dir to PyPI."; cd -; exit 1; }

  echo "Package for $sdk_dir uploaded to PyPI successfully."

  # Navigate back to the base directory
  cd -
}

# Function to find all SDK subfolders
find_all_sdks() {
  echo "Scanning for SDK subfolders with prefix '$SDK_PREFIX'..."
  SDK_LIST=$(find "$SDK_BASE_DIR" -maxdepth 1 -type d -name "${SDK_PREFIX}*" | sort)

  if [[ -z "$SDK_LIST" ]]; then
    error "No SDK subfolders found with prefix '$SDK_PREFIX'."
  fi

  echo "Found SDKs:"
  echo "$SDK_LIST"
}

###############################################################################
# Main Script Execution
###############################################################################

echo "=== PyPI Release Process Initiated ==="

# Find all SDK subfolders
find_all_sdks

# Iterate over each SDK and build/upload to PyPI
for sdk in $SDK_LIST; do
  build_and_upload_sdk "$sdk"
done

echo "=== PyPI Release Process Completed Successfully ==="