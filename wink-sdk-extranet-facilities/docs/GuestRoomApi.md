# wink_sdk_extranet_facilities.GuestRoomApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_guest_room**](GuestRoomApi.md#create_guest_room) | **POST** /api/property/{propertyIdentifier}/facility/room-type | Create Guest Room
[**duplicate_guest_room**](GuestRoomApi.md#duplicate_guest_room) | **POST** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier}/duplicate | Duplicate Guest Room
[**improve_guest_room**](GuestRoomApi.md#improve_guest_room) | **PUT** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier}/improve | Improve Guest Room
[**remove_guest_room**](GuestRoomApi.md#remove_guest_room) | **DELETE** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier} | Delete Guest Room
[**remove_multimedia**](GuestRoomApi.md#remove_multimedia) | **DELETE** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier}/multimedia/{multimediaIdentifier} | Delete Guest Room Multimedia
[**show_guest_room**](GuestRoomApi.md#show_guest_room) | **GET** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier} | Show Guest Room
[**show_guest_rooms**](GuestRoomApi.md#show_guest_rooms) | **GET** /api/property/{propertyIdentifier}/facility/room-type/list | Show Guest Rooms
[**update_guest_room**](GuestRoomApi.md#update_guest_room) | **PUT** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier} | Update Guest Room
[**upload_guest_room_media**](GuestRoomApi.md#upload_guest_room_media) | **POST** /api/property/{propertyIdentifier}/facility/room-type/{roomTypeIdentifier}/multimedia | Add Multimedia to Room


# **create_guest_room**
> RoomTypeSupplier create_guest_room(property_identifier, upsert_room_type_request_supplier, wink_version=wink_version)

Create Guest Room

create a new room type

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
from wink_sdk_extranet_facilities.models.upsert_room_type_request_supplier import UpsertRoomTypeRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Create room type owned by this property identifier
    upsert_room_type_request_supplier = wink_sdk_extranet_facilities.UpsertRoomTypeRequestSupplier() # UpsertRoomTypeRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Guest Room
        api_response = api_instance.create_guest_room(property_identifier, upsert_room_type_request_supplier, wink_version=wink_version)
        print("The response of GuestRoomApi->create_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->create_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create room type owned by this property identifier | 
 **upsert_room_type_request_supplier** | [**UpsertRoomTypeRequestSupplier**](UpsertRoomTypeRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RoomTypeSupplier**](RoomTypeSupplier.md)

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

# **duplicate_guest_room**
> RoomTypeSupplier duplicate_guest_room(property_identifier, room_type_identifier, duplicate_guest_room_request_supplier, wink_version=wink_version)

Duplicate Guest Room

Create a new duplicate of a room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.duplicate_guest_room_request_supplier import DuplicateGuestRoomRequestSupplier
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Duplicate room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Duplicate room type with this identifier
    duplicate_guest_room_request_supplier = wink_sdk_extranet_facilities.DuplicateGuestRoomRequestSupplier() # DuplicateGuestRoomRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Duplicate Guest Room
        api_response = api_instance.duplicate_guest_room(property_identifier, room_type_identifier, duplicate_guest_room_request_supplier, wink_version=wink_version)
        print("The response of GuestRoomApi->duplicate_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->duplicate_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Duplicate room type owned by this property identifier | 
 **room_type_identifier** | **str**| Duplicate room type with this identifier | 
 **duplicate_guest_room_request_supplier** | [**DuplicateGuestRoomRequestSupplier**](DuplicateGuestRoomRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RoomTypeSupplier**](RoomTypeSupplier.md)

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

# **improve_guest_room**
> ImproveRoomTypeResponseSupplier improve_guest_room(property_identifier, room_type_identifier, improve_room_type_request_supplier, wink_version=wink_version)

Improve Guest Room

Tries to improve upon descriptive text and more in the future.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.improve_room_type_request_supplier import ImproveRoomTypeRequestSupplier
from wink_sdk_extranet_facilities.models.improve_room_type_response_supplier import ImproveRoomTypeResponseSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Improve room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Improve room type with this identifier
    improve_room_type_request_supplier = wink_sdk_extranet_facilities.ImproveRoomTypeRequestSupplier() # ImproveRoomTypeRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Improve Guest Room
        api_response = api_instance.improve_guest_room(property_identifier, room_type_identifier, improve_room_type_request_supplier, wink_version=wink_version)
        print("The response of GuestRoomApi->improve_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->improve_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Improve room type owned by this property identifier | 
 **room_type_identifier** | **str**| Improve room type with this identifier | 
 **improve_room_type_request_supplier** | [**ImproveRoomTypeRequestSupplier**](ImproveRoomTypeRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ImproveRoomTypeResponseSupplier**](ImproveRoomTypeResponseSupplier.md)

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

# **remove_guest_room**
> RoomType remove_guest_room(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)

Delete Guest Room

Remove a room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type import RoomType
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Remove room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Remove room type with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Guest Room
        api_response = api_instance.remove_guest_room(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)
        print("The response of GuestRoomApi->remove_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->remove_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove room type owned by this property identifier | 
 **room_type_identifier** | **str**| Remove room type with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RoomType**](RoomType.md)

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

# **remove_multimedia**
> RoomType remove_multimedia(property_identifier, room_type_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Guest Room Multimedia

Remove a room's video or image by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type import RoomType
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Remove room type media owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Remove room type media with this identifier
    multimedia_identifier = 'media-1' # str | Remove media with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Guest Room Multimedia
        api_response = api_instance.remove_multimedia(property_identifier, room_type_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of GuestRoomApi->remove_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->remove_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove room type media owned by this property identifier | 
 **room_type_identifier** | **str**| Remove room type media with this identifier | 
 **multimedia_identifier** | **str**| Remove media with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RoomType**](RoomType.md)

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

# **show_guest_room**
> RoomTypeSupplier show_guest_room(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)

Show Guest Room

Retrieve a room type by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Show room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Show room type identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Guest Room
        api_response = api_instance.show_guest_room(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)
        print("The response of GuestRoomApi->show_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->show_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show room type owned by this property identifier | 
 **room_type_identifier** | **str**| Show room type identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RoomTypeSupplier**](RoomTypeSupplier.md)

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

# **show_guest_rooms**
> List[RoomTypeSupplier] show_guest_rooms(property_identifier, wink_version=wink_version, accept=accept)

Show Guest Rooms

Retrieve list of rooms

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Show list of room types owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Guest Rooms
        api_response = api_instance.show_guest_rooms(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of GuestRoomApi->show_guest_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->show_guest_rooms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show list of room types owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[RoomTypeSupplier]**](RoomTypeSupplier.md)

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

# **update_guest_room**
> RoomTypeSupplier update_guest_room(property_identifier, room_type_identifier, upsert_room_type_request_supplier, wink_version=wink_version)

Update Guest Room

Update a room by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
from wink_sdk_extranet_facilities.models.upsert_room_type_request_supplier import UpsertRoomTypeRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Update room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Update room type with this identifier
    upsert_room_type_request_supplier = wink_sdk_extranet_facilities.UpsertRoomTypeRequestSupplier() # UpsertRoomTypeRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Guest Room
        api_response = api_instance.update_guest_room(property_identifier, room_type_identifier, upsert_room_type_request_supplier, wink_version=wink_version)
        print("The response of GuestRoomApi->update_guest_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->update_guest_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update room type owned by this property identifier | 
 **room_type_identifier** | **str**| Update room type with this identifier | 
 **upsert_room_type_request_supplier** | [**UpsertRoomTypeRequestSupplier**](UpsertRoomTypeRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RoomTypeSupplier**](RoomTypeSupplier.md)

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

# **upload_guest_room_media**
> RoomTypeSupplier upload_guest_room_media(property_identifier, room_type_identifier, files)

Add Multimedia to Room

Uploads a videos and/or images to a room identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.room_type_supplier import RoomTypeSupplier
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
    api_instance = wink_sdk_extranet_facilities.GuestRoomApi(api_client)
    property_identifier = 'hotel-1' # str | Upload media for room type owned by this property identifier
    room_type_identifier = 'guest-room-1' # str | Upload media for room type with this identifier
    files = None # List[bytearray] | 

    try:
        # Add Multimedia to Room
        api_response = api_instance.upload_guest_room_media(property_identifier, room_type_identifier, files)
        print("The response of GuestRoomApi->upload_guest_room_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestRoomApi->upload_guest_room_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload media for room type owned by this property identifier | 
 **room_type_identifier** | **str**| Upload media for room type with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**RoomTypeSupplier**](RoomTypeSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml, text/plain, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**207** | Multi-Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

