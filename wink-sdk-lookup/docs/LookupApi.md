# wink_sdk_lookup.LookupApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**score_inventory_by_agency**](LookupApi.md#score_inventory_by_agency) | **POST** /api/ranked/search/agency | Ranked Agency Search
[**score_inventory_by_city**](LookupApi.md#score_inventory_by_city) | **POST** /api/ranked/search/city | Ranked City Search
[**search_by_geo_location**](LookupApi.md#search_by_geo_location) | **POST** /api/search/geo | By Geo-Location
[**search_inventory_by_city**](LookupApi.md#search_inventory_by_city) | **POST** /api/search/city | City Search
[**search_score_by_country**](LookupApi.md#search_score_by_country) | **POST** /api/ranked/search/country | Ranked Country Search
[**search_score_by_global**](LookupApi.md#search_score_by_global) | **POST** /api/ranked/search/global | Ranked Global Search
[**search_suggestions**](LookupApi.md#search_suggestions) | **GET** /api/search | Search Lookups
[**show_lookup**](LookupApi.md#show_lookup) | **GET** /api/lookup/{urlName} | Show Lookup


# **score_inventory_by_agency**
> PagePropertyWithBestPriceNonAuthenticatedEntity score_inventory_by_agency(agency_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

Ranked Agency Search

Search for hotels represented by a property management agency.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.agency_score_request_non_authenticated_entity import AgencyScoreRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    agency_score_request_non_authenticated_entity = wink_sdk_lookup.AgencyScoreRequestNonAuthenticatedEntity() # AgencyScoreRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Ranked Agency Search
        api_response = api_instance.score_inventory_by_agency(agency_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->score_inventory_by_agency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->score_inventory_by_agency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agency_score_request_non_authenticated_entity** | [**AgencyScoreRequestNonAuthenticatedEntity**](AgencyScoreRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **score_inventory_by_city**
> PagePropertyWithBestPriceNonAuthenticatedEntity score_inventory_by_city(city_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

Ranked City Search

Search for hotels in / around a city and order by scoring type

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.city_score_request_non_authenticated_entity import CityScoreRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    city_score_request_non_authenticated_entity = wink_sdk_lookup.CityScoreRequestNonAuthenticatedEntity() # CityScoreRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Ranked City Search
        api_response = api_instance.score_inventory_by_city(city_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->score_inventory_by_city:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->score_inventory_by_city: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_score_request_non_authenticated_entity** | [**CityScoreRequestNonAuthenticatedEntity**](CityScoreRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **search_by_geo_location**
> PagePropertyWithBestPriceNonAuthenticatedEntity search_by_geo_location(map_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

By Geo-Location

Search for properties near a point or within bounds. Populate either `request.userSession.location` OR `request.userSession.bounds`.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.map_request_non_authenticated_entity import MapRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    map_request_non_authenticated_entity = wink_sdk_lookup.MapRequestNonAuthenticatedEntity() # MapRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # By Geo-Location
        api_response = api_instance.search_by_geo_location(map_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->search_by_geo_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->search_by_geo_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_request_non_authenticated_entity** | [**MapRequestNonAuthenticatedEntity**](MapRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **search_inventory_by_city**
> PagePropertyWithBestPriceNonAuthenticatedEntity search_inventory_by_city(city_search_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

City Search

Search for hotels in / around a city

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.city_search_request_non_authenticated_entity import CitySearchRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    city_search_request_non_authenticated_entity = wink_sdk_lookup.CitySearchRequestNonAuthenticatedEntity() # CitySearchRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # City Search
        api_response = api_instance.search_inventory_by_city(city_search_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->search_inventory_by_city:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->search_inventory_by_city: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_search_request_non_authenticated_entity** | [**CitySearchRequestNonAuthenticatedEntity**](CitySearchRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **search_score_by_country**
> PagePropertyWithBestPriceNonAuthenticatedEntity search_score_by_country(country_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

Ranked Country Search

Search for hotels in a country and order by scoring type

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.country_score_request_non_authenticated_entity import CountryScoreRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    country_score_request_non_authenticated_entity = wink_sdk_lookup.CountryScoreRequestNonAuthenticatedEntity() # CountryScoreRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Ranked Country Search
        api_response = api_instance.search_score_by_country(country_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->search_score_by_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->search_score_by_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_score_request_non_authenticated_entity** | [**CountryScoreRequestNonAuthenticatedEntity**](CountryScoreRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **search_score_by_global**
> PagePropertyWithBestPriceNonAuthenticatedEntity search_score_by_global(global_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)

Ranked Global Search

Search best scoring hotels in the world and order by scoring type

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.global_score_request_non_authenticated_entity import GlobalScoreRequestNonAuthenticatedEntity
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    global_score_request_non_authenticated_entity = wink_sdk_lookup.GlobalScoreRequestNonAuthenticatedEntity() # GlobalScoreRequestNonAuthenticatedEntity | 
    engine_configuration_identifier = 'engine_configuration_identifier_example' # str | Engine configuration identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Ranked Global Search
        api_response = api_instance.search_score_by_global(global_score_request_non_authenticated_entity, engine_configuration_identifier=engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->search_score_by_global:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->search_score_by_global: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_score_request_non_authenticated_entity** | [**GlobalScoreRequestNonAuthenticatedEntity**](GlobalScoreRequestNonAuthenticatedEntity.md)|  | 
 **engine_configuration_identifier** | **str**| Engine configuration identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PagePropertyWithBestPriceNonAuthenticatedEntity**](PagePropertyWithBestPriceNonAuthenticatedEntity.md)

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

# **search_suggestions**
> List[LookupCachedNonAuthenticatedEntity] search_suggestions(term, wink_version=wink_version, accept=accept)

Search Lookups

Searches for hotels, cities or countries by the search term.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.lookup_cached_non_authenticated_entity import LookupCachedNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    term = 'Los A' # str | Search for lookups by this term
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Search Lookups
        api_response = api_instance.search_suggestions(term, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->search_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->search_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Search for lookups by this term | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[LookupCachedNonAuthenticatedEntity]**](LookupCachedNonAuthenticatedEntity.md)

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

# **show_lookup**
> LookupLightweightNonAuthenticatedEntity show_lookup(url_name, type, wink_version=wink_version, accept=accept)

Show Lookup

Show lookup object by its unique url name.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_lookup
from wink_sdk_lookup.models.lookup_lightweight_non_authenticated_entity import LookupLightweightNonAuthenticatedEntity
from wink_sdk_lookup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_lookup.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_lookup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_lookup.LookupApi(api_client)
    url_name = 'los-angeles' # str | Show lookup by unique url name
    type = 'CITY' # str | Filter on type
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Lookup
        api_response = api_instance.show_lookup(url_name, type, wink_version=wink_version, accept=accept)
        print("The response of LookupApi->show_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LookupApi->show_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| Show lookup by unique url name | 
 **type** | **str**| Filter on type | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**LookupLightweightNonAuthenticatedEntity**](LookupLightweightNonAuthenticatedEntity.md)

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

