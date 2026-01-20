# wink_sdk_affiliate.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_affiliate**](AffiliateApi.md#show_affiliate) | **GET** /api/affiliate/{affiliateAccountIdentifier} | Show Affiliate
[**update_company_online_presence**](AffiliateApi.md#update_company_online_presence) | **PATCH** /api/affiliate/{affiliateAccountIdentifier}/online-presence | Update Online Presence


# **show_affiliate**
> AffiliateAccountAffiliate show_affiliate(affiliate_account_identifier, wink_version=wink_version, accept=accept)

Show Affiliate

Retrieve affiliate account by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
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
    api_instance = wink_sdk_affiliate.AffiliateApi(api_client)
    affiliate_account_identifier = 'affiliate_account_identifier_example' # str | Select affiliate account with given identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Affiliate
        api_response = api_instance.show_affiliate(affiliate_account_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_affiliate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_affiliate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affiliate_account_identifier** | **str**| Select affiliate account with given identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_company_online_presence**
> AffiliateAccountAffiliate update_company_online_presence(affiliate_account_identifier, upsert_company_online_presence_request_affiliate, wink_version=wink_version)

Update Online Presence

Updates affiliate account online presence.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_company_online_presence_request_affiliate import UpsertCompanyOnlinePresenceRequestAffiliate
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
    api_instance = wink_sdk_affiliate.AffiliateApi(api_client)
    affiliate_account_identifier = 'affiliate_account_identifier_example' # str | Update logo of affiliate account with given identifier
    upsert_company_online_presence_request_affiliate = wink_sdk_affiliate.UpsertCompanyOnlinePresenceRequestAffiliate() # UpsertCompanyOnlinePresenceRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Online Presence
        api_response = api_instance.update_company_online_presence(affiliate_account_identifier, upsert_company_online_presence_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company_online_presence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company_online_presence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affiliate_account_identifier** | **str**| Update logo of affiliate account with given identifier | 
 **upsert_company_online_presence_request_affiliate** | [**UpsertCompanyOnlinePresenceRequestAffiliate**](UpsertCompanyOnlinePresenceRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

