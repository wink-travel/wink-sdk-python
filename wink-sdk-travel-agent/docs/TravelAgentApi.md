# wink_sdk_travel_agent.TravelAgentApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_booking_as_travel_agent**](TravelAgentApi.md#cancel_booking_as_travel_agent) | **PATCH** /api/affiliate/{companyIdentifier}/booking/{bookingIdentifier} | Cancel Booking
[**create_agent_booking**](TravelAgentApi.md#create_agent_booking) | **POST** /api/booking/agent | Create Agent Booking
[**resend_booking_confirmation_email_as_travel_agent**](TravelAgentApi.md#resend_booking_confirmation_email_as_travel_agent) | **PATCH** /api/affiliate/{companyIdentifier}/booking/{bookingIdentifier}/resend | Resend Booking Confirmation
[**show_booking_as_travel_agent**](TravelAgentApi.md#show_booking_as_travel_agent) | **GET** /api/affiliate/{companyIdentifier}/booking/{bookingIdentifier} | Show Booking
[**show_booking_grid_as_travel_agent**](TravelAgentApi.md#show_booking_grid_as_travel_agent) | **POST** /api/affiliate/{companyIdentifier}/booking/grid | Show Bookings
[**update_agent**](TravelAgentApi.md#update_agent) | **PATCH** /api/affiliate/{companyIdentifier}/agent | Update Agent


# **cancel_booking_as_travel_agent**
> BookingAgent cancel_booking_as_travel_agent(company_identifier, booking_identifier, cancellation_detail_agent, wink_version=wink_version)

Cancel Booking

Cancel a booking by its booking identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.booking_agent import BookingAgent
from wink_sdk_travel_agent.models.cancellation_detail_agent import CancellationDetailAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    company_identifier = 'company-1' # str | Cancel booking owned by company identifier
    booking_identifier = 'booking-1' # str | Cancel booking by identifier
    cancellation_detail_agent = wink_sdk_travel_agent.CancellationDetailAgent() # CancellationDetailAgent | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel Booking
        api_response = api_instance.cancel_booking_as_travel_agent(company_identifier, booking_identifier, cancellation_detail_agent, wink_version=wink_version)
        print("The response of TravelAgentApi->cancel_booking_as_travel_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->cancel_booking_as_travel_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Cancel booking owned by company identifier | 
 **booking_identifier** | **str**| Cancel booking by identifier | 
 **cancellation_detail_agent** | [**CancellationDetailAgent**](CancellationDetailAgent.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingAgent**](BookingAgent.md)

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

# **create_agent_booking**
> BookingConfirmationsAgent create_agent_booking(create_agent_booking_request_agent, wink_version=wink_version)

Create Agent Booking

Create agent booking. Expects the agent to be a registered agent with TripPay and have available funds to cover the booking amount.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.booking_confirmations_agent import BookingConfirmationsAgent
from wink_sdk_travel_agent.models.create_agent_booking_request_agent import CreateAgentBookingRequestAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    create_agent_booking_request_agent = wink_sdk_travel_agent.CreateAgentBookingRequestAgent() # CreateAgentBookingRequestAgent | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Agent Booking
        api_response = api_instance.create_agent_booking(create_agent_booking_request_agent, wink_version=wink_version)
        print("The response of TravelAgentApi->create_agent_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->create_agent_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agent_booking_request_agent** | [**CreateAgentBookingRequestAgent**](CreateAgentBookingRequestAgent.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingConfirmationsAgent**](BookingConfirmationsAgent.md)

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

# **resend_booking_confirmation_email_as_travel_agent**
> BooleanResponseAgent resend_booking_confirmation_email_as_travel_agent(company_identifier, booking_identifier, body, wink_version=wink_version)

Resend Booking Confirmation

Resends booking confirmation email to traveler.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.boolean_response_agent import BooleanResponseAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    company_identifier = 'company-1' # str | Resend booking owned by company identifier
    booking_identifier = 'booking-1' # str | Resend booking by identifier
    body = None # object | Empty request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Resend Booking Confirmation
        api_response = api_instance.resend_booking_confirmation_email_as_travel_agent(company_identifier, booking_identifier, body, wink_version=wink_version)
        print("The response of TravelAgentApi->resend_booking_confirmation_email_as_travel_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->resend_booking_confirmation_email_as_travel_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Resend booking owned by company identifier | 
 **booking_identifier** | **str**| Resend booking by identifier | 
 **body** | **object**| Empty request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BooleanResponseAgent**](BooleanResponseAgent.md)

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

# **show_booking_as_travel_agent**
> BookingAgent show_booking_as_travel_agent(company_identifier, booking_identifier, wink_version=wink_version, accept=accept)

Show Booking

Show a booking record by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.booking_agent import BookingAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    company_identifier = 'company-1' # str | Show booking for company identifier
    booking_identifier = 'booking-1' # str | Show booking with booking identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Booking
        api_response = api_instance.show_booking_as_travel_agent(company_identifier, booking_identifier, wink_version=wink_version, accept=accept)
        print("The response of TravelAgentApi->show_booking_as_travel_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->show_booking_as_travel_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show booking for company identifier | 
 **booking_identifier** | **str**| Show booking with booking identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BookingAgent**](BookingAgent.md)

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

# **show_booking_grid_as_travel_agent**
> PageBookingAgent show_booking_grid_as_travel_agent(company_identifier, state_agent, wink_version=wink_version)

Show Bookings

Show bookings for the company that helped create those booking.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.page_booking_agent import PageBookingAgent
from wink_sdk_travel_agent.models.state_agent import StateAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    company_identifier = 'company-1' # str | Show bookings for company identifier
    state_agent = wink_sdk_travel_agent.StateAgent() # StateAgent | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Bookings
        api_response = api_instance.show_booking_grid_as_travel_agent(company_identifier, state_agent, wink_version=wink_version)
        print("The response of TravelAgentApi->show_booking_grid_as_travel_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->show_booking_grid_as_travel_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Show bookings for company identifier | 
 **state_agent** | [**StateAgent**](StateAgent.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageBookingAgent**](PageBookingAgent.md)

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

# **update_agent**
> AffiliateAccountAgent update_agent(company_identifier, upsert_travel_agent_request_agent, wink_version=wink_version)

Update Agent

Update an existing agent

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_travel_agent
from wink_sdk_travel_agent.models.affiliate_account_agent import AffiliateAccountAgent
from wink_sdk_travel_agent.models.upsert_travel_agent_request_agent import UpsertTravelAgentRequestAgent
from wink_sdk_travel_agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_travel_agent.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_travel_agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_travel_agent.TravelAgentApi(api_client)
    company_identifier = 'company_identifier_example' # str | Update agent by company id
    upsert_travel_agent_request_agent = wink_sdk_travel_agent.UpsertTravelAgentRequestAgent() # UpsertTravelAgentRequestAgent | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Agent
        api_response = api_instance.update_agent(company_identifier, upsert_travel_agent_request_agent, wink_version=wink_version)
        print("The response of TravelAgentApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelAgentApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Update agent by company id | 
 **upsert_travel_agent_request_agent** | [**UpsertTravelAgentRequestAgent**](UpsertTravelAgentRequestAgent.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateAccountAgent**](AffiliateAccountAgent.md)

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

