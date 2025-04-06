# wink_sdk_affiliate_browse.BrowseApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_cities_for_inventory**](BrowseApi.md#show_cities_for_inventory) | **GET** /api/browse/supplier/city/list | Show Supplier Cities
[**show_cities_for_inventory_0**](BrowseApi.md#show_cities_for_inventory_0) | **GET** /api/browse/inventory/city/list | Show Inventory Cities
[**show_countries_for_inventory**](BrowseApi.md#show_countries_for_inventory) | **GET** /api/browse/inventory/country/list | Show Inventory Countries
[**show_countries_for_inventory_supplier**](BrowseApi.md#show_countries_for_inventory_supplier) | **GET** /api/browse/supplier/country/list | Show Supplier Countries
[**show_dynamic_seller_inventory**](BrowseApi.md#show_dynamic_seller_inventory) | **POST** /api/browse/inventory/grid | Inventory Search
[**show_dynamic_seller_inventory_by_id**](BrowseApi.md#show_dynamic_seller_inventory_by_id) | **GET** /api/browse/supplier/grid/{dynamicListIdentifier} | Supplier Search by Saved Search
[**show_dynamic_seller_inventory_by_id_0**](BrowseApi.md#show_dynamic_seller_inventory_by_id_0) | **GET** /api/browse/inventory/grid/{dynamicListIdentifier} | Inventory Search by Saved Search
[**show_inventory_supplier**](BrowseApi.md#show_inventory_supplier) | **GET** /api/browse/supplier/{supplierIdentifier}/sales-channel/{salesChannelIdentifier} | Show Supplier
[**show_latest_inventory**](BrowseApi.md#show_latest_inventory) | **GET** /api/browse/inventory/list | Latest Inventory
[**show_latest_inventory_supplier_list**](BrowseApi.md#show_latest_inventory_supplier_list) | **GET** /api/browse/supplier/list | Latest Suppliers
[**show_suppliers_for_dynamic_seller_inventory**](BrowseApi.md#show_suppliers_for_dynamic_seller_inventory) | **POST** /api/browse/supplier/grid | Supplier Search


# **show_cities_for_inventory**
> List[GeoNameAffiliate] show_cities_for_inventory(wink_version=wink_version, accept=accept)

Show Supplier Cities

Retrieve list of cities affiliate has access to.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.geo_name_affiliate import GeoNameAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier Cities
        api_response = api_instance.show_cities_for_inventory(wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_cities_for_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_cities_for_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[GeoNameAffiliate]**](GeoNameAffiliate.md)

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

# **show_cities_for_inventory_0**
> List[GeoNameAffiliate] show_cities_for_inventory_0(wink_version=wink_version, accept=accept)

Show Inventory Cities

Retrieve list of cities affiliate has access to.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.geo_name_affiliate import GeoNameAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Cities
        api_response = api_instance.show_cities_for_inventory_0(wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_cities_for_inventory_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_cities_for_inventory_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[GeoNameAffiliate]**](GeoNameAffiliate.md)

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

# **show_countries_for_inventory**
> List[CountryAffiliate] show_countries_for_inventory(wink_version=wink_version, accept=accept)

Show Inventory Countries

Retrieve list of countries affiliate has access to.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.country_affiliate import CountryAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Countries
        api_response = api_instance.show_countries_for_inventory(wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_countries_for_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_countries_for_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[CountryAffiliate]**](CountryAffiliate.md)

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

# **show_countries_for_inventory_supplier**
> List[CountryAffiliate] show_countries_for_inventory_supplier(wink_version=wink_version, accept=accept)

Show Supplier Countries

Retrieve list of countries affiliate has access to.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.country_affiliate import CountryAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier Countries
        api_response = api_instance.show_countries_for_inventory_supplier(wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_countries_for_inventory_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_countries_for_inventory_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[CountryAffiliate]**](CountryAffiliate.md)

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

# **show_dynamic_seller_inventory**
> PageInventoryViewAffiliate show_dynamic_seller_inventory(dynamic_seller_list_request_affiliate, wink_version=wink_version)

Inventory Search

Retrieves a paginated result set of inventorybased on the search criteria of the caller.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_request_affiliate import DynamicSellerListRequestAffiliate
from wink_sdk_affiliate_browse.models.page_inventory_view_affiliate import PageInventoryViewAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    dynamic_seller_list_request_affiliate = wink_sdk_affiliate_browse.DynamicSellerListRequestAffiliate() # DynamicSellerListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Inventory Search
        api_response = api_instance.show_dynamic_seller_inventory(dynamic_seller_list_request_affiliate, wink_version=wink_version)
        print("The response of BrowseApi->show_dynamic_seller_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_dynamic_seller_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_seller_list_request_affiliate** | [**DynamicSellerListRequestAffiliate**](DynamicSellerListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageInventoryViewAffiliate**](PageInventoryViewAffiliate.md)

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

# **show_dynamic_seller_inventory_by_id**
> PageInventorySupplierAffiliate show_dynamic_seller_inventory_by_id(dynamic_list_identifier, page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)

Supplier Search by Saved Search

Retrieves a paginated result set based on the given list identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.page_inventory_supplier_affiliate import PageInventorySupplierAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    dynamic_list_identifier = 'dynamic-list-1' # str | Browse inventory supplier on behalf of this dynamic list identifier.
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Skip to page. (optional) (default to 20)
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Supplier Search by Saved Search
        api_response = api_instance.show_dynamic_seller_inventory_by_id(dynamic_list_identifier, page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_dynamic_seller_inventory_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_dynamic_seller_inventory_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_list_identifier** | **str**| Browse inventory supplier on behalf of this dynamic list identifier. | 
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Skip to page. | [optional] [default to 20]
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PageInventorySupplierAffiliate**](PageInventorySupplierAffiliate.md)

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

# **show_dynamic_seller_inventory_by_id_0**
> PageInventoryViewAffiliate show_dynamic_seller_inventory_by_id_0(dynamic_list_identifier, page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)

Inventory Search by Saved Search

Retrieves a paginated result set based on the given saved search ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.page_inventory_view_affiliate import PageInventoryViewAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    dynamic_list_identifier = 'dynamic-list-1' # str | Browse inventory on behalf of this dynamic list identifier.
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Limit the size of results. (optional) (default to 20)
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Inventory Search by Saved Search
        api_response = api_instance.show_dynamic_seller_inventory_by_id_0(dynamic_list_identifier, page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_dynamic_seller_inventory_by_id_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_dynamic_seller_inventory_by_id_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_list_identifier** | **str**| Browse inventory on behalf of this dynamic list identifier. | 
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Limit the size of results. | [optional] [default to 20]
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PageInventoryViewAffiliate**](PageInventoryViewAffiliate.md)

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

# **show_inventory_supplier**
> InventorySupplierAffiliate show_inventory_supplier(supplier_identifier, sales_channel_identifier, display_currency=display_currency, wink_version=wink_version, accept=accept)

Show Supplier

Retrieves supplier details based on existing sales channel ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.inventory_supplier_affiliate import InventorySupplierAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    supplier_identifier = 'supplier-1' # str | Browse inventory supplier on behalf of this supplier identifier.
    sales_channel_identifier = 'sales-channel-1' # str | Browse inventory supplier on behalf of this sales channel identifier.
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier
        api_response = api_instance.show_inventory_supplier(supplier_identifier, sales_channel_identifier, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_inventory_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_inventory_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_identifier** | **str**| Browse inventory supplier on behalf of this supplier identifier. | 
 **sales_channel_identifier** | **str**| Browse inventory supplier on behalf of this sales channel identifier. | 
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventorySupplierAffiliate**](InventorySupplierAffiliate.md)

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

# **show_latest_inventory**
> List[InventoryViewAffiliate] show_latest_inventory(page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)

Latest Inventory

Retrieves a list of latest available inventory.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.inventory_view_affiliate import InventoryViewAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Skip to page. (optional) (default to 20)
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Latest Inventory
        api_response = api_instance.show_latest_inventory(page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_latest_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_latest_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Skip to page. | [optional] [default to 20]
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[InventoryViewAffiliate]**](InventoryViewAffiliate.md)

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

# **show_latest_inventory_supplier_list**
> List[InventorySupplierAffiliate] show_latest_inventory_supplier_list(page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)

Latest Suppliers

Retrieves a list of latest available inventorysuppliers.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.inventory_supplier_affiliate import InventorySupplierAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Skip to page. (optional) (default to 20)
    display_currency = 'USD' # str | Indicate which currency to display prices in. (optional) (default to 'USD')
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Latest Suppliers
        api_response = api_instance.show_latest_inventory_supplier_list(page=page, size=size, display_currency=display_currency, wink_version=wink_version, accept=accept)
        print("The response of BrowseApi->show_latest_inventory_supplier_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_latest_inventory_supplier_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Skip to page. | [optional] [default to 20]
 **display_currency** | **str**| Indicate which currency to display prices in. | [optional] [default to &#39;USD&#39;]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[InventorySupplierAffiliate]**](InventorySupplierAffiliate.md)

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

# **show_suppliers_for_dynamic_seller_inventory**
> PageInventorySupplierAffiliate show_suppliers_for_dynamic_seller_inventory(dynamic_seller_list_request_affiliate, wink_version=wink_version)

Supplier Search

Retrieves a paginated result set of suppliers of inventorybased on the search criteria of the caller.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.dynamic_seller_list_request_affiliate import DynamicSellerListRequestAffiliate
from wink_sdk_affiliate_browse.models.page_inventory_supplier_affiliate import PageInventorySupplierAffiliate
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
    api_instance = wink_sdk_affiliate_browse.BrowseApi(api_client)
    dynamic_seller_list_request_affiliate = wink_sdk_affiliate_browse.DynamicSellerListRequestAffiliate() # DynamicSellerListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Supplier Search
        api_response = api_instance.show_suppliers_for_dynamic_seller_inventory(dynamic_seller_list_request_affiliate, wink_version=wink_version)
        print("The response of BrowseApi->show_suppliers_for_dynamic_seller_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowseApi->show_suppliers_for_dynamic_seller_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_seller_list_request_affiliate** | [**DynamicSellerListRequestAffiliate**](DynamicSellerListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageInventorySupplierAffiliate**](PageInventorySupplierAffiliate.md)

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

