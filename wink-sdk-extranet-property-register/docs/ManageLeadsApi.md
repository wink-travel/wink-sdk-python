# wink_sdk_extranet_property_register.ManageLeadsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lead**](ManageLeadsApi.md#create_lead) | **POST** /api/lead | Create Lead
[**remove_lead**](ManageLeadsApi.md#remove_lead) | **DELETE** /api/lead/{leadIdentifier} | Delete Lead
[**show_lead**](ManageLeadsApi.md#show_lead) | **GET** /api/lead/{leadIdentifier} | Show Lead
[**show_lead_count**](ManageLeadsApi.md#show_lead_count) | **GET** /api/lead/count | Count Leads
[**show_lead_list**](ManageLeadsApi.md#show_lead_list) | **GET** /api/lead/list | Show Lead List


# **create_lead**
> SupplierLeadSupplier create_lead(google_place_detail_request_supplier, wink_version=wink_version)

Create Lead

Creates a new lead based on information retrieved from Google Places

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.google_place_detail_request_supplier import GooglePlaceDetailRequestSupplier
from wink_sdk_extranet_property_register.models.supplier_lead_supplier import SupplierLeadSupplier
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
    api_instance = wink_sdk_extranet_property_register.ManageLeadsApi(api_client)
    google_place_detail_request_supplier = wink_sdk_extranet_property_register.GooglePlaceDetailRequestSupplier() # GooglePlaceDetailRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Lead
        api_response = api_instance.create_lead(google_place_detail_request_supplier, wink_version=wink_version)
        print("The response of ManageLeadsApi->create_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLeadsApi->create_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_place_detail_request_supplier** | [**GooglePlaceDetailRequestSupplier**](GooglePlaceDetailRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SupplierLeadSupplier**](SupplierLeadSupplier.md)

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

# **remove_lead**
> SupplierLeadSupplier remove_lead(lead_identifier, wink_version=wink_version, accept=accept)

Delete Lead

Remove a lead

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.supplier_lead_supplier import SupplierLeadSupplier
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
    api_instance = wink_sdk_extranet_property_register.ManageLeadsApi(api_client)
    lead_identifier = 'lead-1' # str | Remove lead record with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Lead
        api_response = api_instance.remove_lead(lead_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManageLeadsApi->remove_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLeadsApi->remove_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_identifier** | **str**| Remove lead record with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SupplierLeadSupplier**](SupplierLeadSupplier.md)

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

# **show_lead**
> SupplierLeadSupplier show_lead(lead_identifier, wink_version=wink_version, accept=accept)

Show Lead

Retrieves a lead record with the specified ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.supplier_lead_supplier import SupplierLeadSupplier
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
    api_instance = wink_sdk_extranet_property_register.ManageLeadsApi(api_client)
    lead_identifier = 'lead-1' # str | Lead identifier to retrieve a record for.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Lead
        api_response = api_instance.show_lead(lead_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManageLeadsApi->show_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLeadsApi->show_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_identifier** | **str**| Lead identifier to retrieve a record for. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SupplierLeadSupplier**](SupplierLeadSupplier.md)

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

# **show_lead_count**
> CountResponseSupplier show_lead_count(wink_version=wink_version, accept=accept)

Count Leads

Retrieves a count of leads you've created.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.count_response_supplier import CountResponseSupplier
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
    api_instance = wink_sdk_extranet_property_register.ManageLeadsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Count Leads
        api_response = api_instance.show_lead_count(wink_version=wink_version, accept=accept)
        print("The response of ManageLeadsApi->show_lead_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLeadsApi->show_lead_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponseSupplier**](CountResponseSupplier.md)

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

# **show_lead_list**
> List[SupplierLeadSupplier] show_lead_list(wink_version=wink_version, accept=accept)

Show Lead List

Retrieves a list of leads you've created.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property_register
from wink_sdk_extranet_property_register.models.supplier_lead_supplier import SupplierLeadSupplier
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
    api_instance = wink_sdk_extranet_property_register.ManageLeadsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Lead List
        api_response = api_instance.show_lead_list(wink_version=wink_version, accept=accept)
        print("The response of ManageLeadsApi->show_lead_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLeadsApi->show_lead_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SupplierLeadSupplier]**](SupplierLeadSupplier.md)

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

