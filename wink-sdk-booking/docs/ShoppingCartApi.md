# wink_sdk_booking.ShoppingCartApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cart**](ShoppingCartApi.md#create_cart) | **POST** /api/shopping-cart | Create Shopping Cart
[**create_carts**](ShoppingCartApi.md#create_carts) | **POST** /api/shopping-cart/list | Create Shopping Carts
[**delete_cart**](ShoppingCartApi.md#delete_cart) | **DELETE** /api/shopping-cart/{shoppingCartIdentifier} | Remove Shopping Cart
[**delete_cart_item**](ShoppingCartApi.md#delete_cart_item) | **DELETE** /api/shopping-cart/{shoppingCartIdentifier}/item/{shoppingCartItemIdentifier} | Remove Shopping Cart Item
[**delete_cart_item_ancillary**](ShoppingCartApi.md#delete_cart_item_ancillary) | **DELETE** /api/shopping-cart/{shoppingCartIdentifier}/item/{shoppingCartItemIdentifier}/ancillary/{shoppingCartItemAncillaryIdentifier} | Remove Shopping Cart Item Ancillary
[**delete_carts**](ShoppingCartApi.md#delete_carts) | **DELETE** /api/shopping-cart | Empty Shopping Carts
[**empty_cart**](ShoppingCartApi.md#empty_cart) | **DELETE** /api/shopping-cart/{shoppingCartIdentifier}/empty | Empty Shopping Cart
[**show_cart**](ShoppingCartApi.md#show_cart) | **GET** /api/shopping-cart/{shoppingCartIdentifier} | Show Shopping Cart
[**show_carts**](ShoppingCartApi.md#show_carts) | **GET** /api/shopping-cart/list | Show Shopping Carts
[**update_cart_item**](ShoppingCartApi.md#update_cart_item) | **PATCH** /api/shopping-cart/{shoppingCartIdentifier}/item/{shoppingCartItemIdentifier} | Update Shopping Cart Item


# **create_cart**
> RealtimeShoppingCartAuthenticatedEntity create_cart(upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)

Create Shopping Cart

Creates a shopping cart and adds item.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.models.upsert_shopping_cart_item_request_authenticated_entity import UpsertShoppingCartItemRequestAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    upsert_shopping_cart_item_request_authenticated_entity = wink_sdk_booking.UpsertShoppingCartItemRequestAuthenticatedEntity() # UpsertShoppingCartItemRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Shopping Cart
        api_response = api_instance.create_cart(upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)
        print("The response of ShoppingCartApi->create_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->create_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_shopping_cart_item_request_authenticated_entity** | [**UpsertShoppingCartItemRequestAuthenticatedEntity**](UpsertShoppingCartItemRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **create_carts**
> List[RealtimeShoppingCartAuthenticatedEntity] create_carts(upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)

Create Shopping Carts

Creates shopping carts and adds an item to each.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.models.upsert_shopping_cart_item_request_authenticated_entity import UpsertShoppingCartItemRequestAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    upsert_shopping_cart_item_request_authenticated_entity = [wink_sdk_booking.UpsertShoppingCartItemRequestAuthenticatedEntity()] # List[UpsertShoppingCartItemRequestAuthenticatedEntity] | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Shopping Carts
        api_response = api_instance.create_carts(upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)
        print("The response of ShoppingCartApi->create_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->create_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_shopping_cart_item_request_authenticated_entity** | [**List[UpsertShoppingCartItemRequestAuthenticatedEntity]**](UpsertShoppingCartItemRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**List[RealtimeShoppingCartAuthenticatedEntity]**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **delete_cart**
> RemoveEntryResponseAuthenticatedEntity delete_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)

Remove Shopping Cart

Removes the cart. Not necessary as the cart has a TTL of only an hour anyway.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.remove_entry_response_authenticated_entity import RemoveEntryResponseAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to remove
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Shopping Cart
        api_response = api_instance.delete_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->delete_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->delete_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to remove | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RemoveEntryResponseAuthenticatedEntity**](RemoveEntryResponseAuthenticatedEntity.md)

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

# **delete_cart_item**
> RealtimeShoppingCartAuthenticatedEntity delete_cart_item(shopping_cart_identifier, shopping_cart_item_identifier, wink_version=wink_version, accept=accept)

Remove Shopping Cart Item

Remove item from cart

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to update
    shopping_cart_item_identifier = 'cart-item-1' # str | Cart item to remove
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Shopping Cart Item
        api_response = api_instance.delete_cart_item(shopping_cart_identifier, shopping_cart_item_identifier, wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->delete_cart_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->delete_cart_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to update | 
 **shopping_cart_item_identifier** | **str**| Cart item to remove | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **delete_cart_item_ancillary**
> RealtimeShoppingCartAuthenticatedEntity delete_cart_item_ancillary(shopping_cart_identifier, shopping_cart_item_identifier, shopping_cart_item_ancillary_identifier, wink_version=wink_version, accept=accept)

Remove Shopping Cart Item Ancillary

Remove item ancillary from cart

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to update
    shopping_cart_item_identifier = 'cart-item-1' # str | Cart item to update
    shopping_cart_item_ancillary_identifier = 'cart-item-ancillary-1' # str | Cart item ancillary to remove
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Shopping Cart Item Ancillary
        api_response = api_instance.delete_cart_item_ancillary(shopping_cart_identifier, shopping_cart_item_identifier, shopping_cart_item_ancillary_identifier, wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->delete_cart_item_ancillary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->delete_cart_item_ancillary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to update | 
 **shopping_cart_item_identifier** | **str**| Cart item to update | 
 **shopping_cart_item_ancillary_identifier** | **str**| Cart item ancillary to remove | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **delete_carts**
> BooleanResponseAuthenticatedEntity delete_carts(wink_version=wink_version, accept=accept)

Empty Shopping Carts

Empties all carts.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.boolean_response_authenticated_entity import BooleanResponseAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Empty Shopping Carts
        api_response = api_instance.delete_carts(wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->delete_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->delete_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**BooleanResponseAuthenticatedEntity**](BooleanResponseAuthenticatedEntity.md)

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

# **empty_cart**
> RealtimeShoppingCartAuthenticatedEntity empty_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)

Empty Shopping Cart

Empties selected cart.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to empty
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Empty Shopping Cart
        api_response = api_instance.empty_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->empty_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->empty_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to empty | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **show_cart**
> RealtimeShoppingCartAuthenticatedEntity show_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)

Show Shopping Cart

Display user's shopping cart

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to retrieve
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Shopping Cart
        api_response = api_instance.show_cart(shopping_cart_identifier, wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->show_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->show_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to retrieve | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **show_carts**
> List[RealtimeShoppingCartAuthenticatedEntity] show_carts(wink_version=wink_version, accept=accept)

Show Shopping Carts

Display all of user's shopping cart

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Shopping Carts
        api_response = api_instance.show_carts(wink_version=wink_version, accept=accept)
        print("The response of ShoppingCartApi->show_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->show_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[RealtimeShoppingCartAuthenticatedEntity]**](RealtimeShoppingCartAuthenticatedEntity.md)

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

# **update_cart_item**
> RealtimeShoppingCartAuthenticatedEntity update_cart_item(shopping_cart_identifier, shopping_cart_item_identifier, upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)

Update Shopping Cart Item

Updates item in shopping cart.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_booking
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity
from wink_sdk_booking.models.upsert_shopping_cart_item_request_authenticated_entity import UpsertShoppingCartItemRequestAuthenticatedEntity
from wink_sdk_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_booking.ShoppingCartApi(api_client)
    shopping_cart_identifier = 'cart-1' # str | Cart to update
    shopping_cart_item_identifier = 'cart-item-1' # str | Cart item to update
    upsert_shopping_cart_item_request_authenticated_entity = wink_sdk_booking.UpsertShoppingCartItemRequestAuthenticatedEntity() # UpsertShoppingCartItemRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Shopping Cart Item
        api_response = api_instance.update_cart_item(shopping_cart_identifier, shopping_cart_item_identifier, upsert_shopping_cart_item_request_authenticated_entity, wink_version=wink_version)
        print("The response of ShoppingCartApi->update_cart_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShoppingCartApi->update_cart_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_identifier** | **str**| Cart to update | 
 **shopping_cart_item_identifier** | **str**| Cart item to update | 
 **upsert_shopping_cart_item_request_authenticated_entity** | [**UpsertShoppingCartItemRequestAuthenticatedEntity**](UpsertShoppingCartItemRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**RealtimeShoppingCartAuthenticatedEntity**](RealtimeShoppingCartAuthenticatedEntity.md)

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

