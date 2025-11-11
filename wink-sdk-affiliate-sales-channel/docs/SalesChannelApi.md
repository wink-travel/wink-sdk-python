# wink_sdk_affiliate_sales_channel.SalesChannelApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_sales_channels**](SalesChannelApi.md#browse_sales_channels) | **POST** /api/sales-channel/grid | Sales Channel Grid
[**show_sales_channel**](SalesChannelApi.md#show_sales_channel) | **GET** /api/sales-channel/supplier/{supplierIdentifier} | Show Sales Channel


# **browse_sales_channels**
> PageSalesChannelAffiliate browse_sales_channels(state_affiliate, wink_version=wink_version)

Sales Channel Grid

Retrieve page of existing sales channels based on criteria.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.page_sales_channel_affiliate import PageSalesChannelAffiliate
from wink_sdk_affiliate_sales_channel.models.state_affiliate import StateAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.SalesChannelApi(api_client)
    state_affiliate = wink_sdk_affiliate_sales_channel.StateAffiliate() # StateAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Sales Channel Grid
        api_response = api_instance.browse_sales_channels(state_affiliate, wink_version=wink_version)
        print("The response of SalesChannelApi->browse_sales_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->browse_sales_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_affiliate** | [**StateAffiliate**](StateAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageSalesChannelAffiliate**](PageSalesChannelAffiliate.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
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

# **show_sales_channel**
> SalesChannelAffiliate show_sales_channel(supplier_identifier, wink_version=wink_version, accept=accept)

Show Sales Channel

Retrieve sales channel specified by the company ID and the supplier ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_affiliate import SalesChannelAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.SalesChannelApi(api_client)
    supplier_identifier = 'supplier_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Sales Channel
        api_response = api_instance.show_sales_channel(supplier_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->show_sales_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->show_sales_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelAffiliate**](SalesChannelAffiliate.md)

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

