# wink_sdk_affiliate.TravelAgentApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_agent**](TravelAgentApi.md#update_agent) | **PATCH** /api/affiliate/{companyIdentifier}/agent | Update Agent


# **update_agent**
> AffiliateAccountAgent update_agent(company_identifier, update_travel_agent_request_agent, wink_version=wink_version)

Update Agent

Update an existing agent

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_agent import AffiliateAccountAgent
from wink_sdk_affiliate.models.update_travel_agent_request_agent import UpdateTravelAgentRequestAgent
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.TravelAgentApi(api_client)
    company_identifier = 'company_identifier_example' # str | Update agent by company id
    update_travel_agent_request_agent = wink_sdk_affiliate.UpdateTravelAgentRequestAgent() # UpdateTravelAgentRequestAgent | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Agent
        api_response = api_instance.update_agent(company_identifier, update_travel_agent_request_agent, wink_version=wink_version)
        print("The response of TravelAgentApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update agent by company id | 
 **update_travel_agent_request_agent** | [**UpdateTravelAgentRequestAgent**](UpdateTravelAgentRequestAgent.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**AffiliateAccountAgent**](AffiliateAccountAgent.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
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

