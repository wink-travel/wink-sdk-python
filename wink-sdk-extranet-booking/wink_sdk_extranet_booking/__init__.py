# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  # Extranet Booking API The Booking API exposes endpoints to manage bookings. This API lets you:  1. Booking: Manage bookings including cancellations. 2. Review: Manage user reviews. 3. Sync w. Calendar: Manage calendar sync with your favorite calendar software  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.31.2
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.61"

# Define package exports
__all__ = [
    "AnalyticsApi",
    "CalendarSyncApi",
    "ConsumerBookingApi",
    "PropertyBookingApi",
    "ReviewApi",
    "TestBookingApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AddOnLightweightSupplierDetails",
    "AddOnLocalizedInventorySupplierDetails",
    "AggregateDescriptorSupplier",
    "AuthenticatedUserSupplierDetails",
    "BedSupplierDetails",
    "BedroomConfigurationSupplierDetails",
    "BedroomSupplierDetails",
    "BeneficiaryChargeSupplierDetails",
    "BeneficiarySupplierDetails",
    "BookingAnalyticsSupplier",
    "BookingAncillarySupplierDetails",
    "BookingCancellableSupplier",
    "BookingContractItemSupplierDetails",
    "BookingContractPaymentDetailsSupplierDetails",
    "BookingItineraryRoomConfigurationChildSupplierDetails",
    "BookingItineraryRoomConfigurationSupplierDetails",
    "BookingItinerarySupplierDetails",
    "BookingOverviewRequestSupplier",
    "BookingSupplier",
    "BookingSupplierDetails",
    "BookingTestNotificationSupplierDetails",
    "BookingTestRequestSupplierDetails",
    "BookingUserSessionSupplierDetails",
    "BookingUserSupplierDetails",
    "BooleanResponseSupplier",
    "CalDavResponseSupplier",
    "CancellationDetailSupplier",
    "CancellationPolicyExceptionSupplierDetails",
    "CancellationPolicyExceptionsSupplierDetails",
    "CancellationPolicyLightweightSupplierDetails",
    "ChannelNameSupplierDetails",
    "ChartCategoryAxisSupplier",
    "ChartLegendSupplier",
    "ChartSeriesSupplier",
    "ChartTitleSupplier",
    "ChildSupplierDetails",
    "CommissionableEntrySupplierDetails",
    "CompositeFilterDescriptorSupplier",
    "ContactSupplierDetails",
    "CountResponseSupplier",
    "CountryLightweightSupplierDetails",
    "CustomMonetaryAmount",
    "CustomizationLightweightSupplierDetails",
    "CustomizationThemeColorsSupplierDetails",
    "DailyRateRateSupplierDetails",
    "DailyRateSupplierDetails",
    "DowPatternGroupSupplierDetails",
    "ExtraChargeSupplierDetails",
    "ExtraChargesSupplierDetails",
    "FeeSupplierDetails",
    "FilterDescriptorSupplier",
    "GeneralManagerSupplierDetails",
    "GenericErrorMessage",
    "GeoIpLightweightSupplierDetails",
    "GeoJsonPointSupplierDetails",
    "GeoNameCountrySupplierDetails",
    "GeoNameLightweightSupplierDetails",
    "GroupDescriptorSupplier",
    "GroupedBookingSalesMetricsSupplierDetails",
    "GuestRoomLightweightSupplierDetails",
    "GuestUserSupplierDetails",
    "KeyValuePairSupplier",
    "LineChartSupplier",
    "LocalizedDescriptionSupplierDetails",
    "LocalizedPriceSupplierDetails",
    "LocalizedTransactionalTravelInventorySupplierDetails",
    "MediaAuthorAttributionSupplierDetails",
    "PageBookingSupplier",
    "PageReviewSupplier",
    "PageableObjectSupplier",
    "PayoutFeeSupplierDetails",
    "PayoutSupplierDetails",
    "PendingRefundSupplierDetails",
    "PerkLightweightSupplierDetails",
    "PersonalSupplierDetails",
    "PetInfoLightweightSupplierDetails",
    "PreferencesSupplierDetails",
    "ProfileLightweightSupplierDetails",
    "ProfileUserSupplierDetails",
    "PropertyAggregateLightweightSupplierDetails",
    "PropertyBookingRefundRequestSupplier",
    "PropertyPolicySupplierDetails",
    "QuoteLightweightSupplierDetails",
    "RatePlanLevelFeeSupplierDetails",
    "RefundSupplierDetails",
    "ReportingAncillarySupplierDetails",
    "ReportingDailyRateSupplierDetails",
    "ReportingExtraChargeSupplierDetails",
    "ReviewAnswerSupplierDetails",
    "ReviewLightweightSupplierDetails",
    "ReviewResponseSupplier",
    "ReviewSupplier",
    "ReviewUserSupplierDetails",
    "RoomConfigurationPriceRatePlanSupplierDetails",
    "RoomConfigurationPriceSupplierDetails",
    "RoomConfigurationSupplierDetails",
    "RoomStaySupplierDetails",
    "ShowReview400Response",
    "SimpleAddressSupplierDetails",
    "SimpleDateTimeItinerarySupplierDetails",
    "SimpleDescriptionSupplierDetails",
    "SimpleMultimediaSupplierDetails",
    "SocialSupplierDetails",
    "SortDescriptorSupplier",
    "SortObjectSupplier",
    "StateSupplier",
    "StayRateSupplierDetails",
    "SubCountryLightweightSupplierDetails",
    "SubSubCountryLightweightSupplierDetails",
    "SupplierContractItemPolicySupplierDetails",
    "TransactionalTravelInventorySupplierDetails",
    "TravelInventoryRecognitionSupplierDetails",
    "VariableChargeSupplierDetails",
    "VerifyRatesRequestSupplierDetails",
    "WinkBookingContractSupplierDetails",
]

