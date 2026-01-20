# wink_sdk_extranet_property.PropertyApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**improve_welcome_text**](PropertyApi.md#improve_welcome_text) | **POST** /api/property/{propertyIdentifier}/welcome-text/improve | Improve Welcome Text
[**is_hotel_name_unique**](PropertyApi.md#is_hotel_name_unique) | **GET** /api/property/unique/name | Check Property Name Uniqueness
[**is_hotel_url_name_unique**](PropertyApi.md#is_hotel_url_name_unique) | **GET** /api/property/unique/url-name | Check Property Url Slug Uniqueness
[**show_hotel_by_manager**](PropertyApi.md#show_hotel_by_manager) | **GET** /api/property/{propertyIdentifier} | Show Property
[**show_hotel_status**](PropertyApi.md#show_hotel_status) | **GET** /api/property/{propertyIdentifier}/status | Show Property Status
[**suggest_property_profile**](PropertyApi.md#suggest_property_profile) | **POST** /api/property/{propertyIdentifier}/profile/suggest | Suggest property profile
[**suggest_property_welcome_text**](PropertyApi.md#suggest_property_welcome_text) | **POST** /api/property/{propertyIdentifier}/welcome-text/suggest | Suggest Property Welcome Text
[**suggest_property_welcome_text1**](PropertyApi.md#suggest_property_welcome_text1) | **POST** /api/property/{propertyIdentifier}/services/suggest | Suggest property amenities
[**update_general_manager**](PropertyApi.md#update_general_manager) | **PATCH** /api/property/{propertyIdentifier}/general-manager | Update General Manager
[**update_hotel_status**](PropertyApi.md#update_hotel_status) | **PATCH** /api/property/{propertyIdentifier}/status | Update Property Status
[**update_property_profile**](PropertyApi.md#update_property_profile) | **PATCH** /api/property/{propertyIdentifier}/profile | Update Property Profile
[**update_reservations_desk**](PropertyApi.md#update_reservations_desk) | **PATCH** /api/property/{propertyIdentifier}/contact-info | Update Reservations Desk
[**update_services**](PropertyApi.md#update_services) | **PATCH** /api/property/{propertyIdentifier}/services | Update Property Services
[**update_welcome_text**](PropertyApi.md#update_welcome_text) | **PATCH** /api/property/{propertyIdentifier}/welcome-text | Update Property Text
[**upload_general_manager_profile_picture**](PropertyApi.md#upload_general_manager_profile_picture) | **POST** /api/property/{propertyIdentifier}/multimedia/general-manager/upload | Upload General Manager Image


# **improve_welcome_text**
> SimpleDescriptionSupplier improve_welcome_text(property_identifier, improve_welcome_text_request_supplier, wink_version=wink_version)

Improve Welcome Text

Let AI improve existing property descriptions.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.improve_welcome_text_request_supplier import ImproveWelcomeTextRequestSupplier
from wink_sdk_extranet_property.models.simple_description_supplier import SimpleDescriptionSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Update basic information for this property identifier
    improve_welcome_text_request_supplier = wink_sdk_extranet_property.ImproveWelcomeTextRequestSupplier() # ImproveWelcomeTextRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Improve Welcome Text
        api_response = api_instance.improve_welcome_text(property_identifier, improve_welcome_text_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->improve_welcome_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->improve_welcome_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update basic information for this property identifier | 
 **improve_welcome_text_request_supplier** | [**ImproveWelcomeTextRequestSupplier**](ImproveWelcomeTextRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SimpleDescriptionSupplier**](SimpleDescriptionSupplier.md)

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

# **is_hotel_name_unique**
> UniqueResultSupplier is_hotel_name_unique(key, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)

Check Property Name Uniqueness

Check if hotel name is a unique.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.unique_result_supplier import UniqueResultSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    key = 'Blue Orchid' # str | Search for uniqueness for this hotel name.
    hotel_identifier = 'hotelIdentifier' # str | Optional, existing hotel identifier (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Check Property Name Uniqueness
        api_response = api_instance.is_hotel_name_unique(key, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyApi->is_hotel_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->is_hotel_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Search for uniqueness for this hotel name. | 
 **hotel_identifier** | **str**| Optional, existing hotel identifier | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**UniqueResultSupplier**](UniqueResultSupplier.md)

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

# **is_hotel_url_name_unique**
> UniqueResultSupplier is_hotel_url_name_unique(url_name, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)

Check Property Url Slug Uniqueness

Check if hotel name is a unique.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.unique_result_supplier import UniqueResultSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    url_name = 'blue-orchid' # str | Search for uniqueness for this hotel url name.
    hotel_identifier = 'hotelIdentifier' # str | Optional, existing hotel identifier (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Check Property Url Slug Uniqueness
        api_response = api_instance.is_hotel_url_name_unique(url_name, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyApi->is_hotel_url_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->is_hotel_url_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| Search for uniqueness for this hotel url name. | 
 **hotel_identifier** | **str**| Optional, existing hotel identifier | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**UniqueResultSupplier**](UniqueResultSupplier.md)

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

# **show_hotel_by_manager**
> PropertySupplier show_hotel_by_manager(property_identifier, wink_version=wink_version, accept=accept)

Show Property

Retrieve property by record ID

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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Retrieve property record for this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Property
        api_response = api_instance.show_hotel_by_manager(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyApi->show_hotel_by_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->show_hotel_by_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve property record for this property identifier | 
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

# **show_hotel_status**
> UpdateExternalHotelStatusRequestSupplier show_hotel_status(property_identifier, wink_version=wink_version, accept=accept)

Show Property Status

Retrieve hotel status

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.update_external_hotel_status_request_supplier import UpdateExternalHotelStatusRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Show property status for this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Property Status
        api_response = api_instance.show_hotel_status(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyApi->show_hotel_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->show_hotel_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show property status for this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**UpdateExternalHotelStatusRequestSupplier**](UpdateExternalHotelStatusRequestSupplier.md)

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

# **suggest_property_profile**
> SuggestProfileResponseSupplier suggest_property_profile(property_identifier, suggest_profile_request_supplier, wink_version=wink_version)

Suggest property profile

Let AI suggest property profile.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.suggest_profile_request_supplier import SuggestProfileRequestSupplier
from wink_sdk_extranet_property.models.suggest_profile_response_supplier import SuggestProfileResponseSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Suggest for this property identifier
    suggest_profile_request_supplier = wink_sdk_extranet_property.SuggestProfileRequestSupplier() # SuggestProfileRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Suggest property profile
        api_response = api_instance.suggest_property_profile(property_identifier, suggest_profile_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->suggest_property_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->suggest_property_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Suggest for this property identifier | 
 **suggest_profile_request_supplier** | [**SuggestProfileRequestSupplier**](SuggestProfileRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SuggestProfileResponseSupplier**](SuggestProfileResponseSupplier.md)

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

# **suggest_property_welcome_text**
> SimpleDescriptionSupplier suggest_property_welcome_text(property_identifier, suggest_welcome_text_request_supplier, wink_version=wink_version)

Suggest Property Welcome Text

Let AI suggest property descriptions.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.simple_description_supplier import SimpleDescriptionSupplier
from wink_sdk_extranet_property.models.suggest_welcome_text_request_supplier import SuggestWelcomeTextRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Suggest for this property identifier
    suggest_welcome_text_request_supplier = wink_sdk_extranet_property.SuggestWelcomeTextRequestSupplier() # SuggestWelcomeTextRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Suggest Property Welcome Text
        api_response = api_instance.suggest_property_welcome_text(property_identifier, suggest_welcome_text_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->suggest_property_welcome_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->suggest_property_welcome_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Suggest for this property identifier | 
 **suggest_welcome_text_request_supplier** | [**SuggestWelcomeTextRequestSupplier**](SuggestWelcomeTextRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SimpleDescriptionSupplier**](SimpleDescriptionSupplier.md)

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

# **suggest_property_welcome_text1**
> List[KeyValuePairSupplier] suggest_property_welcome_text1(property_identifier, suggest_amenities_request_supplier, wink_version=wink_version)

Suggest property amenities

Let AI suggest property amenities.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_property.models.suggest_amenities_request_supplier import SuggestAmenitiesRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Suggest for this property identifier
    suggest_amenities_request_supplier = wink_sdk_extranet_property.SuggestAmenitiesRequestSupplier() # SuggestAmenitiesRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Suggest property amenities
        api_response = api_instance.suggest_property_welcome_text1(property_identifier, suggest_amenities_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->suggest_property_welcome_text1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->suggest_property_welcome_text1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Suggest for this property identifier | 
 **suggest_amenities_request_supplier** | [**SuggestAmenitiesRequestSupplier**](SuggestAmenitiesRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[KeyValuePairSupplier]**](KeyValuePairSupplier.md)

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

# **update_general_manager**
> PropertySupplier update_general_manager(property_identifier, general_manager_supplier, wink_version=wink_version)

Update General Manager

Update general manager information

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.general_manager_supplier import GeneralManagerSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Update basic information for this property identifier
    general_manager_supplier = wink_sdk_extranet_property.GeneralManagerSupplier() # GeneralManagerSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update General Manager
        api_response = api_instance.update_general_manager(property_identifier, general_manager_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_general_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_general_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update basic information for this property identifier | 
 **general_manager_supplier** | [**GeneralManagerSupplier**](GeneralManagerSupplier.md)|  | 
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

# **update_hotel_status**
> PropertySupplier update_hotel_status(property_identifier, update_external_hotel_status_request_supplier, wink_version=wink_version)

Update Property Status

Update hotel status

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.update_external_hotel_status_request_supplier import UpdateExternalHotelStatusRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Change status for this property identifier
    update_external_hotel_status_request_supplier = wink_sdk_extranet_property.UpdateExternalHotelStatusRequestSupplier() # UpdateExternalHotelStatusRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Property Status
        api_response = api_instance.update_hotel_status(property_identifier, update_external_hotel_status_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_hotel_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_hotel_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Change status for this property identifier | 
 **update_external_hotel_status_request_supplier** | [**UpdateExternalHotelStatusRequestSupplier**](UpdateExternalHotelStatusRequestSupplier.md)|  | 
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

# **update_property_profile**
> PropertySupplier update_property_profile(property_identifier, upsert_property_profile_request_supplier, wink_version=wink_version)

Update Property Profile

Update basic property information

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.upsert_property_profile_request_supplier import UpsertPropertyProfileRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Update basic information for this property identifier
    upsert_property_profile_request_supplier = wink_sdk_extranet_property.UpsertPropertyProfileRequestSupplier() # UpsertPropertyProfileRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Property Profile
        api_response = api_instance.update_property_profile(property_identifier, upsert_property_profile_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_property_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_property_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update basic information for this property identifier | 
 **upsert_property_profile_request_supplier** | [**UpsertPropertyProfileRequestSupplier**](UpsertPropertyProfileRequestSupplier.md)|  | 
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

# **update_reservations_desk**
> PropertySupplier update_reservations_desk(property_identifier, upsert_contact_info_request_supplier, wink_version=wink_version)

Update Reservations Desk

Manage reservation desk hours of operation and contact details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.upsert_contact_info_request_supplier import UpsertContactInfoRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Update important request for this property identifier
    upsert_contact_info_request_supplier = wink_sdk_extranet_property.UpsertContactInfoRequestSupplier() # UpsertContactInfoRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Reservations Desk
        api_response = api_instance.update_reservations_desk(property_identifier, upsert_contact_info_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_reservations_desk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_reservations_desk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update important request for this property identifier | 
 **upsert_contact_info_request_supplier** | [**UpsertContactInfoRequestSupplier**](UpsertContactInfoRequestSupplier.md)|  | 
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

# **update_services**
> PropertySupplier update_services(property_identifier, update_property_amenities_and_services_request_supplier, wink_version=wink_version)

Update Property Services

Manage property amenity, accessibility and security features.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.update_property_amenities_and_services_request_supplier import UpdatePropertyAmenitiesAndServicesRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Set amenities for this property identifier
    update_property_amenities_and_services_request_supplier = wink_sdk_extranet_property.UpdatePropertyAmenitiesAndServicesRequestSupplier() # UpdatePropertyAmenitiesAndServicesRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Property Services
        api_response = api_instance.update_services(property_identifier, update_property_amenities_and_services_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Set amenities for this property identifier | 
 **update_property_amenities_and_services_request_supplier** | [**UpdatePropertyAmenitiesAndServicesRequestSupplier**](UpdatePropertyAmenitiesAndServicesRequestSupplier.md)|  | 
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

# **update_welcome_text**
> PropertySupplier update_welcome_text(property_identifier, upsert_welcome_text_request_supplier, wink_version=wink_version)

Update Property Text

Update localized welcome text

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.upsert_welcome_text_request_supplier import UpsertWelcomeTextRequestSupplier
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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Update basic information for this property identifier
    upsert_welcome_text_request_supplier = wink_sdk_extranet_property.UpsertWelcomeTextRequestSupplier() # UpsertWelcomeTextRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Property Text
        api_response = api_instance.update_welcome_text(property_identifier, upsert_welcome_text_request_supplier, wink_version=wink_version)
        print("The response of PropertyApi->update_welcome_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_welcome_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update basic information for this property identifier | 
 **upsert_welcome_text_request_supplier** | [**UpsertWelcomeTextRequestSupplier**](UpsertWelcomeTextRequestSupplier.md)|  | 
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

# **upload_general_manager_profile_picture**
> PropertySupplier upload_general_manager_profile_picture(property_identifier, file)

Upload General Manager Image

Uploads videos and/or images to the general manager profile associated with hotel identifier

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
    api_instance = wink_sdk_extranet_property.PropertyApi(api_client)
    property_identifier = 'hotel-1' # str | Add general manager profile picture for this property identifier
    file = None # bytearray | 

    try:
        # Upload General Manager Image
        api_response = api_instance.upload_general_manager_profile_picture(property_identifier, file)
        print("The response of PropertyApi->upload_general_manager_profile_picture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->upload_general_manager_profile_picture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Add general manager profile picture for this property identifier | 
 **file** | **bytearray**|  | 

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

