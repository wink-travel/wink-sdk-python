# wink_sdk_inventory.InventoryApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify_property**](InventoryApi.md#notify_property) | **POST** /api/inventory/unavailable | Lacks Inventory
[**show_consumer_map**](InventoryApi.md#show_consumer_map) | **GET** /api/sell/map/{inventoryMapIdentifier}/markers | Map + Markers
[**show_inventory_grid_item**](InventoryApi.md#show_inventory_grid_item) | **POST** /api/inventory/grid/item | Show Inventory Grid Item
[**show_property_add_on**](InventoryApi.md#show_property_add_on) | **POST** /api/add-on | Show Add-On Inventory
[**show_property_aggregate**](InventoryApi.md#show_property_aggregate) | **POST** /api/inventory/property | Show Property Inventory
[**show_property_attraction**](InventoryApi.md#show_property_attraction) | **POST** /api/experience/attraction | Show Attraction Inventory
[**show_property_inventory**](InventoryApi.md#show_property_inventory) | **POST** /api/inventory | Show Property
[**show_property_list**](InventoryApi.md#show_property_list) | **POST** /api/inventory/list | Show Property List
[**show_property_meeting_room**](InventoryApi.md#show_property_meeting_room) | **POST** /api/facility/meeting-room | Show Meeting Room Inventory
[**show_property_place**](InventoryApi.md#show_property_place) | **POST** /api/experience/place | Show Place Inventory
[**show_property_recreation**](InventoryApi.md#show_property_recreation) | **POST** /api/experience/activity | Show Activity Inventory
[**show_property_restaurant**](InventoryApi.md#show_property_restaurant) | **POST** /api/facility/restaurant | Show Restaurant Inventory
[**show_property_room_type**](InventoryApi.md#show_property_room_type) | **POST** /api/facility/room-type | Show Guest Room Inventory
[**show_property_spa**](InventoryApi.md#show_property_spa) | **POST** /api/facility/spa | Show Spa Inventory
[**show_seller_inventory_list**](InventoryApi.md#show_seller_inventory_list) | **POST** /api/inventory/grid | Search Inventory
[**show_seller_inventory_ranked_list**](InventoryApi.md#show_seller_inventory_ranked_list) | **POST** /api/inventory/ranked/grid | Show Ranked Inventories


# **notify_property**
> InventoryUnavailableNotificationNonAuthenticatedEntity notify_property(inventory_unavailable_notification_non_authenticated_entity, wink_version=wink_version)

Lacks Inventory

Notify property that there is a demand but no supply for a specified blocking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.inventory_unavailable_notification_non_authenticated_entity import InventoryUnavailableNotificationNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    inventory_unavailable_notification_non_authenticated_entity = wink_sdk_inventory.InventoryUnavailableNotificationNonAuthenticatedEntity() # InventoryUnavailableNotificationNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Lacks Inventory
        api_response = api_instance.notify_property(inventory_unavailable_notification_non_authenticated_entity, wink_version=wink_version)
        print("The response of InventoryApi->notify_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->notify_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_unavailable_notification_non_authenticated_entity** | [**InventoryUnavailableNotificationNonAuthenticatedEntity**](InventoryUnavailableNotificationNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InventoryUnavailableNotificationNonAuthenticatedEntity**](InventoryUnavailableNotificationNonAuthenticatedEntity.md)

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

# **show_consumer_map**
> ConsumerDataMapNonAuthenticatedEntity show_consumer_map(inventory_map_identifier, wink_version=wink_version, accept=accept)

Map + Markers

Load map and map markers for a configurable map.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.consumer_data_map_non_authenticated_entity import ConsumerDataMapNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    inventory_map_identifier = 'inventory_map_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Map + Markers
        api_response = api_instance.show_consumer_map(inventory_map_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_consumer_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_consumer_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_map_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ConsumerDataMapNonAuthenticatedEntity**](ConsumerDataMapNonAuthenticatedEntity.md)

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

# **show_inventory_grid_item**
> InventoryGridItemNonAuthenticatedEntity show_inventory_grid_item(aggregate_inventory_grid_item_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Inventory Grid Item

Shows single grid based on channel inventory identifier 

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_inventory_grid_item_request_non_authenticated_entity import AggregateInventoryGridItemRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.inventory_grid_item_non_authenticated_entity import InventoryGridItemNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_inventory_grid_item_request_non_authenticated_entity = wink_sdk_inventory.AggregateInventoryGridItemRequestNonAuthenticatedEntity() # AggregateInventoryGridItemRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Grid Item
        api_response = api_instance.show_inventory_grid_item(aggregate_inventory_grid_item_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_inventory_grid_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_inventory_grid_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_inventory_grid_item_request_non_authenticated_entity** | [**AggregateInventoryGridItemRequestNonAuthenticatedEntity**](AggregateInventoryGridItemRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryGridItemNonAuthenticatedEntity**](InventoryGridItemNonAuthenticatedEntity.md)

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

# **show_property_add_on**
> SellerInventoryAddOnNonAuthenticatedEntity show_property_add_on(aggregate_add_on_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Add-On Inventory

Show single add-on based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_add_on_request_non_authenticated_entity import AggregateAddOnRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_add_on_non_authenticated_entity import SellerInventoryAddOnNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_add_on_request_non_authenticated_entity = wink_sdk_inventory.AggregateAddOnRequestNonAuthenticatedEntity() # AggregateAddOnRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Add-On Inventory
        api_response = api_instance.show_property_add_on(aggregate_add_on_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_add_on_request_non_authenticated_entity** | [**AggregateAddOnRequestNonAuthenticatedEntity**](AggregateAddOnRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryAddOnNonAuthenticatedEntity**](SellerInventoryAddOnNonAuthenticatedEntity.md)

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

# **show_property_aggregate**
> SellerInventoryPropertyNonAuthenticatedEntity show_property_aggregate(aggregate_property_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Property Inventory

Show single hotel card with price based on a given record identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_property_request_non_authenticated_entity import AggregatePropertyRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_property_non_authenticated_entity import SellerInventoryPropertyNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_property_request_non_authenticated_entity = wink_sdk_inventory.AggregatePropertyRequestNonAuthenticatedEntity() # AggregatePropertyRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Property Inventory
        api_response = api_instance.show_property_aggregate(aggregate_property_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_property_request_non_authenticated_entity** | [**AggregatePropertyRequestNonAuthenticatedEntity**](AggregatePropertyRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryPropertyNonAuthenticatedEntity**](SellerInventoryPropertyNonAuthenticatedEntity.md)

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

# **show_property_attraction**
> SellerInventoryAttractionNonAuthenticatedEntity show_property_attraction(aggregate_attraction_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Attraction Inventory

Show single attraction based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_attraction_request_non_authenticated_entity import AggregateAttractionRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_attraction_non_authenticated_entity import SellerInventoryAttractionNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_attraction_request_non_authenticated_entity = wink_sdk_inventory.AggregateAttractionRequestNonAuthenticatedEntity() # AggregateAttractionRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attraction Inventory
        api_response = api_instance.show_property_attraction(aggregate_attraction_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_attraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_attraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_attraction_request_non_authenticated_entity** | [**AggregateAttractionRequestNonAuthenticatedEntity**](AggregateAttractionRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryAttractionNonAuthenticatedEntity**](SellerInventoryAttractionNonAuthenticatedEntity.md)

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

# **show_property_inventory**
> HotelInventoryResponseNonAuthenticatedEntity show_property_inventory(hotel_inventory_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, images=images, videos=videos, wink_version=wink_version)

Show Property

Show property content / availability / rate details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.hotel_inventory_request_non_authenticated_entity import HotelInventoryRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_response_non_authenticated_entity import HotelInventoryResponseNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    hotel_inventory_request_non_authenticated_entity = wink_sdk_inventory.HotelInventoryRequestNonAuthenticatedEntity() # HotelInventoryRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    images = 20 # int | Number of images to return for inventory (optional) (default to 20)
    videos = 1 # int | Number of videos to return for inventory (optional) (default to 1)
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Property
        api_response = api_instance.show_property_inventory(hotel_inventory_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, images=images, videos=videos, wink_version=wink_version)
        print("The response of InventoryApi->show_property_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_inventory_request_non_authenticated_entity** | [**HotelInventoryRequestNonAuthenticatedEntity**](HotelInventoryRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **images** | **int**| Number of images to return for inventory | [optional] [default to 20]
 **videos** | **int**| Number of videos to return for inventory | [optional] [default to 1]
 **wink_version** | **str**|  | [optional] 

### Return type

[**HotelInventoryResponseNonAuthenticatedEntity**](HotelInventoryResponseNonAuthenticatedEntity.md)

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

# **show_property_list**
> HotelInventoryListResponseNonAuthenticatedEntity show_property_list(hotel_inventory_list_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, images=images, videos=videos, wink_version=wink_version)

Show Property List

Show property content / availability / rate details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.hotel_inventory_list_request_non_authenticated_entity import HotelInventoryListRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_list_response_non_authenticated_entity import HotelInventoryListResponseNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    hotel_inventory_list_request_non_authenticated_entity = wink_sdk_inventory.HotelInventoryListRequestNonAuthenticatedEntity() # HotelInventoryListRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    images = 20 # int | Number of images to return for inventory (optional) (default to 20)
    videos = 1 # int | Number of videos to return for inventory (optional) (default to 1)
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Property List
        api_response = api_instance.show_property_list(hotel_inventory_list_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, images=images, videos=videos, wink_version=wink_version)
        print("The response of InventoryApi->show_property_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_inventory_list_request_non_authenticated_entity** | [**HotelInventoryListRequestNonAuthenticatedEntity**](HotelInventoryListRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **images** | **int**| Number of images to return for inventory | [optional] [default to 20]
 **videos** | **int**| Number of videos to return for inventory | [optional] [default to 1]
 **wink_version** | **str**|  | [optional] 

### Return type

[**HotelInventoryListResponseNonAuthenticatedEntity**](HotelInventoryListResponseNonAuthenticatedEntity.md)

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

# **show_property_meeting_room**
> SellerInventoryMeetingRoomNonAuthenticatedEntity show_property_meeting_room(aggregate_meeting_room_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Meeting Room Inventory

Show single meeting room based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_meeting_room_request_non_authenticated_entity import AggregateMeetingRoomRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_meeting_room_non_authenticated_entity import SellerInventoryMeetingRoomNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_meeting_room_request_non_authenticated_entity = wink_sdk_inventory.AggregateMeetingRoomRequestNonAuthenticatedEntity() # AggregateMeetingRoomRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Meeting Room Inventory
        api_response = api_instance.show_property_meeting_room(aggregate_meeting_room_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_meeting_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_meeting_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_meeting_room_request_non_authenticated_entity** | [**AggregateMeetingRoomRequestNonAuthenticatedEntity**](AggregateMeetingRoomRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryMeetingRoomNonAuthenticatedEntity**](SellerInventoryMeetingRoomNonAuthenticatedEntity.md)

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

# **show_property_place**
> SellerInventoryPlaceNonAuthenticatedEntity show_property_place(aggregate_place_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Place Inventory

Show single place based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_place_request_non_authenticated_entity import AggregatePlaceRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_place_non_authenticated_entity import SellerInventoryPlaceNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_place_request_non_authenticated_entity = wink_sdk_inventory.AggregatePlaceRequestNonAuthenticatedEntity() # AggregatePlaceRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Place Inventory
        api_response = api_instance.show_property_place(aggregate_place_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_place:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_place: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_place_request_non_authenticated_entity** | [**AggregatePlaceRequestNonAuthenticatedEntity**](AggregatePlaceRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryPlaceNonAuthenticatedEntity**](SellerInventoryPlaceNonAuthenticatedEntity.md)

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

# **show_property_recreation**
> SellerInventoryActivityNonAuthenticatedEntity show_property_recreation(aggregate_activity_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Activity Inventory

Show single activity based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_activity_request_non_authenticated_entity import AggregateActivityRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_activity_non_authenticated_entity import SellerInventoryActivityNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_activity_request_non_authenticated_entity = wink_sdk_inventory.AggregateActivityRequestNonAuthenticatedEntity() # AggregateActivityRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activity Inventory
        api_response = api_instance.show_property_recreation(aggregate_activity_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_recreation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_recreation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_activity_request_non_authenticated_entity** | [**AggregateActivityRequestNonAuthenticatedEntity**](AggregateActivityRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryActivityNonAuthenticatedEntity**](SellerInventoryActivityNonAuthenticatedEntity.md)

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

# **show_property_restaurant**
> SellerInventoryRestaurantNonAuthenticatedEntity show_property_restaurant(aggregate_restaurant_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Restaurant Inventory

Show single restaurant based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_restaurant_request_non_authenticated_entity import AggregateRestaurantRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_restaurant_non_authenticated_entity import SellerInventoryRestaurantNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_restaurant_request_non_authenticated_entity = wink_sdk_inventory.AggregateRestaurantRequestNonAuthenticatedEntity() # AggregateRestaurantRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Restaurant Inventory
        api_response = api_instance.show_property_restaurant(aggregate_restaurant_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_restaurant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_restaurant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_restaurant_request_non_authenticated_entity** | [**AggregateRestaurantRequestNonAuthenticatedEntity**](AggregateRestaurantRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryRestaurantNonAuthenticatedEntity**](SellerInventoryRestaurantNonAuthenticatedEntity.md)

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

# **show_property_room_type**
> SellerInventoryGuestRoomNonAuthenticatedEntity show_property_room_type(aggregate_room_type_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Guest Room Inventory

Show single guest room based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_room_type_request_non_authenticated_entity import AggregateRoomTypeRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_guest_room_non_authenticated_entity import SellerInventoryGuestRoomNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_room_type_request_non_authenticated_entity = wink_sdk_inventory.AggregateRoomTypeRequestNonAuthenticatedEntity() # AggregateRoomTypeRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Guest Room Inventory
        api_response = api_instance.show_property_room_type(aggregate_room_type_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_room_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_room_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_room_type_request_non_authenticated_entity** | [**AggregateRoomTypeRequestNonAuthenticatedEntity**](AggregateRoomTypeRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventoryGuestRoomNonAuthenticatedEntity**](SellerInventoryGuestRoomNonAuthenticatedEntity.md)

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

# **show_property_spa**
> SellerInventorySpaNonAuthenticatedEntity show_property_spa(aggregate_spa_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Spa Inventory

Show single spa based on a channel inventory identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_spa_request_non_authenticated_entity import AggregateSpaRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_spa_non_authenticated_entity import SellerInventorySpaNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_spa_request_non_authenticated_entity = wink_sdk_inventory.AggregateSpaRequestNonAuthenticatedEntity() # AggregateSpaRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Spa Inventory
        api_response = api_instance.show_property_spa(aggregate_spa_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_property_spa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_property_spa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_spa_request_non_authenticated_entity** | [**AggregateSpaRequestNonAuthenticatedEntity**](AggregateSpaRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellerInventorySpaNonAuthenticatedEntity**](SellerInventorySpaNonAuthenticatedEntity.md)

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

# **show_seller_inventory_list**
> SellableListResponseNonAuthenticatedEntity show_seller_inventory_list(aggregate_seller_inventory_list_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Search Inventory

Shows page of blocking items

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_seller_inventory_list_request_non_authenticated_entity import AggregateSellerInventoryListRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.sellable_list_response_non_authenticated_entity import SellableListResponseNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_seller_inventory_list_request_non_authenticated_entity = wink_sdk_inventory.AggregateSellerInventoryListRequestNonAuthenticatedEntity() # AggregateSellerInventoryListRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Search Inventory
        api_response = api_instance.show_seller_inventory_list(aggregate_seller_inventory_list_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_seller_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_seller_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_seller_inventory_list_request_non_authenticated_entity** | [**AggregateSellerInventoryListRequestNonAuthenticatedEntity**](AggregateSellerInventoryListRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableListResponseNonAuthenticatedEntity**](SellableListResponseNonAuthenticatedEntity.md)

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

# **show_seller_inventory_ranked_list**
> SellableRankedListResponseNonAuthenticatedEntity show_seller_inventory_ranked_list(aggregate_seller_inventory_list_request_non_authenticated_entity, wink_version=wink_version, accept=accept)

Show Ranked Inventories

Shows a paginated list of ranked blocking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.aggregate_seller_inventory_list_request_non_authenticated_entity import AggregateSellerInventoryListRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.sellable_ranked_list_response_non_authenticated_entity import SellableRankedListResponseNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.InventoryApi(api_client)
    aggregate_seller_inventory_list_request_non_authenticated_entity = wink_sdk_inventory.AggregateSellerInventoryListRequestNonAuthenticatedEntity() # AggregateSellerInventoryListRequestNonAuthenticatedEntity | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Ranked Inventories
        api_response = api_instance.show_seller_inventory_ranked_list(aggregate_seller_inventory_list_request_non_authenticated_entity, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_seller_inventory_ranked_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_seller_inventory_ranked_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_seller_inventory_list_request_non_authenticated_entity** | [**AggregateSellerInventoryListRequestNonAuthenticatedEntity**](AggregateSellerInventoryListRequestNonAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SellableRankedListResponseNonAuthenticatedEntity**](SellableRankedListResponseNonAuthenticatedEntity.md)

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

