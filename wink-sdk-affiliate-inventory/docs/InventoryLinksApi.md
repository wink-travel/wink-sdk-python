# wink_sdk_affiliate_inventory.InventoryLinksApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_url**](InventoryLinksApi.md#create_seller_url) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/inventory | Create Link
[**create_supplier_url_syndication_entry1**](InventoryLinksApi.md#create_supplier_url_syndication_entry1) | **POST** /api/affiliate/{companyIdentifier}/shareable-link/inventory/syndication/entry | Add to WinkLinks
[**remove_seller_url**](InventoryLinksApi.md#remove_seller_url) | **DELETE** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Delete Link
[**show_inventory_media**](InventoryLinksApi.md#show_inventory_media) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{channelInventoryIdentifier}/media/list | Show Inventory Media
[**show_seller_url**](InventoryLinksApi.md#show_seller_url) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Show Link
[**show_seller_urls**](InventoryLinksApi.md#show_seller_urls) | **GET** /api/affiliate/{companyIdentifier}/shareable-link/inventory/list | Show Links
[**update_seller_url**](InventoryLinksApi.md#update_seller_url) | **PUT** /api/affiliate/{companyIdentifier}/shareable-link/inventory/{sellerUrlIdentifier} | Update link


# **create_seller_url**
> SellerUrlViewAffiliate create_seller_url(company_identifier, upsert_seller_url_request_affiliate, wink_version=wink_version)

Create Link

Create a new shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_url_request_affiliate import UpsertSellerUrlRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Create link owned by this owner identifier.
    upsert_seller_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerUrlRequestAffiliate() # UpsertSellerUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Link
        api_response = api_instance.create_seller_url(company_identifier, upsert_seller_url_request_affiliate, wink_version=wink_version)
        print("The response of InventoryLinksApi->create_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->create_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create link owned by this owner identifier. | 
 **upsert_seller_url_request_affiliate** | [**UpsertSellerUrlRequestAffiliate**](UpsertSellerUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerUrlViewAffiliate**](SellerUrlViewAffiliate.md)

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

# **create_supplier_url_syndication_entry1**
> BooleanResponseAffiliate create_supplier_url_syndication_entry1(company_identifier, create_seller_url_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified link ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.boolean_response_affiliate import BooleanResponseAffiliate
from wink_sdk_affiliate_inventory.models.create_seller_url_syndication_entry_request_affiliate import CreateSellerUrlSyndicationEntryRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to create item for
    create_seller_url_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateSellerUrlSyndicationEntryRequestAffiliate() # CreateSellerUrlSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_supplier_url_syndication_entry1(company_identifier, create_seller_url_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of InventoryLinksApi->create_supplier_url_syndication_entry1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->create_supplier_url_syndication_entry1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to create item for | 
 **create_seller_url_syndication_entry_request_affiliate** | [**CreateSellerUrlSyndicationEntryRequestAffiliate**](CreateSellerUrlSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseAffiliate**](BooleanResponseAffiliate.md)

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

# **remove_seller_url**
> SellerUrlViewAffiliate remove_seller_url(company_identifier, seller_url_identifier, wink_version=wink_version, accept=accept)

Delete Link

Delete a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Remove link owned by this owner identifier.
    seller_url_identifier = 'seller-url-1' # str | Remove url with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Link
        api_response = api_instance.remove_seller_url(company_identifier, seller_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->remove_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->remove_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove link owned by this owner identifier. | 
 **seller_url_identifier** | **str**| Remove url with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerUrlViewAffiliate**](SellerUrlViewAffiliate.md)

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

# **show_inventory_media**
> List[SimpleMultimediaAffiliate] show_inventory_media(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)

Show Inventory Media

Retrieve a list of media for this channel blocking identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.simple_multimedia_affiliate import SimpleMultimediaAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Owner identifier.
    channel_inventory_identifier = 'channel-blocking-1' # str | Channel blocking identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Media
        api_response = api_instance.show_inventory_media(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_inventory_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_inventory_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Owner identifier. | 
 **channel_inventory_identifier** | **str**| Channel blocking identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md)

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

# **show_seller_url**
> SellerUrlViewAffiliate show_seller_url(company_identifier, seller_url_identifier, wink_version=wink_version, accept=accept)

Show Link

Retrieve a specific shareable url for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Show link owned by this owner identifier.
    seller_url_identifier = 'owner-1' # str | Show link with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Link
        api_response = api_instance.show_seller_url(company_identifier, seller_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show link owned by this owner identifier. | 
 **seller_url_identifier** | **str**| Show link with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerUrlViewAffiliate**](SellerUrlViewAffiliate.md)

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

# **show_seller_urls**
> List[SellerUrlViewAffiliate] show_seller_urls(company_identifier, wink_version=wink_version, accept=accept)

Show Links

Retrieve list of shareable urls for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Show links list owned by this owner identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Links
        api_response = api_instance.show_seller_urls(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_seller_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_seller_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show links list owned by this owner identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellerUrlViewAffiliate]**](SellerUrlViewAffiliate.md)

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

# **update_seller_url**
> SellerUrlViewAffiliate update_seller_url(company_identifier, seller_url_identifier, upsert_seller_url_request_affiliate, wink_version=wink_version)

Update link

Modify a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_url_request_affiliate import UpsertSellerUrlRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.InventoryLinksApi(api_client)
    company_identifier = 'owner-1' # str | Update link owned by this owner identifier.
    seller_url_identifier = 'seller-url-1' # str | Update url with this identifier.
    upsert_seller_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerUrlRequestAffiliate() # UpsertSellerUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update link
        api_response = api_instance.update_seller_url(company_identifier, seller_url_identifier, upsert_seller_url_request_affiliate, wink_version=wink_version)
        print("The response of InventoryLinksApi->update_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->update_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update link owned by this owner identifier. | 
 **seller_url_identifier** | **str**| Update url with this identifier. | 
 **upsert_seller_url_request_affiliate** | [**UpsertSellerUrlRequestAffiliate**](UpsertSellerUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerUrlViewAffiliate**](SellerUrlViewAffiliate.md)

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

