# wink_sdk_extranet_distribution.SchedulerApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_item**](SchedulerApi.md#create_schedule_item) | **POST** /api/property/{propertyIdentifier}/schedule/{inventoryIdentifier} | Create Scheduler Item
[**remove_schedule_item**](SchedulerApi.md#remove_schedule_item) | **DELETE** /api/property/{propertyIdentifier}/schedule/{inventoryIdentifier}/item/{identifier} | Delete Scheduler Item
[**show_schedule_items**](SchedulerApi.md#show_schedule_items) | **GET** /api/property/{propertyIdentifier}/schedule/{inventoryIdentifier}/list | Show Scheduler Items
[**update_schedule_item**](SchedulerApi.md#update_schedule_item) | **PUT** /api/property/{propertyIdentifier}/schedule/{inventoryIdentifier}/item/{identifier} | Update Scheduler Item


# **create_schedule_item**
> ScheduleItemSupplier create_schedule_item(property_identifier, inventory_identifier, create_schedule_item_request_supplier, wink_version=wink_version)

Create Scheduler Item

Create a calendar item for any travel inventorysuch as meeting room, restaurant, spa, activity, attraction or place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.create_schedule_item_request_supplier import CreateScheduleItemRequestSupplier
from wink_sdk_extranet_distribution.models.schedule_item_supplier import ScheduleItemSupplier
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
    api_instance = wink_sdk_extranet_distribution.SchedulerApi(api_client)
    property_identifier = 'hotel-1' # str | Create a calendar item for travel inventoryowned by this property identifier
    inventory_identifier = 'travel-blocking-1' # str | Create a calendar item for travel inventorywith this identifier
    create_schedule_item_request_supplier = wink_sdk_extranet_distribution.CreateScheduleItemRequestSupplier() # CreateScheduleItemRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Scheduler Item
        api_response = api_instance.create_schedule_item(property_identifier, inventory_identifier, create_schedule_item_request_supplier, wink_version=wink_version)
        print("The response of SchedulerApi->create_schedule_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApi->create_schedule_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create a calendar item for travel inventoryowned by this property identifier | 
 **inventory_identifier** | **str**| Create a calendar item for travel inventorywith this identifier | 
 **create_schedule_item_request_supplier** | [**CreateScheduleItemRequestSupplier**](CreateScheduleItemRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ScheduleItemSupplier**](ScheduleItemSupplier.md)

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

# **remove_schedule_item**
> ScheduleItemSupplier remove_schedule_item(property_identifier, inventory_identifier, identifier, wink_version=wink_version, accept=accept)

Delete Scheduler Item

Delete a calendar item for any travel inventorysuch as meeting room, restaurant, spa, activity, attraction or place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.schedule_item_supplier import ScheduleItemSupplier
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
    api_instance = wink_sdk_extranet_distribution.SchedulerApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a calendar item for travel inventoryowned by this property identifier
    inventory_identifier = 'travel-blocking-1' # str | Remove a calendar item for travel inventorywith this identifier
    identifier = 'schedule-item-1' # str | Remove a calendar item with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Scheduler Item
        api_response = api_instance.remove_schedule_item(property_identifier, inventory_identifier, identifier, wink_version=wink_version, accept=accept)
        print("The response of SchedulerApi->remove_schedule_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApi->remove_schedule_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a calendar item for travel inventoryowned by this property identifier | 
 **inventory_identifier** | **str**| Remove a calendar item for travel inventorywith this identifier | 
 **identifier** | **str**| Remove a calendar item with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ScheduleItemSupplier**](ScheduleItemSupplier.md)

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

# **show_schedule_items**
> List[ScheduleItemSupplier] show_schedule_items(property_identifier, inventory_identifier, start, end, wink_version=wink_version, accept=accept)

Show Scheduler Items

Retrieve list of calendar items for a meeting room, restaurant, spa, activity, attraction or place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.schedule_item_supplier import ScheduleItemSupplier
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
    api_instance = wink_sdk_extranet_distribution.SchedulerApi(api_client)
    property_identifier = 'hotel-1' # str | Show calendar items for travel inventoryowned by this property identifier
    inventory_identifier = 'travel-blocking-1' # str | Show calendar items for travel inventorywith this identifier
    start = '2017-12-22T03:07:58.742+0000' # datetime | Specify start date range
    end = '2017-12-23T03:07:58.742+0000' # datetime | Specify end date range
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Scheduler Items
        api_response = api_instance.show_schedule_items(property_identifier, inventory_identifier, start, end, wink_version=wink_version, accept=accept)
        print("The response of SchedulerApi->show_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApi->show_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show calendar items for travel inventoryowned by this property identifier | 
 **inventory_identifier** | **str**| Show calendar items for travel inventorywith this identifier | 
 **start** | **datetime**| Specify start date range | 
 **end** | **datetime**| Specify end date range | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ScheduleItemSupplier]**](ScheduleItemSupplier.md)

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

# **update_schedule_item**
> ScheduleItemSupplier update_schedule_item(property_identifier, inventory_identifier, identifier, update_schedule_item_request_supplier, wink_version=wink_version)

Update Scheduler Item

Update an existing calendar item for any travel inventorysuch as meeting room, restaurant, spa, activity, attraction or place.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.schedule_item_supplier import ScheduleItemSupplier
from wink_sdk_extranet_distribution.models.update_schedule_item_request_supplier import UpdateScheduleItemRequestSupplier
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
    api_instance = wink_sdk_extranet_distribution.SchedulerApi(api_client)
    property_identifier = 'hotel-1' # str | Update a calendar item for travel inventoryowned by this property identifier
    inventory_identifier = 'travel-blocking-1' # str | Update a calendar item for travel inventorywith this identifier
    identifier = 'schedule-item-1' # str | Update a calendar item with this identifier
    update_schedule_item_request_supplier = wink_sdk_extranet_distribution.UpdateScheduleItemRequestSupplier() # UpdateScheduleItemRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Scheduler Item
        api_response = api_instance.update_schedule_item(property_identifier, inventory_identifier, identifier, update_schedule_item_request_supplier, wink_version=wink_version)
        print("The response of SchedulerApi->update_schedule_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApi->update_schedule_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update a calendar item for travel inventoryowned by this property identifier | 
 **inventory_identifier** | **str**| Update a calendar item for travel inventorywith this identifier | 
 **identifier** | **str**| Update a calendar item with this identifier | 
 **update_schedule_item_request_supplier** | [**UpdateScheduleItemRequestSupplier**](UpdateScheduleItemRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ScheduleItemSupplier**](ScheduleItemSupplier.md)

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

