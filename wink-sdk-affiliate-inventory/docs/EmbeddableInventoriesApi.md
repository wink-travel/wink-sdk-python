# wink_sdk_affiliate_inventory.EmbeddableInventoriesApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_embeddable_inventory**](EmbeddableInventoriesApi.md#show_embeddable_inventory) | **GET** /api/affiliate/{companyIdentifier}/embeddable-inventory/list | Show Embeddable Inventories


# **show_embeddable_inventory**
> List[CampaignInventoryAffiliate] show_embeddable_inventory(company_identifier, wink_version=wink_version, accept=accept)

Show Embeddable Inventories

List all blocking types that can be embedded by one of our Web Components.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.campaign_inventory_affiliate import CampaignInventoryAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.EmbeddableInventoriesApi(api_client)
    company_identifier = 'company-1' # str | Show campaigns for this company
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Embeddable Inventories
        api_response = api_instance.show_embeddable_inventory(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of EmbeddableInventoriesApi->show_embeddable_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddableInventoriesApi->show_embeddable_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show campaigns for this company | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[CampaignInventoryAffiliate]**](CampaignInventoryAffiliate.md)

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

