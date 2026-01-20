# wink_sdk_extranet_monetize.InventoryApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_channel_add_ons**](InventoryApi.md#show_channel_add_ons) | **GET** /api/property/{propertyIdentifier}/sales/add-on/list | Show Add-On Inventories
[**show_master_rates**](InventoryApi.md#show_master_rates) | **GET** /api/property/{propertyIdentifier}/sales/master-rate/list | Show Master Rates Inventories


# **show_channel_add_ons**
> List[KeyValuePairSupplier] show_channel_add_ons(property_identifier, wink_version=wink_version, accept=accept)

Show Add-On Inventories

Retrieve list of addons for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_monetize.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve add-ons for
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
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
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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

# **show_master_rates**
> List[KeyValuePairSupplier] show_master_rates(property_identifier, wink_version=wink_version, accept=accept)

Show Master Rates Inventories

Retrieve list of master rate names for specified property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.key_value_pair_supplier import KeyValuePairSupplier
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
    api_instance = wink_sdk_extranet_monetize.InventoryApi(api_client)
    property_identifier = 'property_identifier_example' # str | The property ID to retrieve master rates for
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
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
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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

