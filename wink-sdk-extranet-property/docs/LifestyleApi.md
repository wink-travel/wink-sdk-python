# wink_sdk_extranet_property.LifestyleApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_lifestyles**](LifestyleApi.md#show_lifestyles) | **GET** /api/property/{propertyIdentifier}/lifestyles | Show Lifestyles
[**update_lifestyles**](LifestyleApi.md#update_lifestyles) | **PUT** /api/property/{propertyIdentifier}/lifestyles | Update Lifestyles


# **show_lifestyles**
> LifestylesResponseSupplier show_lifestyles(property_identifier, wink_version=wink_version, accept=accept)

Show Lifestyles

Retrieve list of property lifestyles

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.lifestyles_response_supplier import LifestylesResponseSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.LifestyleApi(api_client)
    property_identifier = 'hotel-1' # str | Show Lifestyles for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Lifestyles
        api_response = api_instance.show_lifestyles(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of LifestyleApi->show_lifestyles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifestyleApi->show_lifestyles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show Lifestyles for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**LifestylesResponseSupplier**](LifestylesResponseSupplier.md)

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

# **update_lifestyles**
> PropertySupplier update_lifestyles(property_identifier, update_lifestyles_request_supplier, wink_version=wink_version)

Update Lifestyles

Update selected lifestyles. See [Lifestyle geoname data](#operation/showLifestyles) for supported lifestyles.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.update_lifestyles_request_supplier import UpdateLifestylesRequestSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.LifestyleApi(api_client)
    property_identifier = 'hotel-1' # str | Update lifestyles for this property identifier
    update_lifestyles_request_supplier = wink_sdk_extranet_property.UpdateLifestylesRequestSupplier() # UpdateLifestylesRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Lifestyles
        api_response = api_instance.update_lifestyles(property_identifier, update_lifestyles_request_supplier, wink_version=wink_version)
        print("The response of LifestyleApi->update_lifestyles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifestyleApi->update_lifestyles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update lifestyles for this property identifier | 
 **update_lifestyles_request_supplier** | [**UpdateLifestylesRequestSupplier**](UpdateLifestylesRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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

