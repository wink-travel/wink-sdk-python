# wink_sdk_extranet_distribution.AffiliateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_affiliates**](AffiliateApi.md#browse_affiliates) | **POST** /api/property/{propertyIdentifier}/sales/affiliate/grid | Show Affiliates
[**invite_affiliate**](AffiliateApi.md#invite_affiliate) | **POST** /api/property/{propertyIdentifier}/sales/affiliate/invite | Send invite
[**show_affiliate**](AffiliateApi.md#show_affiliate) | **GET** /api/property/{propertyIdentifier}/sales/affiliate/{affiliateAccountIdentifier} | Show Affiliate
[**show_unique_city_list**](AffiliateApi.md#show_unique_city_list) | **GET** /api/property/{propertyIdentifier}/sales/affiliate/city/list | Show Unique Affiliate Cities
[**show_unique_country_list**](AffiliateApi.md#show_unique_country_list) | **GET** /api/property/{propertyIdentifier}/sales/affiliate/country/list | Show Unique Affiliate Countries


# **browse_affiliates**
> PageDisplayCompanyWithSalesMetricsAuthenticatedEntity browse_affiliates(property_identifier, state_authenticated_entity, wink_version=wink_version)

Show Affiliates

Retrieve page of affiliates.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.page_display_company_with_sales_metrics_authenticated_entity import PageDisplayCompanyWithSalesMetricsAuthenticatedEntity
from wink_sdk_extranet_distribution.models.state_authenticated_entity import StateAuthenticatedEntity
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.AffiliateApi(api_client)
    property_identifier = 'hotel-1' # str | Display affiliates to this specified property
    state_authenticated_entity = wink_sdk_extranet_distribution.StateAuthenticatedEntity() # StateAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Affiliates
        api_response = api_instance.browse_affiliates(property_identifier, state_authenticated_entity, wink_version=wink_version)
        print("The response of AffiliateApi->browse_affiliates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->browse_affiliates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display affiliates to this specified property | 
 **state_authenticated_entity** | [**StateAuthenticatedEntity**](StateAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageDisplayCompanyWithSalesMetricsAuthenticatedEntity**](PageDisplayCompanyWithSalesMetricsAuthenticatedEntity.md)

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

# **invite_affiliate**
> BooleanResponseAuthenticatedEntity invite_affiliate(property_identifier, invite_affiliate_request_authenticated_entity, wink_version=wink_version)

Send invite

Send an email invite to a user

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.boolean_response_authenticated_entity import BooleanResponseAuthenticatedEntity
from wink_sdk_extranet_distribution.models.invite_affiliate_request_authenticated_entity import InviteAffiliateRequestAuthenticatedEntity
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.AffiliateApi(api_client)
    property_identifier = 'hotel-1' # str | Display affiliate to this specified property
    invite_affiliate_request_authenticated_entity = wink_sdk_extranet_distribution.InviteAffiliateRequestAuthenticatedEntity() # InviteAffiliateRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Send invite
        api_response = api_instance.invite_affiliate(property_identifier, invite_affiliate_request_authenticated_entity, wink_version=wink_version)
        print("The response of AffiliateApi->invite_affiliate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->invite_affiliate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display affiliate to this specified property | 
 **invite_affiliate_request_authenticated_entity** | [**InviteAffiliateRequestAuthenticatedEntity**](InviteAffiliateRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**BooleanResponseAuthenticatedEntity**](BooleanResponseAuthenticatedEntity.md)

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

# **show_affiliate**
> CompanyDetailsBookingSalesMetricsAuthenticatedEntity show_affiliate(property_identifier, affiliate_account_identifier, wink_version=wink_version, accept=accept)

Show Affiliate

Retrieve affiliate information specified by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.company_details_booking_sales_metrics_authenticated_entity import CompanyDetailsBookingSalesMetricsAuthenticatedEntity
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.AffiliateApi(api_client)
    property_identifier = 'hotel-1' # str | Display affiliate to this specified property
    affiliate_account_identifier = 'hotel-1' # str | Display affiliate by specified company
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Affiliate
        api_response = api_instance.show_affiliate(property_identifier, affiliate_account_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_affiliate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_affiliate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display affiliate to this specified property | 
 **affiliate_account_identifier** | **str**| Display affiliate by specified company | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**CompanyDetailsBookingSalesMetricsAuthenticatedEntity**](CompanyDetailsBookingSalesMetricsAuthenticatedEntity.md)

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

# **show_unique_city_list**
> List[KeyValuePairSupplier] show_unique_city_list(property_identifier, wink_version=wink_version, accept=accept)

Show Unique Affiliate Cities

Retrieve a list of unique cities where affiliates live

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.AffiliateApi(api_client)
    property_identifier = 'hotel-1' # str | Display unique cities of affiliate to this specified property
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unique Affiliate Cities
        api_response = api_instance.show_unique_city_list(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_unique_city_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_unique_city_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display unique cities of affiliate to this specified property | 
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

# **show_unique_country_list**
> List[KeyValuePairSupplier] show_unique_country_list(property_identifier, wink_version=wink_version, accept=accept)

Show Unique Affiliate Countries

Retrieve a list of unique countries where affiliates live

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.AffiliateApi(api_client)
    property_identifier = 'hotel-1' # str | Display unique countries of affiliate to this specified property
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unique Affiliate Countries
        api_response = api_instance.show_unique_country_list(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of AffiliateApi->show_unique_country_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_unique_country_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Display unique countries of affiliate to this specified property | 
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

