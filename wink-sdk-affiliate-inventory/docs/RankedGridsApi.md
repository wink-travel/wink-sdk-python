# wink_sdk_affiliate_inventory.RankedGridsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_seller_inventory_ranked_list**](RankedGridsApi.md#remove_seller_inventory_ranked_list) | **DELETE** /api/ranked-grid/{listIdentifier} | Delete Ranked Grid
[**show_seller_inventory_ranked_list**](RankedGridsApi.md#show_seller_inventory_ranked_list) | **GET** /api/ranked-grid/{listIdentifier} | Show Ranked Grid
[**show_seller_inventory_ranked_lists**](RankedGridsApi.md#show_seller_inventory_ranked_lists) | **GET** /api/ranked-grid/list | Show Ranked Grids
[**update_seller_inventory_ranked_list**](RankedGridsApi.md#update_seller_inventory_ranked_list) | **PUT** /api/ranked-grid/{listIdentifier} | Update Ranked Grid


# **remove_seller_inventory_ranked_list**
> SellableRankedListAffiliate remove_seller_inventory_ranked_list(list_identifier, wink_version=wink_version, accept=accept)

Delete Ranked Grid

Delete a ranked grid

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_ranked_list_affiliate import SellableRankedListAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.RankedGridsApi(api_client)
    list_identifier = 'ranked-grid-1' # str | Delete grid with this identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Ranked Grid
        api_response = api_instance.remove_seller_inventory_ranked_list(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of RankedGridsApi->remove_seller_inventory_ranked_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankedGridsApi->remove_seller_inventory_ranked_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Delete grid with this identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SellableRankedListAffiliate**](SellableRankedListAffiliate.md)

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

# **show_seller_inventory_ranked_list**
> SellableRankedListAffiliate show_seller_inventory_ranked_list(list_identifier, wink_version=wink_version, accept=accept)

Show Ranked Grid

Retrieve a specific ranked grid.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_ranked_list_affiliate import SellableRankedListAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.RankedGridsApi(api_client)
    list_identifier = 'ranked-grid-1' # str | Retrieve grid with this identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Ranked Grid
        api_response = api_instance.show_seller_inventory_ranked_list(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of RankedGridsApi->show_seller_inventory_ranked_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankedGridsApi->show_seller_inventory_ranked_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Retrieve grid with this identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SellableRankedListAffiliate**](SellableRankedListAffiliate.md)

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

# **show_seller_inventory_ranked_lists**
> List[SellableRankedListAffiliate] show_seller_inventory_ranked_lists(wink_version=wink_version, accept=accept)

Show Ranked Grids

Retrieve list of ranked grids.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_ranked_list_affiliate import SellableRankedListAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.RankedGridsApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Ranked Grids
        api_response = api_instance.show_seller_inventory_ranked_lists(wink_version=wink_version, accept=accept)
        print("The response of RankedGridsApi->show_seller_inventory_ranked_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankedGridsApi->show_seller_inventory_ranked_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellableRankedListAffiliate]**](SellableRankedListAffiliate.md)

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

# **update_seller_inventory_ranked_list**
> SellableRankedListAffiliate update_seller_inventory_ranked_list(list_identifier, upsert_sellable_ranked_list_request_affiliate, wink_version=wink_version)

Update Ranked Grid

Update existing ranked grid

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_ranked_list_affiliate import SellableRankedListAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_ranked_list_request_affiliate import UpsertSellableRankedListRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.RankedGridsApi(api_client)
    list_identifier = 'list-1' # str | Update list with this identifier.
    upsert_sellable_ranked_list_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableRankedListRequestAffiliate() # UpsertSellableRankedListRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Ranked Grid
        api_response = api_instance.update_seller_inventory_ranked_list(list_identifier, upsert_sellable_ranked_list_request_affiliate, wink_version=wink_version)
        print("The response of RankedGridsApi->update_seller_inventory_ranked_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankedGridsApi->update_seller_inventory_ranked_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Update list with this identifier. | 
 **upsert_sellable_ranked_list_request_affiliate** | [**UpsertSellableRankedListRequestAffiliate**](UpsertSellableRankedListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SellableRankedListAffiliate**](SellableRankedListAffiliate.md)

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

