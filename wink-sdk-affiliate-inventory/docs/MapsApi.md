# wink_sdk_affiliate_inventory.MapsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advanced_map_configuration**](MapsApi.md#create_advanced_map_configuration) | **POST** /api/affiliate/{companyIdentifier}/map | Create Inventory Map
[**create_advanced_map_configuration_for_supplier**](MapsApi.md#create_advanced_map_configuration_for_supplier) | **POST** /api/affiliate/{companyIdentifier}/map/supplier | Create Supplier Map
[**create_advanced_map_syndication_entry**](MapsApi.md#create_advanced_map_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/map/syndication/entry | Add to WinkLinks
[**remove_advanced_map_configuration**](MapsApi.md#remove_advanced_map_configuration) | **DELETE** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Delete Map
[**show_advanced_map_configuration**](MapsApi.md#show_advanced_map_configuration) | **GET** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Show Map
[**show_advanced_map_configuration_map_marker**](MapsApi.md#show_advanced_map_configuration_map_marker) | **GET** /api/affiliate/{companyIdentifier}/map/marker/{channelInventoryIdentifier} | Show Map Marker
[**show_advanced_map_configuration_map_markers**](MapsApi.md#show_advanced_map_configuration_map_markers) | **GET** /api/affiliate/{companyIdentifier}/map/markers/{listType}/{listIdentifier} | Show Map Markers
[**show_advanced_map_configurations**](MapsApi.md#show_advanced_map_configurations) | **GET** /api/affiliate/{companyIdentifier}/map | Show Maps
[**update_advanced_map_configuration**](MapsApi.md#update_advanced_map_configuration) | **PUT** /api/affiliate/{companyIdentifier}/map/{mapIdentifier} | Update Map


# **create_advanced_map_configuration**
> AdvancedMapConfigurationViewAffiliate create_advanced_map_configuration(company_identifier, upsert_advanced_map_configuration_request_affiliate, wink_version=wink_version)

Create Inventory Map

Create a new advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_advanced_map_configuration_request_affiliate import UpsertAdvancedMapConfigurationRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Create map owned by this owner identifier.
    upsert_advanced_map_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertAdvancedMapConfigurationRequestAffiliate() # UpsertAdvancedMapConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Inventory Map
        api_response = api_instance.create_advanced_map_configuration(company_identifier, upsert_advanced_map_configuration_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_advanced_map_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_advanced_map_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create map owned by this owner identifier. | 
 **upsert_advanced_map_configuration_request_affiliate** | [**UpsertAdvancedMapConfigurationRequestAffiliate**](UpsertAdvancedMapConfigurationRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AdvancedMapConfigurationViewAffiliate**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advanced_map_configuration_for_supplier**
> AdvancedMapConfigurationViewAffiliate create_advanced_map_configuration_for_supplier(company_identifier, upsert_supplier_advanced_map_configuration_request_affiliate, wink_version=wink_version)

Create Supplier Map

Creates a new advanced map configuration with a single marker for a supplier showing the best priced room.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_advanced_map_configuration_request_affiliate import UpsertSupplierAdvancedMapConfigurationRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Create supplier map owned by this owner identifier.
    upsert_supplier_advanced_map_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertSupplierAdvancedMapConfigurationRequestAffiliate() # UpsertSupplierAdvancedMapConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Supplier Map
        api_response = api_instance.create_advanced_map_configuration_for_supplier(company_identifier, upsert_supplier_advanced_map_configuration_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_advanced_map_configuration_for_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_advanced_map_configuration_for_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create supplier map owned by this owner identifier. | 
 **upsert_supplier_advanced_map_configuration_request_affiliate** | [**UpsertSupplierAdvancedMapConfigurationRequestAffiliate**](UpsertSupplierAdvancedMapConfigurationRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AdvancedMapConfigurationViewAffiliate**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advanced_map_syndication_entry**
> BooleanResponseAffiliate create_advanced_map_syndication_entry(company_identifier, create_advanced_map_configuration_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified map ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.boolean_response_affiliate import BooleanResponseAffiliate
from wink_sdk_affiliate_inventory.models.create_advanced_map_configuration_syndication_entry_request_affiliate import CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to create item for
    create_advanced_map_configuration_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate() # CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_advanced_map_syndication_entry(company_identifier, create_advanced_map_configuration_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_advanced_map_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_advanced_map_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to create item for | 
 **create_advanced_map_configuration_syndication_entry_request_affiliate** | [**CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate**](CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseAffiliate**](BooleanResponseAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_advanced_map_configuration**
> AdvancedMapConfigurationViewAffiliate remove_advanced_map_configuration(company_identifier, map_identifier, wink_version=wink_version, accept=accept)

Delete Map

Remove an advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Remove map owned by this owner identifier.
    map_identifier = 'map-1' # str | Remove map record with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Map
        api_response = api_instance.remove_advanced_map_configuration(company_identifier, map_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->remove_advanced_map_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->remove_advanced_map_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove map owned by this owner identifier. | 
 **map_identifier** | **str**| Remove map record with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AdvancedMapConfigurationViewAffiliate**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_advanced_map_configuration**
> AdvancedMapConfigurationViewAffiliate show_advanced_map_configuration(company_identifier, map_identifier, wink_version=wink_version, accept=accept)

Show Map

Retrieve a specific map record

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Show map record owned by this owner identifier.
    map_identifier = 'map-1' # str | Show map record with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map
        api_response = api_instance.show_advanced_map_configuration(company_identifier, map_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_advanced_map_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_advanced_map_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show map record owned by this owner identifier. | 
 **map_identifier** | **str**| Show map record with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AdvancedMapConfigurationViewAffiliate**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_advanced_map_configuration_map_marker**
> InventoryMapMarkerAffiliate show_advanced_map_configuration_map_marker(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)

Show Map Marker

Retrieve map marker for individual channel blocking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_marker_affiliate import InventoryMapMarkerAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Show map markers for map owned by this owner identifier.
    channel_inventory_identifier = 'channel-blocking-1' # str | Show map marker for specific blocking.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map Marker
        api_response = api_instance.show_advanced_map_configuration_map_marker(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_advanced_map_configuration_map_marker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_advanced_map_configuration_map_marker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show map markers for map owned by this owner identifier. | 
 **channel_inventory_identifier** | **str**| Show map marker for specific blocking. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryMapMarkerAffiliate**](InventoryMapMarkerAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_advanced_map_configuration_map_markers**
> List[InventoryMapMarkerAffiliate] show_advanced_map_configuration_map_markers(company_identifier, list_identifier, list_type, display_currency=display_currency, wink_version=wink_version, accept=accept)

Show Map Markers

Retrieve a list of advanced map configuration blocking markers by type

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_marker_affiliate import InventoryMapMarkerAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Show map markers for list owned by this owner identifier.
    list_identifier = 'list-1' # str | Show map markers for list.
    list_type = 'LIST' # str | Indicate whether this list is a curated or dynamic list.
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map Markers
        api_response = api_instance.show_advanced_map_configuration_map_markers(company_identifier, list_identifier, list_type, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_advanced_map_configuration_map_markers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_advanced_map_configuration_map_markers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show map markers for list owned by this owner identifier. | 
 **list_identifier** | **str**| Show map markers for list. | 
 **list_type** | **str**| Indicate whether this list is a curated or dynamic list. | 
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[InventoryMapMarkerAffiliate]**](InventoryMapMarkerAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_advanced_map_configurations**
> List[AdvancedMapConfigurationViewAffiliate] show_advanced_map_configurations(company_identifier, wink_version=wink_version, accept=accept)

Show Maps

Retrieve list of existing maps.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | List maps owned by this owner identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Maps
        api_response = api_instance.show_advanced_map_configurations(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_advanced_map_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_advanced_map_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| List maps owned by this owner identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[AdvancedMapConfigurationViewAffiliate]**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_advanced_map_configuration**
> AdvancedMapConfigurationViewAffiliate update_advanced_map_configuration(company_identifier, map_identifier, upsert_advanced_map_configuration_request_affiliate, wink_version=wink_version)

Update Map

Update an advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_advanced_map_configuration_request_affiliate import UpsertAdvancedMapConfigurationRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.MapsApi(api_client)
    company_identifier = 'owner-1' # str | Update map owned by this owner identifier.
    map_identifier = 'map-1' # str | update map record with this identifier.
    upsert_advanced_map_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertAdvancedMapConfigurationRequestAffiliate() # UpsertAdvancedMapConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Map
        api_response = api_instance.update_advanced_map_configuration(company_identifier, map_identifier, upsert_advanced_map_configuration_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->update_advanced_map_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->update_advanced_map_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update map owned by this owner identifier. | 
 **map_identifier** | **str**| update map record with this identifier. | 
 **upsert_advanced_map_configuration_request_affiliate** | [**UpsertAdvancedMapConfigurationRequestAffiliate**](UpsertAdvancedMapConfigurationRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AdvancedMapConfigurationViewAffiliate**](AdvancedMapConfigurationViewAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

