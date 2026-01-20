# wink_sdk_affiliate.LeadsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lead**](LeadsApi.md#create_lead) | **POST** /api/affiliate/{companyIdentifier}/lead | Create Lead Request


# **create_lead**
> SupplierLeadAffiliate create_lead(company_identifier, google_place_detail_request_affiliate, wink_version=wink_version)

Create Lead Request

Affiliate can request to onboard a property with information retrieved from Google Places.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.google_place_detail_request_affiliate import GooglePlaceDetailRequestAffiliate
from wink_sdk_affiliate.models.supplier_lead_affiliate import SupplierLeadAffiliate
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
    api_instance = wink_sdk_affiliate.LeadsApi(api_client)
    company_identifier = 'owner-1' # str | Create lead by this owner identifier.
    google_place_detail_request_affiliate = wink_sdk_affiliate.GooglePlaceDetailRequestAffiliate() # GooglePlaceDetailRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Lead Request
        api_response = api_instance.create_lead(company_identifier, google_place_detail_request_affiliate, wink_version=wink_version)
        print("The response of LeadsApi->create_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadsApi->create_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create lead by this owner identifier. | 
 **google_place_detail_request_affiliate** | [**GooglePlaceDetailRequestAffiliate**](GooglePlaceDetailRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SupplierLeadAffiliate**](SupplierLeadAffiliate.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

