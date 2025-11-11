# wink_sdk_affiliate_winklinks.SyndicationSettingsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_syndication_settings**](SyndicationSettingsApi.md#show_syndication_settings) | **GET** /api/syndication/settings | Show WinkLinks Settings
[**upsert_syndication_settings**](SyndicationSettingsApi.md#upsert_syndication_settings) | **PUT** /api/syndication/settings | Upsert WinkLinks Settings


# **show_syndication_settings**
> SyndicationSettingsWithThemeColorsAffiliate show_syndication_settings(wink_version=wink_version, accept=accept)

Show WinkLinks Settings

Load WinkLinks settings.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_settings_with_theme_colors_affiliate import SyndicationSettingsWithThemeColorsAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicationSettingsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show WinkLinks Settings
        api_response = api_instance.show_syndication_settings(wink_version=wink_version, accept=accept)
        print("The response of SyndicationSettingsApi->show_syndication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationSettingsApi->show_syndication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicationSettingsWithThemeColorsAffiliate**](SyndicationSettingsWithThemeColorsAffiliate.md)

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

# **upsert_syndication_settings**
> SyndicationSettingsWithThemeColorsAffiliate upsert_syndication_settings(upsert_syndication_settings_affiliate, wink_version=wink_version)

Upsert WinkLinks Settings

Upsert a new syndication settings.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_settings_with_theme_colors_affiliate import SyndicationSettingsWithThemeColorsAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_settings_affiliate import UpsertSyndicationSettingsAffiliate
from wink_sdk_affiliate_winklinks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate_winklinks.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate_winklinks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate_winklinks.SyndicationSettingsApi(api_client)
    upsert_syndication_settings_affiliate = wink_sdk_affiliate_winklinks.UpsertSyndicationSettingsAffiliate() # UpsertSyndicationSettingsAffiliate | Request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Upsert WinkLinks Settings
        api_response = api_instance.upsert_syndication_settings(upsert_syndication_settings_affiliate, wink_version=wink_version)
        print("The response of SyndicationSettingsApi->upsert_syndication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationSettingsApi->upsert_syndication_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_syndication_settings_affiliate** | [**UpsertSyndicationSettingsAffiliate**](UpsertSyndicationSettingsAffiliate.md)| Request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SyndicationSettingsWithThemeColorsAffiliate**](SyndicationSettingsWithThemeColorsAffiliate.md)

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

