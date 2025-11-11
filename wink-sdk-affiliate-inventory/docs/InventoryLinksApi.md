# wink_sdk_affiliate_inventory.InventoryLinksApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_url**](InventoryLinksApi.md#create_seller_url) | **POST** /api/shareable-link/inventory | Create Link
[**remove_seller_url**](InventoryLinksApi.md#remove_seller_url) | **DELETE** /api/shareable-link/inventory/{sellerUrlIdentifier} | Delete Link
[**show_inventory_media**](InventoryLinksApi.md#show_inventory_media) | **GET** /api/shareable-link/inventory/{channelInventoryIdentifier}/media/list | Show Inventory Media
[**show_seller_url**](InventoryLinksApi.md#show_seller_url) | **GET** /api/shareable-link/inventory/{sellerUrlIdentifier} | Show Link
[**show_seller_urls**](InventoryLinksApi.md#show_seller_urls) | **GET** /api/shareable-link/inventory/list | Show Links
[**update_seller_url**](InventoryLinksApi.md#update_seller_url) | **PUT** /api/shareable-link/inventory/{sellerUrlIdentifier} | Update link


# **create_seller_url**
> SellableInventoryUrlAffiliate create_seller_url(upsert_sellable_inventory_url_request_affiliate, wink_version=wink_version)

Create Link

Create a new shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_inventory_url_request_affiliate import UpsertSellableInventoryUrlRequestAffiliate
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
    upsert_sellable_inventory_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableInventoryUrlRequestAffiliate() # UpsertSellableInventoryUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Link
        api_response = api_instance.create_seller_url(upsert_sellable_inventory_url_request_affiliate, wink_version=wink_version)
        print("The response of InventoryLinksApi->create_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->create_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_sellable_inventory_url_request_affiliate** | [**UpsertSellableInventoryUrlRequestAffiliate**](UpsertSellableInventoryUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellableInventoryUrlAffiliate**](SellableInventoryUrlAffiliate.md)

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

# **remove_seller_url**
> SellableInventoryUrlAffiliate remove_seller_url(seller_url_identifier, wink_version=wink_version, accept=accept)

Delete Link

Delete a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate
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
    seller_url_identifier = 'seller-url-1' # str | Remove url with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Link
        api_response = api_instance.remove_seller_url(seller_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->remove_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->remove_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_url_identifier** | **str**| Remove url with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableInventoryUrlAffiliate**](SellableInventoryUrlAffiliate.md)

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

# **show_inventory_media**
> List[SimpleMultimediaAffiliate] show_inventory_media(channel_inventory_identifier, wink_version=wink_version, accept=accept)

Show Inventory Media

Retrieve a list of media for this channel inventory identifier

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
    channel_inventory_identifier = 'channel-blocking-1' # str | Channel inventory identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Media
        api_response = api_instance.show_inventory_media(channel_inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_inventory_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_inventory_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_inventory_identifier** | **str**| Channel inventory identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md)

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

# **show_seller_url**
> SellableInventoryUrlAffiliate show_seller_url(seller_url_identifier, wink_version=wink_version, accept=accept)

Show Link

Retrieve a specific shareable url for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate
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
    seller_url_identifier = 'owner-1' # str | Show link with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Link
        api_response = api_instance.show_seller_url(seller_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_url_identifier** | **str**| Show link with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableInventoryUrlAffiliate**](SellableInventoryUrlAffiliate.md)

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

# **show_seller_urls**
> List[SellableInventoryUrlAffiliate] show_seller_urls(wink_version=wink_version, accept=accept)

Show Links

Retrieve list of shareable urls for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate
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
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Links
        api_response = api_instance.show_seller_urls(wink_version=wink_version, accept=accept)
        print("The response of InventoryLinksApi->show_seller_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->show_seller_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellableInventoryUrlAffiliate]**](SellableInventoryUrlAffiliate.md)

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

# **update_seller_url**
> SellableInventoryUrlAffiliate update_seller_url(seller_url_identifier, upsert_sellable_inventory_url_request_affiliate, wink_version=wink_version)

Update link

Modify a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_inventory_url_request_affiliate import UpsertSellableInventoryUrlRequestAffiliate
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
    seller_url_identifier = 'seller-url-1' # str | Update url with this identifier.
    upsert_sellable_inventory_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableInventoryUrlRequestAffiliate() # UpsertSellableInventoryUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update link
        api_response = api_instance.update_seller_url(seller_url_identifier, upsert_sellable_inventory_url_request_affiliate, wink_version=wink_version)
        print("The response of InventoryLinksApi->update_seller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryLinksApi->update_seller_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_url_identifier** | **str**| Update url with this identifier. | 
 **upsert_sellable_inventory_url_request_affiliate** | [**UpsertSellableInventoryUrlRequestAffiliate**](UpsertSellableInventoryUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellableInventoryUrlAffiliate**](SellableInventoryUrlAffiliate.md)

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

