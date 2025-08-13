# wink_sdk_inventory.ShareableLinkApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_consumable_url**](ShareableLinkApi.md#show_consumable_url) | **POST** /api/shareable-link/{code} | Show Shareable Link


# **show_consumable_url**
> AbstractOpenGraphRedirectUrlNonAuthenticatedEntity show_consumable_url(code, user_session_non_authenticated_entity, user_agent=user_agent, host=host, referer=referer, cid=cid, gl=gl, wink_version=wink_version)

Show Shareable Link

Retrieve a shareable link by its unique code

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_inventory
from wink_sdk_inventory.models.abstract_open_graph_redirect_url_non_authenticated_entity import AbstractOpenGraphRedirectUrlNonAuthenticatedEntity
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
    user_agent = 'Unknown' # str | User-Agent header. (optional) (default to 'Unknown')
    host = 'Unknown' # str | Host header. (optional) (default to 'Unknown')
    referer = 'Unknown' # str | Referrer header. (optional) (default to 'Unknown')
    cid = 'cid_example' # str | Optional campaignId (optional)
    gl = 'gl_example' # str | Optional GA4 cross link ID (optional)
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Shareable Link
        api_response = api_instance.show_consumable_url(code, user_session_non_authenticated_entity, user_agent=user_agent, host=host, referer=referer, cid=cid, gl=gl, wink_version=wink_version)
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
 **user_agent** | **str**| User-Agent header. | [optional] [default to &#39;Unknown&#39;]
 **host** | **str**| Host header. | [optional] [default to &#39;Unknown&#39;]
 **referer** | **str**| Referrer header. | [optional] [default to &#39;Unknown&#39;]
 **cid** | **str**| Optional campaignId | [optional] 
 **gl** | **str**| Optional GA4 cross link ID | [optional] 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AbstractOpenGraphRedirectUrlNonAuthenticatedEntity**](AbstractOpenGraphRedirectUrlNonAuthenticatedEntity.md)

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

