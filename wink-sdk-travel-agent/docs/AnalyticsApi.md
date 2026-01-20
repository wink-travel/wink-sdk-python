# wink_sdk_travel_agent.AnalyticsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_affiliate_booking_analytics**](AnalyticsApi.md#show_affiliate_booking_analytics) | **POST** /api/affiliate/{companyIdentifier}/booking/analytics | Affiliate Booking Analytics
[**show_booking_overview**](AnalyticsApi.md#show_booking_overview) | **GET** /api/affiliate/{companyIdentifier}/booking/overview | Affiliate Booking Overview


# **show_affiliate_booking_analytics**
> BookingAnalyticsSupplier show_affiliate_booking_analytics(company_identifier, booking_overview_request_supplier, wink_version=wink_version)

Affiliate Booking Analytics

Retrieve the number of upcoming bookings that arrive today for the specific company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.booking_analytics_supplier import BookingAnalyticsSupplier
from wink_sdk_travel_agent.models.booking_overview_request_supplier import BookingOverviewRequestSupplier
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.AnalyticsApi(api_client)
    company_identifier = 'company-1' # str | Show active booking count for company with this identifier
    booking_overview_request_supplier = wink_sdk_travel_agent.BookingOverviewRequestSupplier() # BookingOverviewRequestSupplier | Overview request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Affiliate Booking Analytics
        api_response = api_instance.show_affiliate_booking_analytics(company_identifier, booking_overview_request_supplier, wink_version=wink_version)
        print("The response of AnalyticsApi->show_affiliate_booking_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_affiliate_booking_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show active booking count for company with this identifier | 
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

# **show_booking_overview**
> GroupedBookingSalesMetricsSupplierDetails show_booking_overview(company_identifier, wink_version=wink_version, accept=accept)

Affiliate Booking Overview

Basic booking overview data

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.grouped_booking_sales_metrics_supplier_details import GroupedBookingSalesMetricsSupplierDetails
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.AnalyticsApi(api_client)
    company_identifier = 'company-1' # str | Show booking owned by this company
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Affiliate Booking Overview
        api_response = api_instance.show_booking_overview(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_booking_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_booking_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show booking owned by this company | 
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

