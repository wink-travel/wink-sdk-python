# wink_sdk_engine_client.ConfigurationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_customization_by_client_id**](ConfigurationApi.md#show_customization_by_client_id) | **GET** /api/sell/configuration/client/{clientId} | Load Configuration by Client ID
[**show_customization_by_client_id_header**](ConfigurationApi.md#show_customization_by_client_id_header) | **GET** /api/sell/configuration/client | Load Configuration by Client ID in Header
[**show_customization_by_id**](ConfigurationApi.md#show_customization_by_id) | **GET** /api/sell/configuration/{identifier} | Load Configuration by ID
[**show_customization_by_url_name**](ConfigurationApi.md#show_customization_by_url_name) | **GET** /api/sell/configuration/url-name/{urlName} | Load Configuration by URL name


# **show_customization_by_client_id**
> EngineClientNonAuthenticatedEntity show_customization_by_client_id(client_id, wink_version=wink_version, accept=accept)

Load Configuration by Client ID

Retrieve affiliate configuration by clientId in the path

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_engine_client
from wink_sdk_engine_client.models.engine_client_non_authenticated_entity import EngineClientNonAuthenticatedEntity
from wink_sdk_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_engine_client.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_engine_client.ConfigurationApi(api_client)
    client_id = 'client_id_example' # str | The clientId
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Load Configuration by Client ID
        api_response = api_instance.show_customization_by_client_id(client_id, wink_version=wink_version, accept=accept)
        print("The response of ConfigurationApi->show_customization_by_client_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->show_customization_by_client_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The clientId | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineClientNonAuthenticatedEntity**](EngineClientNonAuthenticatedEntity.md)

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

# **show_customization_by_client_id_header**
> EngineClientNonAuthenticatedEntity show_customization_by_client_id_header(client_id, wink_version=wink_version, accept=accept)

Load Configuration by Client ID in Header

Retrieve affiliate configuration by clientId in the header

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_engine_client
from wink_sdk_engine_client.models.engine_client_non_authenticated_entity import EngineClientNonAuthenticatedEntity
from wink_sdk_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_engine_client.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_engine_client.ConfigurationApi(api_client)
    client_id = 'client_id_example' # str | The clientId
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Load Configuration by Client ID in Header
        api_response = api_instance.show_customization_by_client_id_header(client_id, wink_version=wink_version, accept=accept)
        print("The response of ConfigurationApi->show_customization_by_client_id_header:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->show_customization_by_client_id_header: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The clientId | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineClientNonAuthenticatedEntity**](EngineClientNonAuthenticatedEntity.md)

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

# **show_customization_by_id**
> EngineClientNonAuthenticatedEntity show_customization_by_id(identifier, wink_version=wink_version, accept=accept)

Load Configuration by ID

Retrieve specific affiliate configuration

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_engine_client
from wink_sdk_engine_client.models.engine_client_non_authenticated_entity import EngineClientNonAuthenticatedEntity
from wink_sdk_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_engine_client.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_engine_client.ConfigurationApi(api_client)
    identifier = 'identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Load Configuration by ID
        api_response = api_instance.show_customization_by_id(identifier, wink_version=wink_version, accept=accept)
        print("The response of ConfigurationApi->show_customization_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->show_customization_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineClientNonAuthenticatedEntity**](EngineClientNonAuthenticatedEntity.md)

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

# **show_customization_by_url_name**
> EngineClientNonAuthenticatedEntity show_customization_by_url_name(url_name, wink_version=wink_version, accept=accept)

Load Configuration by URL name

Retrieve affiliate configuration by company urlName

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_engine_client
from wink_sdk_engine_client.models.engine_client_non_authenticated_entity import EngineClientNonAuthenticatedEntity
from wink_sdk_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_engine_client.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_engine_client.ConfigurationApi(api_client)
    url_name = 'url_name_example' # str | The urlName
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Load Configuration by URL name
        api_response = api_instance.show_customization_by_url_name(url_name, wink_version=wink_version, accept=accept)
        print("The response of ConfigurationApi->show_customization_by_url_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->show_customization_by_url_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| The urlName | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineClientNonAuthenticatedEntity**](EngineClientNonAuthenticatedEntity.md)

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

