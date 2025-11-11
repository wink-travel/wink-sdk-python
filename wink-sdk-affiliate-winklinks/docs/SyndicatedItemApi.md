# wink_sdk_affiliate_winklinks.SyndicatedItemApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_syndication_entry**](SyndicatedItemApi.md#create_syndication_entry) | **POST** /api/syndication/entry | Create WinkLinks Entry
[**remove_syndication_entry**](SyndicatedItemApi.md#remove_syndication_entry) | **DELETE** /api/syndication/entry/{syndicatedItemIdentifier} | Delete WinkLinks Entry
[**show_syndication_entry**](SyndicatedItemApi.md#show_syndication_entry) | **GET** /api/syndication/entry/{syndicatedItemIdentifier} | Show WinkLinks Entry
[**show_syndication_entry_list**](SyndicatedItemApi.md#show_syndication_entry_list) | **GET** /api/syndication/entry/list | Show WinkLinks Entries
[**sort_syndication_entry_list**](SyndicatedItemApi.md#sort_syndication_entry_list) | **PATCH** /api/syndication/entry/list/sort | Sort WinkLink Entries
[**update_syndication_entry**](SyndicatedItemApi.md#update_syndication_entry) | **PUT** /api/syndication/entry/{syndicatedItemIdentifier} | Update WinkLinks Entry


# **create_syndication_entry**
> SyndicatedItemAffiliate create_syndication_entry(upsert_syndicated_item_affiliate, wink_version=wink_version)

Create WinkLinks Entry

Creates a new syndication entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndicated_item_affiliate import UpsertSyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    upsert_syndicated_item_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicatedItemAffiliate() # UpsertSyndicatedItemAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create WinkLinks Entry
        api_response = api_instance.create_syndication_entry(upsert_syndicated_item_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->create_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->create_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_syndicated_item_affiliate** | [**UpsertSyndicatedItemAffiliate**](UpsertSyndicatedItemAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_syndication_entry**
> SyndicatedItemAffiliate remove_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)

Delete WinkLinks Entry

Deletes a syndication entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete WinkLinks Entry
        api_response = api_instance.remove_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicatedItemApi->remove_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->remove_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndicated_item_identifier** | **str**| Syndication entry identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_syndication_entry**
> SyndicatedItemAffiliate show_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)

Show WinkLinks Entry

Retrieve syndication entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Entry
        api_response = api_instance.show_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicatedItemApi->show_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->show_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndicated_item_identifier** | **str**| Syndication entry identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_syndication_entry_list**
> List[SyndicatedItemAffiliate] show_syndication_entry_list(status=status, wink_version=wink_version, accept=accept)

Show WinkLinks Entries

Retrieve list of syndication entries.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    status = PUBLISHED # str | Return based on this status. (optional) (default to PUBLISHED)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Entries
        api_response = api_instance.show_syndication_entry_list(status=status, wink_version=wink_version, accept=accept)
        print("The response of SyndicatedItemApi->show_syndication_entry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->show_syndication_entry_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Return based on this status. | [optional] [default to PUBLISHED]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SyndicatedItemAffiliate]**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sort_syndication_entry_list**
> List[SyndicatedItemAffiliate] sort_syndication_entry_list(sorted_affiliate, wink_version=wink_version)

Sort WinkLink Entries

Re-sorts all list entries.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.sorted_affiliate import SortedAffiliate
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    sorted_affiliate = [wink_sdk_affiliate_winklinks.SortedAffiliate()] # List[SortedAffiliate] | List if ids and their new sort slot
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Sort WinkLink Entries
        api_response = api_instance.sort_syndication_entry_list(sorted_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->sort_syndication_entry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->sort_syndication_entry_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorted_affiliate** | [**List[SortedAffiliate]**](SortedAffiliate.md)| List if ids and their new sort slot | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[SyndicatedItemAffiliate]**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_syndication_entry**
> SyndicatedItemAffiliate update_syndication_entry(syndicated_item_identifier, upsert_syndicated_item_affiliate, wink_version=wink_version)

Update WinkLinks Entry

Updates an existing syndication entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndicated_item_affiliate import UpsertSyndicatedItemAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicatedItemApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    upsert_syndicated_item_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicatedItemAffiliate() # UpsertSyndicatedItemAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update WinkLinks Entry
        api_response = api_instance.update_syndication_entry(syndicated_item_identifier, upsert_syndicated_item_affiliate, wink_version=wink_version)
        print("The response of SyndicatedItemApi->update_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicatedItemApi->update_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndicated_item_identifier** | **str**| Syndication entry identifier. | 
 **upsert_syndicated_item_affiliate** | [**UpsertSyndicatedItemAffiliate**](UpsertSyndicatedItemAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

