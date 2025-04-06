# wink_sdk_affiliate_inventory.GridsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_inventory_list**](GridsApi.md#create_seller_inventory_list) | **POST** /api/grids | Create Grid
[**create_seller_inventory_list_syndication_entry**](GridsApi.md#create_seller_inventory_list_syndication_entry) | **POST** /api/grids/syndication/entry | Add List to WinkLinks
[**remove_seller_inventory_list**](GridsApi.md#remove_seller_inventory_list) | **DELETE** /api/grids/{listIdentifier} | Delete Grid
[**show_seller_inventory_list**](GridsApi.md#show_seller_inventory_list) | **GET** /api/grids/{listIdentifier} | Show Grid
[**show_seller_inventory_lists**](GridsApi.md#show_seller_inventory_lists) | **GET** /api/grids/list | Show Grids
[**update_seller_inventory_list**](GridsApi.md#update_seller_inventory_list) | **PUT** /api/grids/{listIdentifier} | Update Grid


# **create_seller_inventory_list**
> SellerInventoryListViewAffiliate create_seller_inventory_list(upsert_seller_inventory_list_request_affiliate, wink_version=wink_version)

Create Grid

Create a new curated / saved search list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_list_request_affiliate import UpsertSellerInventoryListRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    upsert_seller_inventory_list_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerInventoryListRequestAffiliate() # UpsertSellerInventoryListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Grid
        api_response = api_instance.create_seller_inventory_list(upsert_seller_inventory_list_request_affiliate, wink_version=wink_version)
        print("The response of GridsApi->create_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->create_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_seller_inventory_list_request_affiliate** | [**UpsertSellerInventoryListRequestAffiliate**](UpsertSellerInventoryListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerInventoryListViewAffiliate**](SellerInventoryListViewAffiliate.md)

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

# **create_seller_inventory_list_syndication_entry**
> SyndicationEntryAffiliate create_seller_inventory_list_syndication_entry(create_static_seller_list_syndication_entry_request_affiliate, wink_version=wink_version)

Add List to WinkLinks

Creates a new WinkLinks entry from the specified list ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_static_seller_list_syndication_entry_request_affiliate import CreateStaticSellerListSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndication_entry_affiliate import SyndicationEntryAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    create_static_seller_list_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateStaticSellerListSyndicationEntryRequestAffiliate() # CreateStaticSellerListSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add List to WinkLinks
        api_response = api_instance.create_seller_inventory_list_syndication_entry(create_static_seller_list_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of GridsApi->create_seller_inventory_list_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->create_seller_inventory_list_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_seller_list_syndication_entry_request_affiliate** | [**CreateStaticSellerListSyndicationEntryRequestAffiliate**](CreateStaticSellerListSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicationEntryAffiliate**](SyndicationEntryAffiliate.md)

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

# **remove_seller_inventory_list**
> SellerInventoryListViewAffiliate remove_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)

Delete Grid

Remove a curated / saved search list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    list_identifier = 'list-1' # str | Delete curated list with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Grid
        api_response = api_instance.remove_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of GridsApi->remove_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->remove_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Delete curated list with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryListViewAffiliate**](SellerInventoryListViewAffiliate.md)

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

# **show_seller_inventory_list**
> SellerInventoryListViewAffiliate show_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)

Show Grid

Retrieve a specific curated / saved search list.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    list_identifier = 'list-1' # str | Retrieve list with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Grid
        api_response = api_instance.show_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of GridsApi->show_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->show_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Retrieve list with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryListViewAffiliate**](SellerInventoryListViewAffiliate.md)

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

# **show_seller_inventory_lists**
> List[SellerInventoryListViewAffiliate] show_seller_inventory_lists(wink_version=wink_version, accept=accept)

Show Grids

Retrieve curated / saved search list lists.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Grids
        api_response = api_instance.show_seller_inventory_lists(wink_version=wink_version, accept=accept)
        print("The response of GridsApi->show_seller_inventory_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->show_seller_inventory_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellerInventoryListViewAffiliate]**](SellerInventoryListViewAffiliate.md)

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

# **update_seller_inventory_list**
> SellerInventoryListViewAffiliate update_seller_inventory_list(list_identifier, upsert_seller_inventory_list_request_affiliate, wink_version=wink_version)

Update Grid

Update an existing curated / saved search list.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_list_request_affiliate import UpsertSellerInventoryListRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.GridsApi(api_client)
    list_identifier = 'list-1' # str | Update list with this identifier.
    upsert_seller_inventory_list_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerInventoryListRequestAffiliate() # UpsertSellerInventoryListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Grid
        api_response = api_instance.update_seller_inventory_list(list_identifier, upsert_seller_inventory_list_request_affiliate, wink_version=wink_version)
        print("The response of GridsApi->update_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->update_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Update list with this identifier. | 
 **upsert_seller_inventory_list_request_affiliate** | [**UpsertSellerInventoryListRequestAffiliate**](UpsertSellerInventoryListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerInventoryListViewAffiliate**](SellerInventoryListViewAffiliate.md)

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

