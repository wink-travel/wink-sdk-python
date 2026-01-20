# wink_sdk_extranet_booking.AnalyticsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_property_booking_analytics**](AnalyticsApi.md#show_property_booking_analytics) | **POST** /api/property/{propertyIdentifier}/booking/analytics | Property Booking Analytics


# **show_property_booking_analytics**
> BookingAnalyticsSupplier show_property_booking_analytics(property_identifier, booking_overview_request_supplier, wink_version=wink_version)

Property Booking Analytics

Basic booking analytics data

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_analytics_supplier import BookingAnalyticsSupplier
from wink_sdk_extranet_booking.models.booking_overview_request_supplier import BookingOverviewRequestSupplier
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
    api_instance = wink_sdk_extranet_booking.AnalyticsApi(api_client)
    property_identifier = 'hotel-1' # str | Show active booking count for hotel with this identifier
    booking_overview_request_supplier = wink_sdk_extranet_booking.BookingOverviewRequestSupplier() # BookingOverviewRequestSupplier | Overview request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Property Booking Analytics
        api_response = api_instance.show_property_booking_analytics(property_identifier, booking_overview_request_supplier, wink_version=wink_version)
        print("The response of AnalyticsApi->show_property_booking_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_property_booking_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show active booking count for hotel with this identifier | 
 **booking_overview_request_supplier** | [**BookingOverviewRequestSupplier**](BookingOverviewRequestSupplier.md)| Overview request body | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**BookingAnalyticsSupplier**](BookingAnalyticsSupplier.md)

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

