# wink_sdk_affiliate_sales_channel.RelationshipRequestApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplier_request**](RelationshipRequestApi.md#create_supplier_request) | **POST** /api/sales-channel/request | Create Supplier Request
[**re_apply_supplier_request**](RelationshipRequestApi.md#re_apply_supplier_request) | **GET** /api/sales-channel/request/{salesChannelRequestIdentifier}/re-apply | Re-apply Supplier Request
[**remove_supplier_request**](RelationshipRequestApi.md#remove_supplier_request) | **DELETE** /api/sales-channel/request/{salesChannelRequestIdentifier} | Delete Relationship Request
[**show_supplier_request**](RelationshipRequestApi.md#show_supplier_request) | **GET** /api/sales-channel/request/supplier/{supplierIdentifier} | Show Supplier Request
[**show_supplier_requests**](RelationshipRequestApi.md#show_supplier_requests) | **GET** /api/sales-channel/request/list | Show Supplier Requests


# **create_supplier_request**
> SalesChannelRequest create_supplier_request(upsert_sales_channel_request_request, wink_version=wink_version)

Create Supplier Request

Create a new property request.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_request import SalesChannelRequest
from wink_sdk_affiliate_sales_channel.models.upsert_sales_channel_request_request import UpsertSalesChannelRequestRequest
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.RelationshipRequestApi(api_client)
    upsert_sales_channel_request_request = wink_sdk_affiliate_sales_channel.UpsertSalesChannelRequestRequest() # UpsertSalesChannelRequestRequest | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Supplier Request
        api_response = api_instance.create_supplier_request(upsert_sales_channel_request_request, wink_version=wink_version)
        print("The response of RelationshipRequestApi->create_supplier_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipRequestApi->create_supplier_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_sales_channel_request_request** | [**UpsertSalesChannelRequestRequest**](UpsertSalesChannelRequestRequest.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**SalesChannelRequest**](SalesChannelRequest.md)

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

# **re_apply_supplier_request**
> SalesChannelRequest re_apply_supplier_request(sales_channel_request_identifier, wink_version=wink_version, accept=accept)

Re-apply Supplier Request

Allows the affiliate to re-apply a previously rejected property request after 90 days.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_request import SalesChannelRequest
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.RelationshipRequestApi(api_client)
    sales_channel_request_identifier = 'sales-channel-1' # str | Re-apply relationship request with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Re-apply Supplier Request
        api_response = api_instance.re_apply_supplier_request(sales_channel_request_identifier, wink_version=wink_version, accept=accept)
        print("The response of RelationshipRequestApi->re_apply_supplier_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipRequestApi->re_apply_supplier_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_channel_request_identifier** | **str**| Re-apply relationship request with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelRequest**](SalesChannelRequest.md)

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

# **remove_supplier_request**
> SalesChannelRequest remove_supplier_request(sales_channel_request_identifier, wink_version=wink_version, accept=accept)

Delete Relationship Request

Delete a relationship request

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_request import SalesChannelRequest
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.RelationshipRequestApi(api_client)
    sales_channel_request_identifier = 'sales-channel-1' # str | Remove property request with this identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Relationship Request
        api_response = api_instance.remove_supplier_request(sales_channel_request_identifier, wink_version=wink_version, accept=accept)
        print("The response of RelationshipRequestApi->remove_supplier_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipRequestApi->remove_supplier_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_channel_request_identifier** | **str**| Remove property request with this identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelRequest**](SalesChannelRequest.md)

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

# **show_supplier_request**
> SalesChannelRequest show_supplier_request(supplier_identifier, wink_version=wink_version, accept=accept)

Show Supplier Request

Retrieve a specific property request based on a companyId and a supplierId.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_request import SalesChannelRequest
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.RelationshipRequestApi(api_client)
    supplier_identifier = 'supplier-1' # str | Show property request for this supplier identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier Request
        api_response = api_instance.show_supplier_request(supplier_identifier, wink_version=wink_version, accept=accept)
        print("The response of RelationshipRequestApi->show_supplier_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipRequestApi->show_supplier_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_identifier** | **str**| Show property request for this supplier identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**SalesChannelRequest**](SalesChannelRequest.md)

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

# **show_supplier_requests**
> List[SalesChannelRequestAffiliate] show_supplier_requests(wink_version=wink_version, accept=accept)

Show Supplier Requests

Retrieve list of all property requests for this company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_sales_channel
from wink_sdk_affiliate_sales_channel.models.sales_channel_request_affiliate import SalesChannelRequestAffiliate
from wink_sdk_affiliate_sales_channel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_sales_channel.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_sales_channel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_sales_channel.RelationshipRequestApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Supplier Requests
        api_response = api_instance.show_supplier_requests(wink_version=wink_version, accept=accept)
        print("The response of RelationshipRequestApi->show_supplier_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipRequestApi->show_supplier_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[SalesChannelRequestAffiliate]**](SalesChannelRequestAffiliate.md)

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

