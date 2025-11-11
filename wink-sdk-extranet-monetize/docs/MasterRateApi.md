# wink_sdk_extranet_monetize.MasterRateApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_perks**](MasterRateApi.md#set_perks) | **PATCH** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/perks | Set Master Rate Perks
[**show_master_rate**](MasterRateApi.md#show_master_rate) | **GET** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier} | Show Master Rate
[**show_master_rates1**](MasterRateApi.md#show_master_rates1) | **GET** /api/property/{propertyIdentifier}/master-rate/list | Show Master Rates
[**toggle_master_rate**](MasterRateApi.md#toggle_master_rate) | **PATCH** /api/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}/toggle | Toggle Master Rate


# **set_perks**
> MasterRateSupplier set_perks(property_identifier, master_rate_identifier, set_master_rate_perk_request_supplier, wink_version=wink_version)

Set Master Rate Perks

Manage perks for this master rate.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.master_rate_supplier import MasterRateSupplier
from wink_sdk_extranet_monetize.models.set_master_rate_perk_request_supplier import SetMasterRatePerkRequestSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.MasterRateApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing master rate owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Update existing master rate with this identifier.
    set_master_rate_perk_request_supplier = wink_sdk_extranet_monetize.SetMasterRatePerkRequestSupplier() # SetMasterRatePerkRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Set Master Rate Perks
        api_response = api_instance.set_perks(property_identifier, master_rate_identifier, set_master_rate_perk_request_supplier, wink_version=wink_version)
        print("The response of MasterRateApi->set_perks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterRateApi->set_perks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing master rate owned by this property identifier. | 
 **master_rate_identifier** | **str**| Update existing master rate with this identifier. | 
 **set_master_rate_perk_request_supplier** | [**SetMasterRatePerkRequestSupplier**](SetMasterRatePerkRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**MasterRateSupplier**](MasterRateSupplier.md)

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

# **show_master_rate**
> MasterRateSupplier show_master_rate(property_identifier, master_rate_identifier, wink_version=wink_version, accept=accept)

Show Master Rate

Retrieve a master rate by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.master_rate_supplier import MasterRateSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.MasterRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show single master rate owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Show single master rate with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Master Rate
        api_response = api_instance.show_master_rate(property_identifier, master_rate_identifier, wink_version=wink_version, accept=accept)
        print("The response of MasterRateApi->show_master_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterRateApi->show_master_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single master rate owned by this property identifier. | 
 **master_rate_identifier** | **str**| Show single master rate with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**MasterRateSupplier**](MasterRateSupplier.md)

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

# **show_master_rates1**
> List[MasterRateSupplier] show_master_rates1(property_identifier, wink_version=wink_version, accept=accept)

Show Master Rates

Retrieve list of master rates

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.master_rate_supplier import MasterRateSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.MasterRateApi(api_client)
    property_identifier = 'hotel-1' # str | Show all master rates owned by this property identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Master Rates
        api_response = api_instance.show_master_rates1(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of MasterRateApi->show_master_rates1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterRateApi->show_master_rates1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all master rates owned by this property identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[MasterRateSupplier]**](MasterRateSupplier.md)

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

# **toggle_master_rate**
> MasterRateSupplier toggle_master_rate(property_identifier, master_rate_identifier, toggle_master_rate_request_supplier, wink_version=wink_version)

Toggle Master Rate

Update a master rate by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.master_rate_supplier import MasterRateSupplier
from wink_sdk_extranet_monetize.models.toggle_master_rate_request_supplier import ToggleMasterRateRequestSupplier
from wink_sdk_extranet_monetize.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_monetize.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_monetize.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_monetize.MasterRateApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing master rate owned by this property identifier.
    master_rate_identifier = 'master-rate-1' # str | Update existing master rate with this identifier.
    toggle_master_rate_request_supplier = wink_sdk_extranet_monetize.ToggleMasterRateRequestSupplier() # ToggleMasterRateRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Toggle Master Rate
        api_response = api_instance.toggle_master_rate(property_identifier, master_rate_identifier, toggle_master_rate_request_supplier, wink_version=wink_version)
        print("The response of MasterRateApi->toggle_master_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MasterRateApi->toggle_master_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing master rate owned by this property identifier. | 
 **master_rate_identifier** | **str**| Update existing master rate with this identifier. | 
 **toggle_master_rate_request_supplier** | [**ToggleMasterRateRequestSupplier**](ToggleMasterRateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**MasterRateSupplier**](MasterRateSupplier.md)

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

