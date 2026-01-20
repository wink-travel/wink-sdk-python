# wink_sdk_affiliate_inventory.GridsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_seller_inventory_list**](GridsApi.md#remove_seller_inventory_list) | **DELETE** /api/grid/{listIdentifier} | Delete Grid
[**show_seller_inventory_list**](GridsApi.md#show_seller_inventory_list) | **GET** /api/grid/{listIdentifier} | Show Grid
[**show_seller_inventory_lists**](GridsApi.md#show_seller_inventory_lists) | **GET** /api/grid/list | Show Grids
[**update_seller_inventory_list**](GridsApi.md#update_seller_inventory_list) | **PUT** /api/grid/{listIdentifier} | Update Grid


# **remove_seller_inventory_list**
> SellableListAffiliate remove_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)

Delete Grid

Remove a curated / saved search list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_list_affiliate import SellableListAffiliate
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
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
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SellableListAffiliate**](SellableListAffiliate.md)

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

# **show_seller_inventory_list**
> SellableListAffiliate show_seller_inventory_list(list_identifier, wink_version=wink_version, accept=accept)

Show Grid

Retrieve a specific curated / saved search list.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_list_affiliate import SellableListAffiliate
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
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
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SellableListAffiliate**](SellableListAffiliate.md)

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

# **show_seller_inventory_lists**
> List[SellableListAffiliate] show_seller_inventory_lists(wink_version=wink_version, accept=accept)

Show Grids

Retrieve curated / saved search list lists.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_list_affiliate import SellableListAffiliate
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
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
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellableListAffiliate]**](SellableListAffiliate.md)

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

# **update_seller_inventory_list**
> SellableListAffiliate update_seller_inventory_list(list_identifier, upsert_sellable_list_request_affiliate, wink_version=wink_version)

Update Grid

Update an existing curated / saved search list.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_list_affiliate import SellableListAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_list_request_affiliate import UpsertSellableListRequestAffiliate
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
    upsert_sellable_list_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableListRequestAffiliate() # UpsertSellableListRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Grid
        api_response = api_instance.update_seller_inventory_list(list_identifier, upsert_sellable_list_request_affiliate, wink_version=wink_version)
        print("The response of GridsApi->update_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridsApi->update_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Update list with this identifier. | 
 **upsert_sellable_list_request_affiliate** | [**UpsertSellableListRequestAffiliate**](UpsertSellableListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SellableListAffiliate**](SellableListAffiliate.md)

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

