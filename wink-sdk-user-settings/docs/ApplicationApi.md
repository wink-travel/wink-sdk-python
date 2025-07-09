# wink_sdk_user_settings.ApplicationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationApi.md#create_application) | **POST** /api/application | Create Application
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /api/application/{id} | Delete Application
[**load_application**](ApplicationApi.md#load_application) | **GET** /api/application/{id} | Show Application
[**revoke_application**](ApplicationApi.md#revoke_application) | **GET** /api/application/{id}/revoke | Revoke Application Credentials
[**show_applications**](ApplicationApi.md#show_applications) | **GET** /api/application/list | Show Applications
[**update_application**](ApplicationApi.md#update_application) | **PATCH** /api/application/{id} | Update Application


# **create_application**
> CreateApplicationResponse create_application(upsert_application_request, wink_version=wink_version)

Create Application

Create a new application

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.create_application_response import CreateApplicationResponse
from wink_sdk_user_settings.models.upsert_application_request import UpsertApplicationRequest
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    upsert_application_request = wink_sdk_user_settings.UpsertApplicationRequest() # UpsertApplicationRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Application
        api_response = api_instance.create_application(upsert_application_request, wink_version=wink_version)
        print("The response of ApplicationApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_application_request** | [**UpsertApplicationRequest**](UpsertApplicationRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

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

# **delete_application**
> RemoveEntryResponse delete_application(id, wink_version=wink_version, accept=accept)

Delete Application

Remove a specific application

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.remove_entry_response import RemoveEntryResponse
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Application
        api_response = api_instance.delete_application(id, wink_version=wink_version, accept=accept)
        print("The response of ApplicationApi->delete_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RemoveEntryResponse**](RemoveEntryResponse.md)

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

# **load_application**
> Application load_application(id, wink_version=wink_version, accept=accept)

Show Application

Show a specific application

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.application import Application
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Application
        api_response = api_instance.load_application(id, wink_version=wink_version, accept=accept)
        print("The response of ApplicationApi->load_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->load_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **revoke_application**
> RevokeClientIdResponse revoke_application(id, wink_version=wink_version, accept=accept)

Revoke Application Credentials

Refreshes the clientId and secretKey properties.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.revoke_client_id_response import RevokeClientIdResponse
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Revoke Application Credentials
        api_response = api_instance.revoke_application(id, wink_version=wink_version, accept=accept)
        print("The response of ApplicationApi->revoke_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->revoke_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RevokeClientIdResponse**](RevokeClientIdResponse.md)

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

# **show_applications**
> List[Application] show_applications(owner_identifier=owner_identifier, wink_version=wink_version, accept=accept)

Show Applications

List all applications owned by creating entity

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.application import Application
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    owner_identifier = 'owner_identifier_example' # str | Optional ownerIdentifier to filter on (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Applications
        api_response = api_instance.show_applications(owner_identifier=owner_identifier, wink_version=wink_version, accept=accept)
        print("The response of ApplicationApi->show_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->show_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_identifier** | **str**| Optional ownerIdentifier to filter on | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Application]**](Application.md)

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

# **update_application**
> UpdateApplicationResponse update_application(id, upsert_application_request, wink_version=wink_version)

Update Application

Update an existing application

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.update_application_response import UpdateApplicationResponse
from wink_sdk_user_settings.models.upsert_application_request import UpsertApplicationRequest
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.ApplicationApi(api_client)
    id = 'id_example' # str | 
    upsert_application_request = wink_sdk_user_settings.UpsertApplicationRequest() # UpsertApplicationRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Application
        api_response = api_instance.update_application(id, upsert_application_request, wink_version=wink_version)
        print("The response of ApplicationApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->update_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_application_request** | [**UpsertApplicationRequest**](UpsertApplicationRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

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

