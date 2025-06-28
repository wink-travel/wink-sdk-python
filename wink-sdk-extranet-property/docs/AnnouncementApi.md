# wink_sdk_extranet_property.AnnouncementApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_announcement**](AnnouncementApi.md#create_announcement) | **POST** /api/property/{propertyIdentifier}/announcement | Create Announcement
[**remove_announcement**](AnnouncementApi.md#remove_announcement) | **DELETE** /api/property/{propertyIdentifier}/announcement/{announcementIdentifier} | Delete Announcement
[**show_announcement**](AnnouncementApi.md#show_announcement) | **GET** /api/property/{propertyIdentifier}/announcement/{announcementIdentifier} | Show Announcement
[**show_announcements**](AnnouncementApi.md#show_announcements) | **GET** /api/property/{propertyIdentifier}/announcement/list | Show Announcements
[**update_announcement**](AnnouncementApi.md#update_announcement) | **PUT** /api/property/{propertyIdentifier}/announcement/{announcementIdentifier} | Update Announcement


# **create_announcement**
> AnnouncementSupplier create_announcement(property_identifier, upsert_announcement_request_supplier, wink_version=wink_version)

Create Announcement

Create a new announcement

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier
from wink_sdk_extranet_property.models.upsert_announcement_request_supplier import UpsertAnnouncementRequestSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.AnnouncementApi(api_client)
    property_identifier = 'hotel-1' # str | Create announcement for this property identifier
    upsert_announcement_request_supplier = wink_sdk_extranet_property.UpsertAnnouncementRequestSupplier() # UpsertAnnouncementRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Announcement
        api_response = api_instance.create_announcement(property_identifier, upsert_announcement_request_supplier, wink_version=wink_version)
        print("The response of AnnouncementApi->create_announcement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementApi->create_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create announcement for this property identifier | 
 **upsert_announcement_request_supplier** | [**UpsertAnnouncementRequestSupplier**](UpsertAnnouncementRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AnnouncementSupplier**](AnnouncementSupplier.md)

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

# **remove_announcement**
> AnnouncementSupplier remove_announcement(property_identifier, announcement_identifier, wink_version=wink_version, accept=accept)

Delete Announcement

Delete an announcement by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.AnnouncementApi(api_client)
    property_identifier = 'hotel-1' # str | Remove announcement for this property identifier
    announcement_identifier = 'announcement-1' # str | Remove announcement with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Announcement
        api_response = api_instance.remove_announcement(property_identifier, announcement_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnnouncementApi->remove_announcement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementApi->remove_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove announcement for this property identifier | 
 **announcement_identifier** | **str**| Remove announcement with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AnnouncementSupplier**](AnnouncementSupplier.md)

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

# **show_announcement**
> AnnouncementSupplier show_announcement(property_identifier, announcement_identifier, wink_version=wink_version, accept=accept)

Show Announcement

Retrieve an announcement by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.AnnouncementApi(api_client)
    property_identifier = 'hotel-1' # str | Show announcement for this property identifier
    announcement_identifier = 'announcement-1' # str | Show data for this announcement identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Announcement
        api_response = api_instance.show_announcement(property_identifier, announcement_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnnouncementApi->show_announcement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementApi->show_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show announcement for this property identifier | 
 **announcement_identifier** | **str**| Show data for this announcement identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AnnouncementSupplier**](AnnouncementSupplier.md)

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

# **show_announcements**
> List[AnnouncementSupplier] show_announcements(property_identifier, wink_version=wink_version, accept=accept)

Show Announcements

Retrieve list of announcements

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.AnnouncementApi(api_client)
    property_identifier = 'hotel-1' # str | Show announcements for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Announcements
        api_response = api_instance.show_announcements(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AnnouncementApi->show_announcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementApi->show_announcements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show announcements for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[AnnouncementSupplier]**](AnnouncementSupplier.md)

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

# **update_announcement**
> AnnouncementSupplier update_announcement(property_identifier, announcement_identifier, upsert_announcement_request_supplier, wink_version=wink_version)

Update Announcement

Update an announcement by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier
from wink_sdk_extranet_property.models.upsert_announcement_request_supplier import UpsertAnnouncementRequestSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.AnnouncementApi(api_client)
    property_identifier = 'hotel-1' # str | Update announcement for this property identifier
    announcement_identifier = 'announcement-1' # str | Update announcement with this identifier
    upsert_announcement_request_supplier = wink_sdk_extranet_property.UpsertAnnouncementRequestSupplier() # UpsertAnnouncementRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Announcement
        api_response = api_instance.update_announcement(property_identifier, announcement_identifier, upsert_announcement_request_supplier, wink_version=wink_version)
        print("The response of AnnouncementApi->update_announcement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementApi->update_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update announcement for this property identifier | 
 **announcement_identifier** | **str**| Update announcement with this identifier | 
 **upsert_announcement_request_supplier** | [**UpsertAnnouncementRequestSupplier**](UpsertAnnouncementRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AnnouncementSupplier**](AnnouncementSupplier.md)

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

