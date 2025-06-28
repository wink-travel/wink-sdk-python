# wink_sdk_analytics.AnalyticsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chart_request**](AnalyticsApi.md#create_chart_request) | **POST** /api/analytics/chart | Create Chart
[**remove_chart_request**](AnalyticsApi.md#remove_chart_request) | **DELETE** /api/analytics/chart/{chartIdentifier} | Remove Chart
[**show_analytics_grid**](AnalyticsApi.md#show_analytics_grid) | **POST** /api/analytics/grid | Show Analytics Grid
[**show_analytics_list**](AnalyticsApi.md#show_analytics_list) | **GET** /api/analytics/list | Show Analytics
[**show_chart_request**](AnalyticsApi.md#show_chart_request) | **GET** /api/analytics/chart/{chartIdentifier} | Show Chart
[**show_chart_requests**](AnalyticsApi.md#show_chart_requests) | **GET** /api/analytics/chart/list | Show Charts
[**update_chart_request**](AnalyticsApi.md#update_chart_request) | **PUT** /api/analytics/chart/{chartIdentifier} | Update Chart


# **create_chart_request**
> ChartAuthenticatedEntity create_chart_request(upsert_chart_request_authenticated_entity, wink_version=wink_version)

Create Chart

Creates a new chart request.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.chart_authenticated_entity import ChartAuthenticatedEntity
from wink_sdk_analytics.models.upsert_chart_request_authenticated_entity import UpsertChartRequestAuthenticatedEntity
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
    upsert_chart_request_authenticated_entity = wink_sdk_analytics.UpsertChartRequestAuthenticatedEntity() # UpsertChartRequestAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Chart
        api_response = api_instance.create_chart_request(upsert_chart_request_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->create_chart_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->create_chart_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_chart_request_authenticated_entity** | [**UpsertChartRequestAuthenticatedEntity**](UpsertChartRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ChartAuthenticatedEntity**](ChartAuthenticatedEntity.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_chart_request**
> RemoveEntryResponseAuthenticatedEntity remove_chart_request(chart_identifier, wink_version=wink_version, accept=accept)

Remove Chart

Remove chart request for specific identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.remove_entry_response_authenticated_entity import RemoveEntryResponseAuthenticatedEntity
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
    chart_identifier = 'chart-1' # str | Chart identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Chart
        api_response = api_instance.remove_chart_request(chart_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->remove_chart_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->remove_chart_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_identifier** | **str**| Chart identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RemoveEntryResponseAuthenticatedEntity**](RemoveEntryResponseAuthenticatedEntity.md)

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

# **show_analytics_grid**
> PageLineChartNonAuthenticatedEntity show_analytics_grid(state_non_authenticated_entity, wink_version=wink_version)

Show Analytics Grid

Show paginated analytics.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.page_line_chart_non_authenticated_entity import PageLineChartNonAuthenticatedEntity
from wink_sdk_analytics.models.state_non_authenticated_entity import StateNonAuthenticatedEntity
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
    state_non_authenticated_entity = wink_sdk_analytics.StateNonAuthenticatedEntity() # StateNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Analytics Grid
        api_response = api_instance.show_analytics_grid(state_non_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->show_analytics_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_analytics_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_non_authenticated_entity** | [**StateNonAuthenticatedEntity**](StateNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageLineChartNonAuthenticatedEntity**](PageLineChartNonAuthenticatedEntity.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
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

# **show_analytics_list**
> List[LineChartNonAuthenticatedEntity] show_analytics_list(wink_version=wink_version, accept=accept)

Show Analytics

Show analytics.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.line_chart_non_authenticated_entity import LineChartNonAuthenticatedEntity
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
        # Show Analytics
        api_response = api_instance.show_analytics_list(wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_analytics_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_analytics_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[LineChartNonAuthenticatedEntity]**](LineChartNonAuthenticatedEntity.md)

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

# **show_chart_request**
> ChartAuthenticatedEntity show_chart_request(chart_identifier, wink_version=wink_version, accept=accept)

Show Chart

Displays a single chart request by identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.chart_authenticated_entity import ChartAuthenticatedEntity
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
    chart_identifier = 'chart-1' # str | Chart identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Chart
        api_response = api_instance.show_chart_request(chart_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_chart_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_chart_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_identifier** | **str**| Chart identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ChartAuthenticatedEntity**](ChartAuthenticatedEntity.md)

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

# **show_chart_requests**
> List[ChartAuthenticatedEntity] show_chart_requests(wink_version=wink_version, accept=accept)

Show Charts

Displays all charts for caller.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.chart_authenticated_entity import ChartAuthenticatedEntity
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
        # Show Charts
        api_response = api_instance.show_chart_requests(wink_version=wink_version, accept=accept)
        print("The response of AnalyticsApi->show_chart_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->show_chart_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ChartAuthenticatedEntity]**](ChartAuthenticatedEntity.md)

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

# **update_chart_request**
> ChartAuthenticatedEntity update_chart_request(chart_identifier, upsert_chart_request_authenticated_entity, wink_version=wink_version)

Update Chart

Updates an existing chart request by identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_analytics
from wink_sdk_analytics.models.chart_authenticated_entity import ChartAuthenticatedEntity
from wink_sdk_analytics.models.upsert_chart_request_authenticated_entity import UpsertChartRequestAuthenticatedEntity
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
    chart_identifier = 'chart-1' # str | Chart identifier
    upsert_chart_request_authenticated_entity = wink_sdk_analytics.UpsertChartRequestAuthenticatedEntity() # UpsertChartRequestAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Chart
        api_response = api_instance.update_chart_request(chart_identifier, upsert_chart_request_authenticated_entity, wink_version=wink_version)
        print("The response of AnalyticsApi->update_chart_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->update_chart_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_identifier** | **str**| Chart identifier | 
 **upsert_chart_request_authenticated_entity** | [**UpsertChartRequestAuthenticatedEntity**](UpsertChartRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ChartAuthenticatedEntity**](ChartAuthenticatedEntity.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
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

