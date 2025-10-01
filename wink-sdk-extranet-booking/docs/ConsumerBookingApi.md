# wink_sdk_extranet_booking.ConsumerBookingApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**respond_to_review**](ConsumerBookingApi.md#respond_to_review) | **PATCH** /api/property/{propertyIdentifier}/review/{reviewIdentifier}/response | Respond to Review


# **respond_to_review**
> ReviewSupplier respond_to_review(property_identifier, review_identifier, review_response_supplier, wink_version=wink_version)

Respond to Review

Respond to a unique review for a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.review_response_supplier import ReviewResponseSupplier
from wink_sdk_extranet_booking.models.review_supplier import ReviewSupplier
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
    api_instance = wink_sdk_extranet_booking.ConsumerBookingApi(api_client)
    property_identifier = 'hotel-1' # str | Respond to review given hotel with this identifier
    review_identifier = 'review-1' # str | Respond to review with this identifier
    review_response_supplier = wink_sdk_extranet_booking.ReviewResponseSupplier() # ReviewResponseSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Respond to Review
        api_response = api_instance.respond_to_review(property_identifier, review_identifier, review_response_supplier, wink_version=wink_version)
        print("The response of ConsumerBookingApi->respond_to_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumerBookingApi->respond_to_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Respond to review given hotel with this identifier | 
 **review_identifier** | **str**| Respond to review with this identifier | 
 **review_response_supplier** | [**ReviewResponseSupplier**](ReviewResponseSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ReviewSupplier**](ReviewSupplier.md)

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

