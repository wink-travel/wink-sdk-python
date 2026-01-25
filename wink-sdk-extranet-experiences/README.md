# wink-sdk-extranet-experiences
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


# Extranet Experiences API
This part of the documentation concerns itself with the management of experiences, on and off the property. This API lets you create:

1. Activities: Manage activities on and off the premises.
2. Attractions: Manage attractions on and off the premises.
3. Places: Manage places on and off the premises.

Browse the endpoints in the left navigation bar to get started.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.31.5
- Package version: 0.0.63
- Generator version: 7.18.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_experiences
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.63#egg=wink_sdk_extranet_experiences&subdirectory=wink-sdk-extranet-experiences
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.63#egg=wink_sdk_extranet_experiences&subdirectory=wink_sdk_extranet_experiences`)

Then import the package:
```python
import wink_sdk_extranet_experiences
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_extranet_experiences
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Persist activity owned by this property identifier
    upsert_activity_request = wink_sdk_extranet_experiences.UpsertActivityRequest() # UpsertActivityRequest | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Activity
        api_response = api_instance.create_activity(property_identifier, upsert_activity_request, wink_version=wink_version)
        print("The response of ActivityApi->create_activity:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivityApi->create_activity: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivityApi* | [**create_activity**](docs/ActivityApi.md#create_activity) | **POST** /api/property/{propertyIdentifier}/experience/activity | Create Activity
*ActivityApi* | [**remove_activity**](docs/ActivityApi.md#remove_activity) | **DELETE** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Delete Activity
*ActivityApi* | [**show_activities**](docs/ActivityApi.md#show_activities) | **GET** /api/property/{propertyIdentifier}/experience/activity/list | Show Activities
*ActivityApi* | [**show_activity**](docs/ActivityApi.md#show_activity) | **GET** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Show Activity
*ActivityApi* | [**show_activity_pairs**](docs/ActivityApi.md#show_activity_pairs) | **GET** /api/property/{propertyIdentifier}/experience/activity/list/pair | Show Activities as key/value pairs
*ActivityApi* | [**update_activity**](docs/ActivityApi.md#update_activity) | **PUT** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Update Activity
*ActivityApi* | [**upload_activity_media**](docs/ActivityApi.md#upload_activity_media) | **POST** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier}/multimedia | Upload Binary Multimedia
*AttractionApi* | [**create_attraction**](docs/AttractionApi.md#create_attraction) | **POST** /api/property/{propertyIdentifier}/experience/attraction | Create Attraction
*AttractionApi* | [**remove_attraction**](docs/AttractionApi.md#remove_attraction) | **DELETE** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Delete attraction
*AttractionApi* | [**show_attraction**](docs/AttractionApi.md#show_attraction) | **GET** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Show Attraction
*AttractionApi* | [**show_attraction_pairs**](docs/AttractionApi.md#show_attraction_pairs) | **GET** /api/property/{propertyIdentifier}/experience/attraction/list/pair | Show Attractions as Pairs
*AttractionApi* | [**show_attractions**](docs/AttractionApi.md#show_attractions) | **GET** /api/property/{propertyIdentifier}/experience/attraction/list | Show Attractions
*AttractionApi* | [**update_attraction**](docs/AttractionApi.md#update_attraction) | **PUT** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Update Attraction
*AttractionApi* | [**upload_attraction_media**](docs/AttractionApi.md#upload_attraction_media) | **POST** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier}/multimedia | Upload Binary Multimedia
*PlaceApi* | [**create_place**](docs/PlaceApi.md#create_place) | **POST** /api/property/{propertyIdentifier}/experience/place | Create Place
*PlaceApi* | [**remove_place**](docs/PlaceApi.md#remove_place) | **DELETE** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Delete Place
*PlaceApi* | [**show_place**](docs/PlaceApi.md#show_place) | **GET** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Show Place
*PlaceApi* | [**show_place_pairs**](docs/PlaceApi.md#show_place_pairs) | **GET** /api/property/{propertyIdentifier}/experience/place/list/pair | Show Reference Pairs
*PlaceApi* | [**show_places**](docs/PlaceApi.md#show_places) | **GET** /api/property/{propertyIdentifier}/experience/place/list | Show Places
*PlaceApi* | [**update_place**](docs/PlaceApi.md#update_place) | **PUT** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Update Place
*PlaceApi* | [**upload_place_media**](docs/PlaceApi.md#upload_place_media) | **POST** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier}/multimedia | Upload Binary Multimedia


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [Attraction](docs/Attraction.md)
 - [ContactSupplier](docs/ContactSupplier.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [DowPatternGroupSupplier](docs/DowPatternGroupSupplier.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoJsonPointSupplier](docs/GeoJsonPointSupplier.md)
 - [KeyValuePair](docs/KeyValuePair.md)
 - [KeyValuePairSupplier](docs/KeyValuePairSupplier.md)
 - [MediaAuthorAttributionSupplier](docs/MediaAuthorAttributionSupplier.md)
 - [PlaceSupplier](docs/PlaceSupplier.md)
 - [ShowPlace400Response](docs/ShowPlace400Response.md)
 - [SimpleAddressSupplier](docs/SimpleAddressSupplier.md)
 - [SimpleDescriptionSupplier](docs/SimpleDescriptionSupplier.md)
 - [SimpleMultimediaSupplier](docs/SimpleMultimediaSupplier.md)
 - [SocialSupplier](docs/SocialSupplier.md)
 - [TransactionalTravelInventorySupplier](docs/TransactionalTravelInventorySupplier.md)
 - [TravelInventoryRecognitionSupplier](docs/TravelInventoryRecognitionSupplier.md)
 - [UpsertActivityRequest](docs/UpsertActivityRequest.md)
 - [UpsertAttractionRequest](docs/UpsertAttractionRequest.md)
 - [UpsertPlaceRequestSupplier](docs/UpsertPlaceRequestSupplier.md)
 - [UpsertSimpleDescriptionSupplier](docs/UpsertSimpleDescriptionSupplier.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oauth2ClientCredentials"></a>
### oauth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: https://iam.wink.travel/oauth2/authorize
- **Scopes**: 
 - **inventory.read**: Read Wink data
 - **inventory.write**: Create Wink data
 - **inventory.remove**: Remove Wink data


## Author

bjorn@wink.travel

