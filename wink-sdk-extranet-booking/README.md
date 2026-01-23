# wink-sdk-extranet-booking
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

# Extranet Booking API
The Booking API exposes endpoints to manage bookings. This API lets you:

1. Booking: Manage bookings including cancellations.
2. Review: Manage user reviews.
3. Sync w. Calendar: Manage calendar sync with your favorite calendar software

Browse the endpoints in the left navigation bar to get started.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.31.3
- Package version: 0.0.62
- Generator version: 7.18.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_booking
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.62#egg=wink_sdk_extranet_booking&subdirectory=wink-sdk-extranet-booking
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.62#egg=wink_sdk_extranet_booking&subdirectory=wink_sdk_extranet_booking`)

Then import the package:
```python
import wink_sdk_extranet_booking
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wink_sdk_extranet_booking
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import wink_sdk_extranet_booking
from wink_sdk_extranet_booking.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_booking.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with wink_sdk_extranet_booking.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_booking.AnalyticsApi(api_client)
    property_identifier = 'hotel-1' # str | Show active booking count for hotel with this identifier
    booking_overview_request_supplier = wink_sdk_extranet_booking.BookingOverviewRequestSupplier() # BookingOverviewRequestSupplier | Overview request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Property Booking Analytics
        api_response = api_instance.show_property_booking_analytics(property_identifier, booking_overview_request_supplier, wink_version=wink_version)
        print("The response of AnalyticsApi->show_property_booking_analytics:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsApi->show_property_booking_analytics: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsApi* | [**show_property_booking_analytics**](docs/AnalyticsApi.md#show_property_booking_analytics) | **POST** /api/property/{propertyIdentifier}/booking/analytics | Property Booking Analytics
*CalendarSyncApi* | [**caldav**](docs/CalendarSyncApi.md#caldav) | **GET** /api/cal/property/{propertyIdentifier}/booking/list | Load CalDAV Calendar
*CalendarSyncApi* | [**generate_cal_dav_auth**](docs/CalendarSyncApi.md#generate_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth/regen | Create CalDAV Connection
*CalendarSyncApi* | [**retrieve_cal_dav_auth**](docs/CalendarSyncApi.md#retrieve_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth | Show CalDAV Connection
*ConsumerBookingApi* | [**respond_to_review**](docs/ConsumerBookingApi.md#respond_to_review) | **PATCH** /api/property/{propertyIdentifier}/review/{reviewIdentifier}/response | Respond to Review
*PropertyBookingApi* | [**cancel_hotel_booking**](docs/PropertyBookingApi.md#cancel_hotel_booking) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancel | Cancel Booking
*PropertyBookingApi* | [**generate_booking_report**](docs/PropertyBookingApi.md#generate_booking_report) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/report/pdf | Download Booking
*PropertyBookingApi* | [**is_booking_cancellable**](docs/PropertyBookingApi.md#is_booking_cancellable) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancellable | Is Booking Cancellable
*PropertyBookingApi* | [**request_refund**](docs/PropertyBookingApi.md#request_refund) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/request-refund | Request refund
*PropertyBookingApi* | [**resend_booking_confirmation_email**](docs/PropertyBookingApi.md#resend_booking_confirmation_email) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/resend | Resend Booking Confirmation
*PropertyBookingApi* | [**show_active_affiliates**](docs/PropertyBookingApi.md#show_active_affiliates) | **GET** /api/property/{propertyIdentifier}/booking/owner/list | Show Active Affiliates
*PropertyBookingApi* | [**show_active_master_rates**](docs/PropertyBookingApi.md#show_active_master_rates) | **GET** /api/property/{propertyIdentifier}/booking/roomrate/list | Show Active Master Rates
*PropertyBookingApi* | [**show_booking_overview**](docs/PropertyBookingApi.md#show_booking_overview) | **GET** /api/property/{propertyIdentifier}/booking/overview | Property Booking Overview
*PropertyBookingApi* | [**show_hotel_booking**](docs/PropertyBookingApi.md#show_hotel_booking) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier} | Show Booking
*PropertyBookingApi* | [**show_hotel_bookings**](docs/PropertyBookingApi.md#show_hotel_bookings) | **POST** /api/property/{propertyIdentifier}/booking/grid | Search Bookings
*PropertyBookingApi* | [**show_hotel_bookings1**](docs/PropertyBookingApi.md#show_hotel_bookings1) | **GET** /api/property/{propertyIdentifier}/booking/list | Show Bookings
*ReviewApi* | [**show_review**](docs/ReviewApi.md#show_review) | **GET** /api/property/{propertyIdentifier}/review/{reviewIdentifier} | Show Review
*ReviewApi* | [**show_review_count**](docs/ReviewApi.md#show_review_count) | **GET** /api/property/{propertyIdentifier}/review/count | Show Review Count
*ReviewApi* | [**show_reviews**](docs/ReviewApi.md#show_reviews) | **POST** /api/property/{propertyIdentifier}/review/grid | Show Reviews
*TestBookingApi* | [**create_test_booking**](docs/TestBookingApi.md#create_test_booking) | **POST** /api/property/{propertyIdentifier}/sandbox/booking | Test Rate / Availability


## Documentation For Models

 - [AddOnLightweightSupplierDetails](docs/AddOnLightweightSupplierDetails.md)
 - [AddOnLocalizedInventorySupplierDetails](docs/AddOnLocalizedInventorySupplierDetails.md)
 - [AggregateDescriptorSupplier](docs/AggregateDescriptorSupplier.md)
 - [AuthenticatedUserSupplierDetails](docs/AuthenticatedUserSupplierDetails.md)
 - [BedSupplierDetails](docs/BedSupplierDetails.md)
 - [BedroomConfigurationSupplierDetails](docs/BedroomConfigurationSupplierDetails.md)
 - [BedroomSupplierDetails](docs/BedroomSupplierDetails.md)
 - [BeneficiaryChargeSupplierDetails](docs/BeneficiaryChargeSupplierDetails.md)
 - [BeneficiarySupplierDetails](docs/BeneficiarySupplierDetails.md)
 - [BookingAnalyticsSupplier](docs/BookingAnalyticsSupplier.md)
 - [BookingAncillarySupplierDetails](docs/BookingAncillarySupplierDetails.md)
 - [BookingCancellableSupplier](docs/BookingCancellableSupplier.md)
 - [BookingContractItemSupplierDetails](docs/BookingContractItemSupplierDetails.md)
 - [BookingContractPaymentDetailsSupplierDetails](docs/BookingContractPaymentDetailsSupplierDetails.md)
 - [BookingItineraryRoomConfigurationChildSupplierDetails](docs/BookingItineraryRoomConfigurationChildSupplierDetails.md)
 - [BookingItineraryRoomConfigurationSupplierDetails](docs/BookingItineraryRoomConfigurationSupplierDetails.md)
 - [BookingItinerarySupplierDetails](docs/BookingItinerarySupplierDetails.md)
 - [BookingOverviewRequestSupplier](docs/BookingOverviewRequestSupplier.md)
 - [BookingSupplier](docs/BookingSupplier.md)
 - [BookingSupplierDetails](docs/BookingSupplierDetails.md)
 - [BookingTestNotificationSupplierDetails](docs/BookingTestNotificationSupplierDetails.md)
 - [BookingTestRequestSupplierDetails](docs/BookingTestRequestSupplierDetails.md)
 - [BookingUserSessionSupplierDetails](docs/BookingUserSessionSupplierDetails.md)
 - [BookingUserSupplierDetails](docs/BookingUserSupplierDetails.md)
 - [BooleanResponseSupplier](docs/BooleanResponseSupplier.md)
 - [CalDavResponseSupplier](docs/CalDavResponseSupplier.md)
 - [CancellationDetailSupplier](docs/CancellationDetailSupplier.md)
 - [CancellationPolicyExceptionSupplierDetails](docs/CancellationPolicyExceptionSupplierDetails.md)
 - [CancellationPolicyExceptionsSupplierDetails](docs/CancellationPolicyExceptionsSupplierDetails.md)
 - [CancellationPolicyLightweightSupplierDetails](docs/CancellationPolicyLightweightSupplierDetails.md)
 - [ChannelNameSupplierDetails](docs/ChannelNameSupplierDetails.md)
 - [ChartCategoryAxisSupplier](docs/ChartCategoryAxisSupplier.md)
 - [ChartLegendSupplier](docs/ChartLegendSupplier.md)
 - [ChartSeriesSupplier](docs/ChartSeriesSupplier.md)
 - [ChartTitleSupplier](docs/ChartTitleSupplier.md)
 - [ChildSupplierDetails](docs/ChildSupplierDetails.md)
 - [CommissionableEntrySupplierDetails](docs/CommissionableEntrySupplierDetails.md)
 - [CompositeFilterDescriptorSupplier](docs/CompositeFilterDescriptorSupplier.md)
 - [ContactSupplierDetails](docs/ContactSupplierDetails.md)
 - [CountResponseSupplier](docs/CountResponseSupplier.md)
 - [CountryLightweightSupplierDetails](docs/CountryLightweightSupplierDetails.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [CustomizationLightweightSupplierDetails](docs/CustomizationLightweightSupplierDetails.md)
 - [CustomizationThemeColorsSupplierDetails](docs/CustomizationThemeColorsSupplierDetails.md)
 - [DailyRateRateSupplierDetails](docs/DailyRateRateSupplierDetails.md)
 - [DailyRateSupplierDetails](docs/DailyRateSupplierDetails.md)
 - [DowPatternGroupSupplierDetails](docs/DowPatternGroupSupplierDetails.md)
 - [ExtraChargeSupplierDetails](docs/ExtraChargeSupplierDetails.md)
 - [ExtraChargesSupplierDetails](docs/ExtraChargesSupplierDetails.md)
 - [FeeSupplierDetails](docs/FeeSupplierDetails.md)
 - [FilterDescriptorSupplier](docs/FilterDescriptorSupplier.md)
 - [GeneralManagerSupplierDetails](docs/GeneralManagerSupplierDetails.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoIpLightweightSupplierDetails](docs/GeoIpLightweightSupplierDetails.md)
 - [GeoJsonPointSupplierDetails](docs/GeoJsonPointSupplierDetails.md)
 - [GeoNameCountrySupplierDetails](docs/GeoNameCountrySupplierDetails.md)
 - [GeoNameLightweightSupplierDetails](docs/GeoNameLightweightSupplierDetails.md)
 - [GroupDescriptorSupplier](docs/GroupDescriptorSupplier.md)
 - [GroupedBookingSalesMetricsSupplierDetails](docs/GroupedBookingSalesMetricsSupplierDetails.md)
 - [GuestRoomLightweightSupplierDetails](docs/GuestRoomLightweightSupplierDetails.md)
 - [GuestUserSupplierDetails](docs/GuestUserSupplierDetails.md)
 - [KeyValuePairSupplier](docs/KeyValuePairSupplier.md)
 - [LineChartSupplier](docs/LineChartSupplier.md)
 - [LocalizedDescriptionSupplierDetails](docs/LocalizedDescriptionSupplierDetails.md)
 - [LocalizedPriceSupplierDetails](docs/LocalizedPriceSupplierDetails.md)
 - [LocalizedTransactionalTravelInventorySupplierDetails](docs/LocalizedTransactionalTravelInventorySupplierDetails.md)
 - [MediaAuthorAttributionSupplierDetails](docs/MediaAuthorAttributionSupplierDetails.md)
 - [PageBookingSupplier](docs/PageBookingSupplier.md)
 - [PageReviewSupplier](docs/PageReviewSupplier.md)
 - [PageableObjectSupplier](docs/PageableObjectSupplier.md)
 - [PayoutFeeSupplierDetails](docs/PayoutFeeSupplierDetails.md)
 - [PayoutSupplierDetails](docs/PayoutSupplierDetails.md)
 - [PendingRefundSupplierDetails](docs/PendingRefundSupplierDetails.md)
 - [PerkLightweightSupplierDetails](docs/PerkLightweightSupplierDetails.md)
 - [PersonalSupplierDetails](docs/PersonalSupplierDetails.md)
 - [PetInfoLightweightSupplierDetails](docs/PetInfoLightweightSupplierDetails.md)
 - [PreferencesSupplierDetails](docs/PreferencesSupplierDetails.md)
 - [ProfileLightweightSupplierDetails](docs/ProfileLightweightSupplierDetails.md)
 - [ProfileUserSupplierDetails](docs/ProfileUserSupplierDetails.md)
 - [PropertyAggregateLightweightSupplierDetails](docs/PropertyAggregateLightweightSupplierDetails.md)
 - [PropertyBookingRefundRequestSupplier](docs/PropertyBookingRefundRequestSupplier.md)
 - [PropertyPolicySupplierDetails](docs/PropertyPolicySupplierDetails.md)
 - [QuoteLightweightSupplierDetails](docs/QuoteLightweightSupplierDetails.md)
 - [RatePlanLevelFeeSupplierDetails](docs/RatePlanLevelFeeSupplierDetails.md)
 - [RefundSupplierDetails](docs/RefundSupplierDetails.md)
 - [ReportingAncillarySupplierDetails](docs/ReportingAncillarySupplierDetails.md)
 - [ReportingDailyRateSupplierDetails](docs/ReportingDailyRateSupplierDetails.md)
 - [ReportingExtraChargeSupplierDetails](docs/ReportingExtraChargeSupplierDetails.md)
 - [ReviewAnswerSupplierDetails](docs/ReviewAnswerSupplierDetails.md)
 - [ReviewLightweightSupplierDetails](docs/ReviewLightweightSupplierDetails.md)
 - [ReviewResponseSupplier](docs/ReviewResponseSupplier.md)
 - [ReviewSupplier](docs/ReviewSupplier.md)
 - [ReviewUserSupplierDetails](docs/ReviewUserSupplierDetails.md)
 - [RoomConfigurationPriceRatePlanSupplierDetails](docs/RoomConfigurationPriceRatePlanSupplierDetails.md)
 - [RoomConfigurationPriceSupplierDetails](docs/RoomConfigurationPriceSupplierDetails.md)
 - [RoomConfigurationSupplierDetails](docs/RoomConfigurationSupplierDetails.md)
 - [RoomStaySupplierDetails](docs/RoomStaySupplierDetails.md)
 - [ShowReview400Response](docs/ShowReview400Response.md)
 - [SimpleAddressSupplierDetails](docs/SimpleAddressSupplierDetails.md)
 - [SimpleDateTimeItinerarySupplierDetails](docs/SimpleDateTimeItinerarySupplierDetails.md)
 - [SimpleDescriptionSupplierDetails](docs/SimpleDescriptionSupplierDetails.md)
 - [SimpleMultimediaSupplierDetails](docs/SimpleMultimediaSupplierDetails.md)
 - [SocialSupplierDetails](docs/SocialSupplierDetails.md)
 - [SortDescriptorSupplier](docs/SortDescriptorSupplier.md)
 - [SortObjectSupplier](docs/SortObjectSupplier.md)
 - [StateSupplier](docs/StateSupplier.md)
 - [StayRateSupplierDetails](docs/StayRateSupplierDetails.md)
 - [SubCountryLightweightSupplierDetails](docs/SubCountryLightweightSupplierDetails.md)
 - [SubSubCountryLightweightSupplierDetails](docs/SubSubCountryLightweightSupplierDetails.md)
 - [SupplierContractItemPolicySupplierDetails](docs/SupplierContractItemPolicySupplierDetails.md)
 - [TransactionalTravelInventorySupplierDetails](docs/TransactionalTravelInventorySupplierDetails.md)
 - [TravelInventoryRecognitionSupplierDetails](docs/TravelInventoryRecognitionSupplierDetails.md)
 - [VariableChargeSupplierDetails](docs/VariableChargeSupplierDetails.md)
 - [VerifyRatesRequestSupplierDetails](docs/VerifyRatesRequestSupplierDetails.md)
 - [WinkBookingContractSupplierDetails](docs/WinkBookingContractSupplierDetails.md)


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

