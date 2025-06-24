# wink_sdk_extranet_monetize.PromotionBundleApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate_modifier_bundle**](PromotionBundleApi.md#create_rate_modifier_bundle) | **POST** /api/property/{propertyIdentifier}/promotion-bundle | Create Promotion Bundle
[**remove_rate_modifier_bundle**](PromotionBundleApi.md#remove_rate_modifier_bundle) | **DELETE** /api/property/{propertyIdentifier}/promotion-bundle/{rateModifierBundleIdentifier} | Delete Promotion Bundle
[**show_rate_modifier_bundle**](PromotionBundleApi.md#show_rate_modifier_bundle) | **GET** /api/property/{propertyIdentifier}/promotion-bundle/{rateModifierBundleIdentifier} | Show Promotion Bundle
[**show_rate_modifier_bundles**](PromotionBundleApi.md#show_rate_modifier_bundles) | **GET** /api/property/{propertyIdentifier}/promotion-bundle/list | Show Promotion Bundles
[**update_rate_modifier_bundle**](PromotionBundleApi.md#update_rate_modifier_bundle) | **PUT** /api/property/{propertyIdentifier}/promotion-bundle/{rateModifierBundleIdentifier} | Update Promotion Bundle


# **create_rate_modifier_bundle**
> SpecialRateBundleSupplier create_rate_modifier_bundle(property_identifier, upsert_special_rate_bundle_request_supplier, wink_version=wink_version)

Create Promotion Bundle

Create a new rate modifier ancillary

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier
from wink_sdk_extranet_monetize.models.upsert_special_rate_bundle_request_supplier import UpsertSpecialRateBundleRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionBundleApi(api_client)
    property_identifier = 'hotel-1' # str | Create new promotion bundle and associate with this property identifier.
    upsert_special_rate_bundle_request_supplier = wink_sdk_extranet_monetize.UpsertSpecialRateBundleRequestSupplier() # UpsertSpecialRateBundleRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Promotion Bundle
        api_response = api_instance.create_rate_modifier_bundle(property_identifier, upsert_special_rate_bundle_request_supplier, wink_version=wink_version)
        print("The response of PromotionBundleApi->create_rate_modifier_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionBundleApi->create_rate_modifier_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create new promotion bundle and associate with this property identifier. | 
 **upsert_special_rate_bundle_request_supplier** | [**UpsertSpecialRateBundleRequestSupplier**](UpsertSpecialRateBundleRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SpecialRateBundleSupplier**](SpecialRateBundleSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rate_modifier_bundle**
> SpecialRateBundleSupplier remove_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)

Delete Promotion Bundle

Delete a rate modifier ancillary by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionBundleApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a promotion bundle owned by this property identifier.
    rate_modifier_bundle_identifier = 'promotion-bundle-1' # str | Remove a promotion bundle with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Promotion Bundle
        api_response = api_instance.remove_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionBundleApi->remove_rate_modifier_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionBundleApi->remove_rate_modifier_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a promotion bundle owned by this property identifier. | 
 **rate_modifier_bundle_identifier** | **str**| Remove a promotion bundle with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SpecialRateBundleSupplier**](SpecialRateBundleSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_rate_modifier_bundle**
> SpecialRateBundleSupplier show_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)

Show Promotion Bundle

Retrieve a rate modifier ancillary by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionBundleApi(api_client)
    property_identifier = 'hotel-1' # str | Show single promotion bundle owned by this property identifier.
    rate_modifier_bundle_identifier = 'promotion-bundle-1' # str | Show single promotion bundle with this identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Promotion Bundle
        api_response = api_instance.show_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionBundleApi->show_rate_modifier_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionBundleApi->show_rate_modifier_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single promotion bundle owned by this property identifier. | 
 **rate_modifier_bundle_identifier** | **str**| Show single promotion bundle with this identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SpecialRateBundleSupplier**](SpecialRateBundleSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_rate_modifier_bundles**
> List[SpecialRateBundleSupplier] show_rate_modifier_bundles(property_identifier, wink_version=wink_version, accept=accept)

Show Promotion Bundles

Retrieve list of rate modifier bundles

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionBundleApi(api_client)
    property_identifier = 'hotel-1' # str | Show all promotion bundles owned by this property identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Promotion Bundles
        api_response = api_instance.show_rate_modifier_bundles(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionBundleApi->show_rate_modifier_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionBundleApi->show_rate_modifier_bundles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all promotion bundles owned by this property identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SpecialRateBundleSupplier]**](SpecialRateBundleSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rate_modifier_bundle**
> SpecialRateBundleSupplier update_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, upsert_special_rate_bundle_request_supplier, wink_version=wink_version)

Update Promotion Bundle

Update a rate modifier ancillary by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier
from wink_sdk_extranet_monetize.models.upsert_special_rate_bundle_request_supplier import UpsertSpecialRateBundleRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionBundleApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing promotion bundle owned by this property identifier.
    rate_modifier_bundle_identifier = 'promotion-bundle-1' # str | Update existing promotion bundle with this identifier.
    upsert_special_rate_bundle_request_supplier = wink_sdk_extranet_monetize.UpsertSpecialRateBundleRequestSupplier() # UpsertSpecialRateBundleRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Promotion Bundle
        api_response = api_instance.update_rate_modifier_bundle(property_identifier, rate_modifier_bundle_identifier, upsert_special_rate_bundle_request_supplier, wink_version=wink_version)
        print("The response of PromotionBundleApi->update_rate_modifier_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionBundleApi->update_rate_modifier_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing promotion bundle owned by this property identifier. | 
 **rate_modifier_bundle_identifier** | **str**| Update existing promotion bundle with this identifier. | 
 **upsert_special_rate_bundle_request_supplier** | [**UpsertSpecialRateBundleRequestSupplier**](UpsertSpecialRateBundleRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SpecialRateBundleSupplier**](SpecialRateBundleSupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

