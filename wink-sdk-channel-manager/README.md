# wink-sdk-channel-manager
 # Introduction
 Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.
 Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.

 # Integrations
 We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.

 # Intended Audience
 Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.
 - Hotel chains
 - Hotel brands
 - Travel tech companies
 - Destination sites
 - Integrators
 - Aggregators
 - Destination management companies
 - Travel agencies
 - OTAs

 ## APIs
 Not every integrator needs every API. For that reason, we have separated APIs into context.

### Common APIs

- [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.
- [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.
- [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to.
- [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account.
- [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features.
- [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work.
- [Reference](/reference): All APIs related to retrieving platform-supported taxonomies.
- [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.

### Consumer APIs

Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.

 - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.
 - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.
 - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..
 - [Booking](/booking): All APIs related to creating bookings on the platform.
 - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.

### Supplier APIs

Produce endpoints are for developers who want to create and manage travel inventory.

#### Property

- [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.
- [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.
- [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.
- [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.
- [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.
- [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.
- [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.

#### Affiliate

- [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.
- [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.
- [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.
- [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.
- [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.

## SDKs

We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).

### Inventory

 - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)
 - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)

### Payment

- Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java)
- Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)

## Usage

These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.

## Versioning

We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.

Current version: `2.0`
Prior versions: None


# Channel Manager API
Wink exposes a secured REST-based, JSON API to its channel manager partners. The connection is \"channel-wide\". Partners are free to integrate with the REST-based API using any programming language.

# Intended Audience
This document is intended for external channel partners who wish to integrate with Wink.

# Requirements
- Active account with Wink. Sign up for your Channel Manager account:
   - Staging: [https://staging-studio.wink.travel](https://staging-studio.wink.travel).
   - Production: [https://studio.wink.travel](https://studio.wink.travel).
- Active application. An application provides you with Oauth2 credentials you can pass to our endpoints. One is already created for you upon account creation.
- Your production IP numbers. They need to be whitelisted before you can talk to our production environment.

# Performance
A particular attention to performance should be given when integrating with this API. A few things to be aware of:
- Enable gzip compression to make payloads smaller.
- Fewer large REST calls are preferred to many small ones. E.g. It is better to update many dates instead of individual dates.
- It is possible to update both rate and availability with a single request.
- Request only date ranges that you will use. There is no need to request an entire year if you will only be working with the first seven days.

## Reservation notification (PUSH)
Wink supports PUSH notifications to communicate reservations. We also support BASIC AUTH to your endpoint. If you want to enable PUSH, add your PUSH endpoint and credentials (optional) to your account.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.31.2
- Package version: 0.0.61
- Generator version: 7.18.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_channel_manager
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.61#egg=wink_sdk_channel_manager&subdirectory=wink-sdk-channel-manager
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.61#egg=wink_sdk_channel_manager&subdirectory=wink_sdk_channel_manager`)

Then import the package:
```python
import wink_sdk_channel_manager
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_channel_manager
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_channel_manager
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Say Hello
        api_response = api_instance.ping(wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->ping:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelManagerApi->ping: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://integrations.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChannelManagerApi* | [**ping**](docs/ChannelManagerApi.md#ping) | **GET** /api/channel-manager/ping | Say Hello
*ChannelManagerApi* | [**show_properties**](docs/ChannelManagerApi.md#show_properties) | **GET** /api/channel-manager/property/list | Show Properties
*ChannelManagerApi* | [**show_property**](docs/ChannelManagerApi.md#show_property) | **GET** /api/channel-manager/property/{propertyIdentifier} | Show Property
*ChannelManagerApi* | [**show_property_booking**](docs/ChannelManagerApi.md#show_property_booking) | **GET** /api/channel-manager/property/{propertyIdentifier}/booking/{bookingIdentifier} | Show Booking
*ChannelManagerApi* | [**show_property_bookings**](docs/ChannelManagerApi.md#show_property_bookings) | **GET** /api/channel-manager/property/{propertyIdentifier}/booking/list | Show Bookings
*ChannelManagerApi* | [**show_property_room_rates**](docs/ChannelManagerApi.md#show_property_room_rates) | **GET** /api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier} | Show Daily Rates
*ChannelManagerApi* | [**update_rates**](docs/ChannelManagerApi.md#update_rates) | **PUT** /api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier} | Update Daily Rates


## Documentation For Models

 - [ChannelManagerProperty](docs/ChannelManagerProperty.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [PageChannelManagerProperty](docs/PageChannelManagerProperty.md)
 - [PageableObject](docs/PageableObject.md)
 - [PingResponse](docs/PingResponse.md)
 - [PropertyBooking](docs/PropertyBooking.md)
 - [PropertyRate](docs/PropertyRate.md)
 - [PropertyRateUpdateRequest](docs/PropertyRateUpdateRequest.md)
 - [PropertyRoomRate](docs/PropertyRoomRate.md)
 - [PropertyRoomRateWithRateList](docs/PropertyRoomRateWithRateList.md)
 - [PropertyWithRoomRateList](docs/PropertyWithRoomRateList.md)
 - [ShowPropertyRoomRates400Response](docs/ShowPropertyRoomRates400Response.md)
 - [SortObject](docs/SortObject.md)
 - [VariableCharge](docs/VariableCharge.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oAuth2ClientCredentials"></a>
### oAuth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: https://iam.wink.travel/oauth2/authorize
- **Scopes**: 
 - **integrations.read**: Read Wink data
 - **integrations.write**: Create Wink data
 - **integrations.remove**: Remove Wink data


## Author

bjorn@wink.travel

