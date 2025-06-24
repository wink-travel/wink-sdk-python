# wink_sdk_extranet_distribution.DailyRateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_rate**](DailyRateApi.md#bulk_update_rate) | **PUT** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rate/bulk | Update Daily Rates by Range
[**create_test_booking**](DailyRateApi.md#create_test_booking) | **POST** /api/property/{propertyIdentifier}/sandbox/booking | Test Rate / Availability
[**show_all_hotel_rates**](DailyRateApi.md#show_all_hotel_rates) | **POST** /api/property/{propertyIdentifier}/master-rate/rates/dates | Daily Rates by Hotel
[**show_all_master_rates_rates**](DailyRateApi.md#show_all_master_rates_rates) | **POST** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rates/dates | Daily Rates by Master Rate
[**show_channels**](DailyRateApi.md#show_channels) | **GET** /api/property/{propertyIdentifier}/sandbox/channel/list | List Sales Channels
[**show_daily_rates_page**](DailyRateApi.md#show_daily_rates_page) | **POST** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/rate/grid | Show Daily Rate Page
[**show_descriptive_inventory**](DailyRateApi.md#show_descriptive_inventory) | **POST** /api/property/{propertyIdentifier}/sandbox/room/list | Test Rate / Availability
[**update_rate_list**](DailyRateApi.md#update_rate_list) | **PUT** /api/property/{propertyIdentifier}/rate/update | Update Daily Rates by List


# **bulk_update_rate**
> List[RateSupplier] bulk_update_rate(property_identifier, master_rate_identifier, upsert_bulk_rate_request_supplier, wink_version=wink_version)

Update Daily Rates by Range

Bulk update daily rates by date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.rate_supplier import RateSupplier
from wink_sdk_extranet_distribution.models.upsert_bulk_rate_request_supplier import UpsertBulkRateRequestSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Update daily rates by date range owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Update daily rates by date range owned by this master rate.
    upsert_bulk_rate_request_supplier = wink_sdk_extranet_distribution.UpsertBulkRateRequestSupplier() # UpsertBulkRateRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

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
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **create_test_booking**
> BookingSupplierDetails create_test_booking(property_identifier, booking_test_request_supplier_details, wink_version=wink_version)

Test Rate / Availability

Test whether the rates and availability for a sales channel is coming backing the way the property wants

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.booking_supplier_details import BookingSupplierDetails
from wink_sdk_extranet_distribution.models.booking_test_request_supplier_details import BookingTestRequestSupplierDetails
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Create test booking for property ID
    booking_test_request_supplier_details = wink_sdk_extranet_distribution.BookingTestRequestSupplierDetails() # BookingTestRequestSupplierDetails | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Test Rate / Availability
        api_response = api_instance.create_test_booking(property_identifier, booking_test_request_supplier_details, wink_version=wink_version)
        print("The response of DailyRateApi->create_test_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->create_test_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create test booking for property ID | 
 **booking_test_request_supplier_details** | [**BookingTestRequestSupplierDetails**](BookingTestRequestSupplierDetails.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingSupplierDetails**](BookingSupplierDetails.md)

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

# **show_all_hotel_rates**
> List[RateSupplier] show_all_hotel_rates(property_identifier, date_range_supplier, wink_version=wink_version)

Daily Rates by Hotel

Retrieve daily rates for all master rates by date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.date_range_supplier import DateRangeSupplier
from wink_sdk_extranet_distribution.models.rate_supplier import RateSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate list owned by this property identifier.
    date_range_supplier = wink_sdk_extranet_distribution.DateRangeSupplier() # DateRangeSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

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
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **show_all_master_rates_rates**
> List[RateSupplier] show_all_master_rates_rates(property_identifier, master_rate_identifier, date_range_supplier, wink_version=wink_version)

Daily Rates by Master Rate

Retrieve daily rates for a master rate for date range

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.date_range_supplier import DateRangeSupplier
from wink_sdk_extranet_distribution.models.rate_supplier import RateSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate list owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Show daily rate list owned by this master rate.
    date_range_supplier = wink_sdk_extranet_distribution.DateRangeSupplier() # DateRangeSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

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
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

# **show_channels**
> List[ChannelNameSupplier] show_channels(property_identifier, wink_version=wink_version, accept=accept)

List Sales Channels

List sales channels for property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.channel_name_supplier import ChannelNameSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Display existing sales channels for property ID
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # List Sales Channels
        api_response = api_instance.show_channels(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of DailyRateApi->show_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->show_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display existing sales channels for property ID | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ChannelNameSupplier]**](ChannelNameSupplier.md)

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

# **show_daily_rates_page**
> PageRateSupplier show_daily_rates_page(property_identifier, master_rate_identifier, state_supplier, wink_version=wink_version)

Show Daily Rate Page

Retrieve daily rates for a master rate within a certain date range.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.page_rate_supplier import PageRateSupplier
from wink_sdk_extranet_distribution.models.state_supplier import StateSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show daily rate page owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Show daily rate page owned by this master rate.
    state_supplier = wink_sdk_extranet_distribution.StateSupplier() # StateSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

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
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageRateSupplier**](PageRateSupplier.md)

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

# **show_descriptive_inventory**
> List[DescriptiveRoomSupplierDetails] show_descriptive_inventory(property_identifier, verify_rates_request_supplier_details, wink_version=wink_version)

Test Rate / Availability

Test whether the rates and availability for a sales channel is coming backing the way the property wants

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.descriptive_room_supplier_details import DescriptiveRoomSupplierDetails
from wink_sdk_extranet_distribution.models.verify_rates_request_supplier_details import VerifyRatesRequestSupplierDetails
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Display available room for property ID
    verify_rates_request_supplier_details = wink_sdk_extranet_distribution.VerifyRatesRequestSupplierDetails() # VerifyRatesRequestSupplierDetails | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Test Rate / Availability
        api_response = api_instance.show_descriptive_inventory(property_identifier, verify_rates_request_supplier_details, wink_version=wink_version)
        print("The response of DailyRateApi->show_descriptive_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->show_descriptive_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display available room for property ID | 
 **verify_rates_request_supplier_details** | [**VerifyRatesRequestSupplierDetails**](VerifyRatesRequestSupplierDetails.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[DescriptiveRoomSupplierDetails]**](DescriptiveRoomSupplierDetails.md)

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

# **update_rate_list**
> List[RateSupplier] update_rate_list(property_identifier, upsert_individual_rate_request_wrapper_supplier, wink_version=wink_version)

Update Daily Rates by List

Update daily rates with list of daily rate records.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.rate_supplier import RateSupplier
from wink_sdk_extranet_distribution.models.upsert_individual_rate_request_wrapper_supplier import UpsertIndividualRateRequestWrapperSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.DailyRateApi(api_client)
    property_identifier = 'hotel-1' # str | Update daily rates list owned by this property identifier.
    upsert_individual_rate_request_wrapper_supplier = [wink_sdk_extranet_distribution.UpsertIndividualRateRequestWrapperSupplier()] # List[UpsertIndividualRateRequestWrapperSupplier] | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Daily Rates by List
        api_response = api_instance.update_rate_list(property_identifier, upsert_individual_rate_request_wrapper_supplier, wink_version=wink_version)
        print("The response of DailyRateApi->update_rate_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DailyRateApi->update_rate_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update daily rates list owned by this property identifier. | 
 **upsert_individual_rate_request_wrapper_supplier** | [**List[UpsertIndividualRateRequestWrapperSupplier]**](UpsertIndividualRateRequestWrapperSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[RateSupplier]**](RateSupplier.md)

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

