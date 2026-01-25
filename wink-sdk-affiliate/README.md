# wink-sdk-affiliate
 # Introduction
 Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.
 Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.

 # Integrations
 We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.

 # Intended Audience
 Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.
 - Hotel chains
 - Hotel brands
 - Travel tech companies
 - Destination sites
 - Integrators
 - Aggregators
 - Destination management companies
 - Travel agencies
 - OTAs

 ## APIs
 Not every integrator needs every API. For that reason, we have separated APIs into context.

### Common APIs

- [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.
- [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.
- [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to.
- [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account.
- [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features.
- [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work.
- [Reference](/reference): All APIs related to retrieving platform-supported taxonomies.
- [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.

### Consumer APIs

Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.

 - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.
 - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.
 - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..
 - [Booking](/booking): All APIs related to creating bookings on the platform.
 - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.

### Supplier APIs

Produce endpoints are for developers who want to create and manage travel inventory.

#### Property

- [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.
- [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.
- [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.
- [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.
- [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.
- [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.
- [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.

#### Affiliate

- [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.
- [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.
- [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.
- [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.
- [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.

## SDKs

We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).

### Inventory

 - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)
 - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)

### Payment

- Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java)
- Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)

## Usage

These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.

## Versioning

We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.

Current version: `2.0`
Prior versions: None


# Affiliate API
The Affiliate API exposes endpoints to manage affiliate accounts. This API lets you:

1. Create affiliates.
2. Create account managers

Browse the endpoints in the left navigation bar to get started.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.31.5
- Package version: 0.0.63
- Generator version: 7.18.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.63#egg=wink_sdk_affiliate&subdirectory=wink-sdk-affiliate
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.63#egg=wink_sdk_affiliate&subdirectory=wink_sdk_affiliate`)

Then import the package:
```python
import wink_sdk_affiliate
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_affiliate
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_affiliate
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
    managing_entity_identifier = 'hotel-1' # str | ManagingEntity identifier for which to accept invite to
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Accept Invite
        api_response = api_instance.accept_manager_invite(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->accept_manager_invite:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountManagerApi->accept_manager_invite: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountManagerApi* | [**accept_manager_invite**](docs/AccountManagerApi.md#accept_manager_invite) | **GET** /api/manager/invite/{managingEntityIdentifier}/accept | Accept Invite
*AccountManagerApi* | [**invite_manager**](docs/AccountManagerApi.md#invite_manager) | **PATCH** /api/manager/invite | Invite Manager
*AccountManagerApi* | [**reject_invite**](docs/AccountManagerApi.md#reject_invite) | **DELETE** /api/manager/invite/{managingEntityIdentifier}/reject | Reject Invite
*AccountManagerApi* | [**remove_company_user**](docs/AccountManagerApi.md#remove_company_user) | **DELETE** /api/manager/{email} | Remove Manager
*AccountManagerApi* | [**remove_manager_agency**](docs/AccountManagerApi.md#remove_manager_agency) | **DELETE** /api/manager/agency | Remove Managing Agency
*AccountManagerApi* | [**show_manager_invite_count**](docs/AccountManagerApi.md#show_manager_invite_count) | **GET** /api/manager/invite/count | Show Invite Count
*AccountManagerApi* | [**show_manager_invite_list**](docs/AccountManagerApi.md#show_manager_invite_list) | **GET** /api/manager/invite/list | Show Invites
*AccountManagerApi* | [**update_manager_agency**](docs/AccountManagerApi.md#update_manager_agency) | **PATCH** /api/manager/agency | Set Managing Agency
*AffiliateApi* | [**show_affiliate**](docs/AffiliateApi.md#show_affiliate) | **GET** /api/affiliate/{affiliateAccountIdentifier} | Show Affiliate
*AffiliateApi* | [**update_company_online_presence**](docs/AffiliateApi.md#update_company_online_presence) | **PATCH** /api/affiliate/{affiliateAccountIdentifier}/online-presence | Update Online Presence
*LeadsApi* | [**create_lead**](docs/LeadsApi.md#create_lead) | **POST** /api/affiliate/{companyIdentifier}/lead | Create Lead Request
*TravelAgentApi* | [**update_agent**](docs/TravelAgentApi.md#update_agent) | **PATCH** /api/affiliate/{companyIdentifier}/agent | Update Agent


## Documentation For Models

 - [AffiliateAccountAffiliate](docs/AffiliateAccountAffiliate.md)
 - [AffiliateAccountAgent](docs/AffiliateAccountAgent.md)
 - [CountResponseAffiliate](docs/CountResponseAffiliate.md)
 - [CountryLightweightAffiliate](docs/CountryLightweightAffiliate.md)
 - [CreateLead400Response](docs/CreateLead400Response.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoJsonPointAffiliate](docs/GeoJsonPointAffiliate.md)
 - [GeoNameLightweightAffiliate](docs/GeoNameLightweightAffiliate.md)
 - [GeoNameLightweightAgent](docs/GeoNameLightweightAgent.md)
 - [GooglePlaceDetailRequestAffiliate](docs/GooglePlaceDetailRequestAffiliate.md)
 - [InviteManagerRequestAffiliate](docs/InviteManagerRequestAffiliate.md)
 - [KeyValuePairAffiliate](docs/KeyValuePairAffiliate.md)
 - [ManagedByEntityAffiliate](docs/ManagedByEntityAffiliate.md)
 - [ManagedByEntityAgent](docs/ManagedByEntityAgent.md)
 - [ManagedByEntityRulesAffiliate](docs/ManagedByEntityRulesAffiliate.md)
 - [ManagerInviteAffiliate](docs/ManagerInviteAffiliate.md)
 - [ManagingEntityAffiliate](docs/ManagingEntityAffiliate.md)
 - [ManagingEntityManagerAffiliate](docs/ManagingEntityManagerAffiliate.md)
 - [ManagingEntityManagerAgent](docs/ManagingEntityManagerAgent.md)
 - [ManagingEntityProvisionAffiliate](docs/ManagingEntityProvisionAffiliate.md)
 - [ManagingEntitySupplier](docs/ManagingEntitySupplier.md)
 - [MediaAuthorAttributionAffiliate](docs/MediaAuthorAttributionAffiliate.md)
 - [OnlinePresenceAgent](docs/OnlinePresenceAgent.md)
 - [SimpleAddressAffiliate](docs/SimpleAddressAffiliate.md)
 - [SimpleDescriptionAffiliate](docs/SimpleDescriptionAffiliate.md)
 - [SimpleMultimediaAffiliate](docs/SimpleMultimediaAffiliate.md)
 - [SimpleMultimediaAgent](docs/SimpleMultimediaAgent.md)
 - [SubCountryLightweightAffiliate](docs/SubCountryLightweightAffiliate.md)
 - [SubSubCountryLightweightAffiliate](docs/SubSubCountryLightweightAffiliate.md)
 - [SupplierLeadAffiliate](docs/SupplierLeadAffiliate.md)
 - [TravelAgentAgent](docs/TravelAgentAgent.md)
 - [UpdateManagedByAgencyRequestAffiliate](docs/UpdateManagedByAgencyRequestAffiliate.md)
 - [UpdateTravelAgentRequestAgent](docs/UpdateTravelAgentRequestAgent.md)
 - [UpsertCompanyOnlinePresenceRequestAffiliate](docs/UpsertCompanyOnlinePresenceRequestAffiliate.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oauth2ClientCredentials"></a>
### oauth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: https://iam.wink.travel/oauth2/authorize
- **Scopes**: 
 - **inventory.read**: Read Wink data
 - **inventory.write**: Create Wink data
 - **inventory.remove**: Remove Wink data


## Author

bjorn@wink.travel

