# coding: utf-8

# flake8: noqa
"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Inventory API The Inventory API exposes endpoints to retrieve blocking you already know about. This API lets you:  1. Consume shareable links. 2. Load up a known property with availability. 3. Load up all inventories that were created by our affiliates such as grids, maps, and individual items.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from wink_sdk_inventory.models.activity_localized_inventory_non_authenticated_entity import ActivityLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.activity_localized_inventory_with_hotel_best_price_non_authenticated_entity import ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.add_on_localized_inventory_non_authenticated_entity import AddOnLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity import AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.add_on_non_authenticated_entity import AddOnNonAuthenticatedEntity
from wink_sdk_inventory.models.address_non_authenticated_entity import AddressNonAuthenticatedEntity
from wink_sdk_inventory.models.advanced_map_configuration_non_authenticated_entity import AdvancedMapConfigurationNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_activity_request_non_authenticated_entity import AggregateActivityRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_add_on_request_non_authenticated_entity import AggregateAddOnRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_attraction_request_non_authenticated_entity import AggregateAttractionRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_greendex_answers_non_authenticated_entity import AggregateGreendexAnswersNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_greendex_score_by_category_non_authenticated_entity import AggregateGreendexScoreByCategoryNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_guest_room_request_non_authenticated_entity import AggregateGuestRoomRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_hotel_request_non_authenticated_entity import AggregateHotelRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_inventory_grid_item_request_non_authenticated_entity import AggregateInventoryGridItemRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_meeting_room_request_non_authenticated_entity import AggregateMeetingRoomRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_place_request_non_authenticated_entity import AggregatePlaceRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_restaurant_request_non_authenticated_entity import AggregateRestaurantRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_seller_inventory_list_request_non_authenticated_entity import AggregateSellerInventoryListRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.aggregate_spa_request_non_authenticated_entity import AggregateSpaRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.announcement_non_authenticated_entity import AnnouncementNonAuthenticatedEntity
from wink_sdk_inventory.models.attraction_localized_inventory_non_authenticated_entity import AttractionLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity import AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.attraction_non_authenticated_entity import AttractionNonAuthenticatedEntity
from wink_sdk_inventory.models.bed_non_authenticated_entity import BedNonAuthenticatedEntity
from wink_sdk_inventory.models.bedroom_configuration_non_authenticated_entity import BedroomConfigurationNonAuthenticatedEntity
from wink_sdk_inventory.models.bedroom_non_authenticated_entity import BedroomNonAuthenticatedEntity
from wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity import CancellationPolicyExceptionNonAuthenticatedEntity
from wink_sdk_inventory.models.cancellation_policy_exceptions_non_authenticated_entity import CancellationPolicyExceptionsNonAuthenticatedEntity
from wink_sdk_inventory.models.cancellation_policy_non_authenticated_entity import CancellationPolicyNonAuthenticatedEntity
from wink_sdk_inventory.models.child_non_authenticated_entity import ChildNonAuthenticatedEntity
from wink_sdk_inventory.models.configurable_geo_json_circle_non_authenticated_entity import ConfigurableGeoJsonCircleNonAuthenticatedEntity
from wink_sdk_inventory.models.configurable_geo_json_point_non_authenticated_entity import ConfigurableGeoJsonPointNonAuthenticatedEntity
from wink_sdk_inventory.models.configurable_geo_json_polygon_non_authenticated_entity import ConfigurableGeoJsonPolygonNonAuthenticatedEntity
from wink_sdk_inventory.models.configurable_geo_json_rectangle_non_authenticated_entity import ConfigurableGeoJsonRectangleNonAuthenticatedEntity
from wink_sdk_inventory.models.consumable_seller_url_non_authenticated_entity import ConsumableSellerUrlNonAuthenticatedEntity
from wink_sdk_inventory.models.consumer_data_map_non_authenticated_entity import ConsumerDataMapNonAuthenticatedEntity
from wink_sdk_inventory.models.contact_non_authenticated_entity import ContactNonAuthenticatedEntity
from wink_sdk_inventory.models.country_non_authenticated_entity import CountryNonAuthenticatedEntity
from wink_sdk_inventory.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_inventory.models.dow_pattern_group_non_authenticated_entity import DowPatternGroupNonAuthenticatedEntity
from wink_sdk_inventory.models.extra_charge_non_authenticated_entity import ExtraChargeNonAuthenticatedEntity
from wink_sdk_inventory.models.extra_charges_non_authenticated_entity import ExtraChargesNonAuthenticatedEntity
from wink_sdk_inventory.models.general_manager_non_authenticated_entity import GeneralManagerNonAuthenticatedEntity
from wink_sdk_inventory.models.generic_error_message import GenericErrorMessage
from wink_sdk_inventory.models.geo_json_line_string_non_authenticated_entity import GeoJsonLineStringNonAuthenticatedEntity
from wink_sdk_inventory.models.geo_json_point_non_authenticated_entity import GeoJsonPointNonAuthenticatedEntity
from wink_sdk_inventory.models.geo_json_polygon_non_authenticated_entity import GeoJsonPolygonNonAuthenticatedEntity
from wink_sdk_inventory.models.geo_json_rectangle_non_authenticated_entity import GeoJsonRectangleNonAuthenticatedEntity
from wink_sdk_inventory.models.geo_name_non_authenticated_entity import GeoNameNonAuthenticatedEntity
from wink_sdk_inventory.models.guest_room_non_authenticated_entity import GuestRoomNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_list_request_non_authenticated_entity import HotelInventoryListRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_list_response_non_authenticated_entity import HotelInventoryListResponseNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_request_non_authenticated_entity import HotelInventoryRequestNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_inventory_response_non_authenticated_entity import HotelInventoryResponseNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_on_map_non_authenticated_entity import HotelOnMapNonAuthenticatedEntity
from wink_sdk_inventory.models.hotel_with_best_price_non_authenticated_entity import HotelWithBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.image_attribution_non_authenticated_entity import ImageAttributionNonAuthenticatedEntity
from wink_sdk_inventory.models.inventory_grid_item_non_authenticated_entity import InventoryGridItemNonAuthenticatedEntity
from wink_sdk_inventory.models.inventory_map_marker_non_authenticated_entity import InventoryMapMarkerNonAuthenticatedEntity
from wink_sdk_inventory.models.inventory_unavailable_notification_non_authenticated_entity import InventoryUnavailableNotificationNonAuthenticatedEntity
from wink_sdk_inventory.models.itinerary_non_authenticated_entity import ItineraryNonAuthenticatedEntity
from wink_sdk_inventory.models.localized_description_non_authenticated_entity import LocalizedDescriptionNonAuthenticatedEntity
from wink_sdk_inventory.models.localized_price_non_authenticated_entity import LocalizedPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.localized_transactional_travel_inventory_non_authenticated_entity import LocalizedTransactionalTravelInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.lookup_non_authenticated_entity import LookupNonAuthenticatedEntity
from wink_sdk_inventory.models.meeting_room_localized_inventory_non_authenticated_entity import MeetingRoomLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity import MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.meeting_room_non_authenticated_entity import MeetingRoomNonAuthenticatedEntity
from wink_sdk_inventory.models.meta_data_non_authenticated_entity import MetaDataNonAuthenticatedEntity
from wink_sdk_inventory.models.oauth2_show_consumable_url400_response import Oauth2ShowConsumableUrl400Response
from wink_sdk_inventory.models.page_inventory_grid_item_non_authenticated_entity import PageInventoryGridItemNonAuthenticatedEntity
from wink_sdk_inventory.models.pageable_object_non_authenticated_entity import PageableObjectNonAuthenticatedEntity
from wink_sdk_inventory.models.place_localized_inventory_non_authenticated_entity import PlaceLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.place_localized_inventory_with_hotel_best_price_non_authenticated_entity import PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.point_non_authenticated_entity import PointNonAuthenticatedEntity
from wink_sdk_inventory.models.property_policy_non_authenticated_entity import PropertyPolicyNonAuthenticatedEntity
from wink_sdk_inventory.models.quote_non_authenticated_entity import QuoteNonAuthenticatedEntity
from wink_sdk_inventory.models.rate_plan_level_fee_non_authenticated_entity import RatePlanLevelFeeNonAuthenticatedEntity
from wink_sdk_inventory.models.rate_plan_non_authenticated_entity import RatePlanNonAuthenticatedEntity
from wink_sdk_inventory.models.recreation_non_authenticated_entity import RecreationNonAuthenticatedEntity
from wink_sdk_inventory.models.ref_point_non_authenticated_entity import RefPointNonAuthenticatedEntity
from wink_sdk_inventory.models.restaurant_localized_inventory_non_authenticated_entity import RestaurantLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.restaurant_localized_inventory_with_hotel_best_price_non_authenticated_entity import RestaurantLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.restaurant_non_authenticated_entity import RestaurantNonAuthenticatedEntity
from wink_sdk_inventory.models.room_configuration_non_authenticated_entity import RoomConfigurationNonAuthenticatedEntity
from wink_sdk_inventory.models.room_configuration_price_non_authenticated_entity import RoomConfigurationPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.room_type_best_price_non_authenticated_entity import RoomTypeBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.room_type_with_best_price_non_authenticated_entity import RoomTypeWithBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.room_type_with_price_configuration_non_authenticated_entity import RoomTypeWithPriceConfigurationNonAuthenticatedEntity
from wink_sdk_inventory.models.room_type_with_price_configurations_non_authenticated_entity import RoomTypeWithPriceConfigurationsNonAuthenticatedEntity
from wink_sdk_inventory.models.sales_channel_info_non_authenticated_entity import SalesChannelInfoNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_activity_non_authenticated_entity import SellerInventoryActivityNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_add_on_non_authenticated_entity import SellerInventoryAddOnNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_attraction_non_authenticated_entity import SellerInventoryAttractionNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_guest_room_non_authenticated_entity import SellerInventoryGuestRoomNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_hotel_non_authenticated_entity import SellerInventoryHotelNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_item_non_authenticated_entity import SellerInventoryItemNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_list_non_authenticated_entity import SellerInventoryListNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_list_response_non_authenticated_entity import SellerInventoryListResponseNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_meeting_room_non_authenticated_entity import SellerInventoryMeetingRoomNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_place_non_authenticated_entity import SellerInventoryPlaceNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_ranked_list_non_authenticated_entity import SellerInventoryRankedListNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_ranked_list_response_non_authenticated_entity import SellerInventoryRankedListResponseNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_restaurant_non_authenticated_entity import SellerInventoryRestaurantNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_inventory_spa_non_authenticated_entity import SellerInventorySpaNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_media_non_authenticated_entity import SellerMediaNonAuthenticatedEntity
from wink_sdk_inventory.models.seller_url_price_non_authenticated_entity import SellerUrlPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.simple_description_non_authenticated_entity import SimpleDescriptionNonAuthenticatedEntity
from wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity import SimpleMultimediaNonAuthenticatedEntity
from wink_sdk_inventory.models.social_non_authenticated_entity import SocialNonAuthenticatedEntity
from wink_sdk_inventory.models.sort_object import SortObject
from wink_sdk_inventory.models.spa_localized_inventory_non_authenticated_entity import SpaLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_inventory.models.spa_localized_inventory_with_hotel_best_price_non_authenticated_entity import SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity
from wink_sdk_inventory.models.spa_non_authenticated_entity import SpaNonAuthenticatedEntity
from wink_sdk_inventory.models.stay_rate_non_authenticated_entity import StayRateNonAuthenticatedEntity
from wink_sdk_inventory.models.sub_country_non_authenticated_entity import SubCountryNonAuthenticatedEntity
from wink_sdk_inventory.models.sub_sub_country_non_authenticated_entity import SubSubCountryNonAuthenticatedEntity
from wink_sdk_inventory.models.travel_inventory_recognition_non_authenticated_entity import TravelInventoryRecognitionNonAuthenticatedEntity
from wink_sdk_inventory.models.user_review_answer_non_authenticated_entity import UserReviewAnswerNonAuthenticatedEntity
from wink_sdk_inventory.models.user_review_non_authenticated_entity import UserReviewNonAuthenticatedEntity
from wink_sdk_inventory.models.user_session_non_authenticated_entity import UserSessionNonAuthenticatedEntity
