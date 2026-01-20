# wink_sdk_channel_manager.ChannelManagerApi

All URIs are relative to *https://integrations.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](ChannelManagerApi.md#ping) | **GET** /api/channel-manager/ping | Say Hello
[**show_properties**](ChannelManagerApi.md#show_properties) | **GET** /api/channel-manager/property/list | Show Properties
[**show_property**](ChannelManagerApi.md#show_property) | **GET** /api/channel-manager/property/{propertyIdentifier} | Show Property
[**show_property_booking**](ChannelManagerApi.md#show_property_booking) | **GET** /api/channel-manager/property/{propertyIdentifier}/booking/{bookingIdentifier} | Show Booking
[**show_property_bookings**](ChannelManagerApi.md#show_property_bookings) | **GET** /api/channel-manager/property/{propertyIdentifier}/booking/list | Show Bookings
[**show_property_room_rates**](ChannelManagerApi.md#show_property_room_rates) | **GET** /api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier} | Show Daily Rates
[**update_rates**](ChannelManagerApi.md#update_rates) | **PUT** /api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier} | Update Daily Rates


# **ping**
> PingResponse ping(wink_version=wink_version, accept=accept)

Say Hello

Test endpoint to validate your credentials.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.ping_response import PingResponse
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Say Hello
        api_response = api_instance.ping(wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **show_properties**
> PageChannelManagerProperty show_properties(page=page, size=size, wink_version=wink_version, accept=accept)

Show Properties

The properties endpoint provides the entry point into the listener and is used to list properties you have access to.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.page_channel_manager_property import PageChannelManagerProperty
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    page = 0 # int | Page through all properties owned by your account (optional) (default to 0)
    size = 25 # int | Limit results of records per page (optional) (default to 25)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Properties
        api_response = api_instance.show_properties(page=page, size=size, wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->show_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->show_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page through all properties owned by your account | [optional] [default to 0]
 **size** | **int**| Limit results of records per page | [optional] [default to 25]
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PageChannelManagerProperty**](PageChannelManagerProperty.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **show_property**
> PropertyWithRoomRateList show_property(property_identifier, wink_version=wink_version, accept=accept)

Show Property

Retrieves property record with master rates included.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.property_with_room_rate_list import PropertyWithRoomRateList
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    property_identifier = 'property-1' # str | Retrieve record for this propertyIdentifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Property
        api_response = api_instance.show_property(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->show_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->show_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve record for this propertyIdentifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PropertyWithRoomRateList**](PropertyWithRoomRateList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **show_property_booking**
> PropertyBooking show_property_booking(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)

Show Booking

Retrieves a specific booking by property / booking combo.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.property_booking import PropertyBooking
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    property_identifier = 'property-1' # str | Retrieve record owned by propertyIdentifier
    booking_identifier = 'booking-1' # str | Retrieve record for this bookingIdentifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking
        api_response = api_instance.show_property_booking(property_identifier, booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->show_property_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->show_property_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve record owned by propertyIdentifier | 
 **booking_identifier** | **str**| Retrieve record for this bookingIdentifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PropertyBooking**](PropertyBooking.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **show_property_bookings**
> List[PropertyBooking] show_property_bookings(property_identifier, start_date, end_date=end_date, wink_version=wink_version, accept=accept)

Show Bookings

Retrieves a list of all bookings created for the specified property within the specified date range.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.property_booking import PropertyBooking
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    property_identifier = 'property-1' # str | Retrieve record owned by this propertyIdentifier
    start_date = '2018-01-01T03:07:58.742+0000' # datetime | Limit results on date range starting with
    end_date = '2018-01-02T03:07:58.742+0000' # datetime | Limit results on date range ending with (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Bookings
        api_response = api_instance.show_property_bookings(property_identifier, start_date, end_date=end_date, wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->show_property_bookings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->show_property_bookings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve record owned by this propertyIdentifier | 
 **start_date** | **datetime**| Limit results on date range starting with | 
 **end_date** | **datetime**| Limit results on date range ending with | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[PropertyBooking]**](PropertyBooking.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **show_property_room_rates**
> PropertyRoomRateWithRateList show_property_room_rates(property_identifier, master_rate_identifier, start_date, end_date, wink_version=wink_version, accept=accept)

Show Daily Rates

Retrieves all daily rates for for property / master rate combo and a date range.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.property_room_rate_with_rate_list import PropertyRoomRateWithRateList
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    property_identifier = 'property-1' # str | Retrieve record owned by this propertyIdentifier
    master_rate_identifier = 'master-rate-1' # str | Retrieve record owned by this masterRateIdentifier
    start_date = '2018-01-01' # date | Limit results on date range starting with
    end_date = '2018-01-02' # date | Limit results on date range ending with
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Daily Rates
        api_response = api_instance.show_property_room_rates(property_identifier, master_rate_identifier, start_date, end_date, wink_version=wink_version, accept=accept)
        print("The response of ChannelManagerApi->show_property_room_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->show_property_room_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve record owned by this propertyIdentifier | 
 **master_rate_identifier** | **str**| Retrieve record owned by this masterRateIdentifier | 
 **start_date** | **date**| Limit results on date range starting with | 
 **end_date** | **date**| Limit results on date range ending with | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PropertyRoomRateWithRateList**](PropertyRoomRateWithRateList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

# **update_rates**
> List[PropertyRate] update_rates(property_identifier, master_rate_identifier, property_rate_update_request, wink_version=wink_version)

Update Daily Rates

Update daily rate / availability for a property / master rate combo.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import wink_sdk_channel_manager
from wink_sdk_channel_manager.models.property_rate import PropertyRate
from wink_sdk_channel_manager.models.property_rate_update_request import PropertyRateUpdateRequest
from wink_sdk_channel_manager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://integrations.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_channel_manager.Configuration(
    host = "https://integrations.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_channel_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_channel_manager.ChannelManagerApi(api_client)
    property_identifier = 'property-1' # str | Update rates owned by this propertyIdentifier
    master_rate_identifier = 'master-rate-1' # str | Update rates owned by this masterRateIdentifier
    property_rate_update_request = wink_sdk_channel_manager.PropertyRateUpdateRequest() # PropertyRateUpdateRequest | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Daily Rates
        api_response = api_instance.update_rates(property_identifier, master_rate_identifier, property_rate_update_request, wink_version=wink_version)
        print("The response of ChannelManagerApi->update_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->update_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update rates owned by this propertyIdentifier | 
 **master_rate_identifier** | **str**| Update rates owned by this masterRateIdentifier | 
 **property_rate_update_request** | [**PropertyRateUpdateRequest**](PropertyRateUpdateRequest.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[PropertyRate]**](PropertyRate.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

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

