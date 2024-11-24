# wink-sdk-affiliate-sales-channel
 # Introduction
 Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.
 Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.

 # Integrations
 We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.

 # Intended Audience
 Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.
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
Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.

 - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.
 - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.
 - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..
 - [Booking](/booking): All APIs related to creating bookings on the platform.
 - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.

 ### Produce APIs
 Produce endpoints are for developers who want to create and manage travel blocking.

 #### Property
 - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.
 - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.
 - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.
 - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.
 - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.
 - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.
 - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.

 #### Affiliate
 - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.
 - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.
 - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.
 - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.
 - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.

 #### Rate provider
 - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.

 ### Taxonomy APIs
 Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.

 - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.

 ### Insight APIs
 Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.

 - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.

 ### Payment APIs
 Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.

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



# Sales Channel API
The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. This API lets you:

1. Sales Channel: Manage existing sales channels.
2. Relationship Request: Manage relationship requests.
3. Available Supplier: Browse available suppliers to connect with.

Browse the endpoints in the left navigation bar to get started.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.7.10
- Package version: 0.0.3
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate_sales_channel
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_affiliate_sales_channel&subdirectory=wink-sdk-affiliate-sales-channel
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_affiliate_sales_channel&subdirectory=wink_sdk_affiliate_sales_channel`)

Then import the package:
```python
import wink_sdk_affiliate_sales_channel
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_affiliate_sales_channel
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    company_identifier = 'company_identifier_example' # str | The company ID to show suppliers for
    state_affiliate = wink_sdk_affiliate_sales_channel.StateAffiliate() # StateAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Supplier Search
        api_response = api_instance.browse_suppliers(company_identifier, state_affiliate, wink_version=wink_version)
        print("The response of AvailableSupplierApi->browse_suppliers:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AvailableSupplierApi->browse_suppliers: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AvailableSupplierApi* | [**browse_suppliers**](docs/AvailableSupplierApi.md#browse_suppliers) | **POST** /api/affiliate/{companyIdentifier}/supplier/grid | Supplier Search
*AvailableSupplierApi* | [**show_latest_supplier**](docs/AvailableSupplierApi.md#show_latest_supplier) | **GET** /api/affiliate/{companyIdentifier}/supplier/list | Recent Supplier List
*AvailableSupplierApi* | [**show_supplier**](docs/AvailableSupplierApi.md#show_supplier) | **GET** /api/affiliate/{companyIdentifier}/supplier/{supplierIdentifier} | Show Supplier
*AvailableSupplierApi* | [**show_unique_city_list**](docs/AvailableSupplierApi.md#show_unique_city_list) | **GET** /api/affiliate/{companyIdentifier}/supplier/city/list | Cities by Supplier
*AvailableSupplierApi* | [**show_unique_country_list**](docs/AvailableSupplierApi.md#show_unique_country_list) | **GET** /api/affiliate/{companyIdentifier}/supplier/country/list | Countries by Supplier
*RelationshipRequestApi* | [**create_supplier_request**](docs/RelationshipRequestApi.md#create_supplier_request) | **POST** /api/affiliate/{companyIdentifier}/sales-channel/request | Create Supplier Request
*RelationshipRequestApi* | [**re_apply_supplier_request**](docs/RelationshipRequestApi.md#re_apply_supplier_request) | **GET** /api/affiliate/{companyIdentifier}/sales-channel/request/{salesChannelRequestIdentifier}/re-apply | Re-apply Supplier Request
*RelationshipRequestApi* | [**remove_supplier_request**](docs/RelationshipRequestApi.md#remove_supplier_request) | **DELETE** /api/affiliate/{companyIdentifier}/sales-channel/request/{salesChannelRequestIdentifier} | Delete Relationship Request
*RelationshipRequestApi* | [**show_supplier_request**](docs/RelationshipRequestApi.md#show_supplier_request) | **GET** /api/affiliate/{companyIdentifier}/sales-channel/request/supplier/{supplierIdentifier} | Show Supplier Request
*RelationshipRequestApi* | [**show_supplier_requests**](docs/RelationshipRequestApi.md#show_supplier_requests) | **GET** /api/affiliate/{companyIdentifier}/sales-channel/request/list | Show Supplier Requests
*SalesChannelApi* | [**browse_sales_channels**](docs/SalesChannelApi.md#browse_sales_channels) | **POST** /api/affiliate/{companyIdentifier}/sales-channel/grid | Sales Channel Search
*SalesChannelApi* | [**show_sales_channel**](docs/SalesChannelApi.md#show_sales_channel) | **GET** /api/affiliate/{companyIdentifier}/sales-channel/supplier/{supplierIdentifier} | Show Sales Channel


## Documentation For Models

 - [AddressAffiliate](docs/AddressAffiliate.md)
 - [AggregateDescriptorAffiliate](docs/AggregateDescriptorAffiliate.md)
 - [BrowseSuppliers400Response](docs/BrowseSuppliers400Response.md)
 - [CompositeFilterDescriptorAffiliate](docs/CompositeFilterDescriptorAffiliate.md)
 - [ContactAffiliate](docs/ContactAffiliate.md)
 - [CountryAffiliate](docs/CountryAffiliate.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [FilterDescriptorAffiliate](docs/FilterDescriptorAffiliate.md)
 - [GeneralManagerAffiliate](docs/GeneralManagerAffiliate.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoJsonPointAffiliate](docs/GeoJsonPointAffiliate.md)
 - [GeoNameAffiliate](docs/GeoNameAffiliate.md)
 - [GroupDescriptorAffiliate](docs/GroupDescriptorAffiliate.md)
 - [HotelOnMapAffiliate](docs/HotelOnMapAffiliate.md)
 - [HotelOnMapViewAffiliate](docs/HotelOnMapViewAffiliate.md)
 - [ImageAttributionAffiliate](docs/ImageAttributionAffiliate.md)
 - [KeyValuePairAffiliate](docs/KeyValuePairAffiliate.md)
 - [LocalizedDescriptionAffiliate](docs/LocalizedDescriptionAffiliate.md)
 - [PageHotelOnMapViewAffiliate](docs/PageHotelOnMapViewAffiliate.md)
 - [PageSalesChannelViewAffiliate](docs/PageSalesChannelViewAffiliate.md)
 - [PageableObjectAffiliate](docs/PageableObjectAffiliate.md)
 - [PropertyPolicyAffiliate](docs/PropertyPolicyAffiliate.md)
 - [RateModifierAffiliate](docs/RateModifierAffiliate.md)
 - [RateModifierBundleAffiliate](docs/RateModifierBundleAffiliate.md)
 - [RemoveEntryResponse](docs/RemoveEntryResponse.md)
 - [SalesChannelAffiliate](docs/SalesChannelAffiliate.md)
 - [SalesChannelRelationshipRequest](docs/SalesChannelRelationshipRequest.md)
 - [SalesChannelRelationshipRequestAffiliate](docs/SalesChannelRelationshipRequestAffiliate.md)
 - [SalesChannelRelationshipRequestView](docs/SalesChannelRelationshipRequestView.md)
 - [SalesChannelRelationshipRequestViewAffiliate](docs/SalesChannelRelationshipRequestViewAffiliate.md)
 - [SalesChannelViewAffiliate](docs/SalesChannelViewAffiliate.md)
 - [SimpleDescriptionAffiliate](docs/SimpleDescriptionAffiliate.md)
 - [SimpleMultimediaAffiliate](docs/SimpleMultimediaAffiliate.md)
 - [SocialAffiliate](docs/SocialAffiliate.md)
 - [SortDescriptorAffiliate](docs/SortDescriptorAffiliate.md)
 - [SortObject](docs/SortObject.md)
 - [StateAffiliate](docs/StateAffiliate.md)
 - [SubCountryAffiliate](docs/SubCountryAffiliate.md)
 - [SubSubCountryAffiliate](docs/SubSubCountryAffiliate.md)
 - [TravelInventoryRecognitionAffiliate](docs/TravelInventoryRecognitionAffiliate.md)
 - [UpsertSalesChannelRelationshipRequestRequest](docs/UpsertSalesChannelRelationshipRequestRequest.md)


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


