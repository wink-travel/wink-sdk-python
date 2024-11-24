# wink-sdk-extranet-booking
 # Introduction
 Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.
 Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.

 # Integrations
 We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.

 # Intended Audience
 Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.
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

### Test API

 - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.

### Common APIs

- [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account.
- [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.

### Consume APIs
Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.

 - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.
 - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.
 - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..
 - [Booking](/booking): All APIs related to creating bookings on the platform.
 - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.

 ### Produce APIs
 Produce endpoints are for developers who want to create and manage travel blocking.

 #### Property
 - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.
 - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.
 - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.
 - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.
 - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.
 - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.
 - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.

 #### Affiliate
 - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.
 - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.
 - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.
 - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.
 - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.

 #### Rate provider
 - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.

 ### Taxonomy APIs
 Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.

 - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.

 ### Insight APIs
 Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.

 - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.

 ### Payment APIs
 Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.

 - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.

 ## SDKs
 We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).

 - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)

 ## Usage
 These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.

 ## Versioning
 We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.

 ## Release history
 - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md


# Extranet Booking API
The Booking API exposes endpoints to manage bookings. This API lets you:

1. Booking: Manage bookings including cancellations.
2. Review: Manage user reviews.
3. Sync w. Calendar: Manage calendar sync with your favorite calendar software

Browse the endpoints in the left navigation bar to get started.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 30.7.10
- Package version: 0.0.3
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_booking
```

Or you can install it directly from the repository using:
```sh
pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_extranet_booking&subdirectory=wink-sdk-extranet-booking
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wink-travel/wink-sdk-python.git@v0.0.3#egg=wink_sdk_extranet_booking&subdirectory=wink_sdk_extranet_booking`)

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
    api_instance = wink_sdk_extranet_booking.BookingApi(api_client)
    property_identifier = 'hotel-1' # str | Cancel booking for hotel with this identifier
    booking_identifier = 'booking-1' # str | Cancel booking with this identifier
    cancellation_detail_supplier = wink_sdk_extranet_booking.CancellationDetailSupplier() # CancellationDetailSupplier | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel Booking
        api_response = api_instance.cancel_hotel_booking(property_identifier, booking_identifier, cancellation_detail_supplier, wink_version=wink_version)
        print("The response of BookingApi->cancel_hotel_booking:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BookingApi->cancel_hotel_booking: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wink.travel*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BookingApi* | [**cancel_hotel_booking**](docs/BookingApi.md#cancel_hotel_booking) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancel | Cancel Booking
*BookingApi* | [**is_booking_cancellable**](docs/BookingApi.md#is_booking_cancellable) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/cancellable | Is Booking Cancellable
*BookingApi* | [**request_refund**](docs/BookingApi.md#request_refund) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/request-refund | Request refund
*BookingApi* | [**resend_booking_confirmation_email**](docs/BookingApi.md#resend_booking_confirmation_email) | **PATCH** /api/property/{propertyIdentifier}/booking/{bookingIdentifier}/resend | Resend Booking Confirmation
*BookingApi* | [**show_active_affiliates**](docs/BookingApi.md#show_active_affiliates) | **GET** /api/property/{propertyIdentifier}/booking/owner/list | Show Active Affiliates
*BookingApi* | [**show_active_master_rates**](docs/BookingApi.md#show_active_master_rates) | **GET** /api/property/{propertyIdentifier}/booking/roomrate/list | Show Active Master Rates
*BookingApi* | [**show_booking_analytics**](docs/BookingApi.md#show_booking_analytics) | **POST** /api/property/{propertyIdentifier}/booking/analytics | Property Booking Analytics
*BookingApi* | [**show_booking_overview**](docs/BookingApi.md#show_booking_overview) | **GET** /api/property/{propertyIdentifier}/booking/overview | Property Booking Overview
*BookingApi* | [**show_hotel_booking**](docs/BookingApi.md#show_hotel_booking) | **GET** /api/property/{propertyIdentifier}/booking/{bookingIdentifier} | Show Booking
*BookingApi* | [**show_hotel_bookings**](docs/BookingApi.md#show_hotel_bookings) | **POST** /api/property/{propertyIdentifier}/booking/grid | Search Bookings
*BookingApi* | [**show_hotel_bookings1**](docs/BookingApi.md#show_hotel_bookings1) | **GET** /api/property/{propertyIdentifier}/booking/list | Show Bookings
*CalendarSyncApi* | [**caldav**](docs/CalendarSyncApi.md#caldav) | **GET** /api/cal/property/{propertyIdentifier}/booking/list | CalDAV calendar
*CalendarSyncApi* | [**generate_cal_dav_auth**](docs/CalendarSyncApi.md#generate_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth/regen | Create CalDAV connection
*CalendarSyncApi* | [**retrieve_cal_dav_auth**](docs/CalendarSyncApi.md#retrieve_cal_dav_auth) | **GET** /api/property/{propertyIdentifier}/caldav/auth | Show CalDAV Connection
*ReviewApi* | [**respond_to_review**](docs/ReviewApi.md#respond_to_review) | **PATCH** /api/property/{propertyIdentifier}/review/{reviewIdentifier}/response | Respond to Review
*ReviewApi* | [**show_review**](docs/ReviewApi.md#show_review) | **GET** /api/property/{propertyIdentifier}/review/{reviewIdentifier} | Show Review
*ReviewApi* | [**show_review_count**](docs/ReviewApi.md#show_review_count) | **GET** /api/property/{propertyIdentifier}/review/count | Show Review Count
*ReviewApi* | [**show_reviews**](docs/ReviewApi.md#show_reviews) | **POST** /api/property/{propertyIdentifier}/review/grid | Show Reviews


## Documentation For Models

 - [AddressSupplier](docs/AddressSupplier.md)
 - [AddressSupplierDetails](docs/AddressSupplierDetails.md)
 - [AggregateDescriptorSupplier](docs/AggregateDescriptorSupplier.md)
 - [AuthenticatedUserSupplier](docs/AuthenticatedUserSupplier.md)
 - [AuthenticatedUserSupplierDetails](docs/AuthenticatedUserSupplierDetails.md)
 - [BedSupplier](docs/BedSupplier.md)
 - [BedSupplierDetails](docs/BedSupplierDetails.md)
 - [BedroomConfigurationSupplier](docs/BedroomConfigurationSupplier.md)
 - [BedroomConfigurationSupplierDetails](docs/BedroomConfigurationSupplierDetails.md)
 - [BedroomSupplier](docs/BedroomSupplier.md)
 - [BedroomSupplierDetails](docs/BedroomSupplierDetails.md)
 - [BeneficiaryChargeSupplier](docs/BeneficiaryChargeSupplier.md)
 - [BeneficiaryChargeSupplierDetails](docs/BeneficiaryChargeSupplierDetails.md)
 - [BeneficiarySupplier](docs/BeneficiarySupplier.md)
 - [BeneficiarySupplierDetails](docs/BeneficiarySupplierDetails.md)
 - [BookingAnalyticsSupplier](docs/BookingAnalyticsSupplier.md)
 - [BookingAncillarySupplier](docs/BookingAncillarySupplier.md)
 - [BookingAncillarySupplierDetails](docs/BookingAncillarySupplierDetails.md)
 - [BookingCancellableSupplier](docs/BookingCancellableSupplier.md)
 - [BookingContractItemSupplier](docs/BookingContractItemSupplier.md)
 - [BookingContractItemSupplierDetails](docs/BookingContractItemSupplierDetails.md)
 - [BookingContractPaymentDetailsSupplier](docs/BookingContractPaymentDetailsSupplier.md)
 - [BookingContractPaymentDetailsSupplierDetails](docs/BookingContractPaymentDetailsSupplierDetails.md)
 - [BookingContractSupplier](docs/BookingContractSupplier.md)
 - [BookingContractSupplierDetails](docs/BookingContractSupplierDetails.md)
 - [BookingItineraryRoomConfigurationChildSupplier](docs/BookingItineraryRoomConfigurationChildSupplier.md)
 - [BookingItineraryRoomConfigurationChildSupplierDetails](docs/BookingItineraryRoomConfigurationChildSupplierDetails.md)
 - [BookingItineraryRoomConfigurationSupplier](docs/BookingItineraryRoomConfigurationSupplier.md)
 - [BookingItineraryRoomConfigurationSupplierDetails](docs/BookingItineraryRoomConfigurationSupplierDetails.md)
 - [BookingItinerarySupplier](docs/BookingItinerarySupplier.md)
 - [BookingItinerarySupplierDetails](docs/BookingItinerarySupplierDetails.md)
 - [BookingOverviewRequestSupplier](docs/BookingOverviewRequestSupplier.md)
 - [BookingSupplier](docs/BookingSupplier.md)
 - [BookingSupplierDetails](docs/BookingSupplierDetails.md)
 - [BookingUserSessionSupplier](docs/BookingUserSessionSupplier.md)
 - [BookingUserSessionSupplierDetails](docs/BookingUserSessionSupplierDetails.md)
 - [BookingUserSupplier](docs/BookingUserSupplier.md)
 - [BookingUserSupplierDetails](docs/BookingUserSupplierDetails.md)
 - [BookingViewSupplier](docs/BookingViewSupplier.md)
 - [BookingViewSupplierDetails](docs/BookingViewSupplierDetails.md)
 - [BooleanResponseSupplier](docs/BooleanResponseSupplier.md)
 - [CalDavResponseSupplier](docs/CalDavResponseSupplier.md)
 - [CancellationDetailSupplier](docs/CancellationDetailSupplier.md)
 - [CancellationPolicyExceptionSupplier](docs/CancellationPolicyExceptionSupplier.md)
 - [CancellationPolicyExceptionSupplierDetails](docs/CancellationPolicyExceptionSupplierDetails.md)
 - [CancellationPolicyExceptionsSupplier](docs/CancellationPolicyExceptionsSupplier.md)
 - [CancellationPolicyExceptionsSupplierDetails](docs/CancellationPolicyExceptionsSupplierDetails.md)
 - [CancellationPolicySupplier](docs/CancellationPolicySupplier.md)
 - [CancellationPolicySupplierDetails](docs/CancellationPolicySupplierDetails.md)
 - [ChartCategoryAxisSupplier](docs/ChartCategoryAxisSupplier.md)
 - [ChartLegendSupplier](docs/ChartLegendSupplier.md)
 - [ChartSeriesSupplier](docs/ChartSeriesSupplier.md)
 - [ChartTitleSupplier](docs/ChartTitleSupplier.md)
 - [ChildSupplier](docs/ChildSupplier.md)
 - [ChildSupplierDetails](docs/ChildSupplierDetails.md)
 - [CommissionableEntrySupplier](docs/CommissionableEntrySupplier.md)
 - [CommissionableEntrySupplierDetails](docs/CommissionableEntrySupplierDetails.md)
 - [CompositeFilterDescriptorSupplier](docs/CompositeFilterDescriptorSupplier.md)
 - [ContactSupplier](docs/ContactSupplier.md)
 - [ContactSupplierDetails](docs/ContactSupplierDetails.md)
 - [CountResponseSupplier](docs/CountResponseSupplier.md)
 - [CountrySupplier](docs/CountrySupplier.md)
 - [CountrySupplierDetails](docs/CountrySupplierDetails.md)
 - [CustomMonetaryAmount](docs/CustomMonetaryAmount.md)
 - [DailyRateSupplier](docs/DailyRateSupplier.md)
 - [DailyRateSupplierDetails](docs/DailyRateSupplierDetails.md)
 - [DowPatternGroupSupplier](docs/DowPatternGroupSupplier.md)
 - [DowPatternGroupSupplierDetails](docs/DowPatternGroupSupplierDetails.md)
 - [EngineConfigurationBookingReportSupplier](docs/EngineConfigurationBookingReportSupplier.md)
 - [EngineConfigurationBookingReportSupplierDetails](docs/EngineConfigurationBookingReportSupplierDetails.md)
 - [EngineConfigurationThemeSupplier](docs/EngineConfigurationThemeSupplier.md)
 - [EngineConfigurationThemeSupplierDetails](docs/EngineConfigurationThemeSupplierDetails.md)
 - [ExtraChargeSupplier](docs/ExtraChargeSupplier.md)
 - [ExtraChargeSupplierDetails](docs/ExtraChargeSupplierDetails.md)
 - [ExtraChargesSupplier](docs/ExtraChargesSupplier.md)
 - [ExtraChargesSupplierDetails](docs/ExtraChargesSupplierDetails.md)
 - [FeeSupplier](docs/FeeSupplier.md)
 - [FeeSupplierDetails](docs/FeeSupplierDetails.md)
 - [FilterDescriptorSupplier](docs/FilterDescriptorSupplier.md)
 - [GeneralManagerSupplier](docs/GeneralManagerSupplier.md)
 - [GeneralManagerSupplierDetails](docs/GeneralManagerSupplierDetails.md)
 - [GenericErrorMessage](docs/GenericErrorMessage.md)
 - [GeoJsonPointSupplier](docs/GeoJsonPointSupplier.md)
 - [GeoJsonPointSupplierDetails](docs/GeoJsonPointSupplierDetails.md)
 - [GeoNameSupplier](docs/GeoNameSupplier.md)
 - [GeoNameSupplierDetails](docs/GeoNameSupplierDetails.md)
 - [GroupDescriptorSupplier](docs/GroupDescriptorSupplier.md)
 - [GroupedBookingSalesMetricsSupplierDetails](docs/GroupedBookingSalesMetricsSupplierDetails.md)
 - [GuestRoomSupplier](docs/GuestRoomSupplier.md)
 - [GuestRoomSupplierDetails](docs/GuestRoomSupplierDetails.md)
 - [GuestUserSupplier](docs/GuestUserSupplier.md)
 - [GuestUserSupplierDetails](docs/GuestUserSupplierDetails.md)
 - [HotelOnMapSupplier](docs/HotelOnMapSupplier.md)
 - [HotelOnMapSupplierDetails](docs/HotelOnMapSupplierDetails.md)
 - [ImageAttributionSupplier](docs/ImageAttributionSupplier.md)
 - [ImageAttributionSupplierDetails](docs/ImageAttributionSupplierDetails.md)
 - [KeyValuePairSupplier](docs/KeyValuePairSupplier.md)
 - [LineChartSupplier](docs/LineChartSupplier.md)
 - [LocalizedDescriptionSupplier](docs/LocalizedDescriptionSupplier.md)
 - [LocalizedDescriptionSupplierDetails](docs/LocalizedDescriptionSupplierDetails.md)
 - [LocalizedPriceSupplier](docs/LocalizedPriceSupplier.md)
 - [LocalizedPriceSupplierDetails](docs/LocalizedPriceSupplierDetails.md)
 - [PageBookingViewSupplier](docs/PageBookingViewSupplier.md)
 - [PageReviewViewSupplier](docs/PageReviewViewSupplier.md)
 - [PageableObjectSupplier](docs/PageableObjectSupplier.md)
 - [PayoutFeeSupplier](docs/PayoutFeeSupplier.md)
 - [PayoutFeeSupplierDetails](docs/PayoutFeeSupplierDetails.md)
 - [PayoutSupplier](docs/PayoutSupplier.md)
 - [PayoutSupplierDetails](docs/PayoutSupplierDetails.md)
 - [PendingRefundSupplier](docs/PendingRefundSupplier.md)
 - [PendingRefundSupplierDetails](docs/PendingRefundSupplierDetails.md)
 - [PersonalSupplier](docs/PersonalSupplier.md)
 - [PersonalSupplierDetails](docs/PersonalSupplierDetails.md)
 - [PetInfoDtoSupplier](docs/PetInfoDtoSupplier.md)
 - [PetInfoDtoSupplierDetails](docs/PetInfoDtoSupplierDetails.md)
 - [PreferencesSupplier](docs/PreferencesSupplier.md)
 - [PreferencesSupplierDetails](docs/PreferencesSupplierDetails.md)
 - [ProfileSupplier](docs/ProfileSupplier.md)
 - [ProfileSupplierDetails](docs/ProfileSupplierDetails.md)
 - [ProfileUserSupplier](docs/ProfileUserSupplier.md)
 - [ProfileUserSupplierDetails](docs/ProfileUserSupplierDetails.md)
 - [PropertyBookingRefundRequestSupplier](docs/PropertyBookingRefundRequestSupplier.md)
 - [PropertyPolicySupplier](docs/PropertyPolicySupplier.md)
 - [PropertyPolicySupplierDetails](docs/PropertyPolicySupplierDetails.md)
 - [QuoteSupplier](docs/QuoteSupplier.md)
 - [QuoteSupplierDetails](docs/QuoteSupplierDetails.md)
 - [RatePlanLevelFeeSupplier](docs/RatePlanLevelFeeSupplier.md)
 - [RatePlanLevelFeeSupplierDetails](docs/RatePlanLevelFeeSupplierDetails.md)
 - [RatePlanSupplier](docs/RatePlanSupplier.md)
 - [RatePlanSupplierDetails](docs/RatePlanSupplierDetails.md)
 - [RefundSupplier](docs/RefundSupplier.md)
 - [RefundSupplierDetails](docs/RefundSupplierDetails.md)
 - [ReportingAncillarySupplier](docs/ReportingAncillarySupplier.md)
 - [ReportingAncillarySupplierDetails](docs/ReportingAncillarySupplierDetails.md)
 - [ReportingDailyRateSupplier](docs/ReportingDailyRateSupplier.md)
 - [ReportingDailyRateSupplierDetails](docs/ReportingDailyRateSupplierDetails.md)
 - [ReportingExtraChargeSupplier](docs/ReportingExtraChargeSupplier.md)
 - [ReportingExtraChargeSupplierDetails](docs/ReportingExtraChargeSupplierDetails.md)
 - [ReviewAnswerSupplier](docs/ReviewAnswerSupplier.md)
 - [ReviewAnswerSupplierDetails](docs/ReviewAnswerSupplierDetails.md)
 - [ReviewResponseSupplier](docs/ReviewResponseSupplier.md)
 - [ReviewSupplier](docs/ReviewSupplier.md)
 - [ReviewSupplierDetails](docs/ReviewSupplierDetails.md)
 - [ReviewUserSupplier](docs/ReviewUserSupplier.md)
 - [ReviewUserSupplierDetails](docs/ReviewUserSupplierDetails.md)
 - [ReviewViewSupplier](docs/ReviewViewSupplier.md)
 - [RoomConfigurationSupplier](docs/RoomConfigurationSupplier.md)
 - [RoomConfigurationSupplierDetails](docs/RoomConfigurationSupplierDetails.md)
 - [RoomStaySupplier](docs/RoomStaySupplier.md)
 - [RoomStaySupplierDetails](docs/RoomStaySupplierDetails.md)
 - [ShowReview400Response](docs/ShowReview400Response.md)
 - [SimpleDateTimeItinerarySupplier](docs/SimpleDateTimeItinerarySupplier.md)
 - [SimpleDateTimeItinerarySupplierDetails](docs/SimpleDateTimeItinerarySupplierDetails.md)
 - [SimpleDescriptionSupplier](docs/SimpleDescriptionSupplier.md)
 - [SimpleDescriptionSupplierDetails](docs/SimpleDescriptionSupplierDetails.md)
 - [SimpleMultimediaSupplier](docs/SimpleMultimediaSupplier.md)
 - [SimpleMultimediaSupplierDetails](docs/SimpleMultimediaSupplierDetails.md)
 - [SocialSupplier](docs/SocialSupplier.md)
 - [SocialSupplierDetails](docs/SocialSupplierDetails.md)
 - [SortDescriptorSupplier](docs/SortDescriptorSupplier.md)
 - [SortObject](docs/SortObject.md)
 - [StateSupplier](docs/StateSupplier.md)
 - [StayRateSupplier](docs/StayRateSupplier.md)
 - [StayRateSupplierDetails](docs/StayRateSupplierDetails.md)
 - [SubCountrySupplier](docs/SubCountrySupplier.md)
 - [SubCountrySupplierDetails](docs/SubCountrySupplierDetails.md)
 - [SubSubCountrySupplier](docs/SubSubCountrySupplier.md)
 - [SubSubCountrySupplierDetails](docs/SubSubCountrySupplierDetails.md)
 - [SupplierContractItemPolicySupplier](docs/SupplierContractItemPolicySupplier.md)
 - [SupplierContractItemPolicySupplierDetails](docs/SupplierContractItemPolicySupplierDetails.md)
 - [TransactionalTravelInventorySupplier](docs/TransactionalTravelInventorySupplier.md)
 - [TransactionalTravelInventorySupplierDetails](docs/TransactionalTravelInventorySupplierDetails.md)
 - [TravelInventoryRecognitionSupplier](docs/TravelInventoryRecognitionSupplier.md)
 - [TravelInventoryRecognitionSupplierDetails](docs/TravelInventoryRecognitionSupplierDetails.md)
 - [VariableChargeSupplier](docs/VariableChargeSupplier.md)
 - [VariableChargeSupplierDetails](docs/VariableChargeSupplierDetails.md)


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


