# wink_sdk_affiliate_winklinks.SyndicationPublisherApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_syndication_category**](SyndicationPublisherApi.md#create_syndication_category) | **POST** /api/syndication/category | Create WinkLinks Category
[**create_syndication_entry**](SyndicationPublisherApi.md#create_syndication_entry) | **POST** /api/syndication/entry | Create WinkLinks Entry
[**remove_syndication_category**](SyndicationPublisherApi.md#remove_syndication_category) | **DELETE** /api/syndication/category/{syndicationCategoryIdentifier} | Delete WinkLinks Category
[**remove_syndication_entry**](SyndicationPublisherApi.md#remove_syndication_entry) | **DELETE** /api/syndication/entry/{syndicatedItemIdentifier} | Delete WinkLinks Entry
[**show_syndication_category**](SyndicationPublisherApi.md#show_syndication_category) | **GET** /api/syndication/category/{syndicationCategoryIdentifier} | Show WinkLinks Category
[**show_syndication_category_list**](SyndicationPublisherApi.md#show_syndication_category_list) | **GET** /api/syndication/category/list | Show WinkLinks Categories
[**show_syndication_entry**](SyndicationPublisherApi.md#show_syndication_entry) | **GET** /api/syndication/entry/{syndicatedItemIdentifier} | Show WinkLinks Entry
[**show_syndication_entry_list**](SyndicationPublisherApi.md#show_syndication_entry_list) | **GET** /api/syndication/entry/list | Show WinkLinks Entries
[**show_syndication_settings**](SyndicationPublisherApi.md#show_syndication_settings) | **GET** /api/syndication/settings | Show WinkLinks Settings
[**sort_syndication_entry_list**](SyndicationPublisherApi.md#sort_syndication_entry_list) | **PATCH** /api/syndication/entry/list/sort | Sort WinkLink Entries
[**update_syndication_category**](SyndicationPublisherApi.md#update_syndication_category) | **PUT** /api/syndication/category/{syndicationCategoryIdentifier} | Update WinkLinks Category
[**update_syndication_entry**](SyndicationPublisherApi.md#update_syndication_entry) | **PUT** /api/syndication/entry/{syndicatedItemIdentifier} | Update WinkLinks Entry
[**upsert_syndication_settings**](SyndicationPublisherApi.md#upsert_syndication_settings) | **PUT** /api/syndication/settings | Upsert WinkLinks Settings


# **create_syndication_category**
> SyndicationCategoryAffiliate create_syndication_category(upsert_syndication_category_affiliate, wink_version=wink_version)

Create WinkLinks Category

Creates a new syndication category.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_category_affiliate import UpsertSyndicationCategoryAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    upsert_syndication_category_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationCategoryAffiliate() # UpsertSyndicationCategoryAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create WinkLinks Category
        api_response = api_instance.create_syndication_category(upsert_syndication_category_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->create_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->create_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_syndication_category_affiliate** | [**UpsertSyndicationCategoryAffiliate**](UpsertSyndicationCategoryAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicationCategoryAffiliate**](SyndicationCategoryAffiliate.md)

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    upsert_syndicated_item_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicatedItemAffiliate() # UpsertSyndicatedItemAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create WinkLinks Entry
        api_response = api_instance.create_syndication_entry(upsert_syndicated_item_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->create_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->create_syndication_entry: %s\n" % e)
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

# **remove_syndication_category**
> SyndicationCategoryAffiliate remove_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)

Delete WinkLinks Category

Deletes a syndication category.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete WinkLinks Category
        api_response = api_instance.remove_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->remove_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->remove_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicationCategoryAffiliate**](SyndicationCategoryAffiliate.md)

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete WinkLinks Entry
        api_response = api_instance.remove_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->remove_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->remove_syndication_entry: %s\n" % e)
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

# **show_syndication_category**
> SyndicationCategoryAffiliate show_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)

Show WinkLinks Category

Retrieve syndication category.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Category
        api_response = api_instance.show_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->show_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->show_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicationCategoryAffiliate**](SyndicationCategoryAffiliate.md)

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

# **show_syndication_category_list**
> List[SyndicationCategoryAffiliate] show_syndication_category_list(wink_version=wink_version, accept=accept)

Show WinkLinks Categories

Retrieve list of syndication categories.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Categories
        api_response = api_instance.show_syndication_category_list(wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->show_syndication_category_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->show_syndication_category_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SyndicationCategoryAffiliate]**](SyndicationCategoryAffiliate.md)

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Entry
        api_response = api_instance.show_syndication_entry(syndicated_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->show_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->show_syndication_entry: %s\n" % e)
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    status = PUBLISHED # str | Return based on this status. (optional) (default to PUBLISHED)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Entries
        api_response = api_instance.show_syndication_entry_list(status=status, wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->show_syndication_entry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->show_syndication_entry_list: %s\n" % e)
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

# **show_syndication_settings**
> SyndicationSettingsWithThemeColorsAffiliate show_syndication_settings(wink_version=wink_version, accept=accept)

Show WinkLinks Settings

Load WinkLinks settings.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_settings_with_theme_colors_affiliate import SyndicationSettingsWithThemeColorsAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Settings
        api_response = api_instance.show_syndication_settings(wink_version=wink_version, accept=accept)
        print("The response of SyndicationPublisherApi->show_syndication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->show_syndication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicationSettingsWithThemeColorsAffiliate**](SyndicationSettingsWithThemeColorsAffiliate.md)

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    sorted_affiliate = [wink_sdk_affiliate_winklinks.SortedAffiliate()] # List[SortedAffiliate] | List if ids and their new sort slot
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Sort WinkLink Entries
        api_response = api_instance.sort_syndication_entry_list(sorted_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->sort_syndication_entry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->sort_syndication_entry_list: %s\n" % e)
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

# **update_syndication_category**
> SyndicationCategoryAffiliate update_syndication_category(syndication_category_identifier, upsert_syndication_category_affiliate, wink_version=wink_version)

Update WinkLinks Category

Updates an existing syndication category.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_category_affiliate import UpsertSyndicationCategoryAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    upsert_syndication_category_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationCategoryAffiliate() # UpsertSyndicationCategoryAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update WinkLinks Category
        api_response = api_instance.update_syndication_category(syndication_category_identifier, upsert_syndication_category_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->update_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->update_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **upsert_syndication_category_affiliate** | [**UpsertSyndicationCategoryAffiliate**](UpsertSyndicationCategoryAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicationCategoryAffiliate**](SyndicationCategoryAffiliate.md)

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    syndicated_item_identifier = 'syndication-entry-1' # str | Syndication entry identifier.
    upsert_syndicated_item_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicatedItemAffiliate() # UpsertSyndicatedItemAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update WinkLinks Entry
        api_response = api_instance.update_syndication_entry(syndicated_item_identifier, upsert_syndicated_item_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->update_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->update_syndication_entry: %s\n" % e)
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

# **upsert_syndication_settings**
> SyndicationSettingsWithThemeColorsAffiliate upsert_syndication_settings(upsert_syndication_settings_affiliate, wink_version=wink_version)

Upsert WinkLinks Settings

Upsert a new syndication settings.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_settings_with_theme_colors_affiliate import SyndicationSettingsWithThemeColorsAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_settings_affiliate import UpsertSyndicationSettingsAffiliate
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationPublisherApi(api_client)
    upsert_syndication_settings_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationSettingsAffiliate() # UpsertSyndicationSettingsAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Upsert WinkLinks Settings
        api_response = api_instance.upsert_syndication_settings(upsert_syndication_settings_affiliate, wink_version=wink_version)
        print("The response of SyndicationPublisherApi->upsert_syndication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationPublisherApi->upsert_syndication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_syndication_settings_affiliate** | [**UpsertSyndicationSettingsAffiliate**](UpsertSyndicationSettingsAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicationSettingsWithThemeColorsAffiliate**](SyndicationSettingsWithThemeColorsAffiliate.md)

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

