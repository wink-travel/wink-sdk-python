# wink_sdk_extranet_property.MediaApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_multimedia**](MediaApi.md#create_multimedia) | **POST** /api/property/{propertyIdentifier}/multimedia | Create Multimedia
[**remove_media_list**](MediaApi.md#remove_media_list) | **DELETE** /api/property/{propertyIdentifier}/multimedia/list | Delete Multimedia List
[**remove_multimedia**](MediaApi.md#remove_multimedia) | **DELETE** /api/property/{propertyIdentifier}/multimedia/{multimediaIdentifier} | Delete Multimedia
[**show_media_list**](MediaApi.md#show_media_list) | **GET** /api/property/{propertyIdentifier}/multimedia/list | Show Multimedia
[**update_media_list**](MediaApi.md#update_media_list) | **POST** /api/property/{propertyIdentifier}/multimedia/list | Update Multimedia List
[**update_multimedia**](MediaApi.md#update_multimedia) | **PUT** /api/property/{propertyIdentifier}/multimedia/{multimediaIdentifier} | Update Multimedia
[**upload_multipart_files**](MediaApi.md#upload_multipart_files) | **POST** /api/property/{propertyIdentifier}/multimedia/upload | Upload Multimedia


# **create_multimedia**
> PropertySupplier create_multimedia(property_identifier, simple_multimedia_supplier, wink_version=wink_version)

Create Multimedia

Save multimedia of a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.simple_multimedia_supplier import SimpleMultimediaSupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Save a single media associated with this property identifier
    simple_multimedia_supplier = wink_sdk_extranet_property.SimpleMultimediaSupplier() # SimpleMultimediaSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Multimedia
        api_response = api_instance.create_multimedia(property_identifier, simple_multimedia_supplier, wink_version=wink_version)
        print("The response of MediaApi->create_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->create_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Save a single media associated with this property identifier | 
 **simple_multimedia_supplier** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

# **remove_media_list**
> PropertySupplier remove_media_list(property_identifier, multimedia_identifiers, wink_version=wink_version, accept=accept)

Delete Multimedia List

Remove multimedia list of a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Remove selected media for this property identifier
    multimedia_identifiers = ['media-1,media-2,media-3'] # List[str] | Remove media identified by these identifiers
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia List
        api_response = api_instance.remove_media_list(property_identifier, multimedia_identifiers, wink_version=wink_version, accept=accept)
        print("The response of MediaApi->remove_media_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->remove_media_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove selected media for this property identifier | 
 **multimedia_identifiers** | [**List[str]**](str.md)| Remove media identified by these identifiers | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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
**207** | Multi-Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_multimedia**
> PropertySupplier remove_multimedia(property_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Multimedia

Remove multimedia record for hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a single media associated with this property identifier
    multimedia_identifier = 'media-1' # str | Remove record for this media identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia
        api_response = api_instance.remove_multimedia(property_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of MediaApi->remove_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->remove_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a single media associated with this property identifier | 
 **multimedia_identifier** | **str**| Remove record for this media identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

# **show_media_list**
> List[SimpleMultimediaSupplier] show_media_list(property_identifier, wink_version=wink_version, accept=accept)

Show Multimedia

Retrieve list of multimedia (images / videos) for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.simple_multimedia_supplier import SimpleMultimediaSupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Show media associated with this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Multimedia
        api_response = api_instance.show_media_list(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of MediaApi->show_media_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->show_media_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show media associated with this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md)

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

# **update_media_list**
> PropertySupplier update_media_list(property_identifier, simple_multimedia_supplier, wink_version=wink_version)

Update Multimedia List

Save/Update multimedia list of a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.simple_multimedia_supplier import SimpleMultimediaSupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Save media to the property with this property identifier
    simple_multimedia_supplier = [wink_sdk_extranet_property.SimpleMultimediaSupplier()] # List[SimpleMultimediaSupplier] | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Multimedia List
        api_response = api_instance.update_media_list(property_identifier, simple_multimedia_supplier, wink_version=wink_version)
        print("The response of MediaApi->update_media_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->update_media_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Save media to the property with this property identifier | 
 **simple_multimedia_supplier** | [**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

# **update_multimedia**
> PropertySupplier update_multimedia(property_identifier, multimedia_identifier, simple_multimedia_supplier, wink_version=wink_version)

Update Multimedia

Update multimedia properties of a hotel identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.simple_multimedia_supplier import SimpleMultimediaSupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Update a single media associated with this property identifier
    multimedia_identifier = 'media-1' # str | Update record for this media identifier
    simple_multimedia_supplier = wink_sdk_extranet_property.SimpleMultimediaSupplier() # SimpleMultimediaSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Multimedia
        api_response = api_instance.update_multimedia(property_identifier, multimedia_identifier, simple_multimedia_supplier, wink_version=wink_version)
        print("The response of MediaApi->update_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->update_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update a single media associated with this property identifier | 
 **multimedia_identifier** | **str**| Update record for this media identifier | 
 **simple_multimedia_supplier** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

# **upload_multipart_files**
> PropertySupplier upload_multipart_files(property_identifier, files)

Upload Multimedia

Upload videos and/or images and associate it with specified hotelIdentifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
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
    api_instance = wink_sdk_extranet_property.MediaApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart file media for this property identifier
    files = None # List[bytearray] | 

    try:
        # Upload Multimedia
        api_response = api_instance.upload_multipart_files(property_identifier, files)
        print("The response of MediaApi->upload_multipart_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->upload_multipart_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart file media for this property identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

