# wink_sdk_affiliate_inventory.ItemsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seller_inventory_item**](ItemsApi.md#create_seller_inventory_item) | **POST** /api/affiliate/{companyIdentifier}/items | Create Item
[**create_seller_inventory_item_syndication_entry**](ItemsApi.md#create_seller_inventory_item_syndication_entry) | **POST** /api/affiliate/{companyIdentifier}/items/syndication/entry | Add to WinkLinks
[**create_supplier_seller_inventory_item**](ItemsApi.md#create_supplier_seller_inventory_item) | **POST** /api/affiliate/{companyIdentifier}/items/supplier | Create Supplier Item
[**remove_seller_inventory_item**](ItemsApi.md#remove_seller_inventory_item) | **DELETE** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Delete Item
[**show_inventory_media1**](ItemsApi.md#show_inventory_media1) | **GET** /api/affiliate/{companyIdentifier}/items/inventory/{channelInventoryIdentifier}/media/list | Show Item Media
[**show_seller_inventory_item**](ItemsApi.md#show_seller_inventory_item) | **GET** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Show Item
[**show_seller_inventory_items_for_company**](ItemsApi.md#show_seller_inventory_items_for_company) | **GET** /api/affiliate/{companyIdentifier}/items/list | Show Items
[**update_seller_inventory_item**](ItemsApi.md#update_seller_inventory_item) | **PUT** /api/affiliate/{companyIdentifier}/items/{inventoryIdentifier} | Update Item


# **create_seller_inventory_item**
> SellerInventoryItemViewAffiliate create_seller_inventory_item(company_identifier, upsert_seller_inventory_item_request_affiliate, wink_version=wink_version)

Create Item

Create a new blocking card

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_item_request_affiliate import UpsertSellerInventoryItemRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to create item for
    upsert_seller_inventory_item_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerInventoryItemRequestAffiliate() # UpsertSellerInventoryItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Item
        api_response = api_instance.create_seller_inventory_item(company_identifier, upsert_seller_inventory_item_request_affiliate, wink_version=wink_version)
        print("The response of ItemsApi->create_seller_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_seller_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to create item for | 
 **upsert_seller_inventory_item_request_affiliate** | [**UpsertSellerInventoryItemRequestAffiliate**](UpsertSellerInventoryItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerInventoryItemViewAffiliate**](SellerInventoryItemViewAffiliate.md)

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

# **create_seller_inventory_item_syndication_entry**
> BooleanResponseAffiliate create_seller_inventory_item_syndication_entry(company_identifier, create_seller_inventory_item_syndication_entry_request_affiliate, wink_version=wink_version)

Add to WinkLinks

Creates a new WinkLinks entry from the specified item ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.boolean_response_affiliate import BooleanResponseAffiliate
from wink_sdk_affiliate_inventory.models.create_seller_inventory_item_syndication_entry_request_affiliate import CreateSellerInventoryItemSyndicationEntryRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to create item for
    create_seller_inventory_item_syndication_entry_request_affiliate = wink_sdk_affiliate_inventory.CreateSellerInventoryItemSyndicationEntryRequestAffiliate() # CreateSellerInventoryItemSyndicationEntryRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add to WinkLinks
        api_response = api_instance.create_seller_inventory_item_syndication_entry(company_identifier, create_seller_inventory_item_syndication_entry_request_affiliate, wink_version=wink_version)
        print("The response of ItemsApi->create_seller_inventory_item_syndication_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_seller_inventory_item_syndication_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to create item for | 
 **create_seller_inventory_item_syndication_entry_request_affiliate** | [**CreateSellerInventoryItemSyndicationEntryRequestAffiliate**](CreateSellerInventoryItemSyndicationEntryRequestAffiliate.md)|  | 
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

# **create_supplier_seller_inventory_item**
> SellerInventoryItemViewAffiliate create_supplier_seller_inventory_item(company_identifier, upsert_supplier_seller_inventory_item_request_affiliate, wink_version=wink_version)

Create Supplier Item

Creates a new blocking card for a supplier showing the best priced room.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_seller_inventory_item_request_affiliate import UpsertSupplierSellerInventoryItemRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to create item for
    upsert_supplier_seller_inventory_item_request_affiliate = wink_sdk_affiliate_inventory.UpsertSupplierSellerInventoryItemRequestAffiliate() # UpsertSupplierSellerInventoryItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Supplier Item
        api_response = api_instance.create_supplier_seller_inventory_item(company_identifier, upsert_supplier_seller_inventory_item_request_affiliate, wink_version=wink_version)
        print("The response of ItemsApi->create_supplier_seller_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_supplier_seller_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to create item for | 
 **upsert_supplier_seller_inventory_item_request_affiliate** | [**UpsertSupplierSellerInventoryItemRequestAffiliate**](UpsertSupplierSellerInventoryItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerInventoryItemViewAffiliate**](SellerInventoryItemViewAffiliate.md)

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

# **remove_seller_inventory_item**
> SellerInventoryItemViewAffiliate remove_seller_inventory_item(company_identifier, inventory_identifier, wink_version=wink_version, accept=accept)

Delete Item

Remove a unique blocking item

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to delete item from
    inventory_identifier = 'card-blocking-1' # str | Delete blocking with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Item
        api_response = api_instance.remove_seller_inventory_item(company_identifier, inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of ItemsApi->remove_seller_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->remove_seller_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to delete item from | 
 **inventory_identifier** | **str**| Delete blocking with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryItemViewAffiliate**](SellerInventoryItemViewAffiliate.md)

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

# **show_inventory_media1**
> List[SimpleMultimediaAffiliate] show_inventory_media1(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)

Show Item Media

Retrieve list of all media associated with this channel blocking identifier.

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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to retrieve items for
    channel_inventory_identifier = 'channel-blocking-1' # str | Retrieve media for this channel blocking identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Item Media
        api_response = api_instance.show_inventory_media1(company_identifier, channel_inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of ItemsApi->show_inventory_media1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->show_inventory_media1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to retrieve items for | 
 **channel_inventory_identifier** | **str**| Retrieve media for this channel blocking identifier. | 
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

# **show_seller_inventory_item**
> SellerInventoryItemViewAffiliate show_seller_inventory_item(company_identifier, inventory_identifier, wink_version=wink_version, accept=accept)

Show Item

Retrieve a single blocking card.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to retrieve item for
    inventory_identifier = 'card-blocking-1' # str | Retrieve blocking with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Item
        api_response = api_instance.show_seller_inventory_item(company_identifier, inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of ItemsApi->show_seller_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->show_seller_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to retrieve item for | 
 **inventory_identifier** | **str**| Retrieve blocking with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryItemViewAffiliate**](SellerInventoryItemViewAffiliate.md)

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

# **show_seller_inventory_items_for_company**
> List[SellerInventoryItemViewAffiliate] show_seller_inventory_items_for_company(company_identifier, wink_version=wink_version, accept=accept)

Show Items

Retrieve a list of all saved inventories for company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to retrieve items for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Items
        api_response = api_instance.show_seller_inventory_items_for_company(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of ItemsApi->show_seller_inventory_items_for_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->show_seller_inventory_items_for_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to retrieve items for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SellerInventoryItemViewAffiliate]**](SellerInventoryItemViewAffiliate.md)

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

# **update_seller_inventory_item**
> SellerInventoryItemViewAffiliate update_seller_inventory_item(company_identifier, inventory_identifier, upsert_seller_inventory_item_request_affiliate, wink_version=wink_version)

Update Item

Update an existing card

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_item_request_affiliate import UpsertSellerInventoryItemRequestAffiliate
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
    api_instance = wink_sdk_affiliate_inventory.ItemsApi(api_client)
    company_identifier = 'company_identifier_example' # str | Company identifier to update item for
    inventory_identifier = 'card-blocking-1' # str | Update blocking with this identifier.
    upsert_seller_inventory_item_request_affiliate = wink_sdk_affiliate_inventory.UpsertSellerInventoryItemRequestAffiliate() # UpsertSellerInventoryItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Item
        api_response = api_instance.update_seller_inventory_item(company_identifier, inventory_identifier, upsert_seller_inventory_item_request_affiliate, wink_version=wink_version)
        print("The response of ItemsApi->update_seller_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_seller_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Company identifier to update item for | 
 **inventory_identifier** | **str**| Update blocking with this identifier. | 
 **upsert_seller_inventory_item_request_affiliate** | [**UpsertSellerInventoryItemRequestAffiliate**](UpsertSellerInventoryItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SellerInventoryItemViewAffiliate**](SellerInventoryItemViewAffiliate.md)

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

