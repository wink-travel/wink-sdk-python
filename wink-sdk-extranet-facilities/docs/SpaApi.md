# wink_sdk_extranet_facilities.SpaApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spa**](SpaApi.md#create_spa) | **POST** /api/property/{propertyIdentifier}/facility/spa | Create Spa
[**delete_multimedia**](SpaApi.md#delete_multimedia) | **DELETE** /api/property/{propertyIdentifier}/facility/spa/{spaIdentifier}/multimedia/{multimediaIdentifier} | Delete Multimedia
[**remove_spa**](SpaApi.md#remove_spa) | **DELETE** /api/property/{propertyIdentifier}/facility/spa/{spaIdentifier} | Delete Spa
[**show_spa**](SpaApi.md#show_spa) | **GET** /api/property/{propertyIdentifier}/facility/spa/{spaIdentifier} | Show Spa
[**show_spa_pairs**](SpaApi.md#show_spa_pairs) | **GET** /api/property/{propertyIdentifier}/facility/spa/list/pair | Show Reference Pairs
[**show_spas**](SpaApi.md#show_spas) | **GET** /api/property/{propertyIdentifier}/facility/spa/list | Show Spas
[**update_spa**](SpaApi.md#update_spa) | **PUT** /api/property/{propertyIdentifier}/facility/spa/{spaIdentifier} | Update Spa
[**upload_spa_media**](SpaApi.md#upload_spa_media) | **POST** /api/property/{propertyIdentifier}/facility/spa/{spaIdentifier}/multimedia | Upload Binary Multimedia


# **create_spa**
> SpaSupplier create_spa(property_identifier, upsert_spa_request_supplier, wink_version=wink_version)

Create Spa

Create a new spa

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
from wink_sdk_extranet_facilities.models.upsert_spa_request_supplier import UpsertSpaRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new spa record owned by this property identifier
    upsert_spa_request_supplier = wink_sdk_extranet_facilities.UpsertSpaRequestSupplier() # UpsertSpaRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Spa
        api_response = api_instance.create_spa(property_identifier, upsert_spa_request_supplier, wink_version=wink_version)
        print("The response of SpaApi->create_spa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->create_spa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new spa record owned by this property identifier | 
 **upsert_spa_request_supplier** | [**UpsertSpaRequestSupplier**](UpsertSpaRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

# **delete_multimedia**
> SpaSupplier delete_multimedia(property_identifier, spa_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Multimedia

Remove media from an existing spa.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a media record from an existing spa owned by this property identifier.
    spa_identifier = 'spa-1' # str | Remove a media record from an existing spa identified by this identifier.
    multimedia_identifier = 'media-1' # str | Remove a media record with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia
        api_response = api_instance.delete_multimedia(property_identifier, spa_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of SpaApi->delete_multimedia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->delete_multimedia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a media record from an existing spa owned by this property identifier. | 
 **spa_identifier** | **str**| Remove a media record from an existing spa identified by this identifier. | 
 **multimedia_identifier** | **str**| Remove a media record with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

# **remove_spa**
> SpaSupplier remove_spa(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)

Delete Spa

Delete a spa by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Remove spa record owned by this property identifier
    spa_identifier = 'spa-1' # str | Remove restaurant record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Spa
        api_response = api_instance.remove_spa(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)
        print("The response of SpaApi->remove_spa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->remove_spa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove spa record owned by this property identifier | 
 **spa_identifier** | **str**| Remove restaurant record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

# **show_spa**
> SpaSupplier show_spa(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)

Show Spa

Retrieve a spa by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Show single spa owned by this property identifier
    spa_identifier = 'spa-1' # str | Show spa record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Spa
        api_response = api_instance.show_spa(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)
        print("The response of SpaApi->show_spa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->show_spa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single spa owned by this property identifier | 
 **spa_identifier** | **str**| Show spa record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

# **show_spa_pairs**
> List[KeyValuePairSupplier] show_spa_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Reference Pairs

Retrieve list of spas as key/value pairs (identifier, name)

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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Show spa pairs owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Reference Pairs
        api_response = api_instance.show_spa_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of SpaApi->show_spa_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->show_spa_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show spa pairs owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **show_spas**
> List[SpaSupplier] show_spas(property_identifier, wink_version=wink_version, accept=accept)

Show Spas

Retrieve list of spas for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Show spas owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Spas
        api_response = api_instance.show_spas(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of SpaApi->show_spas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->show_spas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show spas owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SpaSupplier]**](SpaSupplier.md)

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

# **update_spa**
> SpaSupplier update_spa(property_identifier, spa_identifier, upsert_spa_request_supplier, wink_version=wink_version)

Update Spa

Update a spa by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
from wink_sdk_extranet_facilities.models.upsert_spa_request_supplier import UpsertSpaRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing spa record owned by this property identifier
    spa_identifier = 'spa-1' # str | Update an existing spa record identified by this identifier
    upsert_spa_request_supplier = wink_sdk_extranet_facilities.UpsertSpaRequestSupplier() # UpsertSpaRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Spa
        api_response = api_instance.update_spa(property_identifier, spa_identifier, upsert_spa_request_supplier, wink_version=wink_version)
        print("The response of SpaApi->update_spa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->update_spa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing spa record owned by this property identifier | 
 **spa_identifier** | **str**| Update an existing spa record identified by this identifier | 
 **upsert_spa_request_supplier** | [**UpsertSpaRequestSupplier**](UpsertSpaRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

# **upload_spa_media**
> SpaSupplier upload_spa_media(property_identifier, spa_identifier, files)

Upload Binary Multimedia

Upload a list of binary / multipart videos and/or images to an existing spa.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.spa_supplier import SpaSupplier
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
    api_instance = wink_sdk_extranet_facilities.SpaApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart files and associate them with an existing spa owned by this property identifier
    spa_identifier = 'spa-1' # str | Upload multipart files and associate them with an existing spa with this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_spa_media(property_identifier, spa_identifier, files)
        print("The response of SpaApi->upload_spa_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaApi->upload_spa_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart files and associate them with an existing spa owned by this property identifier | 
 **spa_identifier** | **str**| Upload multipart files and associate them with an existing spa with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**SpaSupplier**](SpaSupplier.md)

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

