# wink_sdk_extranet_monetize.AddOnApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_multimedia**](AddOnApi.md#add_multimedia) | **PATCH** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier}/multimedia | Add Multimedia
[**create_add_on**](AddOnApi.md#create_add_on) | **POST** /api/property/{propertyIdentifier}/add-on | Create Add-On
[**remove_add_on**](AddOnApi.md#remove_add_on) | **DELETE** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier} | Delete Add-On
[**remove_multimedia**](AddOnApi.md#remove_multimedia) | **DELETE** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier}/multimedia/{multimediaIdentifier} | Delete Multimedia
[**show_add_on**](AddOnApi.md#show_add_on) | **GET** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier} | Show Add-On
[**show_add_ons**](AddOnApi.md#show_add_ons) | **GET** /api/property/{propertyIdentifier}/add-on/list | Show Add-Ons
[**update_add_on**](AddOnApi.md#update_add_on) | **PUT** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier} | Update Add-On
[**update_add_on_multimedia**](AddOnApi.md#update_add_on_multimedia) | **PATCH** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier}/multimedia/{multimediaIdentifier} | Update Multimedia
[**upload_binary_add_on_media**](AddOnApi.md#upload_binary_add_on_media) | **POST** /api/property/{propertyIdentifier}/add-on/{addOnIdentifier}/multimedia | Upload Binary Multimedia


# **add_multimedia**
> AddOn add_multimedia(property_identifier, add_on_identifier, simple_multimedia, wink_version=wink_version)

Add Multimedia

Uploads a videos and/or images to an add-on identified by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.models.simple_multimedia import SimpleMultimedia
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Add multimedia record to add-on record owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Add multimedia record to add-on with this identifier
    simple_multimedia = wink_sdk_extranet_monetize.SimpleMultimedia() # SimpleMultimedia | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add Multimedia
        api_response = api_instance.add_multimedia(property_identifier, add_on_identifier, simple_multimedia, wink_version=wink_version)
        print("The response of AddOnApi->add_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->add_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Add multimedia record to add-on record owned by this property identifier | 
 **add_on_identifier** | **str**| Add multimedia record to add-on with this identifier | 
 **simple_multimedia** | [**SimpleMultimedia**](SimpleMultimedia.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_add_on**
> AddOn create_add_on(property_identifier, upsert_add_on_request, wink_version=wink_version)

Create Add-On

Create a new add-on.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.models.upsert_add_on_request import UpsertAddOnRequest
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new add-on record owned by this property identifier
    upsert_add_on_request = wink_sdk_extranet_monetize.UpsertAddOnRequest() # UpsertAddOnRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Add-On
        api_response = api_instance.create_add_on(property_identifier, upsert_add_on_request, wink_version=wink_version)
        print("The response of AddOnApi->create_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->create_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new add-on record owned by this property identifier | 
 **upsert_add_on_request** | [**UpsertAddOnRequest**](UpsertAddOnRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_add_on**
> RemoveEntryResponse remove_add_on(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)

Delete Add-On

Delete an add-on by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.remove_entry_response import RemoveEntryResponse
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Remove add-on record owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Remove add-on record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Add-On
        api_response = api_instance.remove_add_on(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)
        print("The response of AddOnApi->remove_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->remove_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove add-on record owned by this property identifier | 
 **add_on_identifier** | **str**| Remove add-on record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RemoveEntryResponse**](RemoveEntryResponse.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_multimedia**
> AddOn remove_multimedia(property_identifier, add_on_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Multimedia

Remove media from an existing add-on.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a media record from an existing add-on owned by this property identifier.
    add_on_identifier = 'add-on-1' # str | Remove a media record from an existing add-on identified by this identifier.
    multimedia_identifier = 'media-1' # str | Remove a media record with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia
        api_response = api_instance.remove_multimedia(property_identifier, add_on_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of AddOnApi->remove_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->remove_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a media record from an existing add-on owned by this property identifier. | 
 **add_on_identifier** | **str**| Remove a media record from an existing add-on identified by this identifier. | 
 **multimedia_identifier** | **str**| Remove a media record with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_add_on**
> AddOn show_add_on(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)

Show Add-On

Retrieve an add-on by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Show single add-on owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Show add-on record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Add-On
        api_response = api_instance.show_add_on(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)
        print("The response of AddOnApi->show_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->show_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single add-on owned by this property identifier | 
 **add_on_identifier** | **str**| Show add-on record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_add_ons**
> List[AddOn] show_add_ons(property_identifier, wink_version=wink_version, accept=accept)

Show Add-Ons

Retrieve a list of all add-ons for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Show add-ons owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Add-Ons
        api_response = api_instance.show_add_ons(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AddOnApi->show_add_ons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->show_add_ons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show add-ons owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[AddOn]**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_add_on**
> AddOn update_add_on(property_identifier, add_on_identifier, upsert_add_on_request, wink_version=wink_version)

Update Add-On

Update an existing add-on.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.models.upsert_add_on_request import UpsertAddOnRequest
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing add-on record owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Update an existing add-on record identified by this identifier
    upsert_add_on_request = wink_sdk_extranet_monetize.UpsertAddOnRequest() # UpsertAddOnRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Add-On
        api_response = api_instance.update_add_on(property_identifier, add_on_identifier, upsert_add_on_request, wink_version=wink_version)
        print("The response of AddOnApi->update_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->update_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing add-on record owned by this property identifier | 
 **add_on_identifier** | **str**| Update an existing add-on record identified by this identifier | 
 **upsert_add_on_request** | [**UpsertAddOnRequest**](UpsertAddOnRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_add_on_multimedia**
> AddOn update_add_on_multimedia(property_identifier, add_on_identifier, multimedia_identifier, simple_multimedia, wink_version=wink_version)

Update Multimedia

Update media meta data for a specific package media entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.models.simple_multimedia import SimpleMultimedia
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing multimedia record on add-on record owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Update existing multimedia record on add-on with this identifier
    multimedia_identifier = 'media-1' # str | Update existing multimedia record with this identifier
    simple_multimedia = wink_sdk_extranet_monetize.SimpleMultimedia() # SimpleMultimedia | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Multimedia
        api_response = api_instance.update_add_on_multimedia(property_identifier, add_on_identifier, multimedia_identifier, simple_multimedia, wink_version=wink_version)
        print("The response of AddOnApi->update_add_on_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->update_add_on_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing multimedia record on add-on record owned by this property identifier | 
 **add_on_identifier** | **str**| Update existing multimedia record on add-on with this identifier | 
 **multimedia_identifier** | **str**| Update existing multimedia record with this identifier | 
 **simple_multimedia** | [**SimpleMultimedia**](SimpleMultimedia.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_binary_add_on_media**
> AddOn upload_binary_add_on_media(property_identifier, add_on_identifier, files)

Upload Binary Multimedia

Upload a list of binary / multipart videos and/or images to an existing add-on.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.add_on import AddOn
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.AddOnApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart files and associate them with an existing add-on owned by this property identifier
    add_on_identifier = 'add-on-1' # str | Upload multipart files and associate them with an existing add-on with this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_binary_add_on_media(property_identifier, add_on_identifier, files)
        print("The response of AddOnApi->upload_binary_add_on_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnApi->upload_binary_add_on_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart files and associate them with an existing add-on owned by this property identifier | 
 **add_on_identifier** | **str**| Upload multipart files and associate them with an existing add-on with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**AddOn**](AddOn.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**207** | Multi-Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

