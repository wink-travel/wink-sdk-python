# wink_sdk_affiliate_browse.CuratedListApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_to_curated_list**](CuratedListApi.md#add_inventory_to_curated_list) | **POST** /api/static-list/{listIdentifier}/item | Add Inventory to List
[**add_supplier_to_curated_list**](CuratedListApi.md#add_supplier_to_curated_list) | **POST** /api/static-list/{listIdentifier}/item/supplier | Add Supplier to List
[**copy_inventory_to_curated_list**](CuratedListApi.md#copy_inventory_to_curated_list) | **POST** /api/static-list/{listIdentifier}/item/{itemIdentifier} | Copy Item to List
[**create_curated_list**](CuratedListApi.md#create_curated_list) | **POST** /api/static-list | Create Curated List
[**create_curated_supplier_list**](CuratedListApi.md#create_curated_supplier_list) | **POST** /api/static-list/supplier | Create Curated List
[**move_inventory_to_curated_list**](CuratedListApi.md#move_inventory_to_curated_list) | **PUT** /api/static-list/{listIdentifier}/item/{itemIdentifier} | Move List Item
[**remove_curated_list**](CuratedListApi.md#remove_curated_list) | **DELETE** /api/static-list/{listIdentifier} | Remove Curated List
[**remove_inventory_from_curated_list**](CuratedListApi.md#remove_inventory_from_curated_list) | **DELETE** /api/static-list/{listIdentifier}/item/{itemIdentifier} | Delete List Item
[**show_curated_lists**](CuratedListApi.md#show_curated_lists) | **GET** /api/static-list | Show Curated Lists
[**sort_curated_list_items**](CuratedListApi.md#sort_curated_list_items) | **PATCH** /api/static-list/{listIdentifier}/sort | Re-Order List Items
[**update_curated_list**](CuratedListApi.md#update_curated_list) | **PUT** /api/static-list/{listIdentifier} | Update Curated List


# **add_inventory_to_curated_list**
> StaticListItemAffiliate add_inventory_to_curated_list(list_identifier, add_static_list_item_request_affiliate, wink_version=wink_version)

Add Inventory to List

Add some travel inventoryto your existing curated list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.add_static_list_item_request_affiliate import AddStaticListItemRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    add_static_list_item_request_affiliate = wink_sdk_affiliate_browse.AddStaticListItemRequestAffiliate() # AddStaticListItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add Inventory to List
        api_response = api_instance.add_inventory_to_curated_list(list_identifier, add_static_list_item_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->add_inventory_to_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->add_inventory_to_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **add_static_list_item_request_affiliate** | [**AddStaticListItemRequestAffiliate**](AddStaticListItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListItemAffiliate**](StaticListItemAffiliate.md)

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

# **add_supplier_to_curated_list**
> StaticListItemAffiliate add_supplier_to_curated_list(list_identifier, add_static_list_supplier_request_affiliate, wink_version=wink_version)

Add Supplier to List

Adds a new list item for a supplier showing the best priced room..

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.add_static_list_supplier_request_affiliate import AddStaticListSupplierRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    add_static_list_supplier_request_affiliate = wink_sdk_affiliate_browse.AddStaticListSupplierRequestAffiliate() # AddStaticListSupplierRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add Supplier to List
        api_response = api_instance.add_supplier_to_curated_list(list_identifier, add_static_list_supplier_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->add_supplier_to_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->add_supplier_to_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **add_static_list_supplier_request_affiliate** | [**AddStaticListSupplierRequestAffiliate**](AddStaticListSupplierRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListItemAffiliate**](StaticListItemAffiliate.md)

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

# **copy_inventory_to_curated_list**
> StaticListItemAffiliate copy_inventory_to_curated_list(list_identifier, item_identifier, copy_move_static_list_item_request_affiliate, wink_version=wink_version)

Copy Item to List

Copy an existing list item from one list to another.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.copy_move_static_list_item_request_affiliate import CopyMoveStaticListItemRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    item_identifier = 'item-1' # str | Item identifier.
    copy_move_static_list_item_request_affiliate = wink_sdk_affiliate_browse.CopyMoveStaticListItemRequestAffiliate() # CopyMoveStaticListItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Copy Item to List
        api_response = api_instance.copy_inventory_to_curated_list(list_identifier, item_identifier, copy_move_static_list_item_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->copy_inventory_to_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->copy_inventory_to_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **item_identifier** | **str**| Item identifier. | 
 **copy_move_static_list_item_request_affiliate** | [**CopyMoveStaticListItemRequestAffiliate**](CopyMoveStaticListItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListItemAffiliate**](StaticListItemAffiliate.md)

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

# **create_curated_list**
> StaticListWrapperAffiliate create_curated_list(create_static_list_and_add_item_request_affiliate, wink_version=wink_version)

Create Curated List

Create a new curated list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.create_static_list_and_add_item_request_affiliate import CreateStaticListAndAddItemRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_wrapper_affiliate import StaticListWrapperAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    create_static_list_and_add_item_request_affiliate = wink_sdk_affiliate_browse.CreateStaticListAndAddItemRequestAffiliate() # CreateStaticListAndAddItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Curated List
        api_response = api_instance.create_curated_list(create_static_list_and_add_item_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->create_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->create_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_list_and_add_item_request_affiliate** | [**CreateStaticListAndAddItemRequestAffiliate**](CreateStaticListAndAddItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListWrapperAffiliate**](StaticListWrapperAffiliate.md)

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

# **create_curated_supplier_list**
> StaticListWrapperAffiliate create_curated_supplier_list(create_static_list_and_add_supplier_request_affiliate, wink_version=wink_version)

Create Curated List

Create a new curated list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.create_static_list_and_add_supplier_request_affiliate import CreateStaticListAndAddSupplierRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_wrapper_affiliate import StaticListWrapperAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    create_static_list_and_add_supplier_request_affiliate = wink_sdk_affiliate_browse.CreateStaticListAndAddSupplierRequestAffiliate() # CreateStaticListAndAddSupplierRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Curated List
        api_response = api_instance.create_curated_supplier_list(create_static_list_and_add_supplier_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->create_curated_supplier_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->create_curated_supplier_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_list_and_add_supplier_request_affiliate** | [**CreateStaticListAndAddSupplierRequestAffiliate**](CreateStaticListAndAddSupplierRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListWrapperAffiliate**](StaticListWrapperAffiliate.md)

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

# **move_inventory_to_curated_list**
> StaticListItemAffiliate move_inventory_to_curated_list(list_identifier, item_identifier, copy_move_static_list_item_request_affiliate, wink_version=wink_version)

Move List Item

Move an existing list item from one list to another.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.copy_move_static_list_item_request_affiliate import CopyMoveStaticListItemRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    item_identifier = 'item-1' # str | Item identifier.
    copy_move_static_list_item_request_affiliate = wink_sdk_affiliate_browse.CopyMoveStaticListItemRequestAffiliate() # CopyMoveStaticListItemRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Move List Item
        api_response = api_instance.move_inventory_to_curated_list(list_identifier, item_identifier, copy_move_static_list_item_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->move_inventory_to_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->move_inventory_to_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **item_identifier** | **str**| Item identifier. | 
 **copy_move_static_list_item_request_affiliate** | [**CopyMoveStaticListItemRequestAffiliate**](CopyMoveStaticListItemRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListItemAffiliate**](StaticListItemAffiliate.md)

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

# **remove_curated_list**
> StaticListAffiliate remove_curated_list(list_identifier, wink_version=wink_version, accept=accept)

Remove Curated List

Remove curated list by list identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.static_list_affiliate import StaticListAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Curated List
        api_response = api_instance.remove_curated_list(list_identifier, wink_version=wink_version, accept=accept)
        print("The response of CuratedListApi->remove_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->remove_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**StaticListAffiliate**](StaticListAffiliate.md)

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

# **remove_inventory_from_curated_list**
> StaticListItemAffiliate remove_inventory_from_curated_list(list_identifier, item_identifier, wink_version=wink_version, accept=accept)

Delete List Item

Delete a list item from a curated list by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    item_identifier = 'item-1' # str | Item identifier.
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete List Item
        api_response = api_instance.remove_inventory_from_curated_list(list_identifier, item_identifier, wink_version=wink_version, accept=accept)
        print("The response of CuratedListApi->remove_inventory_from_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->remove_inventory_from_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **item_identifier** | **str**| Item identifier. | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**StaticListItemAffiliate**](StaticListItemAffiliate.md)

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

# **show_curated_lists**
> List[StaticListWrapperAffiliate] show_curated_lists(with_items=with_items, wink_version=wink_version, accept=accept)

Show Curated Lists

Retrieve lists optionally with content.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.static_list_wrapper_affiliate import StaticListWrapperAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    with_items = False # bool | Indicate whether to include all the list items in the result (optional) (default to False)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Curated Lists
        api_response = api_instance.show_curated_lists(with_items=with_items, wink_version=wink_version, accept=accept)
        print("The response of CuratedListApi->show_curated_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->show_curated_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_items** | **bool**| Indicate whether to include all the list items in the result | [optional] [default to False]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[StaticListWrapperAffiliate]**](StaticListWrapperAffiliate.md)

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

# **sort_curated_list_items**
> List[StaticListItemAffiliate] sort_curated_list_items(list_identifier, sort_static_list_items_request_affiliate, wink_version=wink_version)

Re-Order List Items

Re-order list items with an existing list

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.sort_static_list_items_request_affiliate import SortStaticListItemsRequestAffiliate
from wink_sdk_affiliate_browse.models.static_list_item_affiliate import StaticListItemAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    sort_static_list_items_request_affiliate = wink_sdk_affiliate_browse.SortStaticListItemsRequestAffiliate() # SortStaticListItemsRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Re-Order List Items
        api_response = api_instance.sort_curated_list_items(list_identifier, sort_static_list_items_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->sort_curated_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->sort_curated_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **sort_static_list_items_request_affiliate** | [**SortStaticListItemsRequestAffiliate**](SortStaticListItemsRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[StaticListItemAffiliate]**](StaticListItemAffiliate.md)

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

# **update_curated_list**
> StaticListWrapperAffiliate update_curated_list(list_identifier, upsert_static_list_request_affiliate, wink_version=wink_version)

Update Curated List

Update curated list by its unique identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_browse
from wink_sdk_affiliate_browse.models.static_list_wrapper_affiliate import StaticListWrapperAffiliate
from wink_sdk_affiliate_browse.models.upsert_static_list_request_affiliate import UpsertStaticListRequestAffiliate
from wink_sdk_affiliate_browse.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_browse.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_browse.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_browse.CuratedListApi(api_client)
    list_identifier = 'list-1' # str | List identifier.
    upsert_static_list_request_affiliate = wink_sdk_affiliate_browse.UpsertStaticListRequestAffiliate() # UpsertStaticListRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Curated List
        api_response = api_instance.update_curated_list(list_identifier, upsert_static_list_request_affiliate, wink_version=wink_version)
        print("The response of CuratedListApi->update_curated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CuratedListApi->update_curated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_identifier** | **str**| List identifier. | 
 **upsert_static_list_request_affiliate** | [**UpsertStaticListRequestAffiliate**](UpsertStaticListRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**StaticListWrapperAffiliate**](StaticListWrapperAffiliate.md)

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

