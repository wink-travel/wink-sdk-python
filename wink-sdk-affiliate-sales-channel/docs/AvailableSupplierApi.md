# wink_sdk_affiliate_sales_channel.AvailableSupplierApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_suppliers**](AvailableSupplierApi.md#browse_suppliers) | **POST** /api/supplier/grid | Supplier Search
[**show_latest_supplier**](AvailableSupplierApi.md#show_latest_supplier) | **GET** /api/supplier/list | Recent Supplier List
[**show_supplier**](AvailableSupplierApi.md#show_supplier) | **GET** /api/supplier/{supplierIdentifier} | Show Supplier
[**show_unique_city_list**](AvailableSupplierApi.md#show_unique_city_list) | **GET** /api/supplier/city/list | Cities by Supplier
[**show_unique_country_list**](AvailableSupplierApi.md#show_unique_country_list) | **GET** /api/supplier/country/list | Countries by Supplier


# **browse_suppliers**
> PagePropertyAggregateLightweightAffiliate browse_suppliers(state_affiliate, wink_version=wink_version)

Supplier Search

Retrieve page of available suppliers based on search criteria.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.page_property_aggregate_lightweight_affiliate import PagePropertyAggregateLightweightAffiliate
from wink_sdk_affiliate_sales_channel.models.state_affiliate import StateAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    state_affiliate = wink_sdk_affiliate_sales_channel.StateAffiliate() # StateAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Supplier Search
        api_response = api_instance.browse_suppliers(state_affiliate, wink_version=wink_version)
        print("The response of AvailableSupplierApi->browse_suppliers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->browse_suppliers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_affiliate** | [**StateAffiliate**](StateAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PagePropertyAggregateLightweightAffiliate**](PagePropertyAggregateLightweightAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_latest_supplier**
> List[PropertyAggregateLightweightAffiliate] show_latest_supplier(page=page, size=size, wink_version=wink_version, accept=accept)

Recent Supplier List

Retrieves a list of recent suppliers.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.property_aggregate_lightweight_affiliate import PropertyAggregateLightweightAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Skip to page. (optional) (default to 20)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Recent Supplier List
        api_response = api_instance.show_latest_supplier(page=page, size=size, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_latest_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_latest_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Skip to page. | [optional] [default to 20]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[PropertyAggregateLightweightAffiliate]**](PropertyAggregateLightweightAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_supplier**
> PropertyAggregateLightweightAffiliate show_supplier(supplier_identifier, wink_version=wink_version, accept=accept)

Show Supplier

Retrieve supplier information specified by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.property_aggregate_lightweight_affiliate import PropertyAggregateLightweightAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    supplier_identifier = 'supplier_identifier_example' # str | The supplier ID to retrieve
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier
        api_response = api_instance.show_supplier(supplier_identifier, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_identifier** | **str**| The supplier ID to retrieve | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PropertyAggregateLightweightAffiliate**](PropertyAggregateLightweightAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_unique_city_list**
> List[KeyValuePairAffiliate] show_unique_city_list(wink_version=wink_version, accept=accept)

Cities by Supplier

Retrieve a list of unique cities where suppliers are based.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.key_value_pair_affiliate import KeyValuePairAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Cities by Supplier
        api_response = api_instance.show_unique_city_list(wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_unique_city_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_unique_city_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_unique_country_list**
> List[KeyValuePairAffiliate] show_unique_country_list(wink_version=wink_version, accept=accept)

Countries by Supplier

Retrieve a list of unique countries where suppliers are based

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.key_value_pair_affiliate import KeyValuePairAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.AvailableSupplierApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Countries by Supplier
        api_response = api_instance.show_unique_country_list(wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_unique_country_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_unique_country_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

