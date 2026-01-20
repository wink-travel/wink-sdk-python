# wink_sdk_extranet_monetize.DailyRateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_rate**](DailyRateApi.md#bulk_update_rate) | **PUT** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rate/bulk | Update Daily Rates by Range
[**show_all_hotel_rates**](DailyRateApi.md#show_all_hotel_rates) | **POST** /api/property/{propertyIdentifier}/master-rate/rates/dates | Daily Rates by Hotel
[**show_all_master_rates_rates**](DailyRateApi.md#show_all_master_rates_rates) | **POST** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rates/dates | Daily Rates by Master Rate
[**show_daily_rates_page**](DailyRateApi.md#show_daily_rates_page) | **POST** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rate/grid | Show Daily Rate Page


# **bulk_update_rate**
> List[RateSupplier] bulk_update_rate(property_identifier, master_rate_identifier, upsert_bulk_rate_request_supplier, wink_version=wink_version)

Update Daily Rates by Range

Bulk update daily rates by date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_supplier import RateSupplier
from wink_sdk_extranet_monetize.models.upsert_bulk_rate_request_supplier import UpsertBulkRateRequestSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Update daily rates by date range owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Update daily rates by date range owned by this master rate.
    upsert_bulk_rate_request_supplier = wink_sdk_extranet_monetize.UpsertBulkRateRequestSupplier() # UpsertBulkRateRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Daily Rates by Range
        api_response = api_instance.bulk_update_rate(property_identifier, master_rate_identifier, upsert_bulk_rate_request_supplier, wink_version=wink_version)
        print("The response of DailyRateApi->bulk_update_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->bulk_update_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update daily rates by date range owned by this property identifier. | 
 **master_rate_identifier** | **str**| Update daily rates by date range owned by this master rate. | 
 **upsert_bulk_rate_request_supplier** | [**UpsertBulkRateRequestSupplier**](UpsertBulkRateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **show_all_hotel_rates**
> List[RateSupplier] show_all_hotel_rates(property_identifier, date_range_supplier, wink_version=wink_version)

Daily Rates by Hotel

Retrieve daily rates for all master rates by date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.date_range_supplier import DateRangeSupplier
from wink_sdk_extranet_monetize.models.rate_supplier import RateSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate list owned by this property identifier.
    date_range_supplier = wink_sdk_extranet_monetize.DateRangeSupplier() # DateRangeSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Daily Rates by Hotel
        api_response = api_instance.show_all_hotel_rates(property_identifier, date_range_supplier, wink_version=wink_version)
        print("The response of DailyRateApi->show_all_hotel_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->show_all_hotel_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show daily rate list owned by this property identifier. | 
 **date_range_supplier** | [**DateRangeSupplier**](DateRangeSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **show_all_master_rates_rates**
> List[RateSupplier] show_all_master_rates_rates(property_identifier, master_rate_identifier, date_range_supplier, wink_version=wink_version)

Daily Rates by Master Rate

Retrieve daily rates for a master rate for date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.date_range_supplier import DateRangeSupplier
from wink_sdk_extranet_monetize.models.rate_supplier import RateSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate list owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Show daily rate list owned by this master rate.
    date_range_supplier = wink_sdk_extranet_monetize.DateRangeSupplier() # DateRangeSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Daily Rates by Master Rate
        api_response = api_instance.show_all_master_rates_rates(property_identifier, master_rate_identifier, date_range_supplier, wink_version=wink_version)
        print("The response of DailyRateApi->show_all_master_rates_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->show_all_master_rates_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show daily rate list owned by this property identifier. | 
 **master_rate_identifier** | **str**| Show daily rate list owned by this master rate. | 
 **date_range_supplier** | [**DateRangeSupplier**](DateRangeSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **show_daily_rates_page**
> PageRateSupplier show_daily_rates_page(property_identifier, master_rate_identifier, state_supplier, wink_version=wink_version)

Show Daily Rate Page

Retrieve daily rates for a master rate within a certain date range.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.page_rate_supplier import PageRateSupplier
from wink_sdk_extranet_monetize.models.state_supplier import StateSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate page owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Show daily rate page owned by this master rate.
    state_supplier = wink_sdk_extranet_monetize.StateSupplier() # StateSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Daily Rate Page
        api_response = api_instance.show_daily_rates_page(property_identifier, master_rate_identifier, state_supplier, wink_version=wink_version)
        print("The response of DailyRateApi->show_daily_rates_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->show_daily_rates_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show daily rate page owned by this property identifier. | 
 **master_rate_identifier** | **str**| Show daily rate page owned by this master rate. | 
 **state_supplier** | [**StateSupplier**](StateSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageRateSupplier**](PageRateSupplier.md)

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

