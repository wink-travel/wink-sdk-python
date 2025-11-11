# wink_sdk_extranet_monetize.InventoryUsageApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_add_on_usage**](InventoryUsageApi.md#show_add_on_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/add-on/{addOnIdentifier} | Show Add-On Usage
[**show_rate_plan_usage**](InventoryUsageApi.md#show_rate_plan_usage) | **GET** /api/property/{propertyIdentifier}/inventory-usage/rate-plan/{ratePlanIdentifier} | Show Rate Plan Usage


# **show_add_on_usage**
> InventoryUsageSupplier show_add_on_usage(property_identifier, add_on_identifier, wink_version=wink_version, accept=accept)

Show Add-On Usage

Retrieve an aggregate report where specified add-on is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.inventory_usage_supplier import InventoryUsageSupplier
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
    api_instance = wink_sdk_extranet_monetize.InventoryUsageApi(api_client)
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

# **show_rate_plan_usage**
> InventoryUsageSupplier show_rate_plan_usage(property_identifier, rate_plan_identifier, wink_version=wink_version, accept=accept)

Show Rate Plan Usage

Retrieve an aggregate report where specified rate plan is being used on affiliate real estate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.inventory_usage_supplier import InventoryUsageSupplier
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
    api_instance = wink_sdk_extranet_monetize.InventoryUsageApi(api_client)
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

