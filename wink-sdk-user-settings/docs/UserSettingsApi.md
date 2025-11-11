# wink_sdk_user_settings.UserSettingsApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](UserSettingsApi.md#change_password) | **PATCH** /api/user-settings/change-password | Change Password
[**show_user_profile**](UserSettingsApi.md#show_user_profile) | **GET** /api/user-settings/profile | Show User Profile
[**update_user_profile**](UserSettingsApi.md#update_user_profile) | **PATCH** /api/user-settings/profile | Update User Profile


# **change_password**
> BooleanResponse change_password(change_password_request, wink_version=wink_version)

Change Password

Updates currently authenticated user's password.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.boolean_response import BooleanResponse
from wink_sdk_user_settings.models.change_password_request import ChangePasswordRequest
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.UserSettingsApi(api_client)
    change_password_request = wink_sdk_user_settings.ChangePasswordRequest() # ChangePasswordRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Change Password
        api_response = api_instance.change_password(change_password_request, wink_version=wink_version)
        print("The response of UserSettingsApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

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

# **show_user_profile**
> UpsertUserProfileResponse show_user_profile(wink_version=wink_version, accept=accept)

Show User Profile

Retrieves user profile data.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.upsert_user_profile_response import UpsertUserProfileResponse
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.UserSettingsApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show User Profile
        api_response = api_instance.show_user_profile(wink_version=wink_version, accept=accept)
        print("The response of UserSettingsApi->show_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->show_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**UpsertUserProfileResponse**](UpsertUserProfileResponse.md)

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

# **update_user_profile**
> UpsertUserProfileResponse update_user_profile(upsert_user_profile_request, wink_version=wink_version)

Update User Profile

Updates user profile data.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_user_settings
from wink_sdk_user_settings.models.upsert_user_profile_request import UpsertUserProfileRequest
from wink_sdk_user_settings.models.upsert_user_profile_response import UpsertUserProfileResponse
from wink_sdk_user_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_user_settings.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_user_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_user_settings.UserSettingsApi(api_client)
    upsert_user_profile_request = wink_sdk_user_settings.UpsertUserProfileRequest() # UpsertUserProfileRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update User Profile
        api_response = api_instance.update_user_profile(upsert_user_profile_request, wink_version=wink_version)
        print("The response of UserSettingsApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_user_profile_request** | [**UpsertUserProfileRequest**](UpsertUserProfileRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**UpsertUserProfileResponse**](UpsertUserProfileResponse.md)

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

