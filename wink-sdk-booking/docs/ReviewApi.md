# wink_sdk_booking.ReviewApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**populate_review**](ReviewApi.md#populate_review) | **GET** /api/booking/{bookingIdentifier}/review/questions | Show Review Template
[**submit_review**](ReviewApi.md#submit_review) | **POST** /api/booking/{bookingIdentifier}/review | Submit Review


# **populate_review**
> ReviewTemplateAuthenticatedEntity populate_review(booking_identifier, wink_version=wink_version, accept=accept)

Show Review Template

Loads available questions and answer options

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.review_template_authenticated_entity import ReviewTemplateAuthenticatedEntity
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
    api_instance = wink_sdk_booking.ReviewApi(api_client)
    booking_identifier = 'booking_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Review Template
        api_response = api_instance.populate_review(booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of ReviewApi->populate_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->populate_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ReviewTemplateAuthenticatedEntity**](ReviewTemplateAuthenticatedEntity.md)

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

# **submit_review**
> ReviewAuthenticatedEntity submit_review(booking_identifier, submit_review_request_authenticated_entity, wink_version=wink_version)

Submit Review

Submit review for booking

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.review_authenticated_entity import ReviewAuthenticatedEntity
from wink_sdk_booking.models.submit_review_request_authenticated_entity import SubmitReviewRequestAuthenticatedEntity
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
    api_instance = wink_sdk_booking.ReviewApi(api_client)
    booking_identifier = 'booking_identifier_example' # str | 
    submit_review_request_authenticated_entity = wink_sdk_booking.SubmitReviewRequestAuthenticatedEntity() # SubmitReviewRequestAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Submit Review
        api_response = api_instance.submit_review(booking_identifier, submit_review_request_authenticated_entity, wink_version=wink_version)
        print("The response of ReviewApi->submit_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->submit_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_identifier** | **str**|  | 
 **submit_review_request_authenticated_entity** | [**SubmitReviewRequestAuthenticatedEntity**](SubmitReviewRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ReviewAuthenticatedEntity**](ReviewAuthenticatedEntity.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

