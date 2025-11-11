# wink_sdk_extranet_monetize.CancellationPolicyApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cancellation_policy**](CancellationPolicyApi.md#create_cancellation_policy) | **POST** /api/property/{propertyIdentifier}/cancellation-policy | Create Cancellation Policy
[**is_cancellation_policy_removable**](CancellationPolicyApi.md#is_cancellation_policy_removable) | **GET** /api/property/{propertyIdentifier}/cancellation-policy/{cancellationPolicyIdentifier}/removable | Verify Removable
[**remove_cancellation_policy**](CancellationPolicyApi.md#remove_cancellation_policy) | **DELETE** /api/property/{propertyIdentifier}/cancellation-policy/{cancellationPolicyIdentifier} | Delete Cancellation Policy
[**show_cancellation_policy**](CancellationPolicyApi.md#show_cancellation_policy) | **GET** /api/property/{propertyIdentifier}/cancellation-policy/{cancellationPolicyIdentifier} | Show Cancellation Policy
[**show_cancellation_policy_list**](CancellationPolicyApi.md#show_cancellation_policy_list) | **GET** /api/property/{propertyIdentifier}/cancellation-policy/list | Show Cancellation Policies
[**update_cancellation_policy**](CancellationPolicyApi.md#update_cancellation_policy) | **PUT** /api/property/{propertyIdentifier}/cancellation-policy/{cancellationPolicyIdentifier} | Update Cancellation Policy


# **create_cancellation_policy**
> CancellationPolicySupplier create_cancellation_policy(property_identifier, upsert_cancellation_policy_request_supplier, wink_version=wink_version)

Create Cancellation Policy

Create a new cancellation policy

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_supplier import CancellationPolicySupplier
from wink_sdk_extranet_monetize.models.upsert_cancellation_policy_request_supplier import UpsertCancellationPolicyRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Create cancellation policy and associate it with by this property identifier.
    upsert_cancellation_policy_request_supplier = wink_sdk_extranet_monetize.UpsertCancellationPolicyRequestSupplier() # UpsertCancellationPolicyRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Cancellation Policy
        api_response = api_instance.create_cancellation_policy(property_identifier, upsert_cancellation_policy_request_supplier, wink_version=wink_version)
        print("The response of CancellationPolicyApi->create_cancellation_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->create_cancellation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create cancellation policy and associate it with by this property identifier. | 
 **upsert_cancellation_policy_request_supplier** | [**UpsertCancellationPolicyRequestSupplier**](UpsertCancellationPolicyRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CancellationPolicySupplier**](CancellationPolicySupplier.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_cancellation_policy_removable**
> CancellationPolicyRemovableResponseSupplier is_cancellation_policy_removable(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)

Verify Removable

Check if a cancellation policy is removable. If a cancellation policy is associated / linked with a rate plan, it cannot be removed until the associated entity removes it first.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_removable_response_supplier import CancellationPolicyRemovableResponseSupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Verify if cancellation policy is removable and owned by this property identifier.
    cancellation_policy_identifier = 'cancellation-policy-1' # str | Verify if cancellation policy is removable identified by this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Verify Removable
        api_response = api_instance.is_cancellation_policy_removable(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)
        print("The response of CancellationPolicyApi->is_cancellation_policy_removable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->is_cancellation_policy_removable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Verify if cancellation policy is removable and owned by this property identifier. | 
 **cancellation_policy_identifier** | **str**| Verify if cancellation policy is removable identified by this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CancellationPolicyRemovableResponseSupplier**](CancellationPolicyRemovableResponseSupplier.md)

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

# **remove_cancellation_policy**
> CancellationPolicySupplier remove_cancellation_policy(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)

Delete Cancellation Policy

Delete a cancellation policy by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_supplier import CancellationPolicySupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Delete cancellation policy owned by this property identifier.
    cancellation_policy_identifier = 'cancellation-policy-1' # str | Delete cancellation policy with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Cancellation Policy
        api_response = api_instance.remove_cancellation_policy(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)
        print("The response of CancellationPolicyApi->remove_cancellation_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->remove_cancellation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Delete cancellation policy owned by this property identifier. | 
 **cancellation_policy_identifier** | **str**| Delete cancellation policy with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CancellationPolicySupplier**](CancellationPolicySupplier.md)

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

# **show_cancellation_policy**
> CancellationPolicySupplier show_cancellation_policy(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)

Show Cancellation Policy

Retrieve a cancellation policy by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_supplier import CancellationPolicySupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Show single cancellation policy owned by this property identifier.
    cancellation_policy_identifier = 'cancellation-policy-1' # str | Show single cancellation policy with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Cancellation Policy
        api_response = api_instance.show_cancellation_policy(property_identifier, cancellation_policy_identifier, wink_version=wink_version, accept=accept)
        print("The response of CancellationPolicyApi->show_cancellation_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->show_cancellation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single cancellation policy owned by this property identifier. | 
 **cancellation_policy_identifier** | **str**| Show single cancellation policy with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CancellationPolicySupplier**](CancellationPolicySupplier.md)

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

# **show_cancellation_policy_list**
> List[CancellationPolicySupplier] show_cancellation_policy_list(property_identifier, wink_version=wink_version, accept=accept)

Show Cancellation Policies

Retrieve list of cancellation policies for property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_supplier import CancellationPolicySupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | List all cancellation policies for this property identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Cancellation Policies
        api_response = api_instance.show_cancellation_policy_list(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of CancellationPolicyApi->show_cancellation_policy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->show_cancellation_policy_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| List all cancellation policies for this property identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[CancellationPolicySupplier]**](CancellationPolicySupplier.md)

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

# **update_cancellation_policy**
> CancellationPolicySupplier update_cancellation_policy(property_identifier, cancellation_policy_identifier, upsert_cancellation_policy_request_supplier, wink_version=wink_version)

Update Cancellation Policy

Update a cancellation policy by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.cancellation_policy_supplier import CancellationPolicySupplier
from wink_sdk_extranet_monetize.models.upsert_cancellation_policy_request_supplier import UpsertCancellationPolicyRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.CancellationPolicyApi(api_client)
    property_identifier = 'hotel-1' # str | Update an existing cancellation policy owned by this property identifier.
    cancellation_policy_identifier = 'cancellation-policy-1' # str | Update an existing cancellation policy with this identifier.
    upsert_cancellation_policy_request_supplier = wink_sdk_extranet_monetize.UpsertCancellationPolicyRequestSupplier() # UpsertCancellationPolicyRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Cancellation Policy
        api_response = api_instance.update_cancellation_policy(property_identifier, cancellation_policy_identifier, upsert_cancellation_policy_request_supplier, wink_version=wink_version)
        print("The response of CancellationPolicyApi->update_cancellation_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancellationPolicyApi->update_cancellation_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update an existing cancellation policy owned by this property identifier. | 
 **cancellation_policy_identifier** | **str**| Update an existing cancellation policy with this identifier. | 
 **upsert_cancellation_policy_request_supplier** | [**UpsertCancellationPolicyRequestSupplier**](UpsertCancellationPolicyRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CancellationPolicySupplier**](CancellationPolicySupplier.md)

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

