# wink_sdk_affiliate_inventory.MapsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advanced_map_syndication_entry**](MapsApi.md#create_advanced_map_syndication_entry) | **POST** /api/map/syndication/entry | Add to WinkLinks
[**create_inventory_map**](MapsApi.md#create_inventory_map) | **POST** /api/map | Create Inventory Map
[**create_inventory_map_for_supplier**](MapsApi.md#create_inventory_map_for_supplier) | **POST** /api/map/supplier | Create Supplier Map
[**remove_inventory_map**](MapsApi.md#remove_inventory_map) | **DELETE** /api/map/{mapIdentifier} | Delete Map
[**show_inventory_map**](MapsApi.md#show_inventory_map) | **GET** /api/map/{mapIdentifier} | Show Map
[**show_inventory_map_map_marker**](MapsApi.md#show_inventory_map_map_marker) | **GET** /api/map/marker/{channelInventoryIdentifier} | Show Map Marker
[**show_inventory_map_map_markers**](MapsApi.md#show_inventory_map_map_markers) | **GET** /api/map/markers/{listType}/{listIdentifier} | Show Map Markers
[**show_inventory_maps**](MapsApi.md#show_inventory_maps) | **GET** /api/map/list | Show Maps
[**update_inventory_map**](MapsApi.md#update_inventory_map) | **PUT** /api/map/{mapIdentifier} | Update Map


# **create_advanced_map_syndication_entry**
> BooleanResponseAffiliate create_advanced_map_syndication_entry(create_inventory_map_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified map ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.boolean_response_affiliate import BooleanResponseAffiliate
from wink_sdk_affiliate_inventory.models.create_inventory_map_syndication_entry_request_affiliate import CreateInventoryMapSyndicationEntryRequestAffiliate
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
    create_inventory_map_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateInventoryMapSyndicationEntryRequestAffiliate() # CreateInventoryMapSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_advanced_map_syndication_entry(create_inventory_map_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_advanced_map_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_advanced_map_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inventory_map_syndication_entry_request_affiliate** | [**CreateInventoryMapSyndicationEntryRequestAffiliate**](CreateInventoryMapSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseAffiliate**](BooleanResponseAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_map**
> InventoryMapAffiliate create_inventory_map(upsert_inventory_map_request_affiliate, wink_version=wink_version)

Create Inventory Map

Create a new advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
from wink_sdk_affiliate_inventory.models.upsert_inventory_map_request_affiliate import UpsertInventoryMapRequestAffiliate
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
    upsert_inventory_map_request_affiliate = wink_sdk_affiliate_inventory.UpsertInventoryMapRequestAffiliate() # UpsertInventoryMapRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Inventory Map
        api_response = api_instance.create_inventory_map(upsert_inventory_map_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_inventory_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_inventory_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_inventory_map_request_affiliate** | [**UpsertInventoryMapRequestAffiliate**](UpsertInventoryMapRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InventoryMapAffiliate**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_map_for_supplier**
> InventoryMapAffiliate create_inventory_map_for_supplier(upsert_supplier_inventory_map_request_affiliate, wink_version=wink_version)

Create Supplier Map

Creates a new advanced map configuration with a single marker for a supplier showing the best priced room.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_inventory_map_request_affiliate import UpsertSupplierInventoryMapRequestAffiliate
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
    upsert_supplier_inventory_map_request_affiliate = wink_sdk_affiliate_inventory.UpsertSupplierInventoryMapRequestAffiliate() # UpsertSupplierInventoryMapRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Supplier Map
        api_response = api_instance.create_inventory_map_for_supplier(upsert_supplier_inventory_map_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->create_inventory_map_for_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_inventory_map_for_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_supplier_inventory_map_request_affiliate** | [**UpsertSupplierInventoryMapRequestAffiliate**](UpsertSupplierInventoryMapRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InventoryMapAffiliate**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_inventory_map**
> InventoryMapAffiliate remove_inventory_map(map_identifier, wink_version=wink_version, accept=accept)

Delete Map

Remove an advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
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
    map_identifier = 'map-1' # str | Remove map record with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Map
        api_response = api_instance.remove_inventory_map(map_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->remove_inventory_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->remove_inventory_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**| Remove map record with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryMapAffiliate**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_inventory_map**
> InventoryMapAffiliate show_inventory_map(map_identifier, wink_version=wink_version, accept=accept)

Show Map

Retrieve a specific map record

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
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
    map_identifier = 'map-1' # str | Show map record with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map
        api_response = api_instance.show_inventory_map(map_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_inventory_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_inventory_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**| Show map record with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryMapAffiliate**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_inventory_map_map_marker**
> InventoryMapMarkerAffiliate show_inventory_map_map_marker(channel_inventory_identifier, wink_version=wink_version, accept=accept)

Show Map Marker

Retrieve map marker for individual channel inventory.

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
    channel_inventory_identifier = 'channel-inventory-1' # str | Show map marker for specific inventory.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map Marker
        api_response = api_instance.show_inventory_map_map_marker(channel_inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_inventory_map_map_marker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_inventory_map_map_marker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_inventory_identifier** | **str**| Show map marker for specific inventory. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryMapMarkerAffiliate**](InventoryMapMarkerAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_inventory_map_map_markers**
> List[InventoryMapMarkerAffiliate] show_inventory_map_map_markers(list_identifier, list_type, display_currency=display_currency, wink_version=wink_version, accept=accept)

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
    list_identifier = 'list-1' # str | Show map markers for list.
    list_type = 'LIST' # str | Indicate whether this list is a curated or dynamic list.
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Map Markers
        api_response = api_instance.show_inventory_map_map_markers(list_identifier, list_type, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_inventory_map_map_markers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_inventory_map_map_markers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_inventory_maps**
> List[InventoryMapAffiliate] show_inventory_maps(wink_version=wink_version, accept=accept)

Show Maps

Retrieve list of existing maps.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
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
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Maps
        api_response = api_instance.show_inventory_maps(wink_version=wink_version, accept=accept)
        print("The response of MapsApi->show_inventory_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->show_inventory_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[InventoryMapAffiliate]**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_map**
> InventoryMapAffiliate update_inventory_map(map_identifier, upsert_inventory_map_request_affiliate, wink_version=wink_version)

Update Map

Update an advanced map configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate
from wink_sdk_affiliate_inventory.models.upsert_inventory_map_request_affiliate import UpsertInventoryMapRequestAffiliate
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
    map_identifier = 'map-1' # str | update map record with this identifier.
    upsert_inventory_map_request_affiliate = wink_sdk_affiliate_inventory.UpsertInventoryMapRequestAffiliate() # UpsertInventoryMapRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Map
        api_response = api_instance.update_inventory_map(map_identifier, upsert_inventory_map_request_affiliate, wink_version=wink_version)
        print("The response of MapsApi->update_inventory_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->update_inventory_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_identifier** | **str**| update map record with this identifier. | 
 **upsert_inventory_map_request_affiliate** | [**UpsertInventoryMapRequestAffiliate**](UpsertInventoryMapRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InventoryMapAffiliate**](InventoryMapAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

