# wink_sdk_reference.GeoDataApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_for_cities**](GeoDataApi.md#search_for_cities) | **GET** /reference-data/geo/city/search | Find Geo Name by Term
[**search_for_city**](GeoDataApi.md#search_for_city) | **GET** /reference-data/geo-ip/city/{searchTerm} | City Search
[**show_continents**](GeoDataApi.md#show_continents) | **GET** /reference-data/geo-ip/continent/list | Show All Continents
[**show_countries**](GeoDataApi.md#show_countries) | **GET** /reference-data/geo-ip/country/list | Show Geo Name Countries
[**show_geo_name_by_id**](GeoDataApi.md#show_geo_name_by_id) | **GET** /reference-data/geo/{geoNameId} | Find Geo Name by Id
[**show_timezones**](GeoDataApi.md#show_timezones) | **GET** /reference-data/geo-ip/timezone/list | Show Time Zones


# **search_for_cities**
> List[GeoNameLightweightNonAuthenticatedEntity] search_for_cities(term, wink_version=wink_version, accept=accept)

Find Geo Name by Term

Finds a list of geo-name entities for a term that `sounds like`.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.geo_name_lightweight_non_authenticated_entity import GeoNameLightweightNonAuthenticatedEntity
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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    term = 'Denpasar' # str | Geo-name term to be searched
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Find Geo Name by Term
        api_response = api_instance.search_for_cities(term, wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->search_for_cities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->search_for_cities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Geo-name term to be searched | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[GeoNameLightweightNonAuthenticatedEntity]**](GeoNameLightweightNonAuthenticatedEntity.md)

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

# **search_for_city**
> List[GeoIpLightweightNonAuthenticatedEntity] search_for_city(search_term, wink_version=wink_version, accept=accept)

City Search

Searches for city matching search term.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.geo_ip_lightweight_non_authenticated_entity import GeoIpLightweightNonAuthenticatedEntity
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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    search_term = 'Los Ang' # str | Search for city by search term
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # City Search
        api_response = api_instance.search_for_city(search_term, wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->search_for_city:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->search_for_city: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Search for city by search term | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[GeoIpLightweightNonAuthenticatedEntity]**](GeoIpLightweightNonAuthenticatedEntity.md)

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

# **show_continents**
> List[KeyValuePairNonAuthenticatedEntity] show_continents(wink_version=wink_version, accept=accept)

Show All Continents

List all continents.

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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show All Continents
        api_response = api_instance.show_continents(wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->show_continents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->show_continents: %s\n" % e)
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

# **show_countries**
> List[GeoNameCountryNonAuthenticatedEntity] show_countries(wink_version=wink_version, accept=accept)

Show Geo Name Countries

List all countries.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.geo_name_country_non_authenticated_entity import GeoNameCountryNonAuthenticatedEntity
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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Geo Name Countries
        api_response = api_instance.show_countries(wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->show_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->show_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[GeoNameCountryNonAuthenticatedEntity]**](GeoNameCountryNonAuthenticatedEntity.md)

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

# **show_geo_name_by_id**
> GeoNameLightweightNonAuthenticatedEntity show_geo_name_by_id(geo_name_id, wink_version=wink_version, accept=accept)

Find Geo Name by Id

Finds geo-name by given identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_reference
from wink_sdk_reference.models.geo_name_lightweight_non_authenticated_entity import GeoNameLightweightNonAuthenticatedEntity
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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    geo_name_id = '875430' # str | Geo-name identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Find Geo Name by Id
        api_response = api_instance.show_geo_name_by_id(geo_name_id, wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->show_geo_name_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->show_geo_name_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geo_name_id** | **str**| Geo-name identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**GeoNameLightweightNonAuthenticatedEntity**](GeoNameLightweightNonAuthenticatedEntity.md)

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

# **show_timezones**
> List[str] show_timezones(wink_version=wink_version, accept=accept)

Show Time Zones

List all time zones.

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
    api_instance = wink_sdk_reference.GeoDataApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Time Zones
        api_response = api_instance.show_timezones(wink_version=wink_version, accept=accept)
        print("The response of GeoDataApi->show_timezones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoDataApi->show_timezones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

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

