# wink_sdk_extranet_distribution.InventoryApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_channel_activities**](InventoryApi.md#show_channel_activities) | **GET** /api/property/{propertyIdentifier}/sales/experience/activity/list | Show Activity Inventories
[**show_channel_add_ons**](InventoryApi.md#show_channel_add_ons) | **GET** /api/property/{propertyIdentifier}/sales/add-on/list | Show Add-On Inventories
[**show_channel_attractions**](InventoryApi.md#show_channel_attractions) | **GET** /api/property/{propertyIdentifier}/sales/experience/attraction/list | Show Attraction Inventories
[**show_channel_meeting_rooms**](InventoryApi.md#show_channel_meeting_rooms) | **GET** /api/property/{propertyIdentifier}/sales/meeting-room/list | Show Meeting Room Inventories
[**show_channel_places**](InventoryApi.md#show_channel_places) | **GET** /api/property/{propertyIdentifier}/sales/experience/place/list | Show Place Inventories
[**show_channel_restaurants**](InventoryApi.md#show_channel_restaurants) | **GET** /api/property/{propertyIdentifier}/sales/facility/restaurant/list | Show Restaurant Inventories
[**show_channel_spas**](InventoryApi.md#show_channel_spas) | **GET** /api/property/{propertyIdentifier}/sales/facility/spa/list | Show Spa Inventories
[**show_inventory**](InventoryApi.md#show_inventory) | **GET** /api/property/{propertyIdentifier}/sales/inventory/{inventoryIdentifier} | Show Inventory
[**show_inventory_list**](InventoryApi.md#show_inventory_list) | **GET** /api/property/{propertyIdentifier}/sales/inventory/list | Show Inventory List
[**show_inventory_names**](InventoryApi.md#show_inventory_names) | **GET** /api/property/{propertyIdentifier}/sales/inventory/name/list | Show Inventory Names
[**show_inventory_types**](InventoryApi.md#show_inventory_types) | **GET** /api/property/{propertyIdentifier}/sales/inventory/type/list | Show All Inventory Types
[**show_master_rates**](InventoryApi.md#show_master_rates) | **GET** /api/property/{propertyIdentifier}/sales/master-rate/list | Show Master Rates Inventories
[**show_pageable_channel_inventory**](InventoryApi.md#show_pageable_channel_inventory) | **POST** /api/property/{propertyIdentifier}/sales/inventory/grid | Search Inventory
[**show_sales_channel_list_by_inventory**](InventoryApi.md#show_sales_channel_list_by_inventory) | **GET** /api/property/{propertyIdentifier}/sales/inventory/{inventoryTypeIdentifier}/list | Show Inventory as Channels
[**toggle_inventory_availability**](InventoryApi.md#toggle_inventory_availability) | **PATCH** /api/property/{propertyIdentifier}/sales/inventory/{inventoryIdentifier} | Update Inventory
[**toggle_inventory_list_availability**](InventoryApi.md#toggle_inventory_list_availability) | **PATCH** /api/property/{propertyIdentifier}/sales/inventory/list | Update Inventory List


# **show_channel_activities**
> List[KeyValuePairSupplier] show_channel_activities(property_identifier, wink_version=wink_version, accept=accept)

Show Activity Inventories

Retrieve list of activities for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve activities for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activity Inventories
        api_response = api_instance.show_channel_activities(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve activities for | 
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

# **show_channel_add_ons**
> List[KeyValuePairSupplier] show_channel_add_ons(property_identifier, wink_version=wink_version, accept=accept)

Show Add-On Inventories

Retrieve list of addons for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve add-ons for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Add-On Inventories
        api_response = api_instance.show_channel_add_ons(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_add_ons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_add_ons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve add-ons for | 
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

# **show_channel_attractions**
> List[KeyValuePairSupplier] show_channel_attractions(property_identifier, wink_version=wink_version, accept=accept)

Show Attraction Inventories

Retrieve list of attractions for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve attractions for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Attraction Inventories
        api_response = api_instance.show_channel_attractions(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_attractions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_attractions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve attractions for | 
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

# **show_channel_meeting_rooms**
> List[KeyValuePairSupplier] show_channel_meeting_rooms(property_identifier, wink_version=wink_version, accept=accept)

Show Meeting Room Inventories

Retrieve list of meeting room names for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve meeting rooms for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Meeting Room Inventories
        api_response = api_instance.show_channel_meeting_rooms(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_meeting_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_meeting_rooms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve meeting rooms for | 
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

# **show_channel_places**
> List[KeyValuePairSupplier] show_channel_places(property_identifier, wink_version=wink_version, accept=accept)

Show Place Inventories

Retrieve list of places for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve places for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Place Inventories
        api_response = api_instance.show_channel_places(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_places:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_places: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve places for | 
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

# **show_channel_restaurants**
> List[KeyValuePairSupplier] show_channel_restaurants(property_identifier, wink_version=wink_version, accept=accept)

Show Restaurant Inventories

Retrieve list of restaurants for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve restaurants for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Restaurant Inventories
        api_response = api_instance.show_channel_restaurants(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_restaurants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve restaurants for | 
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

# **show_channel_spas**
> List[KeyValuePairSupplier] show_channel_spas(property_identifier, wink_version=wink_version, accept=accept)

Show Spa Inventories

Retrieve list of spas for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve spas for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Spa Inventories
        api_response = api_instance.show_channel_spas(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_channel_spas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_channel_spas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve spas for | 
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

# **show_inventory**
> InventoryViewSupplier show_inventory(property_identifier, inventory_identifier, wink_version=wink_version, accept=accept)

Show Inventory

Retrieve blocking specified by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_view_supplier import InventoryViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve specified blocking for
    inventory_identifier = 'inventory_identifier_example' # str | The blocking ID to retrieve
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory
        api_response = api_instance.show_inventory(property_identifier, inventory_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve specified blocking for | 
 **inventory_identifier** | **str**| The blocking ID to retrieve | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**InventoryViewSupplier**](InventoryViewSupplier.md)

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

# **show_inventory_list**
> List[InventoryViewSupplier] show_inventory_list(property_identifier, wink_version=wink_version, accept=accept)

Show Inventory List

Retrieve list of blocking for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_view_supplier import InventoryViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve inventories for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory List
        api_response = api_instance.show_inventory_list(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_inventory_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_inventory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve inventories for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[InventoryViewSupplier]**](InventoryViewSupplier.md)

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

# **show_inventory_names**
> List[str] show_inventory_names(property_identifier, wink_version=wink_version, accept=accept)

Show Inventory Names

Retrieve list of unique blocking names for chosen property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve blocking names for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory Names
        api_response = api_instance.show_inventory_names(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_inventory_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_inventory_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve blocking names for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

**List[str]**

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

# **show_inventory_types**
> List[str] show_inventory_types(property_identifier, wink_version=wink_version, accept=accept)

Show All Inventory Types

Retrieve array of all blocking types. E.g. ['GUEST_ROOM', 'MEETING_ROOM'].

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve blocking types for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show All Inventory Types
        api_response = api_instance.show_inventory_types(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_inventory_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_inventory_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve blocking types for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

**List[str]**

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

# **show_master_rates**
> List[KeyValuePairSupplier] show_master_rates(property_identifier, wink_version=wink_version, accept=accept)

Show Master Rates Inventories

Retrieve list of master rate names for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve master rates for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Master Rates Inventories
        api_response = api_instance.show_master_rates(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_master_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_master_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve master rates for | 
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

# **show_pageable_channel_inventory**
> PageInventoryViewSupplier show_pageable_channel_inventory(property_identifier, state_supplier, wink_version=wink_version)

Search Inventory

Retrieve page of blocking for specified property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.page_inventory_view_supplier import PageInventoryViewSupplier
from wink_sdk_extranet_distribution.models.state_supplier import StateSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve blocking grid for
    state_supplier = wink_sdk_extranet_distribution.StateSupplier() # StateSupplier | Filter grid by state request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Search Inventory
        api_response = api_instance.show_pageable_channel_inventory(property_identifier, state_supplier, wink_version=wink_version)
        print("The response of InventoryApi->show_pageable_channel_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_pageable_channel_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve blocking grid for | 
 **state_supplier** | [**StateSupplier**](StateSupplier.md)| Filter grid by state request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageInventoryViewSupplier**](PageInventoryViewSupplier.md)

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

# **show_sales_channel_list_by_inventory**
> List[SelectableKeyValuePairSupplier] show_sales_channel_list_by_inventory(property_identifier, inventory_type_identifier, wink_version=wink_version, accept=accept)

Show Inventory as Channels

Retrieve list of blocking specified by blocking identifier. The list will contain the same blocking available to different sales channels. E.g. Inventory A for Seller A. Inventory A for Seller B etc.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.selectable_key_value_pair_supplier import SelectableKeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve sales channels for
    inventory_type_identifier = 'inventory_type_identifier_example' # str | The blocking type ID to retrieve sales channel for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Inventory as Channels
        api_response = api_instance.show_sales_channel_list_by_inventory(property_identifier, inventory_type_identifier, wink_version=wink_version, accept=accept)
        print("The response of InventoryApi->show_sales_channel_list_by_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->show_sales_channel_list_by_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to retrieve sales channels for | 
 **inventory_type_identifier** | **str**| The blocking type ID to retrieve sales channel for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SelectableKeyValuePairSupplier]**](SelectableKeyValuePairSupplier.md)

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

# **toggle_inventory_availability**
> InventoryViewSupplier toggle_inventory_availability(property_identifier, inventory_identifier, inventory_update_request_supplier, wink_version=wink_version)

Update Inventory

Toggle blocking availability. Only used to enable / disable blocking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier
from wink_sdk_extranet_distribution.models.inventory_view_supplier import InventoryViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to update blocking for
    inventory_identifier = 'inventory_identifier_example' # str | The blocking ID to update
    inventory_update_request_supplier = wink_sdk_extranet_distribution.InventoryUpdateRequestSupplier() # InventoryUpdateRequestSupplier | Update blocking request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Inventory
        api_response = api_instance.toggle_inventory_availability(property_identifier, inventory_identifier, inventory_update_request_supplier, wink_version=wink_version)
        print("The response of InventoryApi->toggle_inventory_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->toggle_inventory_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to update blocking for | 
 **inventory_identifier** | **str**| The blocking ID to update | 
 **inventory_update_request_supplier** | [**InventoryUpdateRequestSupplier**](InventoryUpdateRequestSupplier.md)| Update blocking request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InventoryViewSupplier**](InventoryViewSupplier.md)

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

# **toggle_inventory_list_availability**
> List[InventoryViewSupplier] toggle_inventory_list_availability(property_identifier, inventory_update_request_supplier, wink_version=wink_version)

Update Inventory List

Toggle blocking list availability. Only used to enable / disable blocking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier
from wink_sdk_extranet_distribution.models.inventory_view_supplier import InventoryViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to update blocking for
    inventory_update_request_supplier = [wink_sdk_extranet_distribution.InventoryUpdateRequestSupplier()] # List[InventoryUpdateRequestSupplier] | Update inventories request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Inventory List
        api_response = api_instance.toggle_inventory_list_availability(property_identifier, inventory_update_request_supplier, wink_version=wink_version)
        print("The response of InventoryApi->toggle_inventory_list_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->toggle_inventory_list_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| The property ID to update blocking for | 
 **inventory_update_request_supplier** | [**List[InventoryUpdateRequestSupplier]**](InventoryUpdateRequestSupplier.md)| Update inventories request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[InventoryViewSupplier]**](InventoryViewSupplier.md)

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

