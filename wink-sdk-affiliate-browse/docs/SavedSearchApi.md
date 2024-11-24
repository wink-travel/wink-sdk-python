# wink_sdk_affiliate_browse.SavedSearchApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_search**](SavedSearchApi.md#create_saved_search) | **POST** /api/affiliate/{companyIdentifier}/dynamic-list | Create Saved Search
[**remove_saved_search**](SavedSearchApi.md#remove_saved_search) | **DELETE** /api/affiliate/{companyIdentifier}/dynamic-list/{listIdentifier} | Remove Saved Search
[**show_saved_searches**](SavedSearchApi.md#show_saved_searches) | **GET** /api/affiliate/{companyIdentifier}/dynamic-list | Show Saved Searches
[**update_saved_search**](SavedSearchApi.md#update_saved_search) | **PUT** /api/affiliate/{companyIdentifier}/dynamic-list/{listIdentifier} | Update Saved Search


# **create_saved_search**
> DynamicSellerListViewAffiliate create_saved_search(company_identifier, upsert_dynamic_seller_list_affiliate, wink_version=wink_version)

Create Saved Search

Create a new dynamic saved search.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_view_affiliate import DynamicSellerListViewAffiliate
from wink_sdk_affiliate_browse.models.upsert_dynamic_seller_list_affiliate import UpsertDynamicSellerListAffiliate
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
    api_instance = wink_sdk_affiliate_browse.SavedSearchApi(api_client)
    company_identifier = 'owner-1' # str | Create search owned by this owner identifier.
    upsert_dynamic_seller_list_affiliate = wink_sdk_affiliate_browse.UpsertDynamicSellerListAffiliate() # UpsertDynamicSellerListAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Saved Search
        api_response = api_instance.create_saved_search(company_identifier, upsert_dynamic_seller_list_affiliate, wink_version=wink_version)
        print("The response of SavedSearchApi->create_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->create_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create search owned by this owner identifier. | 
 **upsert_dynamic_seller_list_affiliate** | [**UpsertDynamicSellerListAffiliate**](UpsertDynamicSellerListAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**DynamicSellerListViewAffiliate**](DynamicSellerListViewAffiliate.md)

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
> DynamicSellerListViewAffiliate remove_saved_search(company_identifier, list_identifier, wink_version=wink_version, accept=accept)

Remove Saved Search

Remove saved search record by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_view_affiliate import DynamicSellerListViewAffiliate
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
    api_instance = wink_sdk_affiliate_browse.SavedSearchApi(api_client)
    company_identifier = 'owner-1' # str | Remove search owned by this owner identifier.
    list_identifier = 'saved-search-1' # str | Saved search identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Saved Search
        api_response = api_instance.remove_saved_search(company_identifier, list_identifier, wink_version=wink_version, accept=accept)
        print("The response of SavedSearchApi->remove_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->remove_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove search owned by this owner identifier. | 
 **list_identifier** | **str**| Saved search identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**DynamicSellerListViewAffiliate**](DynamicSellerListViewAffiliate.md)

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
> List[DynamicSellerListViewAffiliate] show_saved_searches(company_identifier, wink_version=wink_version, accept=accept)

Show Saved Searches

Retrieve all saved searches for owner

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_view_affiliate import DynamicSellerListViewAffiliate
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
    api_instance = wink_sdk_affiliate_browse.SavedSearchApi(api_client)
    company_identifier = 'owner-1' # str | List searches owned by this owner identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Saved Searches
        api_response = api_instance.show_saved_searches(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of SavedSearchApi->show_saved_searches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->show_saved_searches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| List searches owned by this owner identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[DynamicSellerListViewAffiliate]**](DynamicSellerListViewAffiliate.md)

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
> DynamicSellerListViewAffiliate update_saved_search(company_identifier, list_identifier, upsert_dynamic_seller_list_affiliate, wink_version=wink_version)

Update Saved Search

Update a existing saved search record by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_view_affiliate import DynamicSellerListViewAffiliate
from wink_sdk_affiliate_browse.models.upsert_dynamic_seller_list_affiliate import UpsertDynamicSellerListAffiliate
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
    api_instance = wink_sdk_affiliate_browse.SavedSearchApi(api_client)
    company_identifier = 'owner-1' # str | Update search owned by this owner identifier.
    list_identifier = 'saved-search-1' # str | Saved search identifier.
    upsert_dynamic_seller_list_affiliate = wink_sdk_affiliate_browse.UpsertDynamicSellerListAffiliate() # UpsertDynamicSellerListAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Saved Search
        api_response = api_instance.update_saved_search(company_identifier, list_identifier, upsert_dynamic_seller_list_affiliate, wink_version=wink_version)
        print("The response of SavedSearchApi->update_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->update_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update search owned by this owner identifier. | 
 **list_identifier** | **str**| Saved search identifier. | 
 **upsert_dynamic_seller_list_affiliate** | [**UpsertDynamicSellerListAffiliate**](UpsertDynamicSellerListAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**DynamicSellerListViewAffiliate**](DynamicSellerListViewAffiliate.md)

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

