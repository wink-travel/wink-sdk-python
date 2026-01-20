# wink_sdk_extranet_facilities.MeetingRoomApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meeting_room**](MeetingRoomApi.md#create_meeting_room) | **POST** /api/property/{propertyIdentifier}/facility/meeting-room | Create Meeting Room
[**remove_meeting_room**](MeetingRoomApi.md#remove_meeting_room) | **DELETE** /api/property/{propertyIdentifier}/facility/meeting-room/{meetingRoomIdentifier} | Delete Meeting Room
[**remove_multimedia2**](MeetingRoomApi.md#remove_multimedia2) | **DELETE** /api/property/{propertyIdentifier}/facility/meeting-room/{meetingRoomIdentifier}/multimedia/{multimediaIdentifier} | Delete Multimedia
[**show_meeting_room**](MeetingRoomApi.md#show_meeting_room) | **GET** /api/property/{propertyIdentifier}/facility/meeting-room/{meetingRoomIdentifier} | Show Meeting Room
[**show_meeting_room_pairs**](MeetingRoomApi.md#show_meeting_room_pairs) | **GET** /api/property/{propertyIdentifier}/facility/meeting-room/list/pair | Show Reference Pairs
[**show_meeting_rooms**](MeetingRoomApi.md#show_meeting_rooms) | **GET** /api/property/{propertyIdentifier}/facility/meeting-room/list | Show Meeting Rooms
[**update_meeting_room**](MeetingRoomApi.md#update_meeting_room) | **PUT** /api/property/{propertyIdentifier}/facility/meeting-room/{meetingRoomIdentifier} | Update Meeting Room
[**upload_meeting_room_media**](MeetingRoomApi.md#upload_meeting_room_media) | **POST** /api/property/{propertyIdentifier}/facility/meeting-room/{meetingRoomIdentifier}/multimedia | Upload Binary Multimedia


# **create_meeting_room**
> MeetingRoomSupplier create_meeting_room(property_identifier, upsert_meeting_room_request_supplier, wink_version=wink_version)

Create Meeting Room

Create a new meeting room

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.models.upsert_meeting_room_request_supplier import UpsertMeetingRoomRequestSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new meeting room record and associate it with this property identifier
    upsert_meeting_room_request_supplier = wink_sdk_extranet_facilities.UpsertMeetingRoomRequestSupplier() # UpsertMeetingRoomRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Meeting Room
        api_response = api_instance.create_meeting_room(property_identifier, upsert_meeting_room_request_supplier, wink_version=wink_version)
        print("The response of MeetingRoomApi->create_meeting_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->create_meeting_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new meeting room record and associate it with this property identifier | 
 **upsert_meeting_room_request_supplier** | [**UpsertMeetingRoomRequestSupplier**](UpsertMeetingRoomRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

# **remove_meeting_room**
> MeetingRoomSupplier remove_meeting_room(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)

Delete Meeting Room

Remove a meeting room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Remove meeting room associated with this property identifier
    meeting_room_identifier = 'meeting-room-1' # str | Remove meeting room with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Meeting Room
        api_response = api_instance.remove_meeting_room(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)
        print("The response of MeetingRoomApi->remove_meeting_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->remove_meeting_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove meeting room associated with this property identifier | 
 **meeting_room_identifier** | **str**| Remove meeting room with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

# **remove_multimedia2**
> MeetingRoomSupplier remove_multimedia2(property_identifier, meeting_room_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Multimedia

Remove a meeting room's video or image by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Remove media for meeting room associated with this property identifier
    meeting_room_identifier = 'meeting-room-1' # str | Remove media for meeting room with this identifier
    multimedia_identifier = 'media-1' # str | Remove media with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia
        api_response = api_instance.remove_multimedia2(property_identifier, meeting_room_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of MeetingRoomApi->remove_multimedia2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->remove_multimedia2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove media for meeting room associated with this property identifier | 
 **meeting_room_identifier** | **str**| Remove media for meeting room with this identifier | 
 **multimedia_identifier** | **str**| Remove media with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

# **show_meeting_room**
> MeetingRoomSupplier show_meeting_room(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)

Show Meeting Room

Retrieve a meeting room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Show a single meeting room owned by this property identifier
    meeting_room_identifier = 'meeting-room-1' # str | Show meeting room for identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Meeting Room
        api_response = api_instance.show_meeting_room(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)
        print("The response of MeetingRoomApi->show_meeting_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->show_meeting_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show a single meeting room owned by this property identifier | 
 **meeting_room_identifier** | **str**| Show meeting room for identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

# **show_meeting_room_pairs**
> List[KeyValuePairSupplier] show_meeting_room_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Reference Pairs

Retrieve list of meeting rooms as key/value pairs (identifier, name)

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Show meeting room key/value pairs associated with this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Reference Pairs
        api_response = api_instance.show_meeting_room_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of MeetingRoomApi->show_meeting_room_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->show_meeting_room_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show meeting room key/value pairs associated with this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **show_meeting_rooms**
> List[MeetingRoomSupplier] show_meeting_rooms(property_identifier, wink_version=wink_version, accept=accept)

Show Meeting Rooms

Retrieve list of meeting rooms

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Show meeting rooms associated with this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Meeting Rooms
        api_response = api_instance.show_meeting_rooms(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of MeetingRoomApi->show_meeting_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->show_meeting_rooms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show meeting rooms associated with this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[MeetingRoomSupplier]**](MeetingRoomSupplier.md)

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

# **update_meeting_room**
> MeetingRoomSupplier update_meeting_room(property_identifier, meeting_room_identifier, upsert_meeting_room_request_supplier, wink_version=wink_version)

Update Meeting Room

Update a meeting room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.models.upsert_meeting_room_request_supplier import UpsertMeetingRoomRequestSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Update a meeting room owned by this property identifier
    meeting_room_identifier = 'meeting-room-1' # str | Update meeting room with this identifier
    upsert_meeting_room_request_supplier = wink_sdk_extranet_facilities.UpsertMeetingRoomRequestSupplier() # UpsertMeetingRoomRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Meeting Room
        api_response = api_instance.update_meeting_room(property_identifier, meeting_room_identifier, upsert_meeting_room_request_supplier, wink_version=wink_version)
        print("The response of MeetingRoomApi->update_meeting_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->update_meeting_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update a meeting room owned by this property identifier | 
 **meeting_room_identifier** | **str**| Update meeting room with this identifier | 
 **upsert_meeting_room_request_supplier** | [**UpsertMeetingRoomRequestSupplier**](UpsertMeetingRoomRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

# **upload_meeting_room_media**
> MeetingRoomSupplier upload_meeting_room_media(property_identifier, meeting_room_identifier, files)

Upload Binary Multimedia

Upload binary videos and/or images to a meeting room identified by its identifier. Valid file types: .gif, .jpg, .jpeg, .png, .bmp, .tif, .tiff, .avi, .mpeg, .mov, .mp4, .mkv.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.meeting_room_supplier import MeetingRoomSupplier
from wink_sdk_extranet_facilities.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_facilities.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_facilities.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_facilities.MeetingRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Upload binary media for meeting room associated with this property identifier
    meeting_room_identifier = 'meeting-room-1' # str | Upload binary media for meeting room with this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_meeting_room_media(property_identifier, meeting_room_identifier, files)
        print("The response of MeetingRoomApi->upload_meeting_room_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingRoomApi->upload_meeting_room_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload binary media for meeting room associated with this property identifier | 
 **meeting_room_identifier** | **str**| Upload binary media for meeting room with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**MeetingRoomSupplier**](MeetingRoomSupplier.md)

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

