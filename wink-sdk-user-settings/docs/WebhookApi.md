# wink_sdk_user_settings.WebhookApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /api/webhook | Create Webhook
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /api/webhook/{id} | Delete Webhook
[**load_webhook**](WebhookApi.md#load_webhook) | **GET** /api/webhook/{id} | Show Webhook
[**show_webhook_events**](WebhookApi.md#show_webhook_events) | **GET** /api/webhook/event/list | Show Webhook Event List
[**show_webhooks**](WebhookApi.md#show_webhooks) | **GET** /api/webhook/list | Show Webhooks
[**update_webhook**](WebhookApi.md#update_webhook) | **PATCH** /api/webhook/{id} | Update Webhook


# **create_webhook**
> Webhook create_webhook(upsert_webhook_request, wink_version=wink_version)

Create Webhook

Create a new webhook

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.upsert_webhook_request import UpsertWebhookRequest
from wink_sdk_user_settings.models.webhook import Webhook
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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    upsert_webhook_request = wink_sdk_user_settings.UpsertWebhookRequest() # UpsertWebhookRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Webhook
        api_response = api_instance.create_webhook(upsert_webhook_request, wink_version=wink_version)
        print("The response of WebhookApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_webhook_request** | [**UpsertWebhookRequest**](UpsertWebhookRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> RemoveEntryResponse delete_webhook(id, wink_version=wink_version, accept=accept)

Delete Webhook

Remove a specific webhook

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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Webhook
        api_response = api_instance.delete_webhook(id, wink_version=wink_version, accept=accept)
        print("The response of WebhookApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
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
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_webhook**
> Webhook load_webhook(id, wink_version=wink_version, accept=accept)

Show Webhook

Show a specific webhook

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.webhook import Webhook
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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Webhook
        api_response = api_instance.load_webhook(id, wink_version=wink_version, accept=accept)
        print("The response of WebhookApi->load_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->load_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_webhook_events**
> List[KeyValuePair] show_webhook_events(wink_version=wink_version, accept=accept)

Show Webhook Event List

List all valid webhook events that can be subsccribed to

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.key_value_pair import KeyValuePair
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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Webhook Event List
        api_response = api_instance.show_webhook_events(wink_version=wink_version, accept=accept)
        print("The response of WebhookApi->show_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->show_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePair]**](KeyValuePair.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_webhooks**
> List[Webhook] show_webhooks(owner_identifier=owner_identifier, wink_version=wink_version, accept=accept)

Show Webhooks

List all webhooks owned by creating entity

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.webhook import Webhook
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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    owner_identifier = 'owner_identifier_example' # str | Optional ownerIdentifier to filter on (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Webhooks
        api_response = api_instance.show_webhooks(owner_identifier=owner_identifier, wink_version=wink_version, accept=accept)
        print("The response of WebhookApi->show_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->show_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_identifier** | **str**| Optional ownerIdentifier to filter on | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Webhook]**](Webhook.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(id, upsert_webhook_request, wink_version=wink_version)

Update Webhook

Update an existing webhook

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.upsert_webhook_request import UpsertWebhookRequest
from wink_sdk_user_settings.models.webhook import Webhook
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
    api_instance = wink_sdk_user_settings.WebhookApi(api_client)
    id = 'id_example' # str | 
    upsert_webhook_request = wink_sdk_user_settings.UpsertWebhookRequest() # UpsertWebhookRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Webhook
        api_response = api_instance.update_webhook(id, upsert_webhook_request, wink_version=wink_version)
        print("The response of WebhookApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_webhook_request** | [**UpsertWebhookRequest**](UpsertWebhookRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

