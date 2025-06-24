# wink_sdk_extranet_distribution.InventoryUsageApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_activity_usage**](InventoryUsageApi.md#show_activity_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/activity/{activityIdentifier} | Show Activity Usage
[**show_add_on_usage**](InventoryUsageApi.md#show_add_on_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/add-on/{addOnIdentifier} | Show Add-On Usage
[**show_attraction_usage**](InventoryUsageApi.md#show_attraction_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/attraction/{attractionIdentifier} | Show Attraction Usage
[**show_meeting_room_usage**](InventoryUsageApi.md#show_meeting_room_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/meeting-room/{meetingRoomIdentifier} | Show Meeting Room Usage
[**show_place_usage**](InventoryUsageApi.md#show_place_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/place/{placeIdentifier} | Show Place Usage
[**show_rate_plan_usage**](InventoryUsageApi.md#show_rate_plan_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/rate-plan/{ratePlanIdentifier} | Show Rate Plan Usage
[**show_restaurant_usage**](InventoryUsageApi.md#show_restaurant_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/restaurant/{restaurantIdentifier} | Show Restaurant Usage
[**show_room_type_usage**](InventoryUsageApi.md#show_room_type_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/room-type/{roomTypeIdentifier} | Show Room Type Usage
[**show_spa_usage**](InventoryUsageApi.md#show_spa_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/spa/{spaIdentifier} | Show Spa Usage


# **show_activity_usage**
> InventoryUsageSupplier show_activity_usage(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)

Show Activity Usage

Retrieve an aggregate report where specified activity is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier blocking owner
    activity_identifier = 'activity-1' # str | Activity identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activity Usage
        api_response = api_instance.show_activity_usage(property_identifier, activity_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_activity_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_activity_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier blocking owner | 
 **activity_identifier** | **str**| Activity identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_add_on_usage**
> InventoryUsageSupplier show_add_on_usage(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)

Show Add-On Usage

Retrieve an aggregate report where specified add-on is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    add_on_identifier = 'add-on-1' # str | Add-On identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Add-On Usage
        api_response = api_instance.show_add_on_usage(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_add_on_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_add_on_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **add_on_identifier** | **str**| Add-On identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_attraction_usage**
> InventoryUsageSupplier show_attraction_usage(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)

Show Attraction Usage

Retrieve an aggregate report where specified attraction is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier blocking owner
    attraction_identifier = 'attraction-1' # str | Attraction identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attraction Usage
        api_response = api_instance.show_attraction_usage(property_identifier, attraction_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_attraction_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_attraction_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier blocking owner | 
 **attraction_identifier** | **str**| Attraction identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_meeting_room_usage**
> InventoryUsageSupplier show_meeting_room_usage(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)

Show Meeting Room Usage

Retrieve an aggregate report where specified meeting room is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    meeting_room_identifier = 'meeting-room-1' # str | Meeting room identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Meeting Room Usage
        api_response = api_instance.show_meeting_room_usage(property_identifier, meeting_room_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_meeting_room_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_meeting_room_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **meeting_room_identifier** | **str**| Meeting room identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_place_usage**
> InventoryUsageSupplier show_place_usage(property_identifier, place_identifier, wink_version=wink_version, accept=accept)

Show Place Usage

Retrieve an aggregate report where specified rate plan is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier blocking owner
    place_identifier = 'place-1' # str | Place identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Place Usage
        api_response = api_instance.show_place_usage(property_identifier, place_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_place_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_place_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier blocking owner | 
 **place_identifier** | **str**| Place identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_rate_plan_usage**
> InventoryUsageSupplier show_rate_plan_usage(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)

Show Rate Plan Usage

Retrieve an aggregate report where specified rate plan is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    rate_plan_identifier = 'rate-plan-1' # str | Rate plan identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Rate Plan Usage
        api_response = api_instance.show_rate_plan_usage(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_rate_plan_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_rate_plan_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **rate_plan_identifier** | **str**| Rate plan identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_restaurant_usage**
> InventoryUsageSupplier show_restaurant_usage(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)

Show Restaurant Usage

Retrieve an aggregate report where specified rate plan is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    restaurant_identifier = 'restaurant-1' # str | Restaurant identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Restaurant Usage
        api_response = api_instance.show_restaurant_usage(property_identifier, restaurant_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_restaurant_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_restaurant_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **restaurant_identifier** | **str**| Restaurant identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_room_type_usage**
> InventoryUsageSupplier show_room_type_usage(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)

Show Room Type Usage

Retrieve an aggregate report where specified room type is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    room_type_identifier = 'room-type-1' # str | Room type identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Room Type Usage
        api_response = api_instance.show_room_type_usage(property_identifier, room_type_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_room_type_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_room_type_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **room_type_identifier** | **str**| Room type identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

# **show_spa_usage**
> InventoryUsageSupplier show_spa_usage(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)

Show Spa Usage

Retrieve an aggregate report where specified spa is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.InventoryUsageApi(api_client)
    property_identifier = 'hotel-1' # str | Hotel identifier inventoryowner
    spa_identifier = 'spa-1' # str | Spa identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Spa Usage
        api_response = api_instance.show_spa_usage(property_identifier, spa_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryUsageApi->show_spa_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryUsageApi->show_spa_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Hotel identifier inventoryowner | 
 **spa_identifier** | **str**| Spa identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryUsageSupplier**](InventoryUsageSupplier.md)

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

