# wink_sdk_extranet_booking.PropertyBookingApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_hotel_booking**](PropertyBookingApi.md#cancel_hotel_booking) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancel | Cancel Booking
[**generate_booking_report**](PropertyBookingApi.md#generate_booking_report) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/report/pdf | Download Booking
[**is_booking_cancellable**](PropertyBookingApi.md#is_booking_cancellable) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancellable | Is Booking Cancellable
[**request_refund**](PropertyBookingApi.md#request_refund) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/request-refund | Request refund
[**resend_booking_confirmation_email**](PropertyBookingApi.md#resend_booking_confirmation_email) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/resend | Resend Booking Confirmation
[**show_active_affiliates**](PropertyBookingApi.md#show_active_affiliates) | **GET** /api/property/{propertyIdentifier}/booking/owner/list | Show Active Affiliates
[**show_active_master_rates**](PropertyBookingApi.md#show_active_master_rates) | **GET** /api/property/{propertyIdentifier}/booking/roomrate/list | Show Active Master Rates
[**show_booking_overview**](PropertyBookingApi.md#show_booking_overview) | **GET** /api/property/{propertyIdentifier}/booking/overview | Property Booking Overview
[**show_hotel_booking**](PropertyBookingApi.md#show_hotel_booking) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier} | Show Booking
[**show_hotel_bookings**](PropertyBookingApi.md#show_hotel_bookings) | **POST** /api/property/{propertyIdentifier}/booking/grid | Search Bookings
[**show_hotel_bookings1**](PropertyBookingApi.md#show_hotel_bookings1) | **GET** /api/property/{propertyIdentifier}/booking/list | Show Bookings


# **cancel_hotel_booking**
> BookingSupplier cancel_hotel_booking(property_identifier, booking_identifier, cancellation_detail_supplier, wink_version=wink_version)

Cancel Booking

Booking is cancelled by the property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_supplier import BookingSupplier
from wink_sdk_extranet_booking.models.cancellation_detail_supplier import CancellationDetailSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Cancel booking for hotel with this identifier
    booking_identifier = 'booking-1' # str | Cancel booking with this identifier
    cancellation_detail_supplier = wink_sdk_extranet_booking.CancellationDetailSupplier() # CancellationDetailSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Cancel Booking
        api_response = api_instance.cancel_hotel_booking(property_identifier, booking_identifier, cancellation_detail_supplier, wink_version=wink_version)
        print("The response of PropertyBookingApi->cancel_hotel_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->cancel_hotel_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Cancel booking for hotel with this identifier | 
 **booking_identifier** | **str**| Cancel booking with this identifier | 
 **cancellation_detail_supplier** | [**CancellationDetailSupplier**](CancellationDetailSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**BookingSupplier**](BookingSupplier.md)

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

# **generate_booking_report**
> generate_booking_report(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)

Download Booking

Returns a PDF with booking details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Generate report for property identifier
    booking_identifier = 'booking-1' # str | Generate report for this booking identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Download Booking
        api_instance.generate_booking_report(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->generate_booking_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Generate report for property identifier | 
 **booking_identifier** | **str**| Generate report for this booking identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_booking_cancellable**
> BookingCancellableSupplier is_booking_cancellable(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)

Is Booking Cancellable

Checks to see whether this booking (or group booking) can be cancelled by either the traveler or the hotel.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_cancellable_supplier import BookingCancellableSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Check if booking can be cancelled for hotel with this identifier
    booking_identifier = 'booking-1' # str | Check if booking can be cancelled with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Is Booking Cancellable
        api_response = api_instance.is_booking_cancellable(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->is_booking_cancellable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->is_booking_cancellable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Check if booking can be cancelled for hotel with this identifier | 
 **booking_identifier** | **str**| Check if booking can be cancelled with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**BookingCancellableSupplier**](BookingCancellableSupplier.md)

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

# **request_refund**
> BookingSupplier request_refund(property_identifier, booking_identifier, property_booking_refund_request_supplier, wink_version=wink_version)

Request refund

Under certain circumstances, a property can request a partial refund of the funds that were attributed to them even after a cancellation occurred or the while the funds have not been disbursed yet.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_supplier import BookingSupplier
from wink_sdk_extranet_booking.models.property_booking_refund_request_supplier import PropertyBookingRefundRequestSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Cancel booking for hotel with this identifier
    booking_identifier = 'booking-1' # str | Cancel booking with this identifier
    property_booking_refund_request_supplier = wink_sdk_extranet_booking.PropertyBookingRefundRequestSupplier() # PropertyBookingRefundRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Request refund
        api_response = api_instance.request_refund(property_identifier, booking_identifier, property_booking_refund_request_supplier, wink_version=wink_version)
        print("The response of PropertyBookingApi->request_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->request_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Cancel booking for hotel with this identifier | 
 **booking_identifier** | **str**| Cancel booking with this identifier | 
 **property_booking_refund_request_supplier** | [**PropertyBookingRefundRequestSupplier**](PropertyBookingRefundRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**BookingSupplier**](BookingSupplier.md)

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

# **resend_booking_confirmation_email**
> BooleanResponseSupplier resend_booking_confirmation_email(property_identifier, booking_identifier, body, wink_version=wink_version)

Resend Booking Confirmation

Resends booking confirmation email to traveler.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.boolean_response_supplier import BooleanResponseSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Booking owner
    booking_identifier = 'booking-1' # str | Booking identifier
    body = None # object | Empty request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Resend Booking Confirmation
        api_response = api_instance.resend_booking_confirmation_email(property_identifier, booking_identifier, body, wink_version=wink_version)
        print("The response of PropertyBookingApi->resend_booking_confirmation_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->resend_booking_confirmation_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Booking owner | 
 **booking_identifier** | **str**| Booking identifier | 
 **body** | **object**| Empty request body | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**BooleanResponseSupplier**](BooleanResponseSupplier.md)

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

# **show_active_affiliates**
> List[KeyValuePairSupplier] show_active_affiliates(property_identifier, wink_version=wink_version, accept=accept)

Show Active Affiliates

Return a geo-name list of unique affiliates that have brought the property bookings. This is helpful data you can use to filter on within your dataset.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show active affiliates for hotel with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Active Affiliates
        api_response = api_instance.show_active_affiliates(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->show_active_affiliates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_active_affiliates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show active affiliates for hotel with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **show_active_master_rates**
> List[KeyValuePairSupplier] show_active_master_rates(property_identifier, wink_version=wink_version, accept=accept)

Show Active Master Rates

Return a geoname list of unique master rates that have been booked. This is helpful data you can use to filter on within your dataset.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show booked master rates for this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Active Master Rates
        api_response = api_instance.show_active_master_rates(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->show_active_master_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_active_master_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show booked master rates for this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **show_booking_overview**
> GroupedBookingSalesMetricsSupplierDetails show_booking_overview(property_identifier, wink_version=wink_version, accept=accept)

Property Booking Overview

Basic booking overview data

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.grouped_booking_sales_metrics_supplier_details import GroupedBookingSalesMetricsSupplierDetails
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show booking owned by this hotel
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Property Booking Overview
        api_response = api_instance.show_booking_overview(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->show_booking_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_booking_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show booking owned by this hotel | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**GroupedBookingSalesMetricsSupplierDetails**](GroupedBookingSalesMetricsSupplierDetails.md)

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

# **show_hotel_booking**
> BookingSupplierDetails show_hotel_booking(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)

Show Booking

Retrieve a single booking specific by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_supplier_details import BookingSupplierDetails
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show booking owned by this hotel
    booking_identifier = 'booking-1' # str | Show booking with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking
        api_response = api_instance.show_hotel_booking(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->show_hotel_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_hotel_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show booking owned by this hotel | 
 **booking_identifier** | **str**| Show booking with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**BookingSupplierDetails**](BookingSupplierDetails.md)

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

# **show_hotel_bookings**
> PageBookingSupplier show_hotel_bookings(property_identifier, state_supplier, wink_version=wink_version)

Search Bookings

Retrieve page of bookings for a specific hotel with advanced filtering rules.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.page_booking_supplier import PageBookingSupplier
from wink_sdk_extranet_booking.models.state_supplier import StateSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show bookings for hotel with this identifier
    state_supplier = wink_sdk_extranet_booking.StateSupplier() # StateSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Search Bookings
        api_response = api_instance.show_hotel_bookings(property_identifier, state_supplier, wink_version=wink_version)
        print("The response of PropertyBookingApi->show_hotel_bookings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_hotel_bookings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show bookings for hotel with this identifier | 
 **state_supplier** | [**StateSupplier**](StateSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageBookingSupplier**](PageBookingSupplier.md)

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

# **show_hotel_bookings1**
> PageBookingSupplier show_hotel_bookings1(property_identifier, state=state, page_number=page_number, max_results=max_results, search=search, wink_version=wink_version, accept=accept)

Show Bookings

Retrieve bookings for hotel with simple filter rules.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.page_booking_supplier import PageBookingSupplier
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.PropertyBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Show bookings for hotel with this identifier
    state = 'ACTIVE' # str | Filter on the booking state (optional)
    page_number = 0 # int | Paginate booking list (optional) (default to 0)
    max_results = 30 # int | Limit number of records to return (optional) (default to 30)
    search = 'Smith' # str | Filter on email, first or last name to further narrow down the result set (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Bookings
        api_response = api_instance.show_hotel_bookings1(property_identifier, state=state, page_number=page_number, max_results=max_results, search=search, wink_version=wink_version, accept=accept)
        print("The response of PropertyBookingApi->show_hotel_bookings1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyBookingApi->show_hotel_bookings1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show bookings for hotel with this identifier | 
 **state** | **str**| Filter on the booking state | [optional] 
 **page_number** | **int**| Paginate booking list | [optional] [default to 0]
 **max_results** | **int**| Limit number of records to return | [optional] [default to 30]
 **search** | **str**| Filter on email, first or last name to further narrow down the result set | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PageBookingSupplier**](PageBookingSupplier.md)

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

