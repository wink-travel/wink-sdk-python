# wink_sdk_ping.ACLApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_admin_hello**](ACLApi.md#delete_admin_hello) | **DELETE** /api/administration/hello | DELETE Admin Hello
[**delete_hello**](ACLApi.md#delete_hello) | **DELETE** /api/hello | DELETE Hello
[**get_admin_hello**](ACLApi.md#get_admin_hello) | **GET** /api/administration/hello | GET Admin Hello
[**get_hello**](ACLApi.md#get_hello) | **GET** /api/hello | GET Hello
[**patch_admin_hello**](ACLApi.md#patch_admin_hello) | **PATCH** /api/administration/hello | PATCH Admin Hello
[**patch_hello**](ACLApi.md#patch_hello) | **PATCH** /api/hello | PATCH Hello
[**post_admin_hello**](ACLApi.md#post_admin_hello) | **POST** /api/administration/hello | POST Admin Hello
[**post_hello**](ACLApi.md#post_hello) | **POST** /api/hello | POST Hello
[**put_admin_hello**](ACLApi.md#put_admin_hello) | **PUT** /api/administration/hello | PUT Admin Hello
[**put_hello**](ACLApi.md#put_hello) | **PUT** /api/hello | PUT Hello


# **delete_admin_hello**
> str delete_admin_hello()

DELETE Admin Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)

    try:
        # DELETE Admin Hello
        api_response = api_instance.delete_admin_hello()
        print("The response of ACLApi->delete_admin_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->delete_admin_hello: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **delete_hello**
> str delete_hello()

DELETE Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)

    try:
        # DELETE Hello
        api_response = api_instance.delete_hello()
        print("The response of ACLApi->delete_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->delete_hello: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **get_admin_hello**
> str get_admin_hello()

GET Admin Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)

    try:
        # GET Admin Hello
        api_response = api_instance.get_admin_hello()
        print("The response of ACLApi->get_admin_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->get_admin_hello: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **get_hello**
> str get_hello()

GET Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)

    try:
        # GET Hello
        api_response = api_instance.get_hello()
        print("The response of ACLApi->get_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->get_hello: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **patch_admin_hello**
> str patch_admin_hello(body)

PATCH Admin Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # PATCH Admin Hello
        api_response = api_instance.patch_admin_hello(body)
        print("The response of ACLApi->patch_admin_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->patch_admin_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **patch_hello**
> str patch_hello(body)

PATCH Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # PATCH Hello
        api_response = api_instance.patch_hello(body)
        print("The response of ACLApi->patch_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->patch_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **post_admin_hello**
> str post_admin_hello(body)

POST Admin Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # POST Admin Hello
        api_response = api_instance.post_admin_hello(body)
        print("The response of ACLApi->post_admin_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->post_admin_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **post_hello**
> str post_hello(body)

POST Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # POST Hello
        api_response = api_instance.post_hello(body)
        print("The response of ACLApi->post_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->post_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **put_admin_hello**
> str put_admin_hello(body)

PUT Admin Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # PUT Admin Hello
        api_response = api_instance.put_admin_hello(body)
        print("The response of ACLApi->put_admin_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->put_admin_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **put_hello**
> str put_hello(body)

PUT Hello

Verify you are authenticated.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_ping
from wink_sdk_ping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_ping.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_ping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_ping.ACLApi(api_client)
    body = 'body_example' # str | 

    try:
        # PUT Hello
        api_response = api_instance.put_hello(body)
        print("The response of ACLApi->put_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLApi->put_hello: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

