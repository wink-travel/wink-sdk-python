# wink_sdk_affiliate_winklinks.SyndicationCategoryApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_syndication_category**](SyndicationCategoryApi.md#create_syndication_category) | **POST** /api/syndication/category | Create WinkLinks Category
[**remove_syndication_category**](SyndicationCategoryApi.md#remove_syndication_category) | **DELETE** /api/syndication/category/{syndicationCategoryIdentifier} | Delete WinkLinks Category
[**show_syndication_category**](SyndicationCategoryApi.md#show_syndication_category) | **GET** /api/syndication/category/{syndicationCategoryIdentifier} | Show WinkLinks Category
[**show_syndication_category_list**](SyndicationCategoryApi.md#show_syndication_category_list) | **GET** /api/syndication/category/list | Show WinkLinks Categories
[**update_syndication_category**](SyndicationCategoryApi.md#update_syndication_category) | **PUT** /api/syndication/category/{syndicationCategoryIdentifier} | Update WinkLinks Category


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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationCategoryApi(api_client)
    upsert_syndication_category_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationCategoryAffiliate() # UpsertSyndicationCategoryAffiliate | Request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create WinkLinks Category
        api_response = api_instance.create_syndication_category(upsert_syndication_category_affiliate, wink_version=wink_version)
        print("The response of SyndicationCategoryApi->create_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationCategoryApi->create_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_syndication_category_affiliate** | [**UpsertSyndicationCategoryAffiliate**](UpsertSyndicationCategoryAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationCategoryApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete WinkLinks Category
        api_response = api_instance.remove_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationCategoryApi->remove_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationCategoryApi->remove_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationCategoryApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Category
        api_response = api_instance.show_syndication_category(syndication_category_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationCategoryApi->show_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationCategoryApi->show_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationCategoryApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Categories
        api_response = api_instance.show_syndication_category_list(wink_version=wink_version, accept=accept)
        print("The response of SyndicationCategoryApi->show_syndication_category_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationCategoryApi->show_syndication_category_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationCategoryApi(api_client)
    syndication_category_identifier = 'syndication-category-1' # str | Syndication category identifier.
    upsert_syndication_category_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationCategoryAffiliate() # UpsertSyndicationCategoryAffiliate | Request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update WinkLinks Category
        api_response = api_instance.update_syndication_category(syndication_category_identifier, upsert_syndication_category_affiliate, wink_version=wink_version)
        print("The response of SyndicationCategoryApi->update_syndication_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationCategoryApi->update_syndication_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syndication_category_identifier** | **str**| Syndication category identifier. | 
 **upsert_syndication_category_affiliate** | [**UpsertSyndicationCategoryAffiliate**](UpsertSyndicationCategoryAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

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

