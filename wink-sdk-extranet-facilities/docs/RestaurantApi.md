# wink_sdk_extranet_facilities.RestaurantApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_restaurant**](RestaurantApi.md#create_restaurant) | **POST** /api/property/{propertyIdentifier}/facility/restaurant | Create Restaurant
[**remove_multimedia1**](RestaurantApi.md#remove_multimedia1) | **DELETE** /api/property/{propertyIdentifier}/facility/restaurant/{restaurantIdentifier}/multimedia/{multimediaIdentifier} | Delete Multimedia
[**remove_restaurant**](RestaurantApi.md#remove_restaurant) | **DELETE** /api/property/{propertyIdentifier}/facility/restaurant/{restaurantIdentifier} | Delete Restaurant
[**show_restaurant**](RestaurantApi.md#show_restaurant) | **GET** /api/property/{propertyIdentifier}/facility/restaurant/{restaurantIdentifier} | Show Restaurant
[**show_restaurant_pairs**](RestaurantApi.md#show_restaurant_pairs) | **GET** /api/property/{propertyIdentifier}/facility/restaurant/list/pair | Show Reference Pairs
[**show_restaurants**](RestaurantApi.md#show_restaurants) | **GET** /api/property/{propertyIdentifier}/facility/restaurant/list | Show Restaurants
[**update_restaurant**](RestaurantApi.md#update_restaurant) | **PUT** /api/property/{propertyIdentifier}/facility/restaurant/{restaurantIdentifier} | Update Restaurant
[**upload_restaurant_media**](RestaurantApi.md#upload_restaurant_media) | **POST** /api/property/{propertyIdentifier}/facility/restaurant/{restaurantIdentifier}/multimedia | Upload Binary Multimedia


# **create_restaurant**
> RestaurantSupplier create_restaurant(property_identifier, upsert_restaurant_request_supplier, wink_version=wink_version)

Create Restaurant

Create a new restaurant

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
from wink_sdk_extranet_facilities.models.upsert_restaurant_request_supplier import UpsertRestaurantRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Create a new restaurant record owned by this property identifier
    upsert_restaurant_request_supplier = wink_sdk_extranet_facilities.UpsertRestaurantRequestSupplier() # UpsertRestaurantRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Restaurant
        api_response = api_instance.create_restaurant(property_identifier, upsert_restaurant_request_supplier, wink_version=wink_version)
        print("The response of RestaurantApi->create_restaurant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->create_restaurant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a new restaurant record owned by this property identifier | 
 **upsert_restaurant_request_supplier** | [**UpsertRestaurantRequestSupplier**](UpsertRestaurantRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

# **remove_multimedia1**
> RestaurantSupplier remove_multimedia1(property_identifier, restaurant_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)

Delete Multimedia

Remove media from an existing restaurant.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a media record from an existing restaurant owned by this property identifier.
    restaurant_identifier = 'restaurant-1' # str | Remove a media record from an existing restaurant identified by this identifier.
    multimedia_identifier = 'media-1' # str | Remove a media record with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Multimedia
        api_response = api_instance.remove_multimedia1(property_identifier, restaurant_identifier, multimedia_identifier, wink_version=wink_version, accept=accept)
        print("The response of RestaurantApi->remove_multimedia1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->remove_multimedia1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a media record from an existing restaurant owned by this property identifier. | 
 **restaurant_identifier** | **str**| Remove a media record from an existing restaurant identified by this identifier. | 
 **multimedia_identifier** | **str**| Remove a media record with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

# **remove_restaurant**
> RestaurantSupplier remove_restaurant(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)

Delete Restaurant

Remove a restaurant by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Remove restaurant record owned by this property identifier
    restaurant_identifier = 'restaurant-1' # str | Remove restaurant record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Restaurant
        api_response = api_instance.remove_restaurant(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)
        print("The response of RestaurantApi->remove_restaurant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->remove_restaurant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove restaurant record owned by this property identifier | 
 **restaurant_identifier** | **str**| Remove restaurant record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

# **show_restaurant**
> RestaurantSupplier show_restaurant(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)

Show Restaurant

Retrieve a restaurant by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Show single restaurant owned by this property identifier
    restaurant_identifier = 'restaurant-1' # str | Show restaurant record identified by this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Restaurant
        api_response = api_instance.show_restaurant(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)
        print("The response of RestaurantApi->show_restaurant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->show_restaurant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single restaurant owned by this property identifier | 
 **restaurant_identifier** | **str**| Show restaurant record identified by this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

# **show_restaurant_pairs**
> List[KeyValuePairSupplier] show_restaurant_pairs(property_identifier, wink_version=wink_version, accept=accept)

Show Reference Pairs

Retrieve list of restaurants as key/value pairs (identifier, name)

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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Show restaurant pairs owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Reference Pairs
        api_response = api_instance.show_restaurant_pairs(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of RestaurantApi->show_restaurant_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->show_restaurant_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show restaurant pairs owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
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

# **show_restaurants**
> List[RestaurantSupplier] show_restaurants(property_identifier, wink_version=wink_version, accept=accept)

Show Restaurants

Retrieve list of restaurants for property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Show restaurants owned by this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Restaurants
        api_response = api_instance.show_restaurants(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of RestaurantApi->show_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->show_restaurants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show restaurants owned by this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[RestaurantSupplier]**](RestaurantSupplier.md)

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

# **update_restaurant**
> RestaurantSupplier update_restaurant(property_identifier, restaurant_identifier, upsert_restaurant_request_supplier, wink_version=wink_version)

Update Restaurant

Update a restaurant by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
from wink_sdk_extranet_facilities.models.upsert_restaurant_request_supplier import UpsertRestaurantRequestSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing restaurant record owned by this property identifier
    restaurant_identifier = 'restaurant-1' # str | Update an existing restaurant record identified by this identifier
    upsert_restaurant_request_supplier = wink_sdk_extranet_facilities.UpsertRestaurantRequestSupplier() # UpsertRestaurantRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Restaurant
        api_response = api_instance.update_restaurant(property_identifier, restaurant_identifier, upsert_restaurant_request_supplier, wink_version=wink_version)
        print("The response of RestaurantApi->update_restaurant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->update_restaurant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing restaurant record owned by this property identifier | 
 **restaurant_identifier** | **str**| Update an existing restaurant record identified by this identifier | 
 **upsert_restaurant_request_supplier** | [**UpsertRestaurantRequestSupplier**](UpsertRestaurantRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

# **upload_restaurant_media**
> RestaurantSupplier upload_restaurant_media(property_identifier, restaurant_identifier, files)

Upload Binary Multimedia

Upload a list of binary / multipart videos and/or images to an existing restaurant.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_facilities
from wink_sdk_extranet_facilities.models.restaurant_supplier import RestaurantSupplier
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
    api_instance = wink_sdk_extranet_facilities.RestaurantApi(api_client)
    property_identifier = 'hotel-1' # str | Upload multipart files and associate them with an existing restaurant owned by this property identifier
    restaurant_identifier = 'restaurant-1' # str | Upload multipart files and associate them with an existing restaurant with this identifier
    files = None # List[bytearray] | 

    try:
        # Upload Binary Multimedia
        api_response = api_instance.upload_restaurant_media(property_identifier, restaurant_identifier, files)
        print("The response of RestaurantApi->upload_restaurant_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->upload_restaurant_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Upload multipart files and associate them with an existing restaurant owned by this property identifier | 
 **restaurant_identifier** | **str**| Upload multipart files and associate them with an existing restaurant with this identifier | 
 **files** | **List[bytearray]**|  | 

### Return type

[**RestaurantSupplier**](RestaurantSupplier.md)

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

