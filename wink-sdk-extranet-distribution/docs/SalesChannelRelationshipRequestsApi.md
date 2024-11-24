# wink_sdk_extranet_distribution.SalesChannelRelationshipRequestsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sales_channel_request**](SalesChannelRelationshipRequestsApi.md#create_sales_channel_request) | **POST** /api/property/{propertyIdentifier}/sales-channel/request | Create Sales Channel Request
[**remove_sales_channel_request**](SalesChannelRelationshipRequestsApi.md#remove_sales_channel_request) | **DELETE** /api/property/{propertyIdentifier}/sales-channel/request/{salesChannelRequestIdentifier} | Reject Sales Channel Request
[**show_sales_channel_requests**](SalesChannelRelationshipRequestsApi.md#show_sales_channel_requests) | **GET** /api/property/{propertyIdentifier}/sales-channel/request/list | Show Sales Channel Requests


# **create_sales_channel_request**
> SalesChannelRelationshipRequestViewSupplier create_sales_channel_request(property_identifier, upsert_sales_channel_relationship_request_request_supplier, wink_version=wink_version)

Create Sales Channel Request

Create a new sales channel request.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_relationship_request_view_supplier import SalesChannelRelationshipRequestViewSupplier
from wink_sdk_extranet_distribution.models.upsert_sales_channel_relationship_request_request_supplier import UpsertSalesChannelRelationshipRequestRequestSupplier
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
    api_instance = wink_sdk_extranet_distribution.SalesChannelRelationshipRequestsApi(api_client)
    property_identifier = 'hotel-1' # str | Create sales channel request and associate it with this property identifier
    upsert_sales_channel_relationship_request_request_supplier = wink_sdk_extranet_distribution.UpsertSalesChannelRelationshipRequestRequestSupplier() # UpsertSalesChannelRelationshipRequestRequestSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Sales Channel Request
        api_response = api_instance.create_sales_channel_request(property_identifier, upsert_sales_channel_relationship_request_request_supplier, wink_version=wink_version)
        print("The response of SalesChannelRelationshipRequestsApi->create_sales_channel_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelRelationshipRequestsApi->create_sales_channel_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Create sales channel request and associate it with this property identifier | 
 **upsert_sales_channel_relationship_request_request_supplier** | [**UpsertSalesChannelRelationshipRequestRequestSupplier**](UpsertSalesChannelRelationshipRequestRequestSupplier.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SalesChannelRelationshipRequestViewSupplier**](SalesChannelRelationshipRequestViewSupplier.md)

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

# **remove_sales_channel_request**
> SalesChannelRelationshipRequestViewSupplier remove_sales_channel_request(property_identifier, sales_channel_request_identifier, wink_version=wink_version, accept=accept)

Reject Sales Channel Request

Delete a sales channel request

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_relationship_request_view_supplier import SalesChannelRelationshipRequestViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.SalesChannelRelationshipRequestsApi(api_client)
    property_identifier = 'hotel-1' # str | Remove sales channel request owned by this property identifier
    sales_channel_request_identifier = 'sales-channel-request-1' # str | Remove sales channel request with this identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Reject Sales Channel Request
        api_response = api_instance.remove_sales_channel_request(property_identifier, sales_channel_request_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelRelationshipRequestsApi->remove_sales_channel_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelRelationshipRequestsApi->remove_sales_channel_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Remove sales channel request owned by this property identifier | 
 **sales_channel_request_identifier** | **str**| Remove sales channel request with this identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelRelationshipRequestViewSupplier**](SalesChannelRelationshipRequestViewSupplier.md)

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

# **show_sales_channel_requests**
> List[SalesChannelRelationshipRequestViewSupplier] show_sales_channel_requests(property_identifier, wink_version=wink_version, accept=accept)

Show Sales Channel Requests

Retrieve list of all sales channels for this property. You can decide to retrieve all specific sales channel relationships or only generic ones using the 'owner' request parameter.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_distribution
from wink_sdk_extranet_distribution.models.sales_channel_relationship_request_view_supplier import SalesChannelRelationshipRequestViewSupplier
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
    api_instance = wink_sdk_extranet_distribution.SalesChannelRelationshipRequestsApi(api_client)
    property_identifier = 'hotel-1' # str | Show all sales channel requests for this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Sales Channel Requests
        api_response = api_instance.show_sales_channel_requests(property_identifier, wink_version=wink_version, accept=accept)
        print("The response of SalesChannelRelationshipRequestsApi->show_sales_channel_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelRelationshipRequestsApi->show_sales_channel_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Show all sales channel requests for this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[SalesChannelRelationshipRequestViewSupplier]**](SalesChannelRelationshipRequestViewSupplier.md)

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

