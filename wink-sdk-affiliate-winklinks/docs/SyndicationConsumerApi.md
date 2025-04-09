# wink_sdk_affiliate_winklinks.SyndicationConsumerApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consume_facebook_page_url**](SyndicationConsumerApi.md#consume_facebook_page_url) | **GET** /api/sell/{companyIdentifier}/syndication/facebook/page | Consume Facebook Page URL
[**consume_facebook_post_url**](SyndicationConsumerApi.md#consume_facebook_post_url) | **GET** /api/sell/{companyIdentifier}/syndication/facebook/post | Consume Facebook Post URL
[**consume_facebook_video_url**](SyndicationConsumerApi.md#consume_facebook_video_url) | **GET** /api/sell/{companyIdentifier}/syndication/facebook/video | Consume Facebook Video URL
[**consume_instagram_post_url**](SyndicationConsumerApi.md#consume_instagram_post_url) | **GET** /api/sell/{companyIdentifier}/syndication/instagram/post | Consume Instagram Post URL
[**consume_spotify_url**](SyndicationConsumerApi.md#consume_spotify_url) | **GET** /api/sell/{companyIdentifier}/syndication/spotify | Consume Spotify URL
[**consume_tik_tok_url**](SyndicationConsumerApi.md#consume_tik_tok_url) | **GET** /api/sell/{companyIdentifier}/syndication/tiktok | Consume TikTok URL
[**consume_twitter_url**](SyndicationConsumerApi.md#consume_twitter_url) | **GET** /api/sell/{companyIdentifier}/syndication/tweet | Consume Tweet URL
[**redirect_url**](SyndicationConsumerApi.md#redirect_url) | **GET** /api/sell/{companyIdentifier}/syndication/{syndicationEntryIdentifier}/redirect | Redirect WinkLinks link
[**show_syndication_account**](SyndicationConsumerApi.md#show_syndication_account) | **GET** /api/sell/syndication/{urlName} | Show Syndication Account
[**show_syndication_categories**](SyndicationConsumerApi.md#show_syndication_categories) | **GET** /api/sell/{companyIdentifier}/syndication/category/list | Show Syndication Categories
[**show_syndication_entry_grid**](SyndicationConsumerApi.md#show_syndication_entry_grid) | **POST** /api/sell/{companyIdentifier}/syndication/grid | Show Syndication Entries
[**track_share**](SyndicationConsumerApi.md#track_share) | **GET** /api/sell/{companyIdentifier}/syndication/{syndicationEntryIdentifier}/share | Track WinkLinks share


# **consume_facebook_page_url**
> FacebookEmbedNonAuthenticatedEntity consume_facebook_page_url(company_identifier, url, wink_version=wink_version)

Consume Facebook Page URL

Utility method for reading oEmbed data for Facebook.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.facebook_embed_non_authenticated_entity import FacebookEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'owner-1' # str | Consume this Facebook page URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Facebook Page URL
        api_response = api_instance.consume_facebook_page_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_facebook_page_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_facebook_page_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this Facebook page URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**FacebookEmbedNonAuthenticatedEntity**](FacebookEmbedNonAuthenticatedEntity.md)

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

# **consume_facebook_post_url**
> FacebookEmbedNonAuthenticatedEntity consume_facebook_post_url(company_identifier, url, wink_version=wink_version)

Consume Facebook Post URL

Utility method for reading oEmbed data for Facebook.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.facebook_embed_non_authenticated_entity import FacebookEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'owner-1' # str | Consume this Facebook post URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Facebook Post URL
        api_response = api_instance.consume_facebook_post_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_facebook_post_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_facebook_post_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this Facebook post URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**FacebookEmbedNonAuthenticatedEntity**](FacebookEmbedNonAuthenticatedEntity.md)

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

# **consume_facebook_video_url**
> FacebookEmbedNonAuthenticatedEntity consume_facebook_video_url(company_identifier, url, wink_version=wink_version)

Consume Facebook Video URL

Utility method for reading oEmbed data for Facebook.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.facebook_embed_non_authenticated_entity import FacebookEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'owner-1' # str | Consume this Facebook video URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Facebook Video URL
        api_response = api_instance.consume_facebook_video_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_facebook_video_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_facebook_video_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this Facebook video URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**FacebookEmbedNonAuthenticatedEntity**](FacebookEmbedNonAuthenticatedEntity.md)

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

# **consume_instagram_post_url**
> InstagramEmbedNonAuthenticatedEntity consume_instagram_post_url(company_identifier, url, wink_version=wink_version)

Consume Instagram Post URL

Utility method for reading oEmbed data for Instagram.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.instagram_embed_non_authenticated_entity import InstagramEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'owner-1' # str | Consume this Instagram post URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Instagram Post URL
        api_response = api_instance.consume_instagram_post_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_instagram_post_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_instagram_post_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this Instagram post URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**InstagramEmbedNonAuthenticatedEntity**](InstagramEmbedNonAuthenticatedEntity.md)

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

# **consume_spotify_url**
> SpotifyEmbedNonAuthenticatedEntity consume_spotify_url(company_identifier, url, wink_version=wink_version)

Consume Spotify URL

Utility method for reading oEmbed data from Spotify.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.spotify_embed_non_authenticated_entity import SpotifyEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'https://open.spotify.com%2Fshow%2F5eXZwvvxt3K2dxha3BSaAe' # str | Consume this Spotify URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Spotify URL
        api_response = api_instance.consume_spotify_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_spotify_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_spotify_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this Spotify URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**SpotifyEmbedNonAuthenticatedEntity**](SpotifyEmbedNonAuthenticatedEntity.md)

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

# **consume_tik_tok_url**
> TikTokEmbedNonAuthenticatedEntity consume_tik_tok_url(company_identifier, url, wink_version=wink_version)

Consume TikTok URL

Utility method for reading oEmbed data for Twitter.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.tik_tok_embed_non_authenticated_entity import TikTokEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'https://tiktok/1234' # str | Consume this TikTok URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume TikTok URL
        api_response = api_instance.consume_tik_tok_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_tik_tok_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_tik_tok_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this TikTok URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**TikTokEmbedNonAuthenticatedEntity**](TikTokEmbedNonAuthenticatedEntity.md)

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

# **consume_twitter_url**
> TwitterEmbedNonAuthenticatedEntity consume_twitter_url(company_identifier, url, wink_version=wink_version)

Consume Tweet URL

Utility method for reading oEmbed data for X.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.twitter_embed_non_authenticated_entity import TwitterEmbedNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Consume URL for this owner identifier.
    url = 'https://x.com/1234' # str | Consume this X URL.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Consume Tweet URL
        api_response = api_instance.consume_twitter_url(company_identifier, url, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->consume_twitter_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->consume_twitter_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Consume URL for this owner identifier. | 
 **url** | **str**| Consume this X URL. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**TwitterEmbedNonAuthenticatedEntity**](TwitterEmbedNonAuthenticatedEntity.md)

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

# **redirect_url**
> RedirectViewNonAuthenticatedEntity redirect_url(company_identifier, syndication_entry_identifier, user_agent, host, referer)

Redirect WinkLinks link

Utility method to track external URLs and redirect to it.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.redirect_view_non_authenticated_entity import RedirectViewNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Redirect for this owner identifier.
    syndication_entry_identifier = 'syndication-entry-1' # str | Redirect to URL for this syndication entry ID.
    user_agent = 'user_agent_example' # str | User-Agent header.
    host = 'host_example' # str | Host header.
    referer = 'referer_example' # str | Referrer header.

    try:
        # Redirect WinkLinks link
        api_response = api_instance.redirect_url(company_identifier, syndication_entry_identifier, user_agent, host, referer)
        print("The response of SyndicationConsumerApi->redirect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->redirect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Redirect for this owner identifier. | 
 **syndication_entry_identifier** | **str**| Redirect to URL for this syndication entry ID. | 
 **user_agent** | **str**| User-Agent header. | 
 **host** | **str**| Host header. | 
 **referer** | **str**| Referrer header. | 

### Return type

[**RedirectViewNonAuthenticatedEntity**](RedirectViewNonAuthenticatedEntity.md)

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

# **show_syndication_account**
> SyndicationAccountNonAuthenticatedEntity show_syndication_account(url_name, wink_version=wink_version, accept=accept)

Show Syndication Account

Retrieve syndication account details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.syndication_account_non_authenticated_entity import SyndicationAccountNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    url_name = 'url_name_example' # str | Account url name slug
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Syndication Account
        api_response = api_instance.show_syndication_account(url_name, wink_version=wink_version, accept=accept)
        print("The response of SyndicationConsumerApi->show_syndication_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->show_syndication_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_name** | **str**| Account url name slug | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**SyndicationAccountNonAuthenticatedEntity**](SyndicationAccountNonAuthenticatedEntity.md)

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

# **show_syndication_categories**
> List[KeyValuePairNonAuthenticatedEntity] show_syndication_categories(company_identifier, wink_version=wink_version, accept=accept)

Show Syndication Categories

Retrieve syndication category list.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'company_identifier_example' # str | Account ID
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Syndication Categories
        api_response = api_instance.show_syndication_categories(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of SyndicationConsumerApi->show_syndication_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->show_syndication_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Account ID | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md)

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

# **show_syndication_entry_grid**
> PageConsumableSyndicationEntryNonAuthenticatedEntity show_syndication_entry_grid(company_identifier, state_non_authenticated_entity, wink_version=wink_version)

Show Syndication Entries

Retrieve list of syndication entries.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.page_consumable_syndication_entry_non_authenticated_entity import PageConsumableSyndicationEntryNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.state_non_authenticated_entity import StateNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'company_identifier_example' # str | Account ID
    state_non_authenticated_entity = wink_sdk_affiliate_winklinks.StateNonAuthenticatedEntity() # StateNonAuthenticatedEntity | Body payload filtering and sorting preferences
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Syndication Entries
        api_response = api_instance.show_syndication_entry_grid(company_identifier, state_non_authenticated_entity, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->show_syndication_entry_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->show_syndication_entry_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Account ID | 
 **state_non_authenticated_entity** | [**StateNonAuthenticatedEntity**](StateNonAuthenticatedEntity.md)| Body payload filtering and sorting preferences | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageConsumableSyndicationEntryNonAuthenticatedEntity**](PageConsumableSyndicationEntryNonAuthenticatedEntity.md)

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

# **track_share**
> BooleanResponseNonAuthenticatedEntity track_share(company_identifier, syndication_entry_identifier, platform, user_agent, host, referer, wink_version=wink_version)

Track WinkLinks share

Utility method to track sharing a url.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate_winklinks
from wink_sdk_affiliate_winklinks.models.boolean_response_non_authenticated_entity import BooleanResponseNonAuthenticatedEntity
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
    api_instance = wink_sdk_affiliate_winklinks.SyndicationConsumerApi(api_client)
    company_identifier = 'owner-1' # str | Redirect for this owner identifier.
    syndication_entry_identifier = 'syndication-entry-1' # str | Redirect to URL for this syndication entry ID.
    platform = 'twitter' # str | Platform user is sharing on.
    user_agent = 'user_agent_example' # str | User-Agent header.
    host = 'host_example' # str | Host header.
    referer = 'referer_example' # str | Referrer header.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Track WinkLinks share
        api_response = api_instance.track_share(company_identifier, syndication_entry_identifier, platform, user_agent, host, referer, wink_version=wink_version)
        print("The response of SyndicationConsumerApi->track_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyndicationConsumerApi->track_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Redirect for this owner identifier. | 
 **syndication_entry_identifier** | **str**| Redirect to URL for this syndication entry ID. | 
 **platform** | **str**| Platform user is sharing on. | 
 **user_agent** | **str**| User-Agent header. | 
 **host** | **str**| Host header. | 
 **referer** | **str**| Referrer header. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseNonAuthenticatedEntity**](BooleanResponseNonAuthenticatedEntity.md)

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

