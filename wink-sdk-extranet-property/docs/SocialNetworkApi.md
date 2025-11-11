# wink_sdk_extranet_property.SocialNetworkApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_social_networks**](SocialNetworkApi.md#show_social_networks) | **GET** /api/property/{propertyIdentifier}/social-networks | Show Social Networks
[**update_socials**](SocialNetworkApi.md#update_socials) | **PATCH** /api/property/{propertyIdentifier}/social-networks | Update Social Networks


# **show_social_networks**
> SocialNetworksResponseSupplier show_social_networks(property_identifier, wink_version=wink_version, accept=accept)

Show Social Networks

Show hotel's social networks

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.social_networks_response_supplier import SocialNetworksResponseSupplier
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
    api_instance = wink_sdk_extranet_property.SocialNetworkApi(api_client)
    property_identifier = 'hotel-1' # str | Show Social Networks associated with this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Social Networks
        api_response = api_instance.show_social_networks(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of SocialNetworkApi->show_social_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialNetworkApi->show_social_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show Social Networks associated with this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SocialNetworksResponseSupplier**](SocialNetworksResponseSupplier.md)

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

# **update_socials**
> PropertySupplier update_socials(property_identifier, social_networks_request_supplier, wink_version=wink_version)

Update Social Networks

Update hotel's social networks. Refer to [Social Networks](#tag/Social-Networks) for a list of all supported social networks.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.social_networks_request_supplier import SocialNetworksRequestSupplier
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
    api_instance = wink_sdk_extranet_property.SocialNetworkApi(api_client)
    property_identifier = 'hotel-1' # str | Set social networks this property identifier
    social_networks_request_supplier = wink_sdk_extranet_property.SocialNetworksRequestSupplier() # SocialNetworksRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Social Networks
        api_response = api_instance.update_socials(property_identifier, social_networks_request_supplier, wink_version=wink_version)
        print("The response of SocialNetworkApi->update_socials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialNetworkApi->update_socials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Set social networks this property identifier | 
 **social_networks_request_supplier** | [**SocialNetworksRequestSupplier**](SocialNetworksRequestSupplier.md)|  | 
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

