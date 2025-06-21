# wink_sdk_affiliate_browse.DynamicListApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_search**](DynamicListApi.md#create_saved_search) | **POST** /api/dynamic-list | Create Dynamic List
[**remove_saved_search**](DynamicListApi.md#remove_saved_search) | **DELETE** /api/dynamic-list/{listIdentifier} | Remove Dynamic List
[**show_saved_searches**](DynamicListApi.md#show_saved_searches) | **GET** /api/dynamic-list | Show Dynamic Lists
[**update_saved_search**](DynamicListApi.md#update_saved_search) | **PUT** /api/dynamic-list/{listIdentifier} | Update Dynamic List


# **create_saved_search**
> DynamicListAffiliate create_saved_search(upsert_dynamic_list_request_affiliate, wink_version=wink_version)

Create Dynamic List

Create a new dynamic saved search.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_list_affiliate import DynamicListAffiliate
from wink_sdk_affiliate_browse.models.upsert_dynamic_list_request_affiliate import UpsertDynamicListRequestAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.DynamicListApi(api_client)
    upsert_dynamic_list_request_affiliate = wink_sdk_affiliate_browse.UpsertDynamicListRequestAffiliate() # UpsertDynamicListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Dynamic List
        api_response = api_instance.create_saved_search(upsert_dynamic_list_request_affiliate, wink_version=wink_version)
        print("The response of DynamicListApi->create_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicListApi->create_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_dynamic_list_request_affiliate** | [**UpsertDynamicListRequestAffiliate**](UpsertDynamicListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**DynamicListAffiliate**](DynamicListAffiliate.md)

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

# **remove_saved_search**
> DynamicListAffiliate remove_saved_search(list_identifier, wink_version=wink_version, accept=accept)

Remove Dynamic List

Remove saved search record by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_list_affiliate import DynamicListAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.DynamicListApi(api_client)
    list_identifier = 'saved-search-1' # str | Saved search identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Dynamic List
        api_response = api_instance.remove_saved_search(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of DynamicListApi->remove_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicListApi->remove_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Saved search identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**DynamicListAffiliate**](DynamicListAffiliate.md)

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

# **show_saved_searches**
> List[DynamicListAffiliate] show_saved_searches(wink_version=wink_version, accept=accept)

Show Dynamic Lists

Retrieve all saved searches for owner

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_list_affiliate import DynamicListAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.DynamicListApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Dynamic Lists
        api_response = api_instance.show_saved_searches(wink_version=wink_version, accept=accept)
        print("The response of DynamicListApi->show_saved_searches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicListApi->show_saved_searches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[DynamicListAffiliate]**](DynamicListAffiliate.md)

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

# **update_saved_search**
> DynamicListAffiliate update_saved_search(list_identifier, upsert_dynamic_list_request_affiliate, wink_version=wink_version)

Update Dynamic List

Update a existing saved search record by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_list_affiliate import DynamicListAffiliate
from wink_sdk_affiliate_browse.models.upsert_dynamic_list_request_affiliate import UpsertDynamicListRequestAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.DynamicListApi(api_client)
    list_identifier = 'saved-search-1' # str | Saved search identifier.
    upsert_dynamic_list_request_affiliate = wink_sdk_affiliate_browse.UpsertDynamicListRequestAffiliate() # UpsertDynamicListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Dynamic List
        api_response = api_instance.update_saved_search(list_identifier, upsert_dynamic_list_request_affiliate, wink_version=wink_version)
        print("The response of DynamicListApi->update_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicListApi->update_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| Saved search identifier. | 
 **upsert_dynamic_list_request_affiliate** | [**UpsertDynamicListRequestAffiliate**](UpsertDynamicListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**DynamicListAffiliate**](DynamicListAffiliate.md)

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

