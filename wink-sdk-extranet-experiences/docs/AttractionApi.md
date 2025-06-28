# wink_sdk_extranet_experiences.AttractionApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attraction**](AttractionApi.md#create_attraction) | **POST** /api/property/{propertyIdentifier}/experience/attraction | Create Attraction
[**remove_attraction**](AttractionApi.md#remove_attraction) | **DELETE** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Delete attraction
[**show_attraction**](AttractionApi.md#show_attraction) | **GET** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Show Attraction
[**show_attraction_pairs**](AttractionApi.md#show_attraction_pairs) | **GET** /api/property/{propertyIdentifier}/experience/attraction/list/pair | Show Attractions as Pairs
[**show_attractions**](AttractionApi.md#show_attractions) | **GET** /api/property/{propertyIdentifier}/experience/attraction/list | Show Attractions
[**update_attraction**](AttractionApi.md#update_attraction) | **PUT** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier} | Update Attraction
[**upload_attraction_media**](AttractionApi.md#upload_attraction_media) | **POST** /api/property/{propertyIdentifier}/experience/attraction/{attractionIdentifier}/multimedia | Upload Binary Multimedia


# **create_attraction**
> Attraction create_attraction(property_identifier, upsert_attraction_request, wink_version=wink_version)

Create Attraction

Create a new attraction

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
from wink_sdk_extranet_experiences.models.upsert_attraction_request import UpsertAttractionRequest
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Persist attraction owned by this property identifier
    upsert_attraction_request = wink_sdk_extranet_experiences.UpsertAttractionRequest() # UpsertAttractionRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Attraction
        api_response = api_instance.create_attraction(property_identifier, upsert_attraction_request, wink_version=wink_version)
        print("The response of AttractionApi->create_attraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->create_attraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Persist attraction owned by this property identifier | 
 **upsert_attraction_request** | [**UpsertAttractionRequest**](UpsertAttractionRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Attraction**](Attraction.md)

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

# **remove_attraction**
> Attraction remove_attraction(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)

Delete attraction

Delete an attraction by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Delete attraction owned by this property identifier
    attraction_identifier = 'attraction-1' # str | Delete attraction identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete attraction
        api_response = api_instance.remove_attraction(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)
        print("The response of AttractionApi->remove_attraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->remove_attraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Delete attraction owned by this property identifier | 
 **attraction_identifier** | **str**| Delete attraction identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Attraction**](Attraction.md)

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

# **show_attraction**
> Attraction show_attraction(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)

Show Attraction

Retrieve an attraction by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Show attraction owned by this property identifier
    attraction_identifier = 'attraction-1' # str | Show attraction for identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attraction
        api_response = api_instance.show_attraction(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)
        print("The response of AttractionApi->show_attraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->show_attraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show attraction owned by this property identifier | 
 **attraction_identifier** | **str**| Show attraction for identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Attraction**](Attraction.md)

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

# **show_attraction_pairs**
> List[KeyValuePair] show_attraction_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Attractions as Pairs

Retrieve list of key value pairs (identifier, name)

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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Show attraction key/value pairs associated with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attractions as Pairs
        api_response = api_instance.show_attraction_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AttractionApi->show_attraction_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->show_attraction_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show attraction key/value pairs associated with this property identifier | 
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

# **show_attractions**
> List[Attraction] show_attractions(property_identifier, wink_version=wink_version, accept=accept)

Show Attractions

Retrieve list of attractions

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Show attractions associated with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attractions
        api_response = api_instance.show_attractions(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AttractionApi->show_attractions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->show_attractions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show attractions associated with this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Attraction]**](Attraction.md)

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

# **update_attraction**
> Attraction update_attraction(property_identifier, attraction_identifier, upsert_attraction_request, wink_version=wink_version)

Update Attraction

Update an attraction by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
from wink_sdk_extranet_experiences.models.upsert_attraction_request import UpsertAttractionRequest
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing attraction record owned by this property identifier
    attraction_identifier = 'attraction-1' # str | Update attraction record with this identifier
    upsert_attraction_request = wink_sdk_extranet_experiences.UpsertAttractionRequest() # UpsertAttractionRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Attraction
        api_response = api_instance.update_attraction(property_identifier, attraction_identifier, upsert_attraction_request, wink_version=wink_version)
        print("The response of AttractionApi->update_attraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->update_attraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing attraction record owned by this property identifier | 
 **attraction_identifier** | **str**| Update attraction record with this identifier | 
 **upsert_attraction_request** | [**UpsertAttractionRequest**](UpsertAttractionRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Attraction**](Attraction.md)

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

# **upload_attraction_media**
> Attraction upload_attraction_media(property_identifier, attraction_identifier, files)

Upload Binary Multimedia

Upload binary videos and/or images to an attraction identified by its identifier. Valid file types: .gif, .jpg, .jpeg, .png, .bmp, .tif, .tiff, .avi, .mpeg, .mov, .mp4, .mkv.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_experiences
from wink_sdk_extranet_experiences.models.attraction import Attraction
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
    api_instance = wink_sdk_extranet_experiences.AttractionApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart media for attraction owned by this property identifier
    attraction_identifier = 'attraction-1' # str | Associate multipart media with attraction identified by this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_attraction_media(property_identifier, attraction_identifier, files)
        print("The response of AttractionApi->upload_attraction_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttractionApi->upload_attraction_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart media for attraction owned by this property identifier | 
 **attraction_identifier** | **str**| Associate multipart media with attraction identified by this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**Attraction**](Attraction.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**207** | Multi-Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

