# wink_sdk_affiliate_sales_channel.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_sales_channels**](AffiliateApi.md#show_sales_channels) | **GET** /api/sales-channel/search | Search Sales Channel by Name


# **show_sales_channels**
> List[KeyValuePairAffiliate] show_sales_channels(name, wink_version=wink_version, accept=accept)

Search Sales Channel by Name

Search for sales channels by name

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.key_value_pair_affiliate import KeyValuePairAffiliate
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
    api_instance = wink_sdk_affiliate_sales_channel.AffiliateApi(api_client)
    name = 'name_example' # str | Search for sales channel with name
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Search Sales Channel by Name
        api_response = api_instance.show_sales_channels(name, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_sales_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_sales_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search for sales channel with name | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md)

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

