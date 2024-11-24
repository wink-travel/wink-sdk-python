# wink-sdk-affiliate-inventory
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



# Inventory API
The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it. This API lets you:

1. Manage customizations.
2. Shareable Links: Manage shareable supplier / blocking links.
3. Inventory: Manage individual blocking items.
4. Lists: Manage curated / ranked grids.
5. Maps: Manage maps.

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
pip install wink_sdk_affiliate_inventory
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_affiliate_inventory&subdirectory=wink-sdk-affiliate-inventory
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_affiliate_inventory&subdirectory=wink_sdk_affiliate_inventory`)

Then import the package:
```python
import wink_sdk_affiliate_inventory
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_affiliate_inventory
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Create customization for this company
    upsert_engine_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertEngineConfigurationRequestAffiliate() # UpsertEngineConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Customization
        api_response = api_instance.create_customization(company_identifier, upsert_engine_configuration_request_affiliate, wink_version=wink_version)
        print("The response of CustomizationApi->create_customization:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomizationApi->create_customization: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomizationApi* | [**create_customization**](docs/CustomizationApi.md#create_customization) | **POST** /api/affiliate/{companyIdentifier}/configuration | Create Customization
*CustomizationApi* | [**remove_customization**](docs/CustomizationApi.md#remove_customization) | **DELETE** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Remove Customization
*CustomizationApi* | [**show_application_configuration**](docs/CustomizationApi.md#show_application_configuration) | **GET** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Show Customization
*CustomizationApi* | [**show_application_configurations_by_owner**](docs/CustomizationApi.md#show_application_configurations_by_owner) | **GET** /api/affiliate/{companyIdentifier}/configuration/list | Show Customizations
*CustomizationApi* | [**show_primary_application_configuration**](docs/CustomizationApi.md#show_primary_application_configuration) | **GET** /api/affiliate/{companyIdentifier}/configuration | Show Primary Customization
*CustomizationApi* | [**update_customization**](docs/CustomizationApi.md#update_customization) | **PUT** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Update Customization
*EmbeddableInventoriesApi* | [**show_embeddable_inventory**](docs/EmbeddableInventoriesApi.md#show_embeddable_inventory) | **GET** /api/affiliate/{companyIdentifier}/embeddable-inventory/list | Show Embeddable Inventories
*GridsApi* | [**create_seller_inventory_list**](docs/GridsApi.md#create_seller_inventory_list) | **POST** /api/affiliate/{companyIdentifier}/grids | Create Grid
*GridsApi* | [**create_seller_inventory_list_syndication_entry**](docs/GridsApi.md#create_seller_inventory_list_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/grids/syndication/entry | Add List to WinkLinks
*GridsApi* | [**remove_seller_inventory_list**](docs/GridsApi.md#remove_seller_inventory_list) | **DELETE** /api/affiliate/{companyIdentifier}/grids/{listIdentifier} | Delete Grid
*GridsApi* | [**show_seller_inventory_list**](docs/GridsApi.md#show_seller_inventory_list) | **GET** /api/affiliate/{companyIdentifier}/grids/{listIdentifier} | Show Grid
*GridsApi* | [**show_seller_inventory_lists**](docs/GridsApi.md#show_seller_inventory_lists) | **GET** /api/affiliate/{companyIdentifier}/grids/list | Show Grids
*GridsApi* | [**update_seller_inventory_list**](docs/GridsApi.md#update_seller_inventory_list) | **PUT** /api/affiliate/{companyIdentifier}/grids/{listIdentifier} | Update Grid
*InventoryLinksApi* | [**create_seller_url**](docs/InventoryLinksApi.md#create_seller_url) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/inventory | Create Link
*InventoryLinksApi* | [**create_supplier_url_syndication_entry1**](docs/InventoryLinksApi.md#create_supplier_url_syndication_entry1) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/inventory/syndication/entry | Add to WinkLinks
*InventoryLinksApi* | [**remove_seller_url**](docs/InventoryLinksApi.md#remove_seller_url) | **DELETE** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Delete Link
*InventoryLinksApi* | [**show_inventory_media**](docs/InventoryLinksApi.md#show_inventory_media) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{channelInventoryIdentifier}/media/list | Show Inventory Media
*InventoryLinksApi* | [**show_seller_url**](docs/InventoryLinksApi.md#show_seller_url) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Show Link
*InventoryLinksApi* | [**show_seller_urls**](docs/InventoryLinksApi.md#show_seller_urls) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/list | Show Links
*InventoryLinksApi* | [**update_seller_url**](docs/InventoryLinksApi.md#update_seller_url) | **PUT** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Update link
*ItemsApi* | [**create_seller_inventory_item**](docs/ItemsApi.md#create_seller_inventory_item) | **POST** /api/affiliate/{companyIdentifier}/items | Create Item
*ItemsApi* | [**create_seller_inventory_item_syndication_entry**](docs/ItemsApi.md#create_seller_inventory_item_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/items/syndication/entry | Add to WinkLinks
*ItemsApi* | [**create_supplier_seller_inventory_item**](docs/ItemsApi.md#create_supplier_seller_inventory_item) | **POST** /api/affiliate/{companyIdentifier}/items/supplier | Create Supplier Item
*ItemsApi* | [**remove_seller_inventory_item**](docs/ItemsApi.md#remove_seller_inventory_item) | **DELETE** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Delete Item
*ItemsApi* | [**show_inventory_media1**](docs/ItemsApi.md#show_inventory_media1) | **GET** /api/affiliate/{companyIdentifier}/items/inventory/{channelInventoryIdentifier}/media/list | Show Item Media
*ItemsApi* | [**show_seller_inventory_item**](docs/ItemsApi.md#show_seller_inventory_item) | **GET** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Show Item
*ItemsApi* | [**show_seller_inventory_items_for_company**](docs/ItemsApi.md#show_seller_inventory_items_for_company) | **GET** /api/affiliate/{companyIdentifier}/items/list | Show Items
*ItemsApi* | [**update_seller_inventory_item**](docs/ItemsApi.md#update_seller_inventory_item) | **PUT** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Update Item
*MapsApi* | [**create_advanced_map_configuration**](docs/MapsApi.md#create_advanced_map_configuration) | **POST** /api/affiliate/{companyIdentifier}/map | Create Inventory Map
*MapsApi* | [**create_advanced_map_configuration_for_supplier**](docs/MapsApi.md#create_advanced_map_configuration_for_supplier) | **POST** /api/affiliate/{companyIdentifier}/map/supplier | Create Supplier Map
*MapsApi* | [**create_advanced_map_syndication_entry**](docs/MapsApi.md#create_advanced_map_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/map/syndication/entry | Add to WinkLinks
*MapsApi* | [**remove_advanced_map_configuration**](docs/MapsApi.md#remove_advanced_map_configuration) | **DELETE** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Delete Map
*MapsApi* | [**show_advanced_map_configuration**](docs/MapsApi.md#show_advanced_map_configuration) | **GET** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Show Map
*MapsApi* | [**show_advanced_map_configuration_map_marker**](docs/MapsApi.md#show_advanced_map_configuration_map_marker) | **GET** /api/affiliate/{companyIdentifier}/map/marker/{channelInventoryIdentifier} | Show Map Marker
*MapsApi* | [**show_advanced_map_configuration_map_markers**](docs/MapsApi.md#show_advanced_map_configuration_map_markers) | **GET** /api/affiliate/{companyIdentifier}/map/markers/{listType}/{listIdentifier} | Show Map Markers
*MapsApi* | [**show_advanced_map_configurations**](docs/MapsApi.md#show_advanced_map_configurations) | **GET** /api/affiliate/{companyIdentifier}/map | Show Maps
*MapsApi* | [**update_advanced_map_configuration**](docs/MapsApi.md#update_advanced_map_configuration) | **PUT** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Update Map
*RankedGridsApi* | [**create_seller_inventory_ranked_list**](docs/RankedGridsApi.md#create_seller_inventory_ranked_list) | **POST** /api/affiliate/{companyIdentifier}/ranked-grids | Create Ranked Grid
*RankedGridsApi* | [**create_seller_inventory_ranked_list_syndication_entry**](docs/RankedGridsApi.md#create_seller_inventory_ranked_list_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/ranked-grids/syndication/entry | Add to WinkLinks
*RankedGridsApi* | [**remove_seller_inventory_ranked_list**](docs/RankedGridsApi.md#remove_seller_inventory_ranked_list) | **DELETE** /api/affiliate/{companyIdentifier}/ranked-grids/{listIdentifier} | Delete Ranked Grid
*RankedGridsApi* | [**show_seller_inventory_ranked_list**](docs/RankedGridsApi.md#show_seller_inventory_ranked_list) | **GET** /api/affiliate/{companyIdentifier}/ranked-grids/{listIdentifier} | Show Ranked Grid
*RankedGridsApi* | [**show_seller_inventory_ranked_lists**](docs/RankedGridsApi.md#show_seller_inventory_ranked_lists) | **GET** /api/affiliate/{companyIdentifier}/ranked-grids/list | Show Ranked Grids
*RankedGridsApi* | [**update_seller_inventory_ranked_list**](docs/RankedGridsApi.md#update_seller_inventory_ranked_list) | **PUT** /api/affiliate/{companyIdentifier}/ranked-grids/{listIdentifier} | Update Ranked Grid
*SupplierLinksApi* | [**create_supplier_url**](docs/SupplierLinksApi.md#create_supplier_url) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/supplier | Create Link
*SupplierLinksApi* | [**create_supplier_url_syndication_entry**](docs/SupplierLinksApi.md#create_supplier_url_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/supplier/syndication/entry | Add to WinkLinks
*SupplierLinksApi* | [**remove_supplier_url**](docs/SupplierLinksApi.md#remove_supplier_url) | **DELETE** /api/affiliate/{companyIdentifier}/shareable-link/supplier/{supplierUrlIdentifier} | Delete Link
*SupplierLinksApi* | [**show_supplier_url**](docs/SupplierLinksApi.md#show_supplier_url) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/supplier/{supplierUrlIdentifier} | Show Link
*SupplierLinksApi* | [**show_supplier_urls**](docs/SupplierLinksApi.md#show_supplier_urls) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/supplier/list | Show Links
*SupplierLinksApi* | [**update_supplier_url**](docs/SupplierLinksApi.md#update_supplier_url) | **PUT** /api/affiliate/{companyIdentifier}/shareable-link/supplier/{supplierUrlIdentifier} | Update link


## Documentation For Models

 - [AdvancedMapConfigurationAffiliate](docs/AdvancedMapConfigurationAffiliate.md)
 - [AdvancedMapConfigurationViewAffiliate](docs/AdvancedMapConfigurationViewAffiliate.md)
 - [BooleanResponseAffiliate](docs/BooleanResponseAffiliate.md)
 - [CampaignInventoryAffiliate](docs/CampaignInventoryAffiliate.md)
 - [ChildAffiliate](docs/ChildAffiliate.md)
 - [ConfigurableGeoJsonCircleAffiliate](docs/ConfigurableGeoJsonCircleAffiliate.md)
 - [ConfigurableGeoJsonPointAffiliate](docs/ConfigurableGeoJsonPointAffiliate.md)
 - [ConfigurableGeoJsonPolygonAffiliate](docs/ConfigurableGeoJsonPolygonAffiliate.md)
 - [ConfigurableGeoJsonRectangleAffiliate](docs/ConfigurableGeoJsonRectangleAffiliate.md)
 - [CountryAffiliate](docs/CountryAffiliate.md)
 - [CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate](docs/CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate.md)
 - [CreateSellerInventoryItemSyndicationEntryRequestAffiliate](docs/CreateSellerInventoryItemSyndicationEntryRequestAffiliate.md)
 - [CreateSellerInventoryRankedListSyndicationEntryRequestAffiliate](docs/CreateSellerInventoryRankedListSyndicationEntryRequestAffiliate.md)
 - [CreateSellerUrlSyndicationEntryRequestAffiliate](docs/CreateSellerUrlSyndicationEntryRequestAffiliate.md)
 - [CreateStaticSellerListSyndicationEntryRequestAffiliate](docs/CreateStaticSellerListSyndicationEntryRequestAffiliate.md)
 - [CreateSupplierUrlSyndicationEntryRequestAffiliate](docs/CreateSupplierUrlSyndicationEntryRequestAffiliate.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [EngineConfigurationAffiliate](docs/EngineConfigurationAffiliate.md)
 - [EngineConfigurationThemeAffiliate](docs/EngineConfigurationThemeAffiliate.md)
 - [EngineConfigurationViewAffiliate](docs/EngineConfigurationViewAffiliate.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoJsonLineStringAffiliate](docs/GeoJsonLineStringAffiliate.md)
 - [GeoJsonPointAffiliate](docs/GeoJsonPointAffiliate.md)
 - [GeoJsonPolygonAffiliate](docs/GeoJsonPolygonAffiliate.md)
 - [GeoJsonRectangleAffiliate](docs/GeoJsonRectangleAffiliate.md)
 - [GeoNameAffiliate](docs/GeoNameAffiliate.md)
 - [ImageAttributionAffiliate](docs/ImageAttributionAffiliate.md)
 - [InventoryMapMarkerAffiliate](docs/InventoryMapMarkerAffiliate.md)
 - [KeyValuePairAffiliate](docs/KeyValuePairAffiliate.md)
 - [LookupAffiliate](docs/LookupAffiliate.md)
 - [OpenGraphMediaAffiliate](docs/OpenGraphMediaAffiliate.md)
 - [PointAffiliate](docs/PointAffiliate.md)
 - [RoomConfigurationAffiliate](docs/RoomConfigurationAffiliate.md)
 - [SellerInventoryItemAffiliate](docs/SellerInventoryItemAffiliate.md)
 - [SellerInventoryItemViewAffiliate](docs/SellerInventoryItemViewAffiliate.md)
 - [SellerInventoryListAffiliate](docs/SellerInventoryListAffiliate.md)
 - [SellerInventoryListViewAffiliate](docs/SellerInventoryListViewAffiliate.md)
 - [SellerInventoryRankedListAffiliate](docs/SellerInventoryRankedListAffiliate.md)
 - [SellerInventoryRankedListViewAffiliate](docs/SellerInventoryRankedListViewAffiliate.md)
 - [SellerUrlAffiliate](docs/SellerUrlAffiliate.md)
 - [SellerUrlViewAffiliate](docs/SellerUrlViewAffiliate.md)
 - [ShowSupplierUrl400Response](docs/ShowSupplierUrl400Response.md)
 - [SimpleDescriptionAffiliate](docs/SimpleDescriptionAffiliate.md)
 - [SimpleMultimediaAffiliate](docs/SimpleMultimediaAffiliate.md)
 - [SubCountryAffiliate](docs/SubCountryAffiliate.md)
 - [SubSubCountryAffiliate](docs/SubSubCountryAffiliate.md)
 - [SupplierUrlAffiliate](docs/SupplierUrlAffiliate.md)
 - [SupplierUrlViewAffiliate](docs/SupplierUrlViewAffiliate.md)
 - [SyndicationEntryAffiliate](docs/SyndicationEntryAffiliate.md)
 - [UpsertAdvancedMapConfigurationRequestAffiliate](docs/UpsertAdvancedMapConfigurationRequestAffiliate.md)
 - [UpsertEngineConfigurationRequestAffiliate](docs/UpsertEngineConfigurationRequestAffiliate.md)
 - [UpsertSellerInventoryItemRequestAffiliate](docs/UpsertSellerInventoryItemRequestAffiliate.md)
 - [UpsertSellerInventoryListRequestAffiliate](docs/UpsertSellerInventoryListRequestAffiliate.md)
 - [UpsertSellerInventoryRankedListRequestAffiliate](docs/UpsertSellerInventoryRankedListRequestAffiliate.md)
 - [UpsertSellerUrlRequestAffiliate](docs/UpsertSellerUrlRequestAffiliate.md)
 - [UpsertSupplierAdvancedMapConfigurationRequestAffiliate](docs/UpsertSupplierAdvancedMapConfigurationRequestAffiliate.md)
 - [UpsertSupplierSellerInventoryItemRequestAffiliate](docs/UpsertSupplierSellerInventoryItemRequestAffiliate.md)
 - [UpsertSupplierUrlRequestAffiliate](docs/UpsertSupplierUrlRequestAffiliate.md)


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


