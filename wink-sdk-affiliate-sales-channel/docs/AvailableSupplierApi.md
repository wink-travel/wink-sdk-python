# wink_sdk_affiliate_sales_channel.AvailableSupplierApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_suppliers**](AvailableSupplierApi.md#browse_suppliers) | **POST** /api/affiliate/{companyIdentifier}/supplier/grid | Supplier Search
[**show_latest_supplier**](AvailableSupplierApi.md#show_latest_supplier) | **GET** /api/affiliate/{companyIdentifier}/supplier/list | Recent Supplier List
[**show_supplier**](AvailableSupplierApi.md#show_supplier) | **GET** /api/affiliate/{companyIdentifier}/supplier/{supplierIdentifier} | Show Supplier
[**show_unique_city_list**](AvailableSupplierApi.md#show_unique_city_list) | **GET** /api/affiliate/{companyIdentifier}/supplier/city/list | Cities by Supplier
[**show_unique_country_list**](AvailableSupplierApi.md#show_unique_country_list) | **GET** /api/affiliate/{companyIdentifier}/supplier/country/list | Countries by Supplier


# **browse_suppliers**
> PageHotelOnMapViewAffiliate browse_suppliers(company_identifier, state_affiliate, wink_version=wink_version)

Supplier Search

Retrieve page of available suppliers based on search criteria.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.page_hotel_on_map_view_affiliate import PageHotelOnMapViewAffiliate
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
    company_identifier = 'company_identifier_example' # str | The company ID to show suppliers for
    state_affiliate = wink_sdk_affiliate_sales_channel.StateAffiliate() # StateAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Supplier Search
        api_response = api_instance.browse_suppliers(company_identifier, state_affiliate, wink_version=wink_version)
        print("The response of AvailableSupplierApi->browse_suppliers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->browse_suppliers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| The company ID to show suppliers for | 
 **state_affiliate** | [**StateAffiliate**](StateAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageHotelOnMapViewAffiliate**](PageHotelOnMapViewAffiliate.md)

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

# **show_latest_supplier**
> List[HotelOnMapViewAffiliate] show_latest_supplier(company_identifier, page=page, size=size, wink_version=wink_version, accept=accept)

Recent Supplier List

Retrieves a list of recent suppliers.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.hotel_on_map_view_affiliate import HotelOnMapViewAffiliate
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
    company_identifier = 'owner-1' # str | Browse suppliers on behalf of this owner identifier.
    page = 0 # int | Skip to page. (optional) (default to 0)
    size = 20 # int | Skip to page. (optional) (default to 20)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Recent Supplier List
        api_response = api_instance.show_latest_supplier(company_identifier, page=page, size=size, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_latest_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_latest_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Browse suppliers on behalf of this owner identifier. | 
 **page** | **int**| Skip to page. | [optional] [default to 0]
 **size** | **int**| Skip to page. | [optional] [default to 20]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[HotelOnMapViewAffiliate]**](HotelOnMapViewAffiliate.md)

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

# **show_supplier**
> HotelOnMapViewAffiliate show_supplier(company_identifier, supplier_identifier, wink_version=wink_version, accept=accept)

Show Supplier

Retrieve supplier information specified by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.hotel_on_map_view_affiliate import HotelOnMapViewAffiliate
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
    company_identifier = 'company_identifier_example' # str | The company ID to show supplier for
    supplier_identifier = 'supplier_identifier_example' # str | The supplier ID to retrieve
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier
        api_response = api_instance.show_supplier(company_identifier, supplier_identifier, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| The company ID to show supplier for | 
 **supplier_identifier** | **str**| The supplier ID to retrieve | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**HotelOnMapViewAffiliate**](HotelOnMapViewAffiliate.md)

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

# **show_unique_city_list**
> List[KeyValuePairAffiliate] show_unique_city_list(company_identifier, wink_version=wink_version, accept=accept)

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
    company_identifier = 'company_identifier_example' # str | The company ID to show cities for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Cities by Supplier
        api_response = api_instance.show_unique_city_list(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_unique_city_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_unique_city_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| The company ID to show cities for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md)

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

# **show_unique_country_list**
> List[KeyValuePairAffiliate] show_unique_country_list(company_identifier, wink_version=wink_version, accept=accept)

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
    company_identifier = 'company_identifier_example' # str | The company ID to show countries for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Countries by Supplier
        api_response = api_instance.show_unique_country_list(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AvailableSupplierApi->show_unique_country_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableSupplierApi->show_unique_country_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| The company ID to show countries for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md)

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

