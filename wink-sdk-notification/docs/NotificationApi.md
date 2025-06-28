# wink_sdk_notification.NotificationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_notification**](NotificationApi.md#remove_notification) | **DELETE** /api/affiliate/{companyIdentifier}/message/{messageIdentifier} | Delete Notification
[**show_notification**](NotificationApi.md#show_notification) | **GET** /api/affiliate/{companyIdentifier}/message/{messageIdentifier} | Show Notification
[**show_notifications**](NotificationApi.md#show_notifications) | **GET** /api/affiliate/{companyIdentifier}/message/list | Show Notifications
[**show_unread_message_count**](NotificationApi.md#show_unread_message_count) | **GET** /api/affiliate/{companyIdentifier}/message/count | Show Unread Count


# **remove_notification**
> NotificationAffiliate remove_notification(company_identifier, message_identifier, wink_version=wink_version, accept=accept)

Delete Notification

Remove announcement specified by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_notification
from wink_sdk_notification.models.notification_affiliate import NotificationAffiliate
from wink_sdk_notification.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_notification.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_notification.NotificationApi(api_client)
    company_identifier = 'company-1' # str | Remove a message that belongs to this company identifier
    message_identifier = 'message-1' # str | Message identifier to be removed
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Notification
        api_response = api_instance.remove_notification(company_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->remove_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->remove_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove a message that belongs to this company identifier | 
 **message_identifier** | **str**| Message identifier to be removed | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**NotificationAffiliate**](NotificationAffiliate.md)

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

# **show_notification**
> NotificationAffiliate show_notification(company_identifier, message_identifier, wink_version=wink_version, accept=accept)

Show Notification

Retrieve messages for a specific company by ID

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_notification
from wink_sdk_notification.models.notification_affiliate import NotificationAffiliate
from wink_sdk_notification.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_notification.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_notification.NotificationApi(api_client)
    company_identifier = 'company-1' # str | Retrieve a message for this company identifier
    message_identifier = 'message-1' # str | Message identifier to be retrieved
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notification
        api_response = api_instance.show_notification(company_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Retrieve a message for this company identifier | 
 **message_identifier** | **str**| Message identifier to be retrieved | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**NotificationAffiliate**](NotificationAffiliate.md)

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

# **show_notifications**
> List[NotificationAffiliate] show_notifications(company_identifier, app=app, wink_version=wink_version, accept=accept)

Show Notifications

Retrieve all the messages for this company

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_notification
from wink_sdk_notification.models.notification_affiliate import NotificationAffiliate
from wink_sdk_notification.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_notification.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_notification.NotificationApi(api_client)
    company_identifier = 'company-1' # str | Show all messages for this company identifier
    app = 'company-1' # str | Show all messages for this application (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notifications
        api_response = api_instance.show_notifications(company_identifier, app=app, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show all messages for this company identifier | 
 **app** | **str**| Show all messages for this application | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[NotificationAffiliate]**](NotificationAffiliate.md)

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

# **show_unread_message_count**
> CountResponseAffiliate show_unread_message_count(company_identifier, wink_version=wink_version, accept=accept)

Show Unread Count

Retrieve count of unread messages

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_notification
from wink_sdk_notification.models.count_response_affiliate import CountResponseAffiliate
from wink_sdk_notification.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_notification.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_notification.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_notification.NotificationApi(api_client)
    company_identifier = 'company-1' # str | Show unread message count for this company identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unread Count
        api_response = api_instance.show_unread_message_count(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_unread_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_unread_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show unread message count for this company identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponseAffiliate**](CountResponseAffiliate.md)

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

