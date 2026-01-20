# wink_sdk_booking.CheckoutApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout**](CheckoutApi.md#checkout) | **POST** /api/checkout | Prepare booking


# **checkout**
> CheckoutResponseAuthenticatedEntity checkout(checkout_request_authenticated_entity, wink_version=wink_version)

Prepare booking

Communicates shopping cart to TripPay.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.checkout_request_authenticated_entity import CheckoutRequestAuthenticatedEntity
from wink_sdk_booking.models.checkout_response_authenticated_entity import CheckoutResponseAuthenticatedEntity
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
    api_instance = wink_sdk_booking.CheckoutApi(api_client)
    checkout_request_authenticated_entity = wink_sdk_booking.CheckoutRequestAuthenticatedEntity() # CheckoutRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Prepare booking
        api_response = api_instance.checkout(checkout_request_authenticated_entity, wink_version=wink_version)
        print("The response of CheckoutApi->checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_request_authenticated_entity** | [**CheckoutRequestAuthenticatedEntity**](CheckoutRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**CheckoutResponseAuthenticatedEntity**](CheckoutResponseAuthenticatedEntity.md)

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

