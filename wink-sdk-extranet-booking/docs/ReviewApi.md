# wink_sdk_extranet_booking.ReviewApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_review**](ReviewApi.md#show_review) | **GET** /api/property/{propertyIdentifier}/review/{reviewIdentifier} | Show Review
[**show_review_count**](ReviewApi.md#show_review_count) | **GET** /api/property/{propertyIdentifier}/review/count | Show Review Count
[**show_reviews**](ReviewApi.md#show_reviews) | **POST** /api/property/{propertyIdentifier}/review/grid | Show Reviews


# **show_review**
> ReviewSupplier show_review(property_identifier, review_identifier, wink_version=wink_version, accept=accept)

Show Review

Retrieve a unique review of a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
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
    api_instance = wink_sdk_extranet_booking.ReviewApi(api_client)
    property_identifier = 'hotel-1' # str | Show review given to hotel with this identifier
    review_identifier = 'review-1' # str | Show review for this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Review
        api_response = api_instance.show_review(property_identifier, review_identifier, wink_version=wink_version, accept=accept)
        print("The response of ReviewApi->show_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->show_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show review given to hotel with this identifier | 
 **review_identifier** | **str**| Show review for this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ReviewSupplier**](ReviewSupplier.md)

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

# **show_review_count**
> CountResponseSupplier show_review_count(property_identifier, wink_version=wink_version, accept=accept)

Show Review Count

Retrieve a count of all reviews for a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.count_response_supplier import CountResponseSupplier
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
    api_instance = wink_sdk_extranet_booking.ReviewApi(api_client)
    property_identifier = 'hotel-1' # str | Show review count for hotel with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Review Count
        api_response = api_instance.show_review_count(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of ReviewApi->show_review_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->show_review_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show review count for hotel with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponseSupplier**](CountResponseSupplier.md)

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

# **show_reviews**
> PageReviewSupplier show_reviews(property_identifier, state_supplier, wink_version=wink_version)

Show Reviews

Retrieve a paginated list of reviews for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.models.page_review_supplier import PageReviewSupplier
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
    api_instance = wink_sdk_extranet_booking.ReviewApi(api_client)
    property_identifier = 'hotel-1' # str | Show reviews for hotel with this identifier
    state_supplier = wink_sdk_extranet_booking.StateSupplier() # StateSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Reviews
        api_response = api_instance.show_reviews(property_identifier, state_supplier, wink_version=wink_version)
        print("The response of ReviewApi->show_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->show_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show reviews for hotel with this identifier | 
 **state_supplier** | [**StateSupplier**](StateSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageReviewSupplier**](PageReviewSupplier.md)

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

