# wink_sdk_extranet_property.ChannelManagerApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_channel_manager**](ChannelManagerApi.md#update_channel_manager) | **PATCH** /api/property/{propertyIdentifier}/channel-manager | Set Channel Manager


# **update_channel_manager**
> PropertySupplier update_channel_manager(property_identifier, update_channel_manager_request_supplier, wink_version=wink_version)

Set Channel Manager

Set which channel manager this property uses. Channel managers are not allowed access to rates until the property selects them as their channel manager.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.update_channel_manager_request_supplier import UpdateChannelManagerRequestSupplier
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
    api_instance = wink_sdk_extranet_property.ChannelManagerApi(api_client)
    property_identifier = 'hotel-1' # str | Set channel manager for this property identifier
    update_channel_manager_request_supplier = wink_sdk_extranet_property.UpdateChannelManagerRequestSupplier() # UpdateChannelManagerRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Set Channel Manager
        api_response = api_instance.update_channel_manager(property_identifier, update_channel_manager_request_supplier, wink_version=wink_version)
        print("The response of ChannelManagerApi->update_channel_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->update_channel_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Set channel manager for this property identifier | 
 **update_channel_manager_request_supplier** | [**UpdateChannelManagerRequestSupplier**](UpdateChannelManagerRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

