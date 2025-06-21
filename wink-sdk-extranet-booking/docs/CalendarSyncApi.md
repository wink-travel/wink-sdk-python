# wink_sdk_extranet_booking.CalendarSyncApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**caldav**](CalendarSyncApi.md#caldav) | **GET** /api/cal/property/{propertyIdentifier}/booking/list | CalDAV calendar
[**generate_cal_dav_auth**](CalendarSyncApi.md#generate_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth/regen | Create CalDAV connection
[**retrieve_cal_dav_auth**](CalendarSyncApi.md#retrieve_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth | Show CalDAV Connection


# **caldav**
> str caldav(property_identifier, wink_version=wink_version)

CalDAV calendar

This is the CalDAV URL you can add to your calendar program.

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
    api_instance = wink_sdk_extranet_booking.CalendarSyncApi(api_client)
    property_identifier = 'hotel-1' # str | Retrieve booking list in CalDAV for this specified property
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # CalDAV calendar
        api_response = api_instance.caldav(property_identifier, wink_version=wink_version)
        print("The response of CalendarSyncApi->caldav:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarSyncApi->caldav: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve booking list in CalDAV for this specified property | 
 **wink_version** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**503** | Service Unavailable |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cal_dav_auth**
> CalDavResponseSupplier generate_cal_dav_auth(property_identifier, wink_version=wink_version)

Create CalDAV connection

Generates new CalDav passkey the property can use to authenticate the CalDAV url.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.cal_dav_response_supplier import CalDavResponseSupplier
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
    api_instance = wink_sdk_extranet_booking.CalendarSyncApi(api_client)
    property_identifier = 'hotel-1' # str | Regenrate CalDAV auth for this specified property
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create CalDAV connection
        api_response = api_instance.generate_cal_dav_auth(property_identifier, wink_version=wink_version)
        print("The response of CalendarSyncApi->generate_cal_dav_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarSyncApi->generate_cal_dav_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Regenrate CalDAV auth for this specified property | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CalDavResponseSupplier**](CalDavResponseSupplier.md)

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

# **retrieve_cal_dav_auth**
> CalDavResponseSupplier retrieve_cal_dav_auth(property_identifier, wink_version=wink_version, accept=accept)

Show CalDAV Connection

Retrieve the CalDAV connection for your property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.cal_dav_response_supplier import CalDavResponseSupplier
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
    api_instance = wink_sdk_extranet_booking.CalendarSyncApi(api_client)
    property_identifier = 'hotel-1' # str | Generate CalDAV auth for this specified property
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show CalDAV Connection
        api_response = api_instance.retrieve_cal_dav_auth(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of CalendarSyncApi->retrieve_cal_dav_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarSyncApi->retrieve_cal_dav_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Generate CalDAV auth for this specified property | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CalDavResponseSupplier**](CalDavResponseSupplier.md)

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

