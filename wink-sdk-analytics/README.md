# wink-sdk-analytics
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

### Test API

 - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.

### Common APIs

- [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account.
- [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.

### Consume APIs
Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.

 - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.
 - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.
 - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..
 - [Booking](/booking): All APIs related to creating bookings on the platform.
 - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.

 ### Produce APIs
 Produce endpoints are for developers who want to create and manage travel inventory.

 #### Property
 - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.
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

 #### Rate provider
 - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.

 ### Taxonomy APIs
 Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.

 - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.

 ### Insight APIs
 Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.

 - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.

 ### Payment APIs
 Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.

 - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.

 ## SDKs
 We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).

 - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)

 ## Usage
 These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.

 ## Versioning
 We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.

 ## Release history
 - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md


# Analytics API
Welcome to the Affiliate API - A programmer-friendly way to get insight into platform-level activities and bookings.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.17.14
- Package version: 0.0.36
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_analytics
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.36#egg=wink_sdk_analytics&subdirectory=wink-sdk-analytics
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.36#egg=wink_sdk_analytics&subdirectory=wink_sdk_analytics`)

Then import the package:
```python
import wink_sdk_analytics
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_analytics
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_analytics
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    upsert_chart_request_authenticated_entity = wink_sdk_analytics.UpsertChartRequestAuthenticatedEntity() # UpsertChartRequestAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Chart
        api_response = api_instance.create_chart_request(upsert_chart_request_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->create_chart_request:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsApi->create_chart_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsApi* | [**create_chart_request**](docs/AnalyticsApi.md#create_chart_request) | **POST** /api/analytics/chart | Create Chart
*AnalyticsApi* | [**remove_chart_request**](docs/AnalyticsApi.md#remove_chart_request) | **DELETE** /api/analytics/chart/{chartIdentifier} | Remove Chart
*AnalyticsApi* | [**show_analytics_grid**](docs/AnalyticsApi.md#show_analytics_grid) | **POST** /api/analytics/grid | Show Analytics Grid
*AnalyticsApi* | [**show_analytics_list**](docs/AnalyticsApi.md#show_analytics_list) | **GET** /api/analytics/list | Show Analytics
*AnalyticsApi* | [**show_chart_request**](docs/AnalyticsApi.md#show_chart_request) | **GET** /api/analytics/chart/{chartIdentifier} | Show Chart
*AnalyticsApi* | [**show_chart_requests**](docs/AnalyticsApi.md#show_chart_requests) | **GET** /api/analytics/chart/list | Show Charts
*AnalyticsApi* | [**update_chart_request**](docs/AnalyticsApi.md#update_chart_request) | **PUT** /api/analytics/chart/{chartIdentifier} | Update Chart
*LeaderboardApi* | [**show_leaderboard**](docs/LeaderboardApi.md#show_leaderboard) | **POST** /api/analytics/leaderboard/list | Show Leaderboard by Region
*LeaderboardApi* | [**show_leaderboard_by_owner**](docs/LeaderboardApi.md#show_leaderboard_by_owner) | **POST** /api/analytics/leaderboard | Show Leaderboard by Affiliate 


## Documentation For Models

 - [AggregateDescriptorNonAuthenticatedEntity](docs/AggregateDescriptorNonAuthenticatedEntity.md)
 - [BookingLeaderboardEntryNonAuthenticatedEntity](docs/BookingLeaderboardEntryNonAuthenticatedEntity.md)
 - [ChartAuthenticatedEntity](docs/ChartAuthenticatedEntity.md)
 - [ChartCategoryAxisNonAuthenticatedEntity](docs/ChartCategoryAxisNonAuthenticatedEntity.md)
 - [ChartDetailsAuthenticatedEntity](docs/ChartDetailsAuthenticatedEntity.md)
 - [ChartLegendNonAuthenticatedEntity](docs/ChartLegendNonAuthenticatedEntity.md)
 - [ChartSeriesNonAuthenticatedEntity](docs/ChartSeriesNonAuthenticatedEntity.md)
 - [ChartTitleNonAuthenticatedEntity](docs/ChartTitleNonAuthenticatedEntity.md)
 - [CompositeFilterDescriptorNonAuthenticatedEntity](docs/CompositeFilterDescriptorNonAuthenticatedEntity.md)
 - [FilterDescriptorNonAuthenticatedEntity](docs/FilterDescriptorNonAuthenticatedEntity.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GroupDescriptorNonAuthenticatedEntity](docs/GroupDescriptorNonAuthenticatedEntity.md)
 - [KeyValuePairAuthenticatedEntity](docs/KeyValuePairAuthenticatedEntity.md)
 - [LeaderboardOwnerRequestNonAuthenticatedEntity](docs/LeaderboardOwnerRequestNonAuthenticatedEntity.md)
 - [LeaderboardRequestNonAuthenticatedEntity](docs/LeaderboardRequestNonAuthenticatedEntity.md)
 - [LineChartNonAuthenticatedEntity](docs/LineChartNonAuthenticatedEntity.md)
 - [PageBookingLeaderboardEntryNonAuthenticatedEntity](docs/PageBookingLeaderboardEntryNonAuthenticatedEntity.md)
 - [PageLineChartNonAuthenticatedEntity](docs/PageLineChartNonAuthenticatedEntity.md)
 - [PageableObjectNonAuthenticatedEntity](docs/PageableObjectNonAuthenticatedEntity.md)
 - [RemoveEntryResponseAuthenticatedEntity](docs/RemoveEntryResponseAuthenticatedEntity.md)
 - [ShowChartRequest400Response](docs/ShowChartRequest400Response.md)
 - [SortDescriptorNonAuthenticatedEntity](docs/SortDescriptorNonAuthenticatedEntity.md)
 - [SortObjectNonAuthenticatedEntity](docs/SortObjectNonAuthenticatedEntity.md)
 - [StateNonAuthenticatedEntity](docs/StateNonAuthenticatedEntity.md)
 - [UpsertChartRequestAuthenticatedEntity](docs/UpsertChartRequestAuthenticatedEntity.md)


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


