# wink_sdk_extranet_property_register.PropertyRegistrationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_property_name_unique**](PropertyRegistrationApi.md#is_property_name_unique) | **GET** /api/property/name | Property Name Check
[**register_property_intelligently**](PropertyRegistrationApi.md#register_property_intelligently) | **POST** /api/property/register/intelligent/{leadIdentifier} | Register Property Intelligently
[**register_property_manually**](PropertyRegistrationApi.md#register_property_manually) | **POST** /api/property/register/manual | Register Property Manually


# **is_property_name_unique**
> UniqueResultSupplier is_property_name_unique(geo_name_id, name, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)

Property Name Check

Verifies that the property name is unique in relationship to a city.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.unique_result_supplier import UniqueResultSupplier
from wink_sdk_extranet_property_register.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property_register.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property_register.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property_register.PropertyRegistrationApi(api_client)
    geo_name_id = '12345678' # str | Search for uniqueness in relationship to a city.
    name = 'Blue Orchid' # str | Search for uniqueness for this hotel name.
    hotel_identifier = 'hotel-123' # str | Optional, existing hotel identifier (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Property Name Check
        api_response = api_instance.is_property_name_unique(geo_name_id, name, hotel_identifier=hotel_identifier, wink_version=wink_version, accept=accept)
        print("The response of PropertyRegistrationApi->is_property_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyRegistrationApi->is_property_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geo_name_id** | **str**| Search for uniqueness in relationship to a city. | 
 **name** | **str**| Search for uniqueness for this hotel name. | 
 **hotel_identifier** | **str**| Optional, existing hotel identifier | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**UniqueResultSupplier**](UniqueResultSupplier.md)

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

# **register_property_intelligently**
> HotelViewSupplier register_property_intelligently(lead_identifier, intelligent_property_registration_request_supplier, wink_version=wink_version)

Register Property Intelligently

Registers a new property with the minimum required dataset to onboard a property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.hotel_view_supplier import HotelViewSupplier
from wink_sdk_extranet_property_register.models.intelligent_property_registration_request_supplier import IntelligentPropertyRegistrationRequestSupplier
from wink_sdk_extranet_property_register.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property_register.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property_register.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property_register.PropertyRegistrationApi(api_client)
    lead_identifier = 'lead-123' # str | A lead (property that exists in Google and was added as a Lead on Wink) record is required to create a property this way.
    intelligent_property_registration_request_supplier = wink_sdk_extranet_property_register.IntelligentPropertyRegistrationRequestSupplier() # IntelligentPropertyRegistrationRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Register Property Intelligently
        api_response = api_instance.register_property_intelligently(lead_identifier, intelligent_property_registration_request_supplier, wink_version=wink_version)
        print("The response of PropertyRegistrationApi->register_property_intelligently:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyRegistrationApi->register_property_intelligently: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_identifier** | **str**| A lead (property that exists in Google and was added as a Lead on Wink) record is required to create a property this way. | 
 **intelligent_property_registration_request_supplier** | [**IntelligentPropertyRegistrationRequestSupplier**](IntelligentPropertyRegistrationRequestSupplier.md)|  | 
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

# **register_property_manually**
> HotelViewSupplier register_property_manually(manual_property_registration_request_supplier, wink_version=wink_version)

Register Property Manually

Registers a new property with the minimum required dataset to onboard a property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.hotel_view_supplier import HotelViewSupplier
from wink_sdk_extranet_property_register.models.manual_property_registration_request_supplier import ManualPropertyRegistrationRequestSupplier
from wink_sdk_extranet_property_register.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property_register.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property_register.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property_register.PropertyRegistrationApi(api_client)
    manual_property_registration_request_supplier = wink_sdk_extranet_property_register.ManualPropertyRegistrationRequestSupplier() # ManualPropertyRegistrationRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Register Property Manually
        api_response = api_instance.register_property_manually(manual_property_registration_request_supplier, wink_version=wink_version)
        print("The response of PropertyRegistrationApi->register_property_manually:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyRegistrationApi->register_property_manually: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_property_registration_request_supplier** | [**ManualPropertyRegistrationRequestSupplier**](ManualPropertyRegistrationRequestSupplier.md)|  | 
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

