# wink_sdk_extranet_experiences.ActivityApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivityApi.md#create_activity) | **POST** /api/property/{propertyIdentifier}/experience/activity | Create Activity
[**remove_activity**](ActivityApi.md#remove_activity) | **DELETE** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Delete Activity
[**show_activities**](ActivityApi.md#show_activities) | **GET** /api/property/{propertyIdentifier}/experience/activity/list | Show Activities
[**show_activity**](ActivityApi.md#show_activity) | **GET** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Show Activity
[**show_activity_pairs**](ActivityApi.md#show_activity_pairs) | **GET** /api/property/{propertyIdentifier}/experience/activity/list/pair | Show Activities as key/value pairs
[**update_activity**](ActivityApi.md#update_activity) | **PUT** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier} | Update Activity
[**upload_activity_media**](ActivityApi.md#upload_activity_media) | **POST** /api/property/{propertyIdentifier}/experience/activity/{activityIdentifier}/multimedia | Upload Binary Multimedia


# **create_activity**
> Activity create_activity(property_identifier, upsert_activity_request, wink_version=wink_version)

Create Activity

Persist new activity record.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.models.upsert_activity_request import UpsertActivityRequest
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Persist activity owned by this property identifier
    upsert_activity_request = wink_sdk_extranet_experiences.UpsertActivityRequest() # UpsertActivityRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Activity
        api_response = api_instance.create_activity(property_identifier, upsert_activity_request, wink_version=wink_version)
        print("The response of ActivityApi->create_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->create_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Persist activity owned by this property identifier | 
 **upsert_activity_request** | [**UpsertActivityRequest**](UpsertActivityRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Activity**](Activity.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_activity**
> Activity remove_activity(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)

Delete Activity

Delete a activity by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Delete activity owned by this property identifier
    activity_identifier = 'activity-1' # str | Delete activity identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Activity
        api_response = api_instance.remove_activity(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ActivityApi->remove_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->remove_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Delete activity owned by this property identifier | 
 **activity_identifier** | **str**| Delete activity identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Activity**](Activity.md)

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

# **show_activities**
> List[Activity] show_activities(property_identifier, wink_version=wink_version, accept=accept)

Show Activities

Retrieve list of activities for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Show activities associated with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activities
        api_response = api_instance.show_activities(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of ActivityApi->show_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->show_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show activities associated with this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Activity]**](Activity.md)

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

# **show_activity**
> Activity show_activity(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)

Show Activity

Retrieve activity record by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Show activity owned by this property identifier
    activity_identifier = 'activity-1' # str | Show activity for identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activity
        api_response = api_instance.show_activity(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ActivityApi->show_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->show_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show activity owned by this property identifier | 
 **activity_identifier** | **str**| Show activity for identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Activity**](Activity.md)

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

# **show_activity_pairs**
> List[KeyValuePair] show_activity_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Activities as key/value pairs

This is a more performant way to populate activity lists instead of downloading entire activity object.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.key_value_pair import KeyValuePair
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Show activity key/value pairs associated with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activities as key/value pairs
        api_response = api_instance.show_activity_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of ActivityApi->show_activity_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->show_activity_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show activity key/value pairs associated with this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePair]**](KeyValuePair.md)

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

# **update_activity**
> Activity update_activity(property_identifier, activity_identifier, upsert_activity_request, wink_version=wink_version)

Update Activity

Update a recreation by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.models.upsert_activity_request import UpsertActivityRequest
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing activity record owned by this property identifier
    activity_identifier = 'activity-1' # str | Update activity record with this identifier
    upsert_activity_request = wink_sdk_extranet_experiences.UpsertActivityRequest() # UpsertActivityRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Activity
        api_response = api_instance.update_activity(property_identifier, activity_identifier, upsert_activity_request, wink_version=wink_version)
        print("The response of ActivityApi->update_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->update_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing activity record owned by this property identifier | 
 **activity_identifier** | **str**| Update activity record with this identifier | 
 **upsert_activity_request** | [**UpsertActivityRequest**](UpsertActivityRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Activity**](Activity.md)

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

# **upload_activity_media**
> Activity upload_activity_media(property_identifier, activity_identifier, files)

Upload Binary Multimedia

Upload a list of binary / multipart videos and/or images to an existing add-on.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.activity import Activity
from wink_sdk_extranet_experiences.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_experiences.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_experiences.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_experiences.ActivityApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart media for activity owned by this property identifier
    activity_identifier = 'activity-1' # str | Associate multipart media with activity identified by this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_activity_media(property_identifier, activity_identifier, files)
        print("The response of ActivityApi->upload_activity_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->upload_activity_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart media for activity owned by this property identifier | 
 **activity_identifier** | **str**| Associate multipart media with activity identified by this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**Activity**](Activity.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml, text/html, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**207** | Multi-Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

