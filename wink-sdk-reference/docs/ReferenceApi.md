# wink_sdk_reference.ReferenceApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_all_exchange_rates**](ReferenceApi.md#show_all_exchange_rates) | **GET** /reference-data/fx | Show All Exchange Rates
[**show_available_codes_for_category**](ReferenceApi.md#show_available_codes_for_category) | **GET** /reference-data/ota/{category} | Show OTA Codes
[**show_available_ota_categories**](ReferenceApi.md#show_available_ota_categories) | **GET** /reference-data/ota/list | Show OTA Category Codes
[**show_countries1**](ReferenceApi.md#show_countries1) | **GET** /reference-data/country/list | Show Countries
[**show_currencies**](ReferenceApi.md#show_currencies) | **GET** /reference-data/currency/list | Show Currencies
[**show_exchange_rate**](ReferenceApi.md#show_exchange_rate) | **GET** /reference-data/fx/{sourceCurrency}/{targetCurrency} | Show Exchange Rate
[**show_exchange_rate_count**](ReferenceApi.md#show_exchange_rate_count) | **GET** /reference-data/fx/count | Show Exchange Rates Count
[**show_exchange_rate_for_target_currency**](ReferenceApi.md#show_exchange_rate_for_target_currency) | **GET** /reference-data/fx/{currency} | Show Exchange Rates
[**show_hotel_names**](ReferenceApi.md#show_hotel_names) | **GET** /reference-data/lookup/property/{name} | Hotel Name Search
[**show_languages**](ReferenceApi.md#show_languages) | **GET** /reference-data/language/list | Show Languages
[**show_lifestyles**](ReferenceApi.md#show_lifestyles) | **GET** /reference-data/lifestyle/list | Show Lifestyles
[**show_perks**](ReferenceApi.md#show_perks) | **GET** /reference-data/perk/list | Show Perks
[**show_social_networks**](ReferenceApi.md#show_social_networks) | **GET** /reference-data/social/list | Show Social Networks


# **show_all_exchange_rates**
> PageQuoteNonAuthenticatedEntity show_all_exchange_rates(page, size, wink_version=wink_version, accept=accept)

Show All Exchange Rates

Show exchange rates for target currency and all user-supported currencies.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.page_quote_non_authenticated_entity import PageQuoteNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    page = 56 # int | 
    size = 56 # int | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show All Exchange Rates
        api_response = api_instance.show_all_exchange_rates(page, size, wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_all_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_all_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | 
 **size** | **int**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**PageQuoteNonAuthenticatedEntity**](PageQuoteNonAuthenticatedEntity.md)

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

# **show_available_codes_for_category**
> List[KeyValuePairNonAuthenticatedEntity] show_available_codes_for_category(category, wink_version=wink_version, accept=accept)

Show OTA Codes

Shows reference-supported OTA codes based on given category.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    category = 'LOC' # str | Requested OTA code
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show OTA Codes
        api_response = api_instance.show_available_codes_for_category(category, wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_available_codes_for_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_available_codes_for_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Requested OTA code | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

# **show_available_ota_categories**
> List[KeyValuePairNonAuthenticatedEntity] show_available_ota_categories(wink_version=wink_version, accept=accept)

Show OTA Category Codes

Shows reference-supported OTA categories.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show OTA Category Codes
        api_response = api_instance.show_available_ota_categories(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_available_ota_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_available_ota_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

# **show_countries1**
> List[CountryLightweightNonAuthenticatedEntity] show_countries1(wink_version=wink_version, accept=accept)

Show Countries

Show list of user-supported countries.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.country_lightweight_non_authenticated_entity import CountryLightweightNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Countries
        api_response = api_instance.show_countries1(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_countries1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_countries1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[CountryLightweightNonAuthenticatedEntity]**](CountryLightweightNonAuthenticatedEntity.md)

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

# **show_currencies**
> List[str] show_currencies()

Show Currencies

List of user-supported currencies.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)

    try:
        # Show Currencies
        api_response = api_instance.show_currencies()
        print("The response of ReferenceApi->show_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **show_exchange_rate**
> QuoteLightweightNonAuthenticatedEntity show_exchange_rate(source_currency, target_currency, wink_version=wink_version)

Show Exchange Rate

Show exchange rate between target and source currency

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.quote_lightweight_non_authenticated_entity import QuoteLightweightNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    source_currency = 'source_currency_example' # str | 
    target_currency = 'target_currency_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Exchange Rate
        api_response = api_instance.show_exchange_rate(source_currency, target_currency, wink_version=wink_version)
        print("The response of ReferenceApi->show_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_currency** | **str**|  | 
 **target_currency** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md)

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

# **show_exchange_rate_count**
> CountResponseNonAuthenticatedEntity show_exchange_rate_count(wink_version=wink_version, accept=accept)

Show Exchange Rates Count

Returns a count of number of quotes available.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.count_response_non_authenticated_entity import CountResponseNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Exchange Rates Count
        api_response = api_instance.show_exchange_rate_count(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_exchange_rate_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_exchange_rate_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponseNonAuthenticatedEntity**](CountResponseNonAuthenticatedEntity.md)

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

# **show_exchange_rate_for_target_currency**
> List[QuoteLightweightNonAuthenticatedEntity] show_exchange_rate_for_target_currency(currency, wink_version=wink_version)

Show Exchange Rates

Show exchange rates for target currency and all user-supported currencies.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.quote_lightweight_non_authenticated_entity import QuoteLightweightNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    currency = 'currency_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Exchange Rates
        api_response = api_instance.show_exchange_rate_for_target_currency(currency, wink_version=wink_version)
        print("The response of ReferenceApi->show_exchange_rate_for_target_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_exchange_rate_for_target_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[QuoteLightweightNonAuthenticatedEntity]**](QuoteLightweightNonAuthenticatedEntity.md)

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

# **show_hotel_names**
> List[KeyValuePairNonAuthenticatedEntity] show_hotel_names(name, wink_version=wink_version, accept=accept)

Hotel Name Search

Search for property by name.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    name = 'name_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Hotel Name Search
        api_response = api_instance.show_hotel_names(name, wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_hotel_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_hotel_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

# **show_languages**
> List[LanguageNonAuthenticatedEntity] show_languages()

Show Languages

Retrieve list of system languages

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.language_non_authenticated_entity import LanguageNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)

    try:
        # Show Languages
        api_response = api_instance.show_languages()
        print("The response of ReferenceApi->show_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LanguageNonAuthenticatedEntity]**](LanguageNonAuthenticatedEntity.md)

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

# **show_lifestyles**
> List[KeyValuePairNonAuthenticatedEntity] show_lifestyles(wink_version=wink_version, accept=accept)

Show Lifestyles

Retrieve list of all supported lifestyles indicated by an array of key / value pairs.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Lifestyles
        api_response = api_instance.show_lifestyles(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_lifestyles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_lifestyles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

# **show_perks**
> List[PerkLightweightNonAuthenticatedEntity] show_perks(wink_version=wink_version, accept=accept)

Show Perks

Retrieve list of perks

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.perk_lightweight_non_authenticated_entity import PerkLightweightNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Perks
        api_response = api_instance.show_perks(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_perks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_perks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[PerkLightweightNonAuthenticatedEntity]**](PerkLightweightNonAuthenticatedEntity.md)

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

# **show_social_networks**
> List[KeyValuePairNonAuthenticatedEntity] show_social_networks(wink_version=wink_version, accept=accept)

Show Social Networks

Retrieve list of all supported social networks

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_reference.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_reference.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_reference.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_reference.ReferenceApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Social Networks
        api_response = api_instance.show_social_networks(wink_version=wink_version, accept=accept)
        print("The response of ReferenceApi->show_social_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceApi->show_social_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

