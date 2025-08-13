# wink_sdk_analytics.AnalyticsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_aggregate_share_analytics**](AnalyticsApi.md#show_aggregate_share_analytics) | **GET** /api/analytics/shares/lifetime | Lifetime Shares Analytics
[**show_booking_analytics_grid**](AnalyticsApi.md#show_booking_analytics_grid) | **POST** /api/analytics/booking/grid | Show Booking Analytic Grid
[**show_booking_analytics_list**](AnalyticsApi.md#show_booking_analytics_list) | **GET** /api/analytics/booking/list | Show Booking Analytic List
[**show_leaderboard**](AnalyticsApi.md#show_leaderboard) | **POST** /api/analytics/leaderboard/list | Show Leaderboard by Region
[**show_leaderboard_by_owner**](AnalyticsApi.md#show_leaderboard_by_owner) | **POST** /api/analytics/leaderboard | Show Leaderboard by Affiliate 
[**show_share_analytics**](AnalyticsApi.md#show_share_analytics) | **GET** /api/analytics/shares/list | Share Metrics


# **show_aggregate_share_analytics**
> AggregateSharesProjectionAuthenticatedEntity show_aggregate_share_analytics(wink_version=wink_version, accept=accept)

Lifetime Shares Analytics

Show aggregate share analytics.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.aggregate_shares_projection_authenticated_entity import AggregateSharesProjectionAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Lifetime Shares Analytics
        api_response = api_instance.show_aggregate_share_analytics(wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_aggregate_share_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_aggregate_share_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AggregateSharesProjectionAuthenticatedEntity**](AggregateSharesProjectionAuthenticatedEntity.md)

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

# **show_booking_analytics_grid**
> PageLineChartAuthenticatedEntity show_booking_analytics_grid(state_authenticated_entity, wink_version=wink_version)

Show Booking Analytic Grid

Show paginated analytics.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.page_line_chart_authenticated_entity import PageLineChartAuthenticatedEntity
from wink_sdk_analytics.models.state_authenticated_entity import StateAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    state_authenticated_entity = wink_sdk_analytics.StateAuthenticatedEntity() # StateAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Booking Analytic Grid
        api_response = api_instance.show_booking_analytics_grid(state_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->show_booking_analytics_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_booking_analytics_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_authenticated_entity** | [**StateAuthenticatedEntity**](StateAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageLineChartAuthenticatedEntity**](PageLineChartAuthenticatedEntity.md)

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

# **show_booking_analytics_list**
> List[LineChartAuthenticatedEntity] show_booking_analytics_list(wink_version=wink_version, accept=accept)

Show Booking Analytic List

Show analytics.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.line_chart_authenticated_entity import LineChartAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking Analytic List
        api_response = api_instance.show_booking_analytics_list(wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_booking_analytics_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_booking_analytics_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[LineChartAuthenticatedEntity]**](LineChartAuthenticatedEntity.md)

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

# **show_leaderboard**
> PageBookingLeaderboardEntryNonAuthenticatedEntity show_leaderboard(leaderboard_request_non_authenticated_entity, wink_version=wink_version)

Show Leaderboard by Region

Show leaderboard based on location type such as continent.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.leaderboard_request_non_authenticated_entity import LeaderboardRequestNonAuthenticatedEntity
from wink_sdk_analytics.models.page_booking_leaderboard_entry_non_authenticated_entity import PageBookingLeaderboardEntryNonAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    leaderboard_request_non_authenticated_entity = wink_sdk_analytics.LeaderboardRequestNonAuthenticatedEntity() # LeaderboardRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Leaderboard by Region
        api_response = api_instance.show_leaderboard(leaderboard_request_non_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->show_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_request_non_authenticated_entity** | [**LeaderboardRequestNonAuthenticatedEntity**](LeaderboardRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageBookingLeaderboardEntryNonAuthenticatedEntity**](PageBookingLeaderboardEntryNonAuthenticatedEntity.md)

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

# **show_leaderboard_by_owner**
> BookingLeaderboardEntryNonAuthenticatedEntity show_leaderboard_by_owner(leaderboard_owner_request_non_authenticated_entity, wink_version=wink_version)

Show Leaderboard by Affiliate 

Show leaderboard for a specific affiliate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.booking_leaderboard_entry_non_authenticated_entity import BookingLeaderboardEntryNonAuthenticatedEntity
from wink_sdk_analytics.models.leaderboard_owner_request_non_authenticated_entity import LeaderboardOwnerRequestNonAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    leaderboard_owner_request_non_authenticated_entity = wink_sdk_analytics.LeaderboardOwnerRequestNonAuthenticatedEntity() # LeaderboardOwnerRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Leaderboard by Affiliate 
        api_response = api_instance.show_leaderboard_by_owner(leaderboard_owner_request_non_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->show_leaderboard_by_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_leaderboard_by_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_owner_request_non_authenticated_entity** | [**LeaderboardOwnerRequestNonAuthenticatedEntity**](LeaderboardOwnerRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingLeaderboardEntryNonAuthenticatedEntity**](BookingLeaderboardEntryNonAuthenticatedEntity.md)

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

# **show_share_analytics**
> List[LineChartAuthenticatedEntity] show_share_analytics(wink_version=wink_version, accept=accept)

Share Metrics

Show all account charts.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.line_chart_authenticated_entity import LineChartAuthenticatedEntity
from wink_sdk_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_analytics.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_analytics.AnalyticsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Share Metrics
        api_response = api_instance.show_share_analytics(wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_share_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_share_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[LineChartAuthenticatedEntity]**](LineChartAuthenticatedEntity.md)

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

