# wink_sdk_inventory.ShareableLinkApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_consumable_url**](ShareableLinkApi.md#show_consumable_url) | **POST** /api/shareable-link/{code} | Show Shareable Link


# **show_consumable_url**
> ConsumableSellerUrlNonAuthenticatedEntity show_consumable_url(code, user_session_non_authenticated_entity, cid=cid, gl=gl, wink_version=wink_version)

Show Shareable Link

Retrieve a shareable link by its unique code

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.consumable_seller_url_non_authenticated_entity import ConsumableSellerUrlNonAuthenticatedEntity
from wink_sdk_inventory.models.user_session_non_authenticated_entity import UserSessionNonAuthenticatedEntity
from wink_sdk_inventory.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_inventory.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_inventory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_inventory.ShareableLinkApi(api_client)
    code = 'code_example' # str | Unique link code
    user_session_non_authenticated_entity = wink_sdk_inventory.UserSessionNonAuthenticatedEntity() # UserSessionNonAuthenticatedEntity | 
    cid = 'cid_example' # str | Optional campaign id (optional)
    gl = 'gl_example' # str | Optional GA4 cross-site link id (optional)
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Shareable Link
        api_response = api_instance.show_consumable_url(code, user_session_non_authenticated_entity, cid=cid, gl=gl, wink_version=wink_version)
        print("The response of ShareableLinkApi->show_consumable_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareableLinkApi->show_consumable_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Unique link code | 
 **user_session_non_authenticated_entity** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md)|  | 
 **cid** | **str**| Optional campaign id | [optional] 
 **gl** | **str**| Optional GA4 cross-site link id | [optional] 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ConsumableSellerUrlNonAuthenticatedEntity**](ConsumableSellerUrlNonAuthenticatedEntity.md)

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

