# wink_sdk_user_settings.BucketListApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_add_bucket_list_entry**](BucketListApi.md#oauth2_add_bucket_list_entry) | **POST** /api/bucket-list | Create Bucket List
[**oauth2_remove_bucket_list**](BucketListApi.md#oauth2_remove_bucket_list) | **DELETE** /api/bucket-list/{bucketListItemIdentifier} | Delete Bucket List Entry
[**oauth2_show_bucket_list**](BucketListApi.md#oauth2_show_bucket_list) | **GET** /api/bucket-list | Get Bucket Lists
[**oauth2_show_bucket_list_entries**](BucketListApi.md#oauth2_show_bucket_list_entries) | **GET** /api/bucket-list/entries | Get Bucket List
[**oauth2_show_bucket_list_entry**](BucketListApi.md#oauth2_show_bucket_list_entry) | **GET** /api/bucket-list/{type}/{identifier} | Get Bucket List Entries


# **oauth2_add_bucket_list_entry**
> BucketListEntryViewAuthenticatedEntity oauth2_add_bucket_list_entry(bucket_list_entry_request_authenticated_entity, wink_version=wink_version)

Create Bucket List

Create a new bucket list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.bucket_list_entry_request_authenticated_entity import BucketListEntryRequestAuthenticatedEntity
from wink_sdk_user_settings.models.bucket_list_entry_view_authenticated_entity import BucketListEntryViewAuthenticatedEntity
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.BucketListApi(api_client)
    bucket_list_entry_request_authenticated_entity = wink_sdk_user_settings.BucketListEntryRequestAuthenticatedEntity() # BucketListEntryRequestAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Bucket List
        api_response = api_instance.oauth2_add_bucket_list_entry(bucket_list_entry_request_authenticated_entity, wink_version=wink_version)
        print("The response of BucketListApi->oauth2_add_bucket_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketListApi->oauth2_add_bucket_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_list_entry_request_authenticated_entity** | [**BucketListEntryRequestAuthenticatedEntity**](BucketListEntryRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BucketListEntryViewAuthenticatedEntity**](BucketListEntryViewAuthenticatedEntity.md)

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

# **oauth2_remove_bucket_list**
> BucketListEntryViewAuthenticatedEntity oauth2_remove_bucket_list(bucket_list_item_identifier, wink_version=wink_version, accept=accept)

Delete Bucket List Entry

Remove bucket list entry by entry identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.bucket_list_entry_view_authenticated_entity import BucketListEntryViewAuthenticatedEntity
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.BucketListApi(api_client)
    bucket_list_item_identifier = 'bucket_list_item_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Bucket List Entry
        api_response = api_instance.oauth2_remove_bucket_list(bucket_list_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of BucketListApi->oauth2_remove_bucket_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketListApi->oauth2_remove_bucket_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_list_item_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BucketListEntryViewAuthenticatedEntity**](BucketListEntryViewAuthenticatedEntity.md)

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

# **oauth2_show_bucket_list**
> List[BucketListEntryWrapperAuthenticatedEntity] oauth2_show_bucket_list(wink_version=wink_version, accept=accept)

Get Bucket Lists

Retrieve all bucket lists for caller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.bucket_list_entry_wrapper_authenticated_entity import BucketListEntryWrapperAuthenticatedEntity
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.BucketListApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Get Bucket Lists
        api_response = api_instance.oauth2_show_bucket_list(wink_version=wink_version, accept=accept)
        print("The response of BucketListApi->oauth2_show_bucket_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketListApi->oauth2_show_bucket_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BucketListEntryWrapperAuthenticatedEntity]**](BucketListEntryWrapperAuthenticatedEntity.md)

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

# **oauth2_show_bucket_list_entries**
> List[BucketListEntryAuthenticatedEntity] oauth2_show_bucket_list_entries(wink_version=wink_version, accept=accept)

Get Bucket List

Retrieve all bucket list entries for caller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.bucket_list_entry_authenticated_entity import BucketListEntryAuthenticatedEntity
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.BucketListApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Get Bucket List
        api_response = api_instance.oauth2_show_bucket_list_entries(wink_version=wink_version, accept=accept)
        print("The response of BucketListApi->oauth2_show_bucket_list_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketListApi->oauth2_show_bucket_list_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BucketListEntryAuthenticatedEntity]**](BucketListEntryAuthenticatedEntity.md)

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

# **oauth2_show_bucket_list_entry**
> BucketListEntryAuthenticatedEntity oauth2_show_bucket_list_entry(type, identifier, wink_version=wink_version, accept=accept)

Get Bucket List Entries

Retrieve bucket list entries for a specific by bucket list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.bucket_list_entry_authenticated_entity import BucketListEntryAuthenticatedEntity
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.BucketListApi(api_client)
    type = 'type_example' # str | 
    identifier = 'identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Get Bucket List Entries
        api_response = api_instance.oauth2_show_bucket_list_entry(type, identifier, wink_version=wink_version, accept=accept)
        print("The response of BucketListApi->oauth2_show_bucket_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketListApi->oauth2_show_bucket_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BucketListEntryAuthenticatedEntity**](BucketListEntryAuthenticatedEntity.md)

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

