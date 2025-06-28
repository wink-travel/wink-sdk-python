# wink_sdk_extranet_distribution.SalesChannelApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sales_channel**](SalesChannelApi.md#create_sales_channel) | **POST** /api/property/{propertyIdentifier}/sales/account | Create Sales Channel
[**remove_sales_channel**](SalesChannelApi.md#remove_sales_channel) | **DELETE** /api/property/{propertyIdentifier}/sales/account/{salesChannelIdentifier} | Remove Sales Channel
[**show_accounts**](SalesChannelApi.md#show_accounts) | **GET** /api/property/{propertyIdentifier}/sales/account/list | Show Sales Channels
[**show_sales_channel**](SalesChannelApi.md#show_sales_channel) | **GET** /api/property/{propertyIdentifier}/sales/account/{salesChannelIdentifier} | Show Sales Channel
[**show_sales_channel_context_rate_modifier_bundle_pairs**](SalesChannelApi.md#show_sales_channel_context_rate_modifier_bundle_pairs) | **GET** /api/property/{propertyIdentifier}/sales/account/rate-modifier-bundle/{rateModifierBundleIdentifier}/list | Show Rate Modifier Bundle Availability
[**show_sales_channel_context_rate_modifier_pairs**](SalesChannelApi.md#show_sales_channel_context_rate_modifier_pairs) | **GET** /api/property/{propertyIdentifier}/sales/account/rate-modifier/{rateModifierIdentifier}/list | Show Rate Modifier Availability
[**toggle_sales_channel_promo_availability**](SalesChannelApi.md#toggle_sales_channel_promo_availability) | **PATCH** /api/property/{propertyIdentifier}/sales/account/rate-modifier/{rateModifierIdentifier}/list | Update Sale Channels Rate Modifiers
[**toggle_sales_channel_promo_bundle_availability**](SalesChannelApi.md#toggle_sales_channel_promo_bundle_availability) | **PATCH** /api/property/{propertyIdentifier}/sales/account/rate-modifier-bundle/{rateModifierBundleIdentifier}/list | Update Sale Channels Rate Modifier Bundles
[**update_sales_channel**](SalesChannelApi.md#update_sales_channel) | **PATCH** /api/property/{propertyIdentifier}/sales/account/{salesChannelIdentifier} | Update Sales Channel


# **create_sales_channel**
> SalesChannelSupplier create_sales_channel(property_identifier, sales_channel_create_request_supplier, wink_version=wink_version)

Create Sales Channel

Create a new sales channel.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_create_request_supplier import SalesChannelCreateRequestSupplier
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Create sales channel and associate it with this property identifier
    sales_channel_create_request_supplier = wink_sdk_extranet_distribution.SalesChannelCreateRequestSupplier() # SalesChannelCreateRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Sales Channel
        api_response = api_instance.create_sales_channel(property_identifier, sales_channel_create_request_supplier, wink_version=wink_version)
        print("The response of SalesChannelApi->create_sales_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->create_sales_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create sales channel and associate it with this property identifier | 
 **sales_channel_create_request_supplier** | [**SalesChannelCreateRequestSupplier**](SalesChannelCreateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SalesChannelSupplier**](SalesChannelSupplier.md)

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

# **remove_sales_channel**
> SalesChannelSupplier remove_sales_channel(property_identifier, sales_channel_identifier, wink_version=wink_version, accept=accept)

Remove Sales Channel

Delete a specific sales channel

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Remove sales channel owned by this property identifier
    sales_channel_identifier = 'sales-channel-1' # str | Remove sales channel with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Sales Channel
        api_response = api_instance.remove_sales_channel(property_identifier, sales_channel_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->remove_sales_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->remove_sales_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove sales channel owned by this property identifier | 
 **sales_channel_identifier** | **str**| Remove sales channel with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelSupplier**](SalesChannelSupplier.md)

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

# **show_accounts**
> List[SalesChannelSupplier] show_accounts(property_identifier, wink_version=wink_version, accept=accept)

Show Sales Channels

Retrieve list of all sales channels for this property. You can decide to retrieve all specific sales channel relationships or only generic ones using the 'owner' request parameter.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Show all sales channels for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Sales Channels
        api_response = api_instance.show_accounts(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->show_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->show_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all sales channels for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SalesChannelSupplier]**](SalesChannelSupplier.md)

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

# **show_sales_channel**
> SalesChannelSupplier show_sales_channel(property_identifier, sales_channel_identifier, wink_version=wink_version, accept=accept)

Show Sales Channel

Retrieve a specific sales channel by identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Show sales channel owned by this property identifier
    sales_channel_identifier = 'sales channel-1' # str | Show sales channel with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Sales Channel
        api_response = api_instance.show_sales_channel(property_identifier, sales_channel_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->show_sales_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->show_sales_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show sales channel owned by this property identifier | 
 **sales_channel_identifier** | **str**| Show sales channel with this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelSupplier**](SalesChannelSupplier.md)

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

# **show_sales_channel_context_rate_modifier_bundle_pairs**
> List[SelectableKeyValuePairSupplier] show_sales_channel_context_rate_modifier_bundle_pairs(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)

Show Rate Modifier Bundle Availability

Display a list of key / value pairs that shows the availability of sales channels in the context of rate modifier bundles.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.selectable_key_value_pair_supplier import SelectableKeyValuePairSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Show all sales channel pairs for this property identifier
    rate_modifier_bundle_identifier = 'rate-modifier-bundle-1' # str | Show all sales channels pairs in the context of rate modifier bundle availability
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Rate Modifier Bundle Availability
        api_response = api_instance.show_sales_channel_context_rate_modifier_bundle_pairs(property_identifier, rate_modifier_bundle_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->show_sales_channel_context_rate_modifier_bundle_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->show_sales_channel_context_rate_modifier_bundle_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all sales channel pairs for this property identifier | 
 **rate_modifier_bundle_identifier** | **str**| Show all sales channels pairs in the context of rate modifier bundle availability | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SelectableKeyValuePairSupplier]**](SelectableKeyValuePairSupplier.md)

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

# **show_sales_channel_context_rate_modifier_pairs**
> List[SelectableKeyValuePairSupplier] show_sales_channel_context_rate_modifier_pairs(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)

Show Rate Modifier Availability

Display a list of key / value pairs that shows the availability of sales channels in the context of rate modifiers.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.selectable_key_value_pair_supplier import SelectableKeyValuePairSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Show all sales channel pairs for this property identifier
    rate_modifier_identifier = 'rate-modifier-1' # str | Show all sales channels pairs in the context of rate modifier availability
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Rate Modifier Availability
        api_response = api_instance.show_sales_channel_context_rate_modifier_pairs(property_identifier, rate_modifier_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelApi->show_sales_channel_context_rate_modifier_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->show_sales_channel_context_rate_modifier_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all sales channel pairs for this property identifier | 
 **rate_modifier_identifier** | **str**| Show all sales channels pairs in the context of rate modifier availability | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SelectableKeyValuePairSupplier]**](SelectableKeyValuePairSupplier.md)

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

# **toggle_sales_channel_promo_availability**
> List[SalesChannelSupplier] toggle_sales_channel_promo_availability(property_identifier, rate_modifier_identifier, inventory_update_request_supplier, wink_version=wink_version)

Update Sale Channels Rate Modifiers

Toggles availability of a promo for a list of sales channels

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Update sales channel owned by this property identifier
    rate_modifier_identifier = 'rate-modifier-1' # str | The rate modifier we are enabling / disabling on the sales channel
    inventory_update_request_supplier = [wink_sdk_extranet_distribution.InventoryUpdateRequestSupplier()] # List[InventoryUpdateRequestSupplier] | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Sale Channels Rate Modifiers
        api_response = api_instance.toggle_sales_channel_promo_availability(property_identifier, rate_modifier_identifier, inventory_update_request_supplier, wink_version=wink_version)
        print("The response of SalesChannelApi->toggle_sales_channel_promo_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->toggle_sales_channel_promo_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update sales channel owned by this property identifier | 
 **rate_modifier_identifier** | **str**| The rate modifier we are enabling / disabling on the sales channel | 
 **inventory_update_request_supplier** | [**List[InventoryUpdateRequestSupplier]**](InventoryUpdateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[SalesChannelSupplier]**](SalesChannelSupplier.md)

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

# **toggle_sales_channel_promo_bundle_availability**
> List[SalesChannelSupplier] toggle_sales_channel_promo_bundle_availability(property_identifier, rate_modifier_bundle_identifier, inventory_update_request_supplier, wink_version=wink_version)

Update Sale Channels Rate Modifier Bundles

Toggles availability of a promo bundle for a list of sales channels

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Update sales channel owned by this property identifier
    rate_modifier_bundle_identifier = 'rate-modifier-bundle-1' # str | The rate modifier bundle we are enabling / disabling on the sales channel
    inventory_update_request_supplier = [wink_sdk_extranet_distribution.InventoryUpdateRequestSupplier()] # List[InventoryUpdateRequestSupplier] | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Sale Channels Rate Modifier Bundles
        api_response = api_instance.toggle_sales_channel_promo_bundle_availability(property_identifier, rate_modifier_bundle_identifier, inventory_update_request_supplier, wink_version=wink_version)
        print("The response of SalesChannelApi->toggle_sales_channel_promo_bundle_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->toggle_sales_channel_promo_bundle_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update sales channel owned by this property identifier | 
 **rate_modifier_bundle_identifier** | **str**| The rate modifier bundle we are enabling / disabling on the sales channel | 
 **inventory_update_request_supplier** | [**List[InventoryUpdateRequestSupplier]**](InventoryUpdateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[SalesChannelSupplier]**](SalesChannelSupplier.md)

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

# **update_sales_channel**
> SalesChannelSupplier update_sales_channel(property_identifier, sales_channel_identifier, sales_channel_update_request_supplier, wink_version=wink_version)

Update Sales Channel

Update a chosen sales channel

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_supplier import SalesChannelSupplier
from wink_sdk_extranet_distribution.models.sales_channel_update_request_supplier import SalesChannelUpdateRequestSupplier
from wink_sdk_extranet_distribution.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_distribution.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_distribution.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_distribution.SalesChannelApi(api_client)
    property_identifier = 'hotel-1' # str | Update sales channel owned by this property identifier
    sales_channel_identifier = 'sales channel-1' # str | Update sales channel settings for sales channel with this identifier
    sales_channel_update_request_supplier = wink_sdk_extranet_distribution.SalesChannelUpdateRequestSupplier() # SalesChannelUpdateRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Sales Channel
        api_response = api_instance.update_sales_channel(property_identifier, sales_channel_identifier, sales_channel_update_request_supplier, wink_version=wink_version)
        print("The response of SalesChannelApi->update_sales_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->update_sales_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update sales channel owned by this property identifier | 
 **sales_channel_identifier** | **str**| Update sales channel settings for sales channel with this identifier | 
 **sales_channel_update_request_supplier** | [**SalesChannelUpdateRequestSupplier**](SalesChannelUpdateRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SalesChannelSupplier**](SalesChannelSupplier.md)

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

