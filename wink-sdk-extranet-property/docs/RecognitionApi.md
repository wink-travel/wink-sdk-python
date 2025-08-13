# wink_sdk_extranet_property.RecognitionApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recognition**](RecognitionApi.md#create_recognition) | **POST** /api/property/{propertyIdentifier}/recognition | Create Recognition
[**remove_recognition**](RecognitionApi.md#remove_recognition) | **DELETE** /api/property/{propertyIdentifier}/recognition/{recognitionIdentifier} | Delete Recognition
[**show_recognition**](RecognitionApi.md#show_recognition) | **GET** /api/property/{propertyIdentifier}/recognition/{recognitionIdentifier} | Show Recognition
[**show_recognitions**](RecognitionApi.md#show_recognitions) | **GET** /api/property/{propertyIdentifier}/recognition/list | Show Recognitions
[**show_recognitions_by_category**](RecognitionApi.md#show_recognitions_by_category) | **GET** /api/property/{propertyIdentifier}/recognition/{category}/list | Show Recognition by Category
[**update_recognition**](RecognitionApi.md#update_recognition) | **PUT** /api/property/{propertyIdentifier}/recognition/{recognitionIdentifier} | Update Recognition


# **create_recognition**
> PropertySupplier create_recognition(property_identifier, upsert_recognition_supplier, wink_version=wink_version)

Create Recognition

Create a new request

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.upsert_recognition_supplier import UpsertRecognitionSupplier
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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Associate new request record with this property identifier
    upsert_recognition_supplier = wink_sdk_extranet_property.UpsertRecognitionSupplier() # UpsertRecognitionSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Recognition
        api_response = api_instance.create_recognition(property_identifier, upsert_recognition_supplier, wink_version=wink_version)
        print("The response of RecognitionApi->create_recognition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->create_recognition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Associate new request record with this property identifier | 
 **upsert_recognition_supplier** | [**UpsertRecognitionSupplier**](UpsertRecognitionSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

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

# **remove_recognition**
> PropertySupplier remove_recognition(property_identifier, recognition_identifier, wink_version=wink_version, accept=accept)

Delete Recognition

Delete a recognition by its identifier

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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Delete recognition record for property with this property identifier
    recognition_identifier = 'recognition-1' # str | Delete recognition with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Recognition
        api_response = api_instance.remove_recognition(property_identifier, recognition_identifier, wink_version=wink_version, accept=accept)
        print("The response of RecognitionApi->remove_recognition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->remove_recognition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Delete recognition record for property with this property identifier | 
 **recognition_identifier** | **str**| Delete recognition with this identifier | 
 **wink_version** | **str**|  | [optional] 
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

# **show_recognition**
> TravelInventoryRecognitionSupplier show_recognition(property_identifier, recognition_identifier, wink_version=wink_version, accept=accept)

Show Recognition

Retrieve a recognition by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Show recognition belonging to this property identifier
    recognition_identifier = 'recognition-1' # str | Show recognition associated with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Recognition
        api_response = api_instance.show_recognition(property_identifier, recognition_identifier, wink_version=wink_version, accept=accept)
        print("The response of RecognitionApi->show_recognition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->show_recognition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show recognition belonging to this property identifier | 
 **recognition_identifier** | **str**| Show recognition associated with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**TravelInventoryRecognitionSupplier**](TravelInventoryRecognitionSupplier.md)

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

# **show_recognitions**
> List[TravelInventoryRecognitionSupplier] show_recognitions(property_identifier, wink_version=wink_version, accept=accept)

Show Recognitions

Retrieve a list of all recognitions for property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Show list of recognitions for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Recognitions
        api_response = api_instance.show_recognitions(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of RecognitionApi->show_recognitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->show_recognitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show list of recognitions for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[TravelInventoryRecognitionSupplier]**](TravelInventoryRecognitionSupplier.md)

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

# **show_recognitions_by_category**
> List[TravelInventoryRecognitionSupplier] show_recognitions_by_category(property_identifier, category, wink_version=wink_version, accept=accept)

Show Recognition by Category

Retrieve list recognitions by category

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Show list of recognitions for this property identifier
    category = 'AWARD' # str | Filter list of recognitions by category
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Recognition by Category
        api_response = api_instance.show_recognitions_by_category(property_identifier, category, wink_version=wink_version, accept=accept)
        print("The response of RecognitionApi->show_recognitions_by_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->show_recognitions_by_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show list of recognitions for this property identifier | 
 **category** | **str**| Filter list of recognitions by category | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[TravelInventoryRecognitionSupplier]**](TravelInventoryRecognitionSupplier.md)

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

# **update_recognition**
> PropertySupplier update_recognition(property_identifier, recognition_identifier, upsert_recognition_supplier, wink_version=wink_version)

Update Recognition

Update a recognition by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.upsert_recognition_supplier import UpsertRecognitionSupplier
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
    api_instance = wink_sdk_extranet_property.RecognitionApi(api_client)
    property_identifier = 'hotel-1' # str | Update recognition record associated with this property identifier
    recognition_identifier = 'recognition-1' # str | Update recognition with this identifier
    upsert_recognition_supplier = wink_sdk_extranet_property.UpsertRecognitionSupplier() # UpsertRecognitionSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Recognition
        api_response = api_instance.update_recognition(property_identifier, recognition_identifier, upsert_recognition_supplier, wink_version=wink_version)
        print("The response of RecognitionApi->update_recognition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecognitionApi->update_recognition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update recognition record associated with this property identifier | 
 **recognition_identifier** | **str**| Update recognition with this identifier | 
 **upsert_recognition_supplier** | [**UpsertRecognitionSupplier**](UpsertRecognitionSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

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