# import apis into sdk package
from wink_sdk_extranet_booking.api.analytics_api import AnalyticsApi as AnalyticsApi
from wink_sdk_extranet_booking.api.calendar_sync_api import CalendarSyncApi as CalendarSyncApi
from wink_sdk_extranet_booking.api.consumer_booking_api import ConsumerBookingApi as ConsumerBookingApi
from wink_sdk_extranet_booking.api.property_booking_api import PropertyBookingApi as PropertyBookingApi
from wink_sdk_extranet_booking.api.review_api import ReviewApi as ReviewApi
from wink_sdk_extranet_booking.api.test_booking_api import TestBookingApi as TestBookingApi

# import ApiClient
from wink_sdk_extranet_booking.api_response import ApiResponse as ApiResponse
from wink_sdk_extranet_booking.api_client import ApiClient as ApiClient
from wink_sdk_extranet_booking.configuration import Configuration as Configuration
from wink_sdk_extranet_booking.exceptions import OpenApiException as OpenApiException
from wink_sdk_extranet_booking.exceptions import ApiTypeError as ApiTypeError
from wink_sdk_extranet_booking.exceptions import ApiValueError as ApiValueError
from wink_sdk_extranet_booking.exceptions import ApiKeyError as ApiKeyError
from wink_sdk_extranet_booking.exceptions import ApiAttributeError as ApiAttributeError
from wink_sdk_extranet_booking.exceptions import ApiException as ApiException

