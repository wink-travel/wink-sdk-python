# wink_sdk_extranet_property_register.RegistrationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_property_intelligently**](RegistrationApi.md#register_property_intelligently) | **POST** /api/property/register/intelligent/{leadIdentifier} | Intelligent
[**register_property_manually**](RegistrationApi.md#register_property_manually) | **POST** /api/property/register/manual | Manual


# **register_property_intelligently**
> PropertySupplier register_property_intelligently(lead_identifier, intelligent_property_registration_request_supplier, wink_version=wink_version)

Intelligent

Registers a new property with the minimum required dataset to onboard a property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.intelligent_property_registration_request_supplier import IntelligentPropertyRegistrationRequestSupplier
from wink_sdk_extranet_property_register.models.property_supplier import PropertySupplier
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
    api_instance = wink_sdk_extranet_property_register.RegistrationApi(api_client)
    lead_identifier = 'lead-123' # str | A lead (property that exists in Google and was added as a Lead on Wink) record is required to create a property this way.
    intelligent_property_registration_request_supplier = wink_sdk_extranet_property_register.IntelligentPropertyRegistrationRequestSupplier() # IntelligentPropertyRegistrationRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Intelligent
        api_response = api_instance.register_property_intelligently(lead_identifier, intelligent_property_registration_request_supplier, wink_version=wink_version)
        print("The response of RegistrationApi->register_property_intelligently:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationApi->register_property_intelligently: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_identifier** | **str**| A lead (property that exists in Google and was added as a Lead on Wink) record is required to create a property this way. | 
 **intelligent_property_registration_request_supplier** | [**IntelligentPropertyRegistrationRequestSupplier**](IntelligentPropertyRegistrationRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_property_manually**
> PropertySupplier register_property_manually(manual_property_registration_request_supplier, wink_version=wink_version)

Manual

Registers a new property with the minimum required dataset to onboard a property.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.manual_property_registration_request_supplier import ManualPropertyRegistrationRequestSupplier
from wink_sdk_extranet_property_register.models.property_supplier import PropertySupplier
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
    api_instance = wink_sdk_extranet_property_register.RegistrationApi(api_client)
    manual_property_registration_request_supplier = wink_sdk_extranet_property_register.ManualPropertyRegistrationRequestSupplier() # ManualPropertyRegistrationRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Manual
        api_response = api_instance.register_property_manually(manual_property_registration_request_supplier, wink_version=wink_version)
        print("The response of RegistrationApi->register_property_manually:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrationApi->register_property_manually: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_property_registration_request_supplier** | [**ManualPropertyRegistrationRequestSupplier**](ManualPropertyRegistrationRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

