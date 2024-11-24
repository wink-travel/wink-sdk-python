# wink_sdk_extranet_experiences.PlaceApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_place**](PlaceApi.md#create_place) | **POST** /api/property/{propertyIdentifier}/experience/place | Create Place
[**remove_place**](PlaceApi.md#remove_place) | **DELETE** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Delete Place
[**show_place**](PlaceApi.md#show_place) | **GET** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Show Place
[**show_place_pairs**](PlaceApi.md#show_place_pairs) | **GET** /api/property/{propertyIdentifier}/experience/place/list/pair | Show Reference Pairs
[**show_places**](PlaceApi.md#show_places) | **GET** /api/property/{propertyIdentifier}/experience/place/list | Show Places
[**update_place**](PlaceApi.md#update_place) | **PUT** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier} | Update Place
[**upload_place_media**](PlaceApi.md#upload_place_media) | **POST** /api/property/{propertyIdentifier}/experience/place/{placeIdentifier}/multimedia | Upload Binary Multimedia


# **create_place**
> RefPointViewSupplier create_place(property_identifier, upsert_place_request_supplier, wink_version=wink_version)

Create Place

Create a new place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
from wink_sdk_extranet_experiences.models.upsert_place_request_supplier import UpsertPlaceRequestSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new place record owned by this property identifier
    upsert_place_request_supplier = wink_sdk_extranet_experiences.UpsertPlaceRequestSupplier() # UpsertPlaceRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Place
        api_response = api_instance.create_place(property_identifier, upsert_place_request_supplier, wink_version=wink_version)
        print("The response of PlaceApi->create_place:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->create_place: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new place record owned by this property identifier | 
 **upsert_place_request_supplier** | [**UpsertPlaceRequestSupplier**](UpsertPlaceRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RefPointViewSupplier**](RefPointViewSupplier.md)

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

# **remove_place**
> RefPointViewSupplier remove_place(property_identifier, place_identifier, wink_version=wink_version, accept=accept)

Delete Place

Delete a place by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Remove place record owned by this property identifier
    place_identifier = 'place-1' # str | Remove place record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Place
        api_response = api_instance.remove_place(property_identifier, place_identifier, wink_version=wink_version, accept=accept)
        print("The response of PlaceApi->remove_place:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->remove_place: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove place record owned by this property identifier | 
 **place_identifier** | **str**| Remove place record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RefPointViewSupplier**](RefPointViewSupplier.md)

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

# **show_place**
> RefPointViewSupplier show_place(property_identifier, place_identifier, wink_version=wink_version, accept=accept)

Show Place

Retrieve a place by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Show single place owned by this property identifier
    place_identifier = 'place-1' # str | Show place record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Place
        api_response = api_instance.show_place(property_identifier, place_identifier, wink_version=wink_version, accept=accept)
        print("The response of PlaceApi->show_place:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->show_place: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single place owned by this property identifier | 
 **place_identifier** | **str**| Show place record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RefPointViewSupplier**](RefPointViewSupplier.md)

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

# **show_place_pairs**
> List[KeyValuePairSupplier] show_place_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Reference Pairs

Retrieve list of places as key/value pairs (identifier, name)

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Show place pairs owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Reference Pairs
        api_response = api_instance.show_place_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PlaceApi->show_place_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->show_place_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show place pairs owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **show_places**
> List[RefPointViewSupplier] show_places(property_identifier, wink_version=wink_version, accept=accept)

Show Places

Retrieve list of places for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Show places owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Places
        api_response = api_instance.show_places(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PlaceApi->show_places:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->show_places: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show places owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[RefPointViewSupplier]**](RefPointViewSupplier.md)

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

# **update_place**
> RefPointViewSupplier update_place(property_identifier, place_identifier, upsert_place_request_supplier, wink_version=wink_version)

Update Place

Update a place by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
from wink_sdk_extranet_experiences.models.upsert_place_request_supplier import UpsertPlaceRequestSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing place record owned by this property identifier
    place_identifier = 'place-1' # str | Update an existing place record identified by this identifier
    upsert_place_request_supplier = wink_sdk_extranet_experiences.UpsertPlaceRequestSupplier() # UpsertPlaceRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Place
        api_response = api_instance.update_place(property_identifier, place_identifier, upsert_place_request_supplier, wink_version=wink_version)
        print("The response of PlaceApi->update_place:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->update_place: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing place record owned by this property identifier | 
 **place_identifier** | **str**| Update an existing place record identified by this identifier | 
 **upsert_place_request_supplier** | [**UpsertPlaceRequestSupplier**](UpsertPlaceRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RefPointViewSupplier**](RefPointViewSupplier.md)

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

# **upload_place_media**
> RefPointViewSupplier upload_place_media(property_identifier, place_identifier, files)

Upload Binary Multimedia

Upload a list of binary / multipart videos and/or images to an existing place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
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
    api_instance = wink_sdk_extranet_experiences.PlaceApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart files and associate them with an existing place owned by this property identifier
    place_identifier = 'place-1' # str | Upload multipart files and associate them with an existing place with this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_place_media(property_identifier, place_identifier, files)
        print("The response of PlaceApi->upload_place_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaceApi->upload_place_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart files and associate them with an existing place owned by this property identifier | 
 **place_identifier** | **str**| Upload multipart files and associate them with an existing place with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**RefPointViewSupplier**](RefPointViewSupplier.md)

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

