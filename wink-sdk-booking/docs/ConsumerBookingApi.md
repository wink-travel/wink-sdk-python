# wink_sdk_booking.ConsumerBookingApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_booking**](ConsumerBookingApi.md#cancel_booking) | **PATCH** /api/booking/{bookingIdentifier} | Cancel Booking
[**cancel_group_booking**](ConsumerBookingApi.md#cancel_group_booking) | **PATCH** /api/booking/group/{groupIdentifier} | Cancel Group Booking
[**resend_booking_confirmation_email**](ConsumerBookingApi.md#resend_booking_confirmation_email) | **PATCH** /api/booking/{bookingIdentifier}/resend | Resend Booking Confirmation
[**show_booking**](ConsumerBookingApi.md#show_booking) | **GET** /api/booking/{bookingIdentifier} | Show Booking
[**show_booking_by_transaction_id**](ConsumerBookingApi.md#show_booking_by_transaction_id) | **GET** /api/booking/tx/{transactionIdentifier} | Show Booking by TX ID
[**show_booking_grid**](ConsumerBookingApi.md#show_booking_grid) | **POST** /api/booking/grid | Search Bookings
[**show_bookings**](ConsumerBookingApi.md#show_bookings) | **GET** /api/booking/list | Show Booking List
[**show_bookings_by_review_state**](ConsumerBookingApi.md#show_bookings_by_review_state) | **GET** /api/booking/review/list | Show Bookings by Review
[**show_bookings_by_state**](ConsumerBookingApi.md#show_bookings_by_state) | **GET** /api/booking/state | Show Bookings by Time
[**show_grouped_bookings**](ConsumerBookingApi.md#show_grouped_bookings) | **GET** /api/booking/group/{groupIdentifier} | Show Grouped Bookings


# **cancel_booking**
> BookingBooker cancel_booking(booking_identifier, cancellation_detail_booker, wink_version=wink_version)

Cancel Booking

Cancel a booking by its booking identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.models.cancellation_detail_booker import CancellationDetailBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    booking_identifier = 'booking-1' # str | Cancel booking by identifier
    cancellation_detail_booker = wink_sdk_booking.CancellationDetailBooker() # CancellationDetailBooker | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel Booking
        api_response = api_instance.cancel_booking(booking_identifier, cancellation_detail_booker, wink_version=wink_version)
        print("The response of ConsumerBookingApi->cancel_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->cancel_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_identifier** | **str**| Cancel booking by identifier | 
 **cancellation_detail_booker** | [**CancellationDetailBooker**](CancellationDetailBooker.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingBooker**](BookingBooker.md)

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

# **cancel_group_booking**
> List[BookingBooker] cancel_group_booking(group_identifier, cancellation_detail_booker, wink_version=wink_version)

Cancel Group Booking

Cancel a group booking by its group identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.models.cancellation_detail_booker import CancellationDetailBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    group_identifier = 'trace-1' # str | Cancel booking by group identifier
    cancellation_detail_booker = wink_sdk_booking.CancellationDetailBooker() # CancellationDetailBooker | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel Group Booking
        api_response = api_instance.cancel_group_booking(group_identifier, cancellation_detail_booker, wink_version=wink_version)
        print("The response of ConsumerBookingApi->cancel_group_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->cancel_group_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_identifier** | **str**| Cancel booking by group identifier | 
 **cancellation_detail_booker** | [**CancellationDetailBooker**](CancellationDetailBooker.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[BookingBooker]**](BookingBooker.md)

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

# **resend_booking_confirmation_email**
> BooleanResponseBooker resend_booking_confirmation_email(booking_identifier, body, wink_version=wink_version)

Resend Booking Confirmation

Resends booking confirmation email to traveler.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.boolean_response_booker import BooleanResponseBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    booking_identifier = 'booking-1' # str | Retrieve booking by identifier
    body = None # object | Empty request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Resend Booking Confirmation
        api_response = api_instance.resend_booking_confirmation_email(booking_identifier, body, wink_version=wink_version)
        print("The response of ConsumerBookingApi->resend_booking_confirmation_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->resend_booking_confirmation_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_identifier** | **str**| Retrieve booking by identifier | 
 **body** | **object**| Empty request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseBooker**](BooleanResponseBooker.md)

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

# **show_booking**
> BookingBooker show_booking(booking_identifier, wink_version=wink_version, accept=accept)

Show Booking

Retrieve a booking by its booking identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    booking_identifier = 'booking-1' # str | Retrieve booking by identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking
        api_response = api_instance.show_booking(booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_identifier** | **str**| Retrieve booking by identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BookingBooker**](BookingBooker.md)

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

# **show_booking_by_transaction_id**
> BookingBooker show_booking_by_transaction_id(transaction_identifier, wink_version=wink_version, accept=accept)

Show Booking by TX ID

Retrieve a booking by its transaction identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    transaction_identifier = 'booking-1' # str | Retrieve booking by transaction identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking by TX ID
        api_response = api_instance.show_booking_by_transaction_id(transaction_identifier, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_booking_by_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_booking_by_transaction_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_identifier** | **str**| Retrieve booking by transaction identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BookingBooker**](BookingBooker.md)

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

# **show_booking_grid**
> PageBookingBooker show_booking_grid(state_booker, wink_version=wink_version)

Search Bookings

Retrieve paginated bookings based on a query state

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.page_booking_booker import PageBookingBooker
from wink_sdk_booking.models.state_booker import StateBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    state_booker = wink_sdk_booking.StateBooker() # StateBooker | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Search Bookings
        api_response = api_instance.show_booking_grid(state_booker, wink_version=wink_version)
        print("The response of ConsumerBookingApi->show_booking_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_booking_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_booker** | [**StateBooker**](StateBooker.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageBookingBooker**](PageBookingBooker.md)

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

# **show_bookings**
> PageBookingBooker show_bookings(page=page, size=size, wink_version=wink_version, accept=accept)

Show Booking List

Retrieve bookings in a paginated list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.page_booking_booker import PageBookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    page = 0 # int | Page to start retrieving records for (optional) (default to 0)
    size = 10 # int | Number of records to retrieve (optional) (default to 10)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking List
        api_response = api_instance.show_bookings(page=page, size=size, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_bookings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_bookings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to start retrieving records for | [optional] [default to 0]
 **size** | **int**| Number of records to retrieve | [optional] [default to 10]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PageBookingBooker**](PageBookingBooker.md)

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

# **show_bookings_by_review_state**
> List[BookingBooker] show_bookings_by_review_state(state=state, wink_version=wink_version, accept=accept)

Show Bookings by Review

List bookings by their review state

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    state = NEEDS_REVIEW # str | Retrieve bookings by review state (optional) (default to NEEDS_REVIEW)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Bookings by Review
        api_response = api_instance.show_bookings_by_review_state(state=state, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_bookings_by_review_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_bookings_by_review_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Retrieve bookings by review state | [optional] [default to NEEDS_REVIEW]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BookingBooker]**](BookingBooker.md)

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

# **show_bookings_by_state**
> List[BookingBooker] show_bookings_by_state(state=state, wink_version=wink_version, accept=accept)

Show Bookings by Time

Retrieve bookings for a date state

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    state = FUTURE # str | Retrieve bookings by state (optional) (default to FUTURE)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Bookings by Time
        api_response = api_instance.show_bookings_by_state(state=state, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_bookings_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_bookings_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Retrieve bookings by state | [optional] [default to FUTURE]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BookingBooker]**](BookingBooker.md)

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

# **show_grouped_bookings**
> List[BookingBooker] show_grouped_bookings(group_identifier, wink_version=wink_version, accept=accept)

Show Grouped Bookings

Retrieve a list of bookings by group identifier. User needs to be authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.booking_booker import BookingBooker
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ConsumerBookingApi(api_client)
    group_identifier = 'booking-1' # str | Retrieve booking by identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Grouped Bookings
        api_response = api_instance.show_grouped_bookings(group_identifier, wink_version=wink_version, accept=accept)
        print("The response of ConsumerBookingApi->show_grouped_bookings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->show_grouped_bookings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_identifier** | **str**| Retrieve booking by identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BookingBooker]**](BookingBooker.md)

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

