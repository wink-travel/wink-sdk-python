# wink_sdk_affiliate_inventory.CustomizationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customization**](CustomizationApi.md#create_customization) | **POST** /api/affiliate/{companyIdentifier}/configuration | Create Customization
[**remove_customization**](CustomizationApi.md#remove_customization) | **DELETE** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Remove Customization
[**show_application_configuration**](CustomizationApi.md#show_application_configuration) | **GET** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Show Customization
[**show_application_configurations_by_owner**](CustomizationApi.md#show_application_configurations_by_owner) | **GET** /api/affiliate/{companyIdentifier}/configuration/list | Show Customizations
[**show_primary_application_configuration**](CustomizationApi.md#show_primary_application_configuration) | **GET** /api/affiliate/{companyIdentifier}/configuration | Show Primary Customization
[**update_customization**](CustomizationApi.md#update_customization) | **PUT** /api/affiliate/{companyIdentifier}/configuration/{engineConfigurationIdentifier} | Update Customization


# **create_customization**
> EngineConfigurationViewAffiliate create_customization(company_identifier, upsert_engine_configuration_request_affiliate, wink_version=wink_version)

Create Customization

Create a new customization and associate it with the specified application.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_engine_configuration_request_affiliate import UpsertEngineConfigurationRequestAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Create customization for this company
    upsert_engine_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertEngineConfigurationRequestAffiliate() # UpsertEngineConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Customization
        api_response = api_instance.create_customization(company_identifier, upsert_engine_configuration_request_affiliate, wink_version=wink_version)
        print("The response of CustomizationApi->create_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->create_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Create customization for this company | 
 **upsert_engine_configuration_request_affiliate** | [**UpsertEngineConfigurationRequestAffiliate**](UpsertEngineConfigurationRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**EngineConfigurationViewAffiliate**](EngineConfigurationViewAffiliate.md)

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

# **remove_customization**
> EngineConfigurationViewAffiliate remove_customization(company_identifier, engine_configuration_identifier, wink_version=wink_version, accept=accept)

Remove Customization

Remove an existing customization.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Remove customization for this company
    engine_configuration_identifier = 'customization-1' # str | Remove customization with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Customization
        api_response = api_instance.remove_customization(company_identifier, engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of CustomizationApi->remove_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->remove_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove customization for this company | 
 **engine_configuration_identifier** | **str**| Remove customization with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineConfigurationViewAffiliate**](EngineConfigurationViewAffiliate.md)

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

# **show_application_configuration**
> EngineConfigurationViewAffiliate show_application_configuration(company_identifier, engine_configuration_identifier, wink_version=wink_version, accept=accept)

Show Customization

Retrieve the primary customization for an application.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Show customization for this company
    engine_configuration_identifier = 'customization-1' # str | Load customization with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Customization
        api_response = api_instance.show_application_configuration(company_identifier, engine_configuration_identifier, wink_version=wink_version, accept=accept)
        print("The response of CustomizationApi->show_application_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->show_application_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show customization for this company | 
 **engine_configuration_identifier** | **str**| Load customization with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineConfigurationViewAffiliate**](EngineConfigurationViewAffiliate.md)

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

# **show_application_configurations_by_owner**
> List[EngineConfigurationViewAffiliate] show_application_configurations_by_owner(company_identifier, wink_version=wink_version, accept=accept)

Show Customizations

Retrieve a list of customizations for specified company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Show customizations for this company
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Customizations
        api_response = api_instance.show_application_configurations_by_owner(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of CustomizationApi->show_application_configurations_by_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->show_application_configurations_by_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show customizations for this company | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[EngineConfigurationViewAffiliate]**](EngineConfigurationViewAffiliate.md)

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

# **show_primary_application_configuration**
> EngineConfigurationViewAffiliate show_primary_application_configuration(company_identifier, wink_version=wink_version, accept=accept)

Show Primary Customization

Retrieve the primary customization for an application.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Show customization for this company
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Primary Customization
        api_response = api_instance.show_primary_application_configuration(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of CustomizationApi->show_primary_application_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->show_primary_application_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show customization for this company | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**EngineConfigurationViewAffiliate**](EngineConfigurationViewAffiliate.md)

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

# **update_customization**
> EngineConfigurationViewAffiliate update_customization(company_identifier, engine_configuration_identifier, upsert_engine_configuration_request_affiliate, wink_version=wink_version)

Update Customization

Update an existing customization.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_inventory
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.upsert_engine_configuration_request_affiliate import UpsertEngineConfigurationRequestAffiliate
from wink_sdk_affiliate_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_inventory.CustomizationApi(api_client)
    company_identifier = 'company-1' # str | Update customization for this company
    engine_configuration_identifier = 'customization-1' # str | Update customization with this application
    upsert_engine_configuration_request_affiliate = wink_sdk_affiliate_inventory.UpsertEngineConfigurationRequestAffiliate() # UpsertEngineConfigurationRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Customization
        api_response = api_instance.update_customization(company_identifier, engine_configuration_identifier, upsert_engine_configuration_request_affiliate, wink_version=wink_version)
        print("The response of CustomizationApi->update_customization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomizationApi->update_customization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update customization for this company | 
 **engine_configuration_identifier** | **str**| Update customization with this application | 
 **upsert_engine_configuration_request_affiliate** | [**UpsertEngineConfigurationRequestAffiliate**](UpsertEngineConfigurationRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**EngineConfigurationViewAffiliate**](EngineConfigurationViewAffiliate.md)

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

