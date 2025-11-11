# wink_sdk_analytics.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_leaderboard**](AffiliateApi.md#show_leaderboard) | **POST** /api/analytics/leaderboard/list | Show Leaderboard by Region
[**show_leaderboard_by_owner**](AffiliateApi.md#show_leaderboard_by_owner) | **POST** /api/analytics/leaderboard | Show Leaderboard by Affiliate 


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
    api_instance = wink_sdk_analytics.AffiliateApi(api_client)
    leaderboard_request_non_authenticated_entity = wink_sdk_analytics.LeaderboardRequestNonAuthenticatedEntity() # LeaderboardRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Leaderboard by Region
        api_response = api_instance.show_leaderboard(leaderboard_request_non_authenticated_entity, wink_version=wink_version)
        print("The response of AffiliateApi->show_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_leaderboard: %s\n" % e)
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
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
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
    api_instance = wink_sdk_analytics.AffiliateApi(api_client)
    leaderboard_owner_request_non_authenticated_entity = wink_sdk_analytics.LeaderboardOwnerRequestNonAuthenticatedEntity() # LeaderboardOwnerRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Leaderboard by Affiliate 
        api_response = api_instance.show_leaderboard_by_owner(leaderboard_owner_request_non_authenticated_entity, wink_version=wink_version)
        print("The response of AffiliateApi->show_leaderboard_by_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_leaderboard_by_owner: %s\n" % e)
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
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

