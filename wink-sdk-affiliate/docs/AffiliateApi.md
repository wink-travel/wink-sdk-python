# wink_sdk_affiliate.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company**](AffiliateApi.md#create_company) | **POST** /api/affiliate | Create Affiliate
[**is_company_name_unique**](AffiliateApi.md#is_company_name_unique) | **POST** /api/affiliate/unique | Verify Affiliate Name
[**remove_company**](AffiliateApi.md#remove_company) | **DELETE** /api/affiliate/{companyIdentifier} | Delete Affiliate
[**search_affiliates**](AffiliateApi.md#search_affiliates) | **POST** /api/affiliate/grid | Affiliate Search
[**show_booking_analytics**](AffiliateApi.md#show_booking_analytics) | **POST** /api/affiliate/{companyIdentifier}/booking/analytics | Affiliate Booking Analytics
[**show_booking_overview**](AffiliateApi.md#show_booking_overview) | **GET** /api/affiliate/{companyIdentifier}/booking/overview | Affiliate Booking Overview
[**show_companies**](AffiliateApi.md#show_companies) | **GET** /api/affiliate/list | Show Affiliates
[**show_company**](AffiliateApi.md#show_company) | **GET** /api/affiliate/{companyIdentifier} | Show Affiliate
[**update_company**](AffiliateApi.md#update_company) | **PATCH** /api/affiliate/{companyIdentifier} | Update Affiliate
[**update_company1**](AffiliateApi.md#update_company1) | **PATCH** /api/affiliate/{companyIdentifier}/status | Toggle Affiliate Status
[**update_company_address**](AffiliateApi.md#update_company_address) | **PATCH** /api/affiliate/{companyIdentifier}/address | Update Affiliate Address
[**update_company_photo**](AffiliateApi.md#update_company_photo) | **PATCH** /api/affiliate/{companyIdentifier}/logo | Update Affiliate Logo


# **create_company**
> CompanyViewAffiliate create_company(create_company_request_affiliate, wink_version=wink_version)

Create Affiliate

Create a new affiliate

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
from wink_sdk_affiliate.models.create_company_request_affiliate import CreateCompanyRequestAffiliate
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
    create_company_request_affiliate = wink_sdk_affiliate.CreateCompanyRequestAffiliate() # CreateCompanyRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Affiliate
        api_response = api_instance.create_company(create_company_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->create_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->create_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_company_request_affiliate** | [**CreateCompanyRequestAffiliate**](CreateCompanyRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_company_name_unique**
> UniqueResultAffiliate is_company_name_unique(unique_request_affiliate, wink_version=wink_version)

Verify Affiliate Name

Check if company name is unique

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.unique_request_affiliate import UniqueRequestAffiliate
from wink_sdk_affiliate.models.unique_result_affiliate import UniqueResultAffiliate
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
    unique_request_affiliate = wink_sdk_affiliate.UniqueRequestAffiliate() # UniqueRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Verify Affiliate Name
        api_response = api_instance.is_company_name_unique(unique_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->is_company_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->is_company_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_request_affiliate** | [**UniqueRequestAffiliate**](UniqueRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**UniqueResultAffiliate**](UniqueResultAffiliate.md)

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

# **remove_company**
> CompanyViewAffiliate remove_company(company_identifier, wink_version=wink_version, accept=accept)

Delete Affiliate

Delete a company by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

# **search_affiliates**
> PageCompanyViewSupplier search_affiliates(state_supplier, wink_version=wink_version)

Affiliate Search

Retrieve a paginated list of affiliates that you manage.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.page_company_view_supplier import PageCompanyViewSupplier
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

[**PageCompanyViewSupplier**](PageCompanyViewSupplier.md)

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

# **show_booking_analytics**
> BookingAnalyticsSupplier show_booking_analytics(company_identifier, booking_overview_request_supplier, wink_version=wink_version)

Affiliate Booking Analytics

Retrieve the number of upcoming bookings that arrive today for the specific company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.booking_analytics_supplier import BookingAnalyticsSupplier
from wink_sdk_affiliate.models.booking_overview_request_supplier import BookingOverviewRequestSupplier
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
    company_identifier = 'company-1' # str | Show active booking count for company with this identifier
    booking_overview_request_supplier = wink_sdk_affiliate.BookingOverviewRequestSupplier() # BookingOverviewRequestSupplier | Overview request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Affiliate Booking Analytics
        api_response = api_instance.show_booking_analytics(company_identifier, booking_overview_request_supplier, wink_version=wink_version)
        print("The response of AffiliateApi->show_booking_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_booking_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show active booking count for company with this identifier | 
 **booking_overview_request_supplier** | [**BookingOverviewRequestSupplier**](BookingOverviewRequestSupplier.md)| Overview request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingAnalyticsSupplier**](BookingAnalyticsSupplier.md)

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

# **show_booking_overview**
> GroupedBookingSalesMetricsSupplierDetails show_booking_overview(company_identifier, wink_version=wink_version, accept=accept)

Affiliate Booking Overview

Basic booking overview data

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.grouped_booking_sales_metrics_supplier_details import GroupedBookingSalesMetricsSupplierDetails
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
    company_identifier = 'company-1' # str | Show booking owned by this company
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Affiliate Booking Overview
        api_response = api_instance.show_booking_overview(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_booking_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_booking_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show booking owned by this company | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**GroupedBookingSalesMetricsSupplierDetails**](GroupedBookingSalesMetricsSupplierDetails.md)

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

# **show_companies**
> List[CompanyViewAffiliate] show_companies(type=type, wink_version=wink_version, accept=accept)

Show Affiliates

List all companies owned by caller.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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

[**List[CompanyViewAffiliate]**](CompanyViewAffiliate.md)

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

# **show_company**
> CompanyViewAffiliate show_company(company_identifier, wink_version=wink_version, accept=accept)

Show Affiliate

Retrieve company by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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
        api_response = api_instance.show_company(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Select company with given identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

# **update_company**
> CompanyViewAffiliate update_company(company_identifier, upsert_company_request_affiliate, wink_version=wink_version)

Update Affiliate

Update an existing company

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

# **update_company1**
> CompanyViewAffiliate update_company1(company_identifier, upsert_company_status_request_affiliate, wink_version=wink_version)

Toggle Affiliate Status

Update company status

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

# **update_company_address**
> CompanyViewAffiliate update_company_address(company_identifier, upsert_address_request_affiliate, wink_version=wink_version)

Update Affiliate Address

Updates company address.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

# **update_company_photo**
> CompanyViewAffiliate update_company_photo(company_identifier, upsert_company_logo_request_affiliate, wink_version=wink_version)

Update Affiliate Logo

Updates company logo.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.company_view_affiliate import CompanyViewAffiliate
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
        api_response = api_instance.update_company_photo(company_identifier, upsert_company_logo_request_affiliate, wink_version=wink_version)
        print("The response of AffiliateApi->update_company_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->update_company_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update logo of company with given identifier | 
 **upsert_company_logo_request_affiliate** | [**UpsertCompanyLogoRequestAffiliate**](UpsertCompanyLogoRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CompanyViewAffiliate**](CompanyViewAffiliate.md)

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

