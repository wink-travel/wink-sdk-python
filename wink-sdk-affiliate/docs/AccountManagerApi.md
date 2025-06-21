# wink_sdk_affiliate.AccountManagerApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_manager_invite**](AccountManagerApi.md#accept_manager_invite) | **GET** /api/manager/invite/{companyIdentifier}/accept | Accept Invite
[**invite_manager**](AccountManagerApi.md#invite_manager) | **PATCH** /api/manager/invite | Invite Manager
[**reject_invite**](AccountManagerApi.md#reject_invite) | **DELETE** /api/manager/invite/{companyIdentifier}/reject | Reject Invite
[**remove_company_user**](AccountManagerApi.md#remove_company_user) | **DELETE** /api/manager/{email} | Remove Manager
[**remove_manager_agency**](AccountManagerApi.md#remove_manager_agency) | **DELETE** /api/manager/agency | Remove Managing Agency
[**show_manager_invite_list**](AccountManagerApi.md#show_manager_invite_list) | **GET** /api/manager/invite/list | Show Invites
[**update_manager_agency**](AccountManagerApi.md#update_manager_agency) | **PATCH** /api/manager/agency | Set Managing Agency


# **accept_manager_invite**
> ManagerInviteAcceptedSupplier accept_manager_invite(company_identifier, wink_version=wink_version, accept=accept)

Accept Invite

Accepts the invite to manager a property or account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.manager_invite_accepted_supplier import ManagerInviteAcceptedSupplier
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    company_identifier = 'hotel-1' # str | AffiliateAccountLightweight identifier for which to accept invite to
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Accept Invite
        api_response = api_instance.accept_manager_invite(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->accept_manager_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->accept_manager_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| AffiliateAccountLightweight identifier for which to accept invite to | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ManagerInviteAcceptedSupplier**](ManagerInviteAcceptedSupplier.md)

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

# **invite_manager**
> AffiliateAccountAffiliate invite_manager(invite_manager_request_affiliate, wink_version=wink_version)

Invite Manager

Invite user to be a manager for this company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.invite_manager_request_affiliate import InviteManagerRequestAffiliate
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    invite_manager_request_affiliate = wink_sdk_affiliate.InviteManagerRequestAffiliate() # InviteManagerRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Invite Manager
        api_response = api_instance.invite_manager(invite_manager_request_affiliate, wink_version=wink_version)
        print("The response of AccountManagerApi->invite_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->invite_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_manager_request_affiliate** | [**InviteManagerRequestAffiliate**](InviteManagerRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **reject_invite**
> AffiliateAccountSupplier reject_invite(company_identifier, wink_version=wink_version, accept=accept)

Reject Invite

Remove manager by specified identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_supplier import AffiliateAccountSupplier
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    company_identifier = 'hotel-1' # str | Remove manager from this property identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Reject Invite
        api_response = api_instance.reject_invite(company_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->reject_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->reject_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Remove manager from this property identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountSupplier**](AffiliateAccountSupplier.md)

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

# **remove_company_user**
> AffiliateAccountAffiliate remove_company_user(email, wink_version=wink_version, accept=accept)

Remove Manager

Disassociate user from this company.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    email = 'email_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Manager
        api_response = api_instance.remove_company_user(email, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->remove_company_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->remove_company_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **remove_manager_agency**
> AffiliateAccountAffiliate remove_manager_agency(wink_version=wink_version, accept=accept)

Remove Managing Agency

Unset managing agency.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Managing Agency
        api_response = api_instance.remove_manager_agency(wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->remove_manager_agency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->remove_manager_agency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

# **show_manager_invite_list**
> List[ManagerInviteAffiliate] show_manager_invite_list(wink_version=wink_version, accept=accept)

Show Invites

Retrieve list of invites for user

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.manager_invite_affiliate import ManagerInviteAffiliate
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Invites
        api_response = api_instance.show_manager_invite_list(wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->show_manager_invite_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->show_manager_invite_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ManagerInviteAffiliate]**](ManagerInviteAffiliate.md)

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

# **update_manager_agency**
> AffiliateAccountAffiliate update_manager_agency(upsert_managed_by_agency_request_affiliate, wink_version=wink_version)

Set Managing Agency

Indicates that the entity is managed by an another entity on the platform. This does not give privileges to manage the account but entitles the agency to a commission.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_affiliate
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate
from wink_sdk_affiliate.models.upsert_managed_by_agency_request_affiliate import UpsertManagedByAgencyRequestAffiliate
from wink_sdk_affiliate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_affiliate.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_affiliate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_affiliate.AccountManagerApi(api_client)
    upsert_managed_by_agency_request_affiliate = wink_sdk_affiliate.UpsertManagedByAgencyRequestAffiliate() # UpsertManagedByAgencyRequestAffiliate | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Set Managing Agency
        api_response = api_instance.update_manager_agency(upsert_managed_by_agency_request_affiliate, wink_version=wink_version)
        print("The response of AccountManagerApi->update_manager_agency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->update_manager_agency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_managed_by_agency_request_affiliate** | [**UpsertManagedByAgencyRequestAffiliate**](UpsertManagedByAgencyRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAffiliate**](AffiliateAccountAffiliate.md)

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

