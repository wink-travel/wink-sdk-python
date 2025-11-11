# wink_sdk_extranet_booking.TestBookingApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_booking**](TestBookingApi.md#create_test_booking) | **POST** /api/property/{propertyIdentifier}/sandbox/booking | Test Rate / Availability


# **create_test_booking**
> BookingSupplierDetails create_test_booking(property_identifier, booking_test_request_supplier_details, wink_version=wink_version)

Test Rate / Availability

Test whether the rates and availability for a sales channel is coming backing the way the property wants

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.booking_supplier_details import BookingSupplierDetails
from wink_sdk_extranet_booking.models.booking_test_request_supplier_details import BookingTestRequestSupplierDetails
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
    api_instance = wink_sdk_extranet_booking.TestBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Create test booking for property ID
    booking_test_request_supplier_details = wink_sdk_extranet_booking.BookingTestRequestSupplierDetails() # BookingTestRequestSupplierDetails | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Test Rate / Availability
        api_response = api_instance.create_test_booking(property_identifier, booking_test_request_supplier_details, wink_version=wink_version)
        print("The response of TestBookingApi->create_test_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBookingApi->create_test_booking: %s\n" % e)
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
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

