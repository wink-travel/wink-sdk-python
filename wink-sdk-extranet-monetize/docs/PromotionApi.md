# wink_sdk_extranet_monetize.PromotionApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_promotion**](PromotionApi.md#create_promotion) | **POST** /api/property/{propertyIdentifier}/promotion | Create Promotion
[**remove_rate_modifier**](PromotionApi.md#remove_rate_modifier) | **DELETE** /api/property/{propertyIdentifier}/promotion/{rateModifierIdentifier} | Delete Promotion
[**show_promotion**](PromotionApi.md#show_promotion) | **GET** /api/property/{propertyIdentifier}/promotion/{rateModifierIdentifier} | Show Promotion
[**show_promotions**](PromotionApi.md#show_promotions) | **GET** /api/property/{propertyIdentifier}/promotion/list | Show Promotions
[**update_promotion**](PromotionApi.md#update_promotion) | **PUT** /api/property/{propertyIdentifier}/promotion/{rateModifierIdentifier} | Update Promotion


# **create_promotion**
> SpecialRateSupplier create_promotion(property_identifier, upsert_special_rate_request_supplier, wink_version=wink_version)

Create Promotion

Create a new promotion

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_supplier import SpecialRateSupplier
from wink_sdk_extranet_monetize.models.upsert_special_rate_request_supplier import UpsertSpecialRateRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionApi(api_client)
    property_identifier = 'hotel-1' # str | Create new promotion and associate with this property identifier.
    upsert_special_rate_request_supplier = wink_sdk_extranet_monetize.UpsertSpecialRateRequestSupplier() # UpsertSpecialRateRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Promotion
        api_response = api_instance.create_promotion(property_identifier, upsert_special_rate_request_supplier, wink_version=wink_version)
        print("The response of PromotionApi->create_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionApi->create_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create new promotion and associate with this property identifier. | 
 **upsert_special_rate_request_supplier** | [**UpsertSpecialRateRequestSupplier**](UpsertSpecialRateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SpecialRateSupplier**](SpecialRateSupplier.md)

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

# **remove_rate_modifier**
> SpecialRateSupplier remove_rate_modifier(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)

Delete Promotion

Delete a promotion by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_supplier import SpecialRateSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionApi(api_client)
    property_identifier = 'hotel-1' # str | Remove a promotion owned by this property identifier.
    rate_modifier_identifier = 'promotion-1' # str | Remove a promotion with this identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Promotion
        api_response = api_instance.remove_rate_modifier(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionApi->remove_rate_modifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionApi->remove_rate_modifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove a promotion owned by this property identifier. | 
 **rate_modifier_identifier** | **str**| Remove a promotion with this identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SpecialRateSupplier**](SpecialRateSupplier.md)

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

# **show_promotion**
> SpecialRateSupplier show_promotion(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)

Show Promotion

Retrieve a rate modifier by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_supplier import SpecialRateSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionApi(api_client)
    property_identifier = 'hotel-1' # str | Show single promotion owned by this property identifier.
    rate_modifier_identifier = 'promotion-1' # str | Show single promotion with this identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Promotion
        api_response = api_instance.show_promotion(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionApi->show_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionApi->show_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show single promotion owned by this property identifier. | 
 **rate_modifier_identifier** | **str**| Show single promotion with this identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SpecialRateSupplier**](SpecialRateSupplier.md)

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

# **show_promotions**
> List[SpecialRateSupplier] show_promotions(property_identifier, wink_version=wink_version, accept=accept)

Show Promotions

Retrieve list of promotions for property

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_supplier import SpecialRateSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionApi(api_client)
    property_identifier = 'hotel-1' # str | Show all promotions owned by this property identifier.
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Promotions
        api_response = api_instance.show_promotions(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of PromotionApi->show_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionApi->show_promotions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all promotions owned by this property identifier. | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[SpecialRateSupplier]**](SpecialRateSupplier.md)

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

# **update_promotion**
> SpecialRateSupplier update_promotion(property_identifier, rate_modifier_identifier, upsert_special_rate_request_supplier, wink_version=wink_version)

Update Promotion

Update an existing promotion by its identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_monetize
from wink_sdk_extranet_monetize.models.special_rate_supplier import SpecialRateSupplier
from wink_sdk_extranet_monetize.models.upsert_special_rate_request_supplier import UpsertSpecialRateRequestSupplier
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
    api_instance = wink_sdk_extranet_monetize.PromotionApi(api_client)
    property_identifier = 'hotel-1' # str | Update existing promotion owned by this property identifier.
    rate_modifier_identifier = 'promotion-1' # str | Update existing promotion with this identifier.
    upsert_special_rate_request_supplier = wink_sdk_extranet_monetize.UpsertSpecialRateRequestSupplier() # UpsertSpecialRateRequestSupplier | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Promotion
        api_response = api_instance.update_promotion(property_identifier, rate_modifier_identifier, upsert_special_rate_request_supplier, wink_version=wink_version)
        print("The response of PromotionApi->update_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionApi->update_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update existing promotion owned by this property identifier. | 
 **rate_modifier_identifier** | **str**| Update existing promotion with this identifier. | 
 **upsert_special_rate_request_supplier** | [**UpsertSpecialRateRequestSupplier**](UpsertSpecialRateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SpecialRateSupplier**](SpecialRateSupplier.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

