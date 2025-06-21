# wink_sdk_extranet_monetize.RatePlanApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate_plan**](RatePlanApi.md#create_rate_plan) | **POST** /api/property/{propertyIdentifier}/rate-plan | Create Rate Plan
[**remove_rate_plan**](RatePlanApi.md#remove_rate_plan) | **DELETE** /api/property/{propertyIdentifier}/rate-plan/{ratePlanIdentifier} | Delete Rate Plan
[**show_rate_plan**](RatePlanApi.md#show_rate_plan) | **GET** /api/property/{propertyIdentifier}/rate-plan/{ratePlanIdentifier} | Show Rate Plan
[**show_rate_plans**](RatePlanApi.md#show_rate_plans) | **GET** /api/property/{propertyIdentifier}/rate-plan/list | Show Rate Plans
[**update_rate_plan**](RatePlanApi.md#update_rate_plan) | **PUT** /api/property/{propertyIdentifier}/rate-plan/{ratePlanIdentifier} | Update Rate Plan


# **create_rate_plan**
> RatePlanSupplier create_rate_plan(property_identifier, upsert_rate_plan_request_supplier, wink_version=wink_version)

Create Rate Plan

Create a new rate plan

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_plan_supplier import RatePlanSupplier
from wink_sdk_extranet_monetize.models.upsert_rate_plan_request_supplier import UpsertRatePlanRequestSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.RatePlanApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new rate plan and associate it with this property identifier.
    upsert_rate_plan_request_supplier = wink_sdk_extranet_monetize.UpsertRatePlanRequestSupplier() # UpsertRatePlanRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Rate Plan
        api_response = api_instance.create_rate_plan(property_identifier, upsert_rate_plan_request_supplier, wink_version=wink_version)
        print("The response of RatePlanApi->create_rate_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlanApi->create_rate_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new rate plan and associate it with this property identifier. | 
 **upsert_rate_plan_request_supplier** | [**UpsertRatePlanRequestSupplier**](UpsertRatePlanRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RatePlanSupplier**](RatePlanSupplier.md)

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

# **remove_rate_plan**
> RatePlanSupplier remove_rate_plan(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)

Delete Rate Plan

Remove a rate plan by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_plan_supplier import RatePlanSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.RatePlanApi(api_client)
    property_identifier = 'hotel-1' # str | Remove rate plan owned by this property identifier.
    rate_plan_identifier = 'rate-plan-1' # str | Remove rate plan with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Rate Plan
        api_response = api_instance.remove_rate_plan(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)
        print("The response of RatePlanApi->remove_rate_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlanApi->remove_rate_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove rate plan owned by this property identifier. | 
 **rate_plan_identifier** | **str**| Remove rate plan with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RatePlanSupplier**](RatePlanSupplier.md)

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

# **show_rate_plan**
> RatePlanSupplier show_rate_plan(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)

Show Rate Plan

Retrieve a single rate plan identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_plan_supplier import RatePlanSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.RatePlanApi(api_client)
    property_identifier = 'hotel-1' # str | Show single rate plan owned by this property identifier.
    rate_plan_identifier = 'rate-plan-1' # str | Show rate plan with this property identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Rate Plan
        api_response = api_instance.show_rate_plan(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)
        print("The response of RatePlanApi->show_rate_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlanApi->show_rate_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single rate plan owned by this property identifier. | 
 **rate_plan_identifier** | **str**| Show rate plan with this property identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RatePlanSupplier**](RatePlanSupplier.md)

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

# **show_rate_plans**
> List[RatePlanSupplier] show_rate_plans(property_identifier, wink_version=wink_version, accept=accept)

Show Rate Plans

Retrieve list of rate plans for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_plan_supplier import RatePlanSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.RatePlanApi(api_client)
    property_identifier = 'hotel-1' # str | Show list of rate plans owned by this property identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Rate Plans
        api_response = api_instance.show_rate_plans(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of RatePlanApi->show_rate_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlanApi->show_rate_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show list of rate plans owned by this property identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[RatePlanSupplier]**](RatePlanSupplier.md)

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

# **update_rate_plan**
> RatePlanSupplier update_rate_plan(property_identifier, rate_plan_identifier, upsert_rate_plan_request_supplier, wink_version=wink_version)

Update Rate Plan

Update an existing rate plan by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.rate_plan_supplier import RatePlanSupplier
from wink_sdk_extranet_monetize.models.upsert_rate_plan_request_supplier import UpsertRatePlanRequestSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.RatePlanApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing rate plan owned by this property identifier.
    rate_plan_identifier = 'rate-plan-1' # str | Update an existing rate plan identified with this identifier.
    upsert_rate_plan_request_supplier = wink_sdk_extranet_monetize.UpsertRatePlanRequestSupplier() # UpsertRatePlanRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Rate Plan
        api_response = api_instance.update_rate_plan(property_identifier, rate_plan_identifier, upsert_rate_plan_request_supplier, wink_version=wink_version)
        print("The response of RatePlanApi->update_rate_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlanApi->update_rate_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing rate plan owned by this property identifier. | 
 **rate_plan_identifier** | **str**| Update an existing rate plan identified with this identifier. | 
 **upsert_rate_plan_request_supplier** | [**UpsertRatePlanRequestSupplier**](UpsertRatePlanRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RatePlanSupplier**](RatePlanSupplier.md)

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

