# wink_sdk_affiliate_inventory.SyndicatedItemApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advanced_map_syndication_entry**](SyndicatedItemApi.md#create_advanced_map_syndication_entry) | **POST** /api/map/syndication/entry | Add to WinkLinks
[**create_seller_inventory_item_syndication_entry**](SyndicatedItemApi.md#create_seller_inventory_item_syndication_entry) | **POST** /api/item/syndication/entry | Add to WinkLinks
[**create_seller_inventory_list_syndication_entry**](SyndicatedItemApi.md#create_seller_inventory_list_syndication_entry) | **POST** /api/grid/syndication/entry | Add List to WinkLinks
[**create_seller_inventory_ranked_list_syndication_entry**](SyndicatedItemApi.md#create_seller_inventory_ranked_list_syndication_entry) | **POST** /api/ranked-grid/syndication/entry | Add to WinkLinks
[**create_supplier_url_syndication_entry**](SyndicatedItemApi.md#create_supplier_url_syndication_entry) | **POST** /api/shareable-link/supplier/syndication/entry | Add to WinkLinks
[**create_supplier_url_syndication_entry1**](SyndicatedItemApi.md#create_supplier_url_syndication_entry1) | **POST** /api/shareable-link/inventory/syndication/entry | Add to WinkLinks


# **create_advanced_map_syndication_entry**
> SyndicatedItemAffiliate create_advanced_map_syndication_entry(create_inventory_map_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified map ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_inventory_map_syndication_entry_request_affiliate import CreateInventoryMapSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_inventory_map_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateInventoryMapSyndicationEntryRequestAffiliate() # CreateInventoryMapSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_advanced_map_syndication_entry(create_inventory_map_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_advanced_map_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_advanced_map_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inventory_map_syndication_entry_request_affiliate** | [**CreateInventoryMapSyndicationEntryRequestAffiliate**](CreateInventoryMapSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **create_seller_inventory_item_syndication_entry**
> SyndicatedItemAffiliate create_seller_inventory_item_syndication_entry(create_sellable_item_syndicated_item_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified item ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_sellable_item_syndicated_item_request_affiliate import CreateSellableItemSyndicatedItemRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_sellable_item_syndicated_item_request_affiliate = wink_sdk_affiliate_inventory.CreateSellableItemSyndicatedItemRequestAffiliate() # CreateSellableItemSyndicatedItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_seller_inventory_item_syndication_entry(create_sellable_item_syndicated_item_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_seller_inventory_item_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_seller_inventory_item_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sellable_item_syndicated_item_request_affiliate** | [**CreateSellableItemSyndicatedItemRequestAffiliate**](CreateSellableItemSyndicatedItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **create_seller_inventory_list_syndication_entry**
> SyndicatedItemAffiliate create_seller_inventory_list_syndication_entry(create_static_list_syndication_entry_request_affiliate, wink_version=wink_version)

Add List to WinkLinks

Creates a new WinkLinks entry from the specified list ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_static_list_syndication_entry_request_affiliate import CreateStaticListSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_static_list_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateStaticListSyndicationEntryRequestAffiliate() # CreateStaticListSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add List to WinkLinks
        api_response = api_instance.create_seller_inventory_list_syndication_entry(create_static_list_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_seller_inventory_list_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_seller_inventory_list_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_list_syndication_entry_request_affiliate** | [**CreateStaticListSyndicationEntryRequestAffiliate**](CreateStaticListSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **create_seller_inventory_ranked_list_syndication_entry**
> SyndicatedItemAffiliate create_seller_inventory_ranked_list_syndication_entry(create_sellable_ranked_list_syndicated_item_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified list ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_sellable_ranked_list_syndicated_item_request_affiliate import CreateSellableRankedListSyndicatedItemRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_sellable_ranked_list_syndicated_item_request_affiliate = wink_sdk_affiliate_inventory.CreateSellableRankedListSyndicatedItemRequestAffiliate() # CreateSellableRankedListSyndicatedItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_seller_inventory_ranked_list_syndication_entry(create_sellable_ranked_list_syndicated_item_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_seller_inventory_ranked_list_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_seller_inventory_ranked_list_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sellable_ranked_list_syndicated_item_request_affiliate** | [**CreateSellableRankedListSyndicatedItemRequestAffiliate**](CreateSellableRankedListSyndicatedItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **create_supplier_url_syndication_entry**
> SyndicatedItemAffiliate create_supplier_url_syndication_entry(create_syndicated_item_from_sellable_supplier_url_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified link ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_syndicated_item_from_sellable_supplier_url_request_affiliate import CreateSyndicatedItemFromSellableSupplierUrlRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_syndicated_item_from_sellable_supplier_url_request_affiliate = wink_sdk_affiliate_inventory.CreateSyndicatedItemFromSellableSupplierUrlRequestAffiliate() # CreateSyndicatedItemFromSellableSupplierUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_supplier_url_syndication_entry(create_syndicated_item_from_sellable_supplier_url_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_supplier_url_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_supplier_url_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_syndicated_item_from_sellable_supplier_url_request_affiliate** | [**CreateSyndicatedItemFromSellableSupplierUrlRequestAffiliate**](CreateSyndicatedItemFromSellableSupplierUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **create_supplier_url_syndication_entry1**
> SyndicatedItemAffiliate create_supplier_url_syndication_entry1(create_syndicated_item_from_sellable_inventory_url_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified link ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_syndicated_item_from_sellable_inventory_url_request_affiliate import CreateSyndicatedItemFromSellableInventoryUrlRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SyndicatedItemApi(api_client)
    create_syndicated_item_from_sellable_inventory_url_request_affiliate = wink_sdk_affiliate_inventory.CreateSyndicatedItemFromSellableInventoryUrlRequestAffiliate() # CreateSyndicatedItemFromSellableInventoryUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_supplier_url_syndication_entry1(create_syndicated_item_from_sellable_inventory_url_request_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_supplier_url_syndication_entry1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_supplier_url_syndication_entry1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_syndicated_item_from_sellable_inventory_url_request_affiliate** | [**CreateSyndicatedItemFromSellableInventoryUrlRequestAffiliate**](CreateSyndicatedItemFromSellableInventoryUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

