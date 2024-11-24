# wink_sdk_extranet_property.PolicyApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PolicyApi.md#create_policy) | **POST** /api/property/{propertyIdentifier}/policy/property | Create property policy
[**show_property_policy**](PolicyApi.md#show_property_policy) | **GET** /api/property/{propertyIdentifier}/policy/property | Show property policy
[**update_property_policy**](PolicyApi.md#update_property_policy) | **PUT** /api/property/{propertyIdentifier}/policy/property | Update property policy


# **create_policy**
> HotelViewSupplier create_policy(property_identifier, property_policy_supplier, wink_version=wink_version)

Create property policy

Creates the initial property policy record for the hotel.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.hotel_view_supplier import HotelViewSupplier
from wink_sdk_extranet_property.models.property_policy_supplier import PropertyPolicySupplier
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
    api_instance = wink_sdk_extranet_property.PolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Create property policy for this property identifier
    property_policy_supplier = wink_sdk_extranet_property.PropertyPolicySupplier() # PropertyPolicySupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create property policy
        api_response = api_instance.create_policy(property_identifier, property_policy_supplier, wink_version=wink_version)
        print("The response of PolicyApi->create_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create property policy for this property identifier | 
 **property_policy_supplier** | [**PropertyPolicySupplier**](PropertyPolicySupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**HotelViewSupplier**](HotelViewSupplier.md)

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

# **show_property_policy**
> PropertyPolicySupplier show_property_policy(property_identifier, wink_version=wink_version, accept=accept)

Show property policy

Returns property policy for hotel

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_policy_supplier import PropertyPolicySupplier
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
    api_instance = wink_sdk_extranet_property.PolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Retrieve property policy for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show property policy
        api_response = api_instance.show_property_policy(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PolicyApi->show_property_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->show_property_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Retrieve property policy for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PropertyPolicySupplier**](PropertyPolicySupplier.md)

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

# **update_property_policy**
> HotelViewSupplier update_property_policy(property_identifier, property_policy_supplier, wink_version=wink_version)

Update property policy

Update property policy record for the hotel.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.hotel_view_supplier import HotelViewSupplier
from wink_sdk_extranet_property.models.property_policy_supplier import PropertyPolicySupplier
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
    api_instance = wink_sdk_extranet_property.PolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Update property policy record for this property identifier
    property_policy_supplier = wink_sdk_extranet_property.PropertyPolicySupplier() # PropertyPolicySupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update property policy
        api_response = api_instance.update_property_policy(property_identifier, property_policy_supplier, wink_version=wink_version)
        print("The response of PolicyApi->update_property_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->update_property_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update property policy record for this property identifier | 
 **property_policy_supplier** | [**PropertyPolicySupplier**](PropertyPolicySupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**HotelViewSupplier**](HotelViewSupplier.md)

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

