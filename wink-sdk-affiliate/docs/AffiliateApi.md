# wink_sdk_affiliate.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_affiliate**](AffiliateApi.md#create_affiliate) | **POST** /api/affiliate | Create Affiliate
[**remove_company**](AffiliateApi.md#remove_company) | **DELETE** /api/affiliate/{companyIdentifier} | Delete Affiliate
[**search_affiliates**](AffiliateApi.md#search_affiliates) | **POST** /api/affiliate/grid | Affiliate Search
[**show_affiliate**](AffiliateApi.md#show_affiliate) | **GET** /api/affiliate/{companyIdentifier} | Show Affiliate
[**show_companies**](AffiliateApi.md#show_companies) | **GET** /api/affiliate/list | Show Affiliates
[**update_company**](AffiliateApi.md#update_company) | **PATCH** /api/affiliate/{companyIdentifier} | Update Affiliate
[**update_company1**](AffiliateApi.md#update_company1) | **PATCH** /api/affiliate/{companyIdentifier}/status | Toggle Affiliate Status
[**update_company_address**](AffiliateApi.md#update_company_address) | **PATCH** /api/affiliate/{companyIdentifier}/address | Update Affiliate Address
[**update_company_logo**](AffiliateApi.md#update_company_logo) | **PATCH** /api/affiliate/{companyIdentifier}/logo | Update Affiliate Logo
[**update_company_online_presence**](AffiliateApi.md#update_company_online_presence) | **PATCH** /api/affiliate/{companyIdentifier}/online-presence | Update Affiliate Online Presence
[**update_profile**](AffiliateApi.md#update_profile) | **PATCH** /api/affiliate/{companyIdentifier}/profile | Update Profile


# **create_affiliate**
> AffiliateAccountAffiliate create_affiliate(create_affiliate_account_request_affiliate, wink_version=wink_version)

Create Affiliate

Create a new affiliate

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.create_affiliate_account_request_affiliate import CreateAffiliateAccountRequestAffiliate
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
    create_affiliate_account_request_affiliate = wink_sdk_affiliate.CreateAffiliateAccountRequestAffiliate() # CreateAffiliateAccountRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Affiliate
        api_response = api_instance.create_affiliate(create_affiliate_account_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->create_affiliate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->create_affiliate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_affiliate_account_request_affiliate** | [**CreateAffiliateAccountRequestAffiliate**](CreateAffiliateAccountRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_company**
> AffiliateAccountAffiliate remove_company(company_identifier, wink_version=wink_version, accept=accept)

Delete Affiliate

Delete a company by identifier

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
    company_identifier = 'company_identifier_example' # str | Delete company with given identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Affiliate
        api_response = api_instance.remove_company(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->remove_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->remove_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Delete company with given identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **search_affiliates**
> PageAffiliateAccountSupplier search_affiliates(state_supplier, wink_version=wink_version)

Affiliate Search

Retrieve a paginated list of affiliates that you manage.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.page_affiliate_account_supplier import PageAffiliateAccountSupplier
from wink_sdk_affiliate.models.state_supplier import StateSupplier
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
    state_supplier = wink_sdk_affiliate.StateSupplier() # StateSupplier | Filter grid by state request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Affiliate Search
        api_response = api_instance.search_affiliates(state_supplier, wink_version=wink_version)
        print("The response of AffiliateApi->search_affiliates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->search_affiliates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_supplier** | [**StateSupplier**](StateSupplier.md)| Filter grid by state request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageAffiliateAccountSupplier**](PageAffiliateAccountSupplier.md)

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

# **show_affiliate**
> AffiliateAccountAffiliate show_affiliate(company_identifier, wink_version=wink_version, accept=accept)

Show Affiliate

Retrieve company by identifier

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
    company_identifier = 'company_identifier_example' # str | Select company with given identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Affiliate
        api_response = api_instance.show_affiliate(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_affiliate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_affiliate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Select company with given identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **show_companies**
> List[AffiliateAccountAffiliate] show_companies(type=type, wink_version=wink_version, accept=accept)

Show Affiliates

List all companies owned by caller.

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
    type = 'type_example' # str | Filter on companies of a specific type (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Affiliates
        api_response = api_instance.show_companies(type=type, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_companies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on companies of a specific type | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[AffiliateAccountAffiliate]**](AffiliateAccountAffiliate.md)

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

# **update_company**
> AffiliateAccountAffiliate update_company(company_identifier, upsert_company_request_affiliate, wink_version=wink_version)

Update Affiliate

Update an existing company

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_company_request_affiliate import UpsertCompanyRequestAffiliate
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
    company_identifier = 'company_identifier_example' # str | Update company with given identifier
    upsert_company_request_affiliate = wink_sdk_affiliate.UpsertCompanyRequestAffiliate() # UpsertCompanyRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Affiliate
        api_response = api_instance.update_company(company_identifier, upsert_company_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update company with given identifier | 
 **upsert_company_request_affiliate** | [**UpsertCompanyRequestAffiliate**](UpsertCompanyRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_company1**
> AffiliateAccountAffiliate update_company1(company_identifier, upsert_company_status_request_affiliate, wink_version=wink_version)

Toggle Affiliate Status

Update company status

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_company_status_request_affiliate import UpsertCompanyStatusRequestAffiliate
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
    company_identifier = 'company_identifier_example' # str | Update status of company with given identifier
    upsert_company_status_request_affiliate = wink_sdk_affiliate.UpsertCompanyStatusRequestAffiliate() # UpsertCompanyStatusRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Toggle Affiliate Status
        api_response = api_instance.update_company1(company_identifier, upsert_company_status_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update status of company with given identifier | 
 **upsert_company_status_request_affiliate** | [**UpsertCompanyStatusRequestAffiliate**](UpsertCompanyStatusRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_company_address**
> AffiliateAccountAffiliate update_company_address(company_identifier, upsert_address_request_affiliate, wink_version=wink_version)

Update Affiliate Address

Updates company address.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_address_request_affiliate import UpsertAddressRequestAffiliate
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
    company_identifier = 'company_identifier_example' # str | Update address of company with given identifier
    upsert_address_request_affiliate = wink_sdk_affiliate.UpsertAddressRequestAffiliate() # UpsertAddressRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Affiliate Address
        api_response = api_instance.update_company_address(company_identifier, upsert_address_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update address of company with given identifier | 
 **upsert_address_request_affiliate** | [**UpsertAddressRequestAffiliate**](UpsertAddressRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_company_logo**
> AffiliateAccountAffiliate update_company_logo(company_identifier, upsert_company_logo_request_affiliate, wink_version=wink_version)

Update Affiliate Logo

Updates company logo.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_company_logo_request_affiliate import UpsertCompanyLogoRequestAffiliate
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
    company_identifier = 'company_identifier_example' # str | Update logo of company with given identifier
    upsert_company_logo_request_affiliate = wink_sdk_affiliate.UpsertCompanyLogoRequestAffiliate() # UpsertCompanyLogoRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Affiliate Logo
        api_response = api_instance.update_company_logo(company_identifier, upsert_company_logo_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update logo of company with given identifier | 
 **upsert_company_logo_request_affiliate** | [**UpsertCompanyLogoRequestAffiliate**](UpsertCompanyLogoRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_company_online_presence**
> AffiliateAccountAffiliate update_company_online_presence(company_identifier, upsert_company_online_presence_request_affiliate, wink_version=wink_version)

Update Affiliate Online Presence

Updates company online presence.

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
    company_identifier = 'company_identifier_example' # str | Update logo of company with given identifier
    upsert_company_online_presence_request_affiliate = wink_sdk_affiliate.UpsertCompanyOnlinePresenceRequestAffiliate() # UpsertCompanyOnlinePresenceRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Affiliate Online Presence
        api_response = api_instance.update_company_online_presence(company_identifier, upsert_company_online_presence_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company_online_presence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company_online_presence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update logo of company with given identifier | 
 **upsert_company_online_presence_request_affiliate** | [**UpsertCompanyOnlinePresenceRequestAffiliate**](UpsertCompanyOnlinePresenceRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **update_profile**
> AffiliateAccountAffiliate update_profile(company_identifier, upsert_affiliate_account_profile_request_affiliate, wink_version=wink_version)

Update Profile

Update affiliate account profile.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_affiliate_account_profile_request_affiliate import UpsertAffiliateAccountProfileRequestAffiliate
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
    company_identifier = 'company_identifier_example' # str | Update company with given identifier
    upsert_affiliate_account_profile_request_affiliate = wink_sdk_affiliate.UpsertAffiliateAccountProfileRequestAffiliate() # UpsertAffiliateAccountProfileRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Profile
        api_response = api_instance.update_profile(company_identifier, upsert_affiliate_account_profile_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update company with given identifier | 
 **upsert_affiliate_account_profile_request_affiliate** | [**UpsertAffiliateAccountProfileRequestAffiliate**](UpsertAffiliateAccountProfileRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

