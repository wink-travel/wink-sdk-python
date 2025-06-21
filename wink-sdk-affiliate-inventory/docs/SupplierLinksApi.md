# wink_sdk_affiliate_inventory.SupplierLinksApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplier_url**](SupplierLinksApi.md#create_supplier_url) | **POST** /api/shareable-link/supplier | Create Link
[**create_supplier_url_syndication_entry**](SupplierLinksApi.md#create_supplier_url_syndication_entry) | **POST** /api/shareable-link/supplier/syndication/entry | Add to WinkLinks
[**remove_supplier_url**](SupplierLinksApi.md#remove_supplier_url) | **DELETE** /api/shareable-link/supplier/{supplierUrlIdentifier} | Delete Link
[**show_supplier_url**](SupplierLinksApi.md#show_supplier_url) | **GET** /api/shareable-link/supplier/{supplierUrlIdentifier} | Show Link
[**show_supplier_urls**](SupplierLinksApi.md#show_supplier_urls) | **GET** /api/shareable-link/supplier/list | Show Links
[**update_supplier_url**](SupplierLinksApi.md#update_supplier_url) | **PUT** /api/shareable-link/supplier/{supplierUrlIdentifier} | Update link


# **create_supplier_url**
> SellableSupplierUrlAffiliate create_supplier_url(upsert_sellable_supplier_url_request_affiliate, wink_version=wink_version)

Create Link

Create a new shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_supplier_url_affiliate import SellableSupplierUrlAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_supplier_url_request_affiliate import UpsertSellableSupplierUrlRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    upsert_sellable_supplier_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableSupplierUrlRequestAffiliate() # UpsertSellableSupplierUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Link
        api_response = api_instance.create_supplier_url(upsert_sellable_supplier_url_request_affiliate, wink_version=wink_version)
        print("The response of SupplierLinksApi->create_supplier_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->create_supplier_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_sellable_supplier_url_request_affiliate** | [**UpsertSellableSupplierUrlRequestAffiliate**](UpsertSellableSupplierUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellableSupplierUrlAffiliate**](SellableSupplierUrlAffiliate.md)

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

# **create_supplier_url_syndication_entry**
> SyndicatedItemAffiliate create_supplier_url_syndication_entry(create_supplier_url_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified link ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.create_supplier_url_syndication_entry_request_affiliate import CreateSupplierUrlSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.syndicated_item_affiliate import SyndicatedItemAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    create_supplier_url_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateSupplierUrlSyndicationEntryRequestAffiliate() # CreateSupplierUrlSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_supplier_url_syndication_entry(create_supplier_url_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of SupplierLinksApi->create_supplier_url_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->create_supplier_url_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_supplier_url_syndication_entry_request_affiliate** | [**CreateSupplierUrlSyndicationEntryRequestAffiliate**](CreateSupplierUrlSyndicationEntryRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicatedItemAffiliate**](SyndicatedItemAffiliate.md)

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

# **remove_supplier_url**
> SellableSupplierUrlAffiliate remove_supplier_url(supplier_url_identifier, wink_version=wink_version, accept=accept)

Delete Link

Delete a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_supplier_url_affiliate import SellableSupplierUrlAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    supplier_url_identifier = 'seller-url-1' # str | Remove url with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Link
        api_response = api_instance.remove_supplier_url(supplier_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of SupplierLinksApi->remove_supplier_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->remove_supplier_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_url_identifier** | **str**| Remove url with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableSupplierUrlAffiliate**](SellableSupplierUrlAffiliate.md)

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

# **show_supplier_url**
> SellableSupplierUrlAffiliate show_supplier_url(supplier_url_identifier, wink_version=wink_version, accept=accept)

Show Link

Retrieve a specific shareable url for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_supplier_url_affiliate import SellableSupplierUrlAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    supplier_url_identifier = 'owner-1' # str | Show link with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Link
        api_response = api_instance.show_supplier_url(supplier_url_identifier, wink_version=wink_version, accept=accept)
        print("The response of SupplierLinksApi->show_supplier_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->show_supplier_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_url_identifier** | **str**| Show link with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableSupplierUrlAffiliate**](SellableSupplierUrlAffiliate.md)

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

# **show_supplier_urls**
> List[SellableSupplierUrlAffiliate] show_supplier_urls(wink_version=wink_version, accept=accept)

Show Links

Retrieve list of shareable urls for this seller

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_supplier_url_affiliate import SellableSupplierUrlAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Links
        api_response = api_instance.show_supplier_urls(wink_version=wink_version, accept=accept)
        print("The response of SupplierLinksApi->show_supplier_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->show_supplier_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellableSupplierUrlAffiliate]**](SellableSupplierUrlAffiliate.md)

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

# **update_supplier_url**
> SellableSupplierUrlAffiliate update_supplier_url(supplier_url_identifier, upsert_sellable_supplier_url_request_affiliate, wink_version=wink_version)

Update link

Modify a shareable link

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.sellable_supplier_url_affiliate import SellableSupplierUrlAffiliate
from wink_sdk_affiliate_inventory.models.upsert_sellable_supplier_url_request_affiliate import UpsertSellableSupplierUrlRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.SupplierLinksApi(api_client)
    supplier_url_identifier = 'seller-url-1' # str | Update url with this identifier.
    upsert_sellable_supplier_url_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellableSupplierUrlRequestAffiliate() # UpsertSellableSupplierUrlRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update link
        api_response = api_instance.update_supplier_url(supplier_url_identifier, upsert_sellable_supplier_url_request_affiliate, wink_version=wink_version)
        print("The response of SupplierLinksApi->update_supplier_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierLinksApi->update_supplier_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_url_identifier** | **str**| Update url with this identifier. | 
 **upsert_sellable_supplier_url_request_affiliate** | [**UpsertSellableSupplierUrlRequestAffiliate**](UpsertSellableSupplierUrlRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellableSupplierUrlAffiliate**](SellableSupplierUrlAffiliate.md)

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