# import models into sdk package
from wink_sdk_extranet_booking.models.add_on_lightweight_supplier_details import AddOnLightweightSupplierDetails as AddOnLightweightSupplierDetails
from wink_sdk_extranet_booking.models.add_on_localized_inventory_supplier_details import AddOnLocalizedInventorySupplierDetails as AddOnLocalizedInventorySupplierDetails
from wink_sdk_extranet_booking.models.aggregate_descriptor_supplier import AggregateDescriptorSupplier as AggregateDescriptorSupplier
from wink_sdk_extranet_booking.models.authenticated_user_supplier_details import AuthenticatedUserSupplierDetails as AuthenticatedUserSupplierDetails
from wink_sdk_extranet_booking.models.bed_supplier_details import BedSupplierDetails as BedSupplierDetails
from wink_sdk_extranet_booking.models.bedroom_configuration_supplier_details import BedroomConfigurationSupplierDetails as BedroomConfigurationSupplierDetails
from wink_sdk_extranet_booking.models.bedroom_supplier_details import BedroomSupplierDetails as BedroomSupplierDetails
from wink_sdk_extranet_booking.models.beneficiary_charge_supplier_details import BeneficiaryChargeSupplierDetails as BeneficiaryChargeSupplierDetails
from wink_sdk_extranet_booking.models.beneficiary_supplier_details import BeneficiarySupplierDetails as BeneficiarySupplierDetails
from wink_sdk_extranet_booking.models.booking_analytics_supplier import BookingAnalyticsSupplier as BookingAnalyticsSupplier
from wink_sdk_extranet_booking.models.booking_ancillary_supplier_details import BookingAncillarySupplierDetails as BookingAncillarySupplierDetails
from wink_sdk_extranet_booking.models.booking_cancellable_supplier import BookingCancellableSupplier as BookingCancellableSupplier
from wink_sdk_extranet_booking.models.booking_contract_item_supplier_details import BookingContractItemSupplierDetails as BookingContractItemSupplierDetails
from wink_sdk_extranet_booking.models.booking_contract_payment_details_supplier_details import BookingContractPaymentDetailsSupplierDetails as BookingContractPaymentDetailsSupplierDetails
from wink_sdk_extranet_booking.models.booking_itinerary_room_configuration_child_supplier_details import BookingItineraryRoomConfigurationChildSupplierDetails as BookingItineraryRoomConfigurationChildSupplierDetails
from wink_sdk_extranet_booking.models.booking_itinerary_room_configuration_supplier_details import BookingItineraryRoomConfigurationSupplierDetails as BookingItineraryRoomConfigurationSupplierDetails
from wink_sdk_extranet_booking.models.booking_itinerary_supplier_details import BookingItinerarySupplierDetails as BookingItinerarySupplierDetails
from wink_sdk_extranet_booking.models.booking_overview_request_supplier import BookingOverviewRequestSupplier as BookingOverviewRequestSupplier
from wink_sdk_extranet_booking.models.booking_supplier import BookingSupplier as BookingSupplier
from wink_sdk_extranet_booking.models.booking_supplier_details import BookingSupplierDetails as BookingSupplierDetails
from wink_sdk_extranet_booking.models.booking_test_notification_supplier_details import BookingTestNotificationSupplierDetails as BookingTestNotificationSupplierDetails
from wink_sdk_extranet_booking.models.booking_test_request_supplier_details import BookingTestRequestSupplierDetails as BookingTestRequestSupplierDetails
from wink_sdk_extranet_booking.models.booking_user_session_supplier_details import BookingUserSessionSupplierDetails as BookingUserSessionSupplierDetails
from wink_sdk_extranet_booking.models.booking_user_supplier_details import BookingUserSupplierDetails as BookingUserSupplierDetails
from wink_sdk_extranet_booking.models.boolean_response_supplier import BooleanResponseSupplier as BooleanResponseSupplier
from wink_sdk_extranet_booking.models.cal_dav_response_supplier import CalDavResponseSupplier as CalDavResponseSupplier
from wink_sdk_extranet_booking.models.cancellation_detail_supplier import CancellationDetailSupplier as CancellationDetailSupplier
from wink_sdk_extranet_booking.models.cancellation_policy_exception_supplier_details import CancellationPolicyExceptionSupplierDetails as CancellationPolicyExceptionSupplierDetails
from wink_sdk_extranet_booking.models.cancellation_policy_exceptions_supplier_details import CancellationPolicyExceptionsSupplierDetails as CancellationPolicyExceptionsSupplierDetails
from wink_sdk_extranet_booking.models.cancellation_policy_lightweight_supplier_details import CancellationPolicyLightweightSupplierDetails as CancellationPolicyLightweightSupplierDetails
from wink_sdk_extranet_booking.models.channel_name_supplier_details import ChannelNameSupplierDetails as ChannelNameSupplierDetails
from wink_sdk_extranet_booking.models.chart_category_axis_supplier import ChartCategoryAxisSupplier as ChartCategoryAxisSupplier
from wink_sdk_extranet_booking.models.chart_legend_supplier import ChartLegendSupplier as ChartLegendSupplier
from wink_sdk_extranet_booking.models.chart_series_supplier import ChartSeriesSupplier as ChartSeriesSupplier
from wink_sdk_extranet_booking.models.chart_title_supplier import ChartTitleSupplier as ChartTitleSupplier
from wink_sdk_extranet_booking.models.child_supplier_details import ChildSupplierDetails as ChildSupplierDetails
from wink_sdk_extranet_booking.models.commissionable_entry_supplier_details import CommissionableEntrySupplierDetails as CommissionableEntrySupplierDetails
from wink_sdk_extranet_booking.models.composite_filter_descriptor_supplier import CompositeFilterDescriptorSupplier as CompositeFilterDescriptorSupplier
from wink_sdk_extranet_booking.models.contact_supplier_details import ContactSupplierDetails as ContactSupplierDetails
from wink_sdk_extranet_booking.models.count_response_supplier import CountResponseSupplier as CountResponseSupplier
from wink_sdk_extranet_booking.models.country_lightweight_supplier_details import CountryLightweightSupplierDetails as CountryLightweightSupplierDetails
from wink_sdk_extranet_booking.models.custom_monetary_amount import CustomMonetaryAmount as CustomMonetaryAmount
from wink_sdk_extranet_booking.models.customization_lightweight_supplier_details import CustomizationLightweightSupplierDetails as CustomizationLightweightSupplierDetails
from wink_sdk_extranet_booking.models.customization_theme_colors_supplier_details import CustomizationThemeColorsSupplierDetails as CustomizationThemeColorsSupplierDetails
from wink_sdk_extranet_booking.models.daily_rate_rate_supplier_details import DailyRateRateSupplierDetails as DailyRateRateSupplierDetails
from wink_sdk_extranet_booking.models.daily_rate_supplier_details import DailyRateSupplierDetails as DailyRateSupplierDetails
from wink_sdk_extranet_booking.models.dow_pattern_group_supplier_details import DowPatternGroupSupplierDetails as DowPatternGroupSupplierDetails
from wink_sdk_extranet_booking.models.extra_charge_supplier_details import ExtraChargeSupplierDetails as ExtraChargeSupplierDetails
from wink_sdk_extranet_booking.models.extra_charges_supplier_details import ExtraChargesSupplierDetails as ExtraChargesSupplierDetails
from wink_sdk_extranet_booking.models.fee_supplier_details import FeeSupplierDetails as FeeSupplierDetails
from wink_sdk_extranet_booking.models.filter_descriptor_supplier import FilterDescriptorSupplier as FilterDescriptorSupplier
from wink_sdk_extranet_booking.models.general_manager_supplier_details import GeneralManagerSupplierDetails as GeneralManagerSupplierDetails
from wink_sdk_extranet_booking.models.generic_error_message import GenericErrorMessage as GenericErrorMessage
from wink_sdk_extranet_booking.models.geo_ip_lightweight_supplier_details import GeoIpLightweightSupplierDetails as GeoIpLightweightSupplierDetails
from wink_sdk_extranet_booking.models.geo_json_point_supplier_details import GeoJsonPointSupplierDetails as GeoJsonPointSupplierDetails
from wink_sdk_extranet_booking.models.geo_name_country_supplier_details import GeoNameCountrySupplierDetails as GeoNameCountrySupplierDetails
from wink_sdk_extranet_booking.models.geo_name_lightweight_supplier_details import GeoNameLightweightSupplierDetails as GeoNameLightweightSupplierDetails
from wink_sdk_extranet_booking.models.group_descriptor_supplier import GroupDescriptorSupplier as GroupDescriptorSupplier
from wink_sdk_extranet_booking.models.grouped_booking_sales_metrics_supplier_details import GroupedBookingSalesMetricsSupplierDetails as GroupedBookingSalesMetricsSupplierDetails
from wink_sdk_extranet_booking.models.guest_room_lightweight_supplier_details import GuestRoomLightweightSupplierDetails as GuestRoomLightweightSupplierDetails
from wink_sdk_extranet_booking.models.guest_user_supplier_details import GuestUserSupplierDetails as GuestUserSupplierDetails
from wink_sdk_extranet_booking.models.key_value_pair_supplier import KeyValuePairSupplier as KeyValuePairSupplier
from wink_sdk_extranet_booking.models.line_chart_supplier import LineChartSupplier as LineChartSupplier
from wink_sdk_extranet_booking.models.localized_description_supplier_details import LocalizedDescriptionSupplierDetails as LocalizedDescriptionSupplierDetails
from wink_sdk_extranet_booking.models.localized_price_supplier_details import LocalizedPriceSupplierDetails as LocalizedPriceSupplierDetails
from wink_sdk_extranet_booking.models.localized_transactional_travel_inventory_supplier_details import LocalizedTransactionalTravelInventorySupplierDetails as LocalizedTransactionalTravelInventorySupplierDetails
from wink_sdk_extranet_booking.models.media_author_attribution_supplier_details import MediaAuthorAttributionSupplierDetails as MediaAuthorAttributionSupplierDetails
from wink_sdk_extranet_booking.models.page_booking_supplier import PageBookingSupplier as PageBookingSupplier
from wink_sdk_extranet_booking.models.page_review_supplier import PageReviewSupplier as PageReviewSupplier
from wink_sdk_extranet_booking.models.pageable_object_supplier import PageableObjectSupplier as PageableObjectSupplier
from wink_sdk_extranet_booking.models.payout_fee_supplier_details import PayoutFeeSupplierDetails as PayoutFeeSupplierDetails
from wink_sdk_extranet_booking.models.payout_supplier_details import PayoutSupplierDetails as PayoutSupplierDetails
from wink_sdk_extranet_booking.models.pending_refund_supplier_details import PendingRefundSupplierDetails as PendingRefundSupplierDetails
from wink_sdk_extranet_booking.models.perk_lightweight_supplier_details import PerkLightweightSupplierDetails as PerkLightweightSupplierDetails
from wink_sdk_extranet_booking.models.personal_supplier_details import PersonalSupplierDetails as PersonalSupplierDetails
from wink_sdk_extranet_booking.models.pet_info_lightweight_supplier_details import PetInfoLightweightSupplierDetails as PetInfoLightweightSupplierDetails
from wink_sdk_extranet_booking.models.preferences_supplier_details import PreferencesSupplierDetails as PreferencesSupplierDetails
from wink_sdk_extranet_booking.models.profile_lightweight_supplier_details import ProfileLightweightSupplierDetails as ProfileLightweightSupplierDetails
from wink_sdk_extranet_booking.models.profile_user_supplier_details import ProfileUserSupplierDetails as ProfileUserSupplierDetails
from wink_sdk_extranet_booking.models.property_aggregate_lightweight_supplier_details import PropertyAggregateLightweightSupplierDetails as PropertyAggregateLightweightSupplierDetails
from wink_sdk_extranet_booking.models.property_booking_refund_request_supplier import PropertyBookingRefundRequestSupplier as PropertyBookingRefundRequestSupplier
from wink_sdk_extranet_booking.models.property_policy_supplier_details import PropertyPolicySupplierDetails as PropertyPolicySupplierDetails
from wink_sdk_extranet_booking.models.quote_lightweight_supplier_details import QuoteLightweightSupplierDetails as QuoteLightweightSupplierDetails
from wink_sdk_extranet_booking.models.rate_plan_level_fee_supplier_details import RatePlanLevelFeeSupplierDetails as RatePlanLevelFeeSupplierDetails
from wink_sdk_extranet_booking.models.refund_supplier_details import RefundSupplierDetails as RefundSupplierDetails
from wink_sdk_extranet_booking.models.reporting_ancillary_supplier_details import ReportingAncillarySupplierDetails as ReportingAncillarySupplierDetails
from wink_sdk_extranet_booking.models.reporting_daily_rate_supplier_details import ReportingDailyRateSupplierDetails as ReportingDailyRateSupplierDetails
from wink_sdk_extranet_booking.models.reporting_extra_charge_supplier_details import ReportingExtraChargeSupplierDetails as ReportingExtraChargeSupplierDetails
from wink_sdk_extranet_booking.models.review_answer_supplier_details import ReviewAnswerSupplierDetails as ReviewAnswerSupplierDetails
from wink_sdk_extranet_booking.models.review_lightweight_supplier_details import ReviewLightweightSupplierDetails as ReviewLightweightSupplierDetails
from wink_sdk_extranet_booking.models.review_response_supplier import ReviewResponseSupplier as ReviewResponseSupplier
from wink_sdk_extranet_booking.models.review_supplier import ReviewSupplier as ReviewSupplier
from wink_sdk_extranet_booking.models.review_user_supplier_details import ReviewUserSupplierDetails as ReviewUserSupplierDetails
from wink_sdk_extranet_booking.models.room_configuration_price_rate_plan_supplier_details import RoomConfigurationPriceRatePlanSupplierDetails as RoomConfigurationPriceRatePlanSupplierDetails
from wink_sdk_extranet_booking.models.room_configuration_price_supplier_details import RoomConfigurationPriceSupplierDetails as RoomConfigurationPriceSupplierDetails
from wink_sdk_extranet_booking.models.room_configuration_supplier_details import RoomConfigurationSupplierDetails as RoomConfigurationSupplierDetails
from wink_sdk_extranet_booking.models.room_stay_supplier_details import RoomStaySupplierDetails as RoomStaySupplierDetails
from wink_sdk_extranet_booking.models.show_review400_response import ShowReview400Response as ShowReview400Response
from wink_sdk_extranet_booking.models.simple_address_supplier_details import SimpleAddressSupplierDetails as SimpleAddressSupplierDetails
from wink_sdk_extranet_booking.models.simple_date_time_itinerary_supplier_details import SimpleDateTimeItinerarySupplierDetails as SimpleDateTimeItinerarySupplierDetails
from wink_sdk_extranet_booking.models.simple_description_supplier_details import SimpleDescriptionSupplierDetails as SimpleDescriptionSupplierDetails
from wink_sdk_extranet_booking.models.simple_multimedia_supplier_details import SimpleMultimediaSupplierDetails as SimpleMultimediaSupplierDetails
from wink_sdk_extranet_booking.models.social_supplier_details import SocialSupplierDetails as SocialSupplierDetails
from wink_sdk_extranet_booking.models.sort_descriptor_supplier import SortDescriptorSupplier as SortDescriptorSupplier
from wink_sdk_extranet_booking.models.sort_object_supplier import SortObjectSupplier as SortObjectSupplier
from wink_sdk_extranet_booking.models.state_supplier import StateSupplier as StateSupplier
from wink_sdk_extranet_booking.models.stay_rate_supplier_details import StayRateSupplierDetails as StayRateSupplierDetails
from wink_sdk_extranet_booking.models.sub_country_lightweight_supplier_details import SubCountryLightweightSupplierDetails as SubCountryLightweightSupplierDetails
from wink_sdk_extranet_booking.models.sub_sub_country_lightweight_supplier_details import SubSubCountryLightweightSupplierDetails as SubSubCountryLightweightSupplierDetails
from wink_sdk_extranet_booking.models.supplier_contract_item_policy_supplier_details import SupplierContractItemPolicySupplierDetails as SupplierContractItemPolicySupplierDetails
from wink_sdk_extranet_booking.models.transactional_travel_inventory_supplier_details import TransactionalTravelInventorySupplierDetails as TransactionalTravelInventorySupplierDetails
from wink_sdk_extranet_booking.models.travel_inventory_recognition_supplier_details import TravelInventoryRecognitionSupplierDetails as TravelInventoryRecognitionSupplierDetails
from wink_sdk_extranet_booking.models.variable_charge_supplier_details import VariableChargeSupplierDetails as VariableChargeSupplierDetails
from wink_sdk_extranet_booking.models.verify_rates_request_supplier_details import VerifyRatesRequestSupplierDetails as VerifyRatesRequestSupplierDetails
from wink_sdk_extranet_booking.models.wink_booking_contract_supplier_details import WinkBookingContractSupplierDetails as WinkBookingContractSupplierDetails

