# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Inventory API The Inventory API exposes endpoints to retrieve inventory you already know about. This API lets you:  1. Consume shareable links. 2. Load up a known property with availability. 3. Load up all inventories that were created by our affiliates such as grids, maps, and individual items.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.17.1
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wink_sdk_inventory.models.property_with_best_price_non_authenticated_entity import PropertyWithBestPriceNonAuthenticatedEntity

class TestPropertyWithBestPriceNonAuthenticatedEntity(unittest.TestCase):
    """PropertyWithBestPriceNonAuthenticatedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyWithBestPriceNonAuthenticatedEntity:
        """Test PropertyWithBestPriceNonAuthenticatedEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyWithBestPriceNonAuthenticatedEntity`
        """
        model = PropertyWithBestPriceNonAuthenticatedEntity()
        if include_optional:
            return PropertyWithBestPriceNonAuthenticatedEntity(
                hotel = wink_sdk_inventory.models.property_aggregate_lightweight_non_authenticated_entity.PropertyAggregateLightweight_Non_Authenticated_Entity(
                    hotel_identifier = 'hotel-1', 
                    name = 'The Loveliest Hotel', 
                    local_name = 'Det Beste Hotellet', 
                    chain = 'Hotel chain', 
                    brand = 'Hotel brand', 
                    url_name = 'the-loveliest-hotel-new-york-united-states', 
                    star_rating = 4, 
                    bookings = 6054, 
                    aggregate_review_rating = 7.8, 
                    location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                    descriptions = [
                        wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                            name = 'An example title', 
                            description = 'This is a longer description in the specified language.', 
                            language = 'en', )
                        ], 
                    aggregate_greendex_rating = 7.0, 
                    lifestyle_types = [
                        null
                        ], 
                    total_reviews = 989, 
                    reservations = wink_sdk_inventory.models.contact_non_authenticated_entity.Contact_Non_Authenticated_Entity(
                        first_name = 'John', 
                        last_name = 'Smith', 
                        email = 'johnsmith@email.com', 
                        secondary_email = 'johnsmith2@email.com', 
                        phone_number = '+12125551212', 
                        full_name = 'John Smith', 
                        summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                    socials = [
                        wink_sdk_inventory.models.social_non_authenticated_entity.Social_Non_Authenticated_Entity(
                            type = 'FACEBOOK', 
                            location = '', )
                        ], 
                    images = [
                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                            multimedia_identifier = 'image-1', 
                            identifier = 'cloudinary-image-1', 
                            type = 'IMAGE', 
                            source = 'CLOUDINARY', 
                            sort = 10, 
                            angle = '-90', 
                            width = 2560, 
                            height = 1600, 
                            published = True, 
                            category = '1', 
                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                            attribution = [
                                wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                    url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                    name = 'Samuel Adams', )
                                ], 
                            is_landscape = True, )
                        ], 
                    videos = [
                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                            multimedia_identifier = 'image-1', 
                            identifier = 'cloudinary-image-1', 
                            type = 'IMAGE', 
                            source = 'CLOUDINARY', 
                            sort = 10, 
                            angle = '-90', 
                            width = 2560, 
                            height = 1600, 
                            published = True, 
                            category = '1', 
                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                            is_landscape = True, )
                        ], 
                    policy = wink_sdk_inventory.models.property_policy_non_authenticated_entity.PropertyPolicy_Non_Authenticated_Entity(
                        children_allowed = True, 
                        children_minimum_age = 6, 
                        internet_availability = 'YES', 
                        internet_connection_type = 'WIFI', 
                        internet_connection_location = 'ENTIRE_PROPERTY', 
                        parking_availability = 'YES', 
                        parking_access = 'PRIVATE', 
                        pets_allowed = True, 
                        pet_max_weight_in_kilos = 10, 
                        pet_charge = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                            amount = 1.337, 
                            currency = '0', ), 
                        check_out_time = '10:00', 
                        check_in_time = '14:00', ), 
                    third_party_reviews = [
                        wink_sdk_inventory.models.travel_inventory_recognition_non_authenticated_entity.TravelInventoryRecognition_Non_Authenticated_Entity(
                            identifier = 'recognition-1', 
                            category = 'AWARD', 
                            type = 'PERCENT_RATING', 
                            provider = 'Michelin', 
                            rating = 8.5, 
                            max_rating = 10, 
                            date = '2020-10-24', 
                            official_appointment_ind = True, 
                            rating_symbol = '*', )
                        ], 
                    attractions = 5, 
                    activities = 3, 
                    places = 9, 
                    restaurants = 2, 
                    meeting_rooms = 2, 
                    spas = 1, 
                    add_ons = 5, 
                    general_manager = wink_sdk_inventory.models.general_manager_non_authenticated_entity.GeneralManager_Non_Authenticated_Entity(
                        name = 'Jane Doe', 
                        image = cl-image-1, ), 
                    location_category = '34', 
                    segment_category = '7', 
                    hotel_category = '45', 
                    architectural_style = '7', 
                    when_built = '1927', 
                    currency_code = 'USD', 
                    membership_rate_discount = 9, 
                    price_score = 9, 
                    perk_score = 4, 
                    add_on_score = 4, 
                    loyalty_score = 5, 
                    popular_score = 45, 
                    experience_score = 5, 
                    hotel_amenity_codes = [1, 7], 
                    property_accessibility_codes = [1, 7], 
                    property_security_codes = [1, 7], 
                    number_of_rooms = 32, 
                    address = wink_sdk_inventory.models.simple_address_non_authenticated_entity.SimpleAddress_Non_Authenticated_Entity(
                        address1 = '234', 
                        address2 = 'Pebble #5001', 
                        state = 'CA', 
                        postal_code = '90210', 
                        county = 'Alameda county', 
                        city = '0', 
                        country_code = '0', 
                        country = 'United States', 
                        full_address = '11', ), 
                    active = True, 
                    url_parameters = '', ),
                lowest_price = wink_sdk_inventory.models.room_type_best_price_non_authenticated_entity.RoomTypeBestPrice_Non_Authenticated_Entity(
                    room_type_identifier = '', 
                    price = wink_sdk_inventory.models.room_configuration_price_non_authenticated_entity.RoomConfigurationPrice_Non_Authenticated_Entity(
                        adults = 56, 
                        children = 56, 
                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        room_rate_identifier = '', 
                        room_rate_internal_name = '', 
                        rate_plan = wink_sdk_inventory.models.room_configuration_price_rate_plan_non_authenticated_entity.RoomConfigurationPriceRatePlan_Non_Authenticated_Entity(
                            identifier = '0', 
                            name = 'BAR 1', 
                            breakfast = False, 
                            brunch = False, 
                            lunch = False, 
                            dinner = False, 
                            all_inclusive = False, 
                            all_inclusive_plus_alcohol = False, 
                            early_check_in_charge = null, 
                            late_check_out_charge = null, 
                            cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                identifier = '', 
                                hotel_identifier = '', 
                                refundable = False, 
                                advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                policy_code = '', ), 
                            cancellation_policy_exceptions = wink_sdk_inventory.models.cancellation_policy_exceptions_non_authenticated_entity.CancellationPolicyExceptions_Non_Authenticated_Entity(
                                list = [
                                    wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity.CancellationPolicyException_Non_Authenticated_Entity(
                                        cancellation_policy_identifier = '0', 
                                        cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                            identifier = '', 
                                            hotel_identifier = '', 
                                            refundable = False, 
                                            advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                            refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                            no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                            non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                            non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                            non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                            policy_code = '', ), 
                                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                                    ], ), ), 
                        perk_types = [
                            null
                            ], 
                        price = wink_sdk_inventory.models.stay_rate_non_authenticated_entity.StayRate_Non_Authenticated_Entity(
                            user_specified_currency_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                amount = 1.337, 
                                currency = '0', ), 
                            source_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                amount = 1.337, 
                                currency = '0', ), 
                            internal_base_total = , 
                            source_extra_pax_modifier = 15, 
                            internal_extra_pax_modifier = 15, 
                            user_specified_currency_extra_pax_modifier = 15, 
                            source_extra_child_modifier = 15, 
                            internal_extra_child_modifier = 15, 
                            user_specified_currency_extra_child_modifier = 15, 
                            source_single_occupant_modifier = -15, 
                            internal_single_occupant_modifier = -15, 
                            user_specified_currency_single_occupant_modifier = -15, 
                            source_promotional_modifier = -40, 
                            internal_promotional_modifier = -40, 
                            user_specified_currency_promotional_modifier = -40, 
                            source_premium_modifier = 40, 
                            internal_premium_modifier = 40, 
                            user_specified_currency_premium_modifier = 40, 
                            source_channel_modifier = -10, 
                            internal_channel_modifier = -10, 
                            user_specified_currency_channel_modifier = -10, 
                            quantity = 56, 
                            min_occupancy = 56, 
                            max_occupancy = 56, 
                            rate_source = '', 
                            promotional_discount_percent = 1.337, 
                            channel_discount_percent = 1.337, 
                            premium_percent = 1.337, 
                            available = True, 
                            source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                source = '0', 
                                target = '0', 
                                exchange_rate = 1.337, 
                                timestamp = 56, ), 
                            source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                source = '0', 
                                target = '0', 
                                exchange_rate = 1.337, 
                                timestamp = 56, ), 
                            offer_details = [
                                wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                    description = 'This is a longer description in the specified language.', 
                                    language = 'en', )
                                ], 
                            promotional_codes = [
                                ''
                                ], 
                            user_specified_currency_total = , 
                            source_total = , 
                            internal_total = , 
                            user_specified_currency_average_price_per_night = , 
                            internal_average_price_per_night = , 
                            source_average_price_per_night = , 
                            total_discount_percent = 1.337, ), 
                        extra_charges = wink_sdk_inventory.models.extra_charges_non_authenticated_entity.ExtraCharges_Non_Authenticated_Entity(
                            items = [
                                wink_sdk_inventory.models.extra_charge_non_authenticated_entity.ExtraCharge_Non_Authenticated_Entity(
                                    rate_plan_level_fee = wink_sdk_inventory.models.rate_plan_level_fee_non_authenticated_entity.RatePlanLevelFee_Non_Authenticated_Entity(
                                        descriptions = [
                                            wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                                description = 'This is a longer description in the specified language.', 
                                                language = 'en', )
                                            ], 
                                        fixed_amount = , 
                                        type = 'PER_DAY', ), 
                                    unit_price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                        source_to_user_currency_quote = , 
                                        source_to_internal_currency_quote = , 
                                        user_specified_currency_base_total = , 
                                        source_base_total = , 
                                        internal_base_total = , 
                                        user_specified_currency_promotional_modifier = -40, 
                                        source_promotional_modifier = -40, 
                                        internal_promotional_modifier = -40, 
                                        user_specified_currency_premium_modifier = 40, 
                                        source_premium_modifier = 40, 
                                        internal_premium_modifier = 40, 
                                        user_specified_currency_channel_modifier = -10, 
                                        source_channel_modifier = -10, 
                                        internal_channel_modifier = -10, 
                                        quantity = 56, 
                                        promotional_discount_percent = 1.337, 
                                        channel_discount_percent = 1.337, 
                                        premium_percent = 1.337, 
                                        has_premium = True, 
                                        has_promotion = True, 
                                        total_discount_percent = 1.337, 
                                        has_channel_discount = True, ), )
                                ], ), 
                        configuration = wink_sdk_inventory.models.room_configuration_non_authenticated_entity.RoomConfiguration_Non_Authenticated_Entity(
                            adults = 2, 
                            children = [
                                wink_sdk_inventory.models.child_non_authenticated_entity.Child_Non_Authenticated_Entity(
                                    quantity = 1, 
                                    age = 0, )
                                ], ), 
                        add_on_offers = [
                            null
                            ], 
                        perk_value = 56, 
                        active_cancellation_policy = , 
                        room_nights = 56, 
                        list = [
                            wink_sdk_inventory.models.localized_transactional_travel_inventory_non_authenticated_entity.LocalizedTransactionalTravelInventory_Non_Authenticated_Entity(
                                identifier = 'travel-blocking-1', 
                                name = '1', 
                                descriptions = [
                                    wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                        name = 'An example title', 
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', )
                                    ], 
                                pricing_type = 'PER_STAY', 
                                price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                    source_to_user_currency_quote = , 
                                    source_to_internal_currency_quote = , 
                                    user_specified_currency_base_total = , 
                                    source_base_total = , 
                                    internal_base_total = , 
                                    user_specified_currency_promotional_modifier = -40, 
                                    source_promotional_modifier = -40, 
                                    internal_promotional_modifier = -40, 
                                    user_specified_currency_premium_modifier = 40, 
                                    source_premium_modifier = 40, 
                                    internal_premium_modifier = 40, 
                                    user_specified_currency_channel_modifier = -10, 
                                    source_channel_modifier = -10, 
                                    internal_channel_modifier = -10, 
                                    quantity = 56, 
                                    promotional_discount_percent = 1.337, 
                                    channel_discount_percent = 1.337, 
                                    premium_percent = 1.337, 
                                    has_premium = True, 
                                    has_promotion = True, 
                                    total_discount_percent = 1.337, 
                                    has_channel_discount = True, ), 
                                multimedias = [
                                    wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                        multimedia_identifier = 'image-1', 
                                        identifier = 'cloudinary-image-1', 
                                        type = 'IMAGE', 
                                        source = 'CLOUDINARY', 
                                        sort = 10, 
                                        angle = '-90', 
                                        width = 2560, 
                                        height = 1600, 
                                        published = True, 
                                        category = '1', 
                                        lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                        attribution = [
                                            wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                                url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                                name = 'Samuel Adams', )
                                            ], 
                                        is_landscape = True, )
                                    ], 
                                min_pax = 2, 
                                max_pax = 10, 
                                promotion = '', )
                            ], 
                        channel_inventory_identifier = '', 
                        commissionable = True, 
                        commission = 0.1, 
                        direct = True, 
                        price_list = [
                            null
                            ], 
                        available = True, 
                        rate_source = '', 
                        source_total = , 
                        user_specified_currency_total = , 
                        internal_total = , ), 
                    perk_value = 56, 
                    available = True, 
                    sort = 56, ),
                room_type_list = [
                    wink_sdk_inventory.models.guest_room_lightweight_non_authenticated_entity.GuestRoomLightweight_Non_Authenticated_Entity(
                        identifier = 'document-1', 
                        hotel_identifier = 'hotel-1', 
                        featured_ind = False, 
                        lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                        location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                        descriptions = [
                            wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                name = 'An example title', 
                                description = 'This is a longer description in the specified language.', 
                                language = 'en', )
                            ], 
                        multimedias = [
                            wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                multimedia_identifier = 'image-1', 
                                identifier = 'cloudinary-image-1', 
                                type = 'IMAGE', 
                                source = 'CLOUDINARY', 
                                sort = 10, 
                                angle = '-90', 
                                width = 2560, 
                                height = 1600, 
                                published = True, 
                                category = '1', 
                                lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                attribution = [
                                    wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                        url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                        name = 'Samuel Adams', )
                                    ], 
                                is_landscape = True, )
                            ], 
                        contact = wink_sdk_inventory.models.contact_non_authenticated_entity.Contact_Non_Authenticated_Entity(
                            first_name = 'John', 
                            last_name = 'Smith', 
                            email = 'johnsmith@email.com', 
                            secondary_email = 'johnsmith2@email.com', 
                            phone_number = '+12125551212', 
                            full_name = 'John Smith', 
                            summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                        address = wink_sdk_inventory.models.simple_address_non_authenticated_entity.SimpleAddress_Non_Authenticated_Entity(
                            address1 = '234', 
                            address2 = 'Pebble #5001', 
                            state = 'CA', 
                            postal_code = '90210', 
                            county = 'Alameda county', 
                            city = '0', 
                            country_code = '0', 
                            country = 'United States', 
                            full_address = '11', ), 
                        commissionable = True, 
                        name = 'Archery lesson', 
                        proximity_code = '1', 
                        sort = 1, 
                        min_age_appropriate_code = '1', 
                        bookable = True, 
                        active = True, 
                        disability_features = [
                            ''
                            ], 
                        security_features = [
                            ''
                            ], 
                        socials = [
                            wink_sdk_inventory.models.social_non_authenticated_entity.Social_Non_Authenticated_Entity(
                                type = 'FACEBOOK', 
                                location = '', )
                            ], 
                        price_point = 'THREE', 
                        recognition_list = [
                            wink_sdk_inventory.models.travel_inventory_recognition_non_authenticated_entity.TravelInventoryRecognition_Non_Authenticated_Entity(
                                identifier = 'recognition-1', 
                                category = 'AWARD', 
                                type = 'PERCENT_RATING', 
                                provider = 'Michelin', 
                                rating = 8.5, 
                                max_rating = 10, 
                                date = '2020-10-24', 
                                official_appointment_ind = True, 
                                rating_symbol = '*', )
                            ], 
                        max_occupancy = 2, 
                        min_occupancy = 1, 
                        quantity = 40, 
                        non_smoking = True, 
                        bedroom_configuration_list = [
                            wink_sdk_inventory.models.bedroom_configuration_non_authenticated_entity.BedroomConfiguration_Non_Authenticated_Entity(
                                identifier = '0', 
                                name = '0', 
                                bedroom_list = [
                                    wink_sdk_inventory.models.bedroom_non_authenticated_entity.Bedroom_Non_Authenticated_Entity(
                                        type = 'MASTER', 
                                        bed_list = [
                                            wink_sdk_inventory.models.bed_non_authenticated_entity.Bed_Non_Authenticated_Entity(
                                                bed_type_code = '1', 
                                                quantity = 10, )
                                            ], )
                                    ], )
                            ], 
                        size = 55, 
                        max_adult_occupancy = 1, 
                        max_child_occupancy = 0, 
                        bathroom_count = 0, 
                        living_room_count = 0, 
                        max_rollaways = 0, 
                        room_category = '1', 
                        floor = '', 
                        room_location_code = '1', 
                        room_view_code = '1', 
                        composite = False, 
                        composite_count = 2, 
                        room_classification_code = '1', 
                        room_architecture_code = '1', 
                        room_gender = 'Unknown', 
                        shared_room_ind = False, 
                        max_cribs = 1, 
                        amenities = [
                            ''
                            ], 
                        included_adult_occupancy = 2, 
                        included_child_occupancy = 0, )
                    ],
                price_list = [
                    wink_sdk_inventory.models.room_type_best_price_non_authenticated_entity.RoomTypeBestPrice_Non_Authenticated_Entity(
                        room_type_identifier = '', 
                        price = wink_sdk_inventory.models.room_configuration_price_non_authenticated_entity.RoomConfigurationPrice_Non_Authenticated_Entity(
                            adults = 56, 
                            children = 56, 
                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            room_rate_identifier = '', 
                            room_rate_internal_name = '', 
                            rate_plan = wink_sdk_inventory.models.room_configuration_price_rate_plan_non_authenticated_entity.RoomConfigurationPriceRatePlan_Non_Authenticated_Entity(
                                identifier = '0', 
                                name = 'BAR 1', 
                                breakfast = False, 
                                brunch = False, 
                                lunch = False, 
                                dinner = False, 
                                all_inclusive = False, 
                                all_inclusive_plus_alcohol = False, 
                                early_check_in_charge = null, 
                                late_check_out_charge = null, 
                                cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                    identifier = '', 
                                    hotel_identifier = '', 
                                    refundable = False, 
                                    advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                    refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                    no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                    non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                    non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                    non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                    policy_code = '', ), 
                                cancellation_policy_exceptions = wink_sdk_inventory.models.cancellation_policy_exceptions_non_authenticated_entity.CancellationPolicyExceptions_Non_Authenticated_Entity(
                                    list = [
                                        wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity.CancellationPolicyException_Non_Authenticated_Entity(
                                            cancellation_policy_identifier = '0', 
                                            cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                                identifier = '', 
                                                hotel_identifier = '', 
                                                refundable = False, 
                                                advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                                refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                                no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                                non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                                non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                                non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                                policy_code = '', ), 
                                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                            end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                                        ], ), ), 
                            perk_types = [
                                null
                                ], 
                            price = wink_sdk_inventory.models.stay_rate_non_authenticated_entity.StayRate_Non_Authenticated_Entity(
                                user_specified_currency_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                    amount = 1.337, 
                                    currency = '0', ), 
                                source_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                    amount = 1.337, 
                                    currency = '0', ), 
                                internal_base_total = , 
                                source_extra_pax_modifier = 15, 
                                internal_extra_pax_modifier = 15, 
                                user_specified_currency_extra_pax_modifier = 15, 
                                source_extra_child_modifier = 15, 
                                internal_extra_child_modifier = 15, 
                                user_specified_currency_extra_child_modifier = 15, 
                                source_single_occupant_modifier = -15, 
                                internal_single_occupant_modifier = -15, 
                                user_specified_currency_single_occupant_modifier = -15, 
                                source_promotional_modifier = -40, 
                                internal_promotional_modifier = -40, 
                                user_specified_currency_promotional_modifier = -40, 
                                source_premium_modifier = 40, 
                                internal_premium_modifier = 40, 
                                user_specified_currency_premium_modifier = 40, 
                                source_channel_modifier = -10, 
                                internal_channel_modifier = -10, 
                                user_specified_currency_channel_modifier = -10, 
                                quantity = 56, 
                                min_occupancy = 56, 
                                max_occupancy = 56, 
                                rate_source = '', 
                                promotional_discount_percent = 1.337, 
                                channel_discount_percent = 1.337, 
                                premium_percent = 1.337, 
                                available = True, 
                                source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                offer_details = [
                                    wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', )
                                    ], 
                                promotional_codes = [
                                    ''
                                    ], 
                                user_specified_currency_total = , 
                                source_total = , 
                                internal_total = , 
                                user_specified_currency_average_price_per_night = , 
                                internal_average_price_per_night = , 
                                source_average_price_per_night = , 
                                total_discount_percent = 1.337, ), 
                            extra_charges = wink_sdk_inventory.models.extra_charges_non_authenticated_entity.ExtraCharges_Non_Authenticated_Entity(
                                items = [
                                    wink_sdk_inventory.models.extra_charge_non_authenticated_entity.ExtraCharge_Non_Authenticated_Entity(
                                        rate_plan_level_fee = wink_sdk_inventory.models.rate_plan_level_fee_non_authenticated_entity.RatePlanLevelFee_Non_Authenticated_Entity(
                                            descriptions = [
                                                wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                                    description = 'This is a longer description in the specified language.', 
                                                    language = 'en', )
                                                ], 
                                            fixed_amount = , 
                                            type = 'PER_DAY', ), 
                                        unit_price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                            source_to_user_currency_quote = , 
                                            source_to_internal_currency_quote = , 
                                            user_specified_currency_base_total = , 
                                            source_base_total = , 
                                            internal_base_total = , 
                                            user_specified_currency_promotional_modifier = -40, 
                                            source_promotional_modifier = -40, 
                                            internal_promotional_modifier = -40, 
                                            user_specified_currency_premium_modifier = 40, 
                                            source_premium_modifier = 40, 
                                            internal_premium_modifier = 40, 
                                            user_specified_currency_channel_modifier = -10, 
                                            source_channel_modifier = -10, 
                                            internal_channel_modifier = -10, 
                                            quantity = 56, 
                                            promotional_discount_percent = 1.337, 
                                            channel_discount_percent = 1.337, 
                                            premium_percent = 1.337, 
                                            has_premium = True, 
                                            has_promotion = True, 
                                            total_discount_percent = 1.337, 
                                            has_channel_discount = True, ), )
                                    ], ), 
                            configuration = wink_sdk_inventory.models.room_configuration_non_authenticated_entity.RoomConfiguration_Non_Authenticated_Entity(
                                adults = 2, 
                                children = [
                                    wink_sdk_inventory.models.child_non_authenticated_entity.Child_Non_Authenticated_Entity(
                                        quantity = 1, 
                                        age = 0, )
                                    ], ), 
                            add_on_offers = [
                                null
                                ], 
                            perk_value = 56, 
                            active_cancellation_policy = , 
                            room_nights = 56, 
                            list = [
                                wink_sdk_inventory.models.localized_transactional_travel_inventory_non_authenticated_entity.LocalizedTransactionalTravelInventory_Non_Authenticated_Entity(
                                    identifier = 'travel-blocking-1', 
                                    name = '1', 
                                    descriptions = [
                                        wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                            name = 'An example title', 
                                            description = 'This is a longer description in the specified language.', 
                                            language = 'en', )
                                        ], 
                                    pricing_type = 'PER_STAY', 
                                    price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                        source_to_user_currency_quote = , 
                                        source_to_internal_currency_quote = , 
                                        user_specified_currency_base_total = , 
                                        source_base_total = , 
                                        internal_base_total = , 
                                        user_specified_currency_promotional_modifier = -40, 
                                        source_promotional_modifier = -40, 
                                        internal_promotional_modifier = -40, 
                                        user_specified_currency_premium_modifier = 40, 
                                        source_premium_modifier = 40, 
                                        internal_premium_modifier = 40, 
                                        user_specified_currency_channel_modifier = -10, 
                                        source_channel_modifier = -10, 
                                        internal_channel_modifier = -10, 
                                        quantity = 56, 
                                        promotional_discount_percent = 1.337, 
                                        channel_discount_percent = 1.337, 
                                        premium_percent = 1.337, 
                                        has_premium = True, 
                                        has_promotion = True, 
                                        total_discount_percent = 1.337, 
                                        has_channel_discount = True, ), 
                                    multimedias = [
                                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                            multimedia_identifier = 'image-1', 
                                            identifier = 'cloudinary-image-1', 
                                            type = 'IMAGE', 
                                            source = 'CLOUDINARY', 
                                            sort = 10, 
                                            angle = '-90', 
                                            width = 2560, 
                                            height = 1600, 
                                            published = True, 
                                            category = '1', 
                                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                            attribution = [
                                                wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                                    url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                                    name = 'Samuel Adams', )
                                                ], 
                                            is_landscape = True, )
                                        ], 
                                    min_pax = 2, 
                                    max_pax = 10, 
                                    promotion = '', )
                                ], 
                            channel_inventory_identifier = '', 
                            commissionable = True, 
                            commission = 0.1, 
                            direct = True, 
                            available = True, 
                            rate_source = '', 
                            source_total = , 
                            user_specified_currency_total = , 
                            internal_total = , ), 
                        perk_value = 56, 
                        available = True, 
                        sort = 56, )
                    ],
                potential_channel_discount_percent = 1.337,
                source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                    source = '0', 
                    target = '0', 
                    exchange_rate = 1.337, 
                    timestamp = 56, ),
                source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                    source = '0', 
                    target = '0', 
                    exchange_rate = 1.337, 
                    timestamp = 56, ),
                available = True
            )
        else:
            return PropertyWithBestPriceNonAuthenticatedEntity(
                hotel = wink_sdk_inventory.models.property_aggregate_lightweight_non_authenticated_entity.PropertyAggregateLightweight_Non_Authenticated_Entity(
                    hotel_identifier = 'hotel-1', 
                    name = 'The Loveliest Hotel', 
                    local_name = 'Det Beste Hotellet', 
                    chain = 'Hotel chain', 
                    brand = 'Hotel brand', 
                    url_name = 'the-loveliest-hotel-new-york-united-states', 
                    star_rating = 4, 
                    bookings = 6054, 
                    aggregate_review_rating = 7.8, 
                    location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                    descriptions = [
                        wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                            name = 'An example title', 
                            description = 'This is a longer description in the specified language.', 
                            language = 'en', )
                        ], 
                    aggregate_greendex_rating = 7.0, 
                    lifestyle_types = [
                        null
                        ], 
                    total_reviews = 989, 
                    reservations = wink_sdk_inventory.models.contact_non_authenticated_entity.Contact_Non_Authenticated_Entity(
                        first_name = 'John', 
                        last_name = 'Smith', 
                        email = 'johnsmith@email.com', 
                        secondary_email = 'johnsmith2@email.com', 
                        phone_number = '+12125551212', 
                        full_name = 'John Smith', 
                        summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                    socials = [
                        wink_sdk_inventory.models.social_non_authenticated_entity.Social_Non_Authenticated_Entity(
                            type = 'FACEBOOK', 
                            location = '', )
                        ], 
                    images = [
                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                            multimedia_identifier = 'image-1', 
                            identifier = 'cloudinary-image-1', 
                            type = 'IMAGE', 
                            source = 'CLOUDINARY', 
                            sort = 10, 
                            angle = '-90', 
                            width = 2560, 
                            height = 1600, 
                            published = True, 
                            category = '1', 
                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                            attribution = [
                                wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                    url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                    name = 'Samuel Adams', )
                                ], 
                            is_landscape = True, )
                        ], 
                    videos = [
                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                            multimedia_identifier = 'image-1', 
                            identifier = 'cloudinary-image-1', 
                            type = 'IMAGE', 
                            source = 'CLOUDINARY', 
                            sort = 10, 
                            angle = '-90', 
                            width = 2560, 
                            height = 1600, 
                            published = True, 
                            category = '1', 
                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                            is_landscape = True, )
                        ], 
                    policy = wink_sdk_inventory.models.property_policy_non_authenticated_entity.PropertyPolicy_Non_Authenticated_Entity(
                        children_allowed = True, 
                        children_minimum_age = 6, 
                        internet_availability = 'YES', 
                        internet_connection_type = 'WIFI', 
                        internet_connection_location = 'ENTIRE_PROPERTY', 
                        parking_availability = 'YES', 
                        parking_access = 'PRIVATE', 
                        pets_allowed = True, 
                        pet_max_weight_in_kilos = 10, 
                        pet_charge = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                            amount = 1.337, 
                            currency = '0', ), 
                        check_out_time = '10:00', 
                        check_in_time = '14:00', ), 
                    third_party_reviews = [
                        wink_sdk_inventory.models.travel_inventory_recognition_non_authenticated_entity.TravelInventoryRecognition_Non_Authenticated_Entity(
                            identifier = 'recognition-1', 
                            category = 'AWARD', 
                            type = 'PERCENT_RATING', 
                            provider = 'Michelin', 
                            rating = 8.5, 
                            max_rating = 10, 
                            date = '2020-10-24', 
                            official_appointment_ind = True, 
                            rating_symbol = '*', )
                        ], 
                    attractions = 5, 
                    activities = 3, 
                    places = 9, 
                    restaurants = 2, 
                    meeting_rooms = 2, 
                    spas = 1, 
                    add_ons = 5, 
                    general_manager = wink_sdk_inventory.models.general_manager_non_authenticated_entity.GeneralManager_Non_Authenticated_Entity(
                        name = 'Jane Doe', 
                        image = cl-image-1, ), 
                    location_category = '34', 
                    segment_category = '7', 
                    hotel_category = '45', 
                    architectural_style = '7', 
                    when_built = '1927', 
                    currency_code = 'USD', 
                    membership_rate_discount = 9, 
                    price_score = 9, 
                    perk_score = 4, 
                    add_on_score = 4, 
                    loyalty_score = 5, 
                    popular_score = 45, 
                    experience_score = 5, 
                    hotel_amenity_codes = [1, 7], 
                    property_accessibility_codes = [1, 7], 
                    property_security_codes = [1, 7], 
                    number_of_rooms = 32, 
                    address = wink_sdk_inventory.models.simple_address_non_authenticated_entity.SimpleAddress_Non_Authenticated_Entity(
                        address1 = '234', 
                        address2 = 'Pebble #5001', 
                        state = 'CA', 
                        postal_code = '90210', 
                        county = 'Alameda county', 
                        city = '0', 
                        country_code = '0', 
                        country = 'United States', 
                        full_address = '11', ), 
                    active = True, 
                    url_parameters = '', ),
                lowest_price = wink_sdk_inventory.models.room_type_best_price_non_authenticated_entity.RoomTypeBestPrice_Non_Authenticated_Entity(
                    room_type_identifier = '', 
                    price = wink_sdk_inventory.models.room_configuration_price_non_authenticated_entity.RoomConfigurationPrice_Non_Authenticated_Entity(
                        adults = 56, 
                        children = 56, 
                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        room_rate_identifier = '', 
                        room_rate_internal_name = '', 
                        rate_plan = wink_sdk_inventory.models.room_configuration_price_rate_plan_non_authenticated_entity.RoomConfigurationPriceRatePlan_Non_Authenticated_Entity(
                            identifier = '0', 
                            name = 'BAR 1', 
                            breakfast = False, 
                            brunch = False, 
                            lunch = False, 
                            dinner = False, 
                            all_inclusive = False, 
                            all_inclusive_plus_alcohol = False, 
                            early_check_in_charge = null, 
                            late_check_out_charge = null, 
                            cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                identifier = '', 
                                hotel_identifier = '', 
                                refundable = False, 
                                advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                policy_code = '', ), 
                            cancellation_policy_exceptions = wink_sdk_inventory.models.cancellation_policy_exceptions_non_authenticated_entity.CancellationPolicyExceptions_Non_Authenticated_Entity(
                                list = [
                                    wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity.CancellationPolicyException_Non_Authenticated_Entity(
                                        cancellation_policy_identifier = '0', 
                                        cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                            identifier = '', 
                                            hotel_identifier = '', 
                                            refundable = False, 
                                            advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                            refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                            no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                            non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                            non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                            non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                            policy_code = '', ), 
                                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                                    ], ), ), 
                        perk_types = [
                            null
                            ], 
                        price = wink_sdk_inventory.models.stay_rate_non_authenticated_entity.StayRate_Non_Authenticated_Entity(
                            user_specified_currency_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                amount = 1.337, 
                                currency = '0', ), 
                            source_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                amount = 1.337, 
                                currency = '0', ), 
                            internal_base_total = , 
                            source_extra_pax_modifier = 15, 
                            internal_extra_pax_modifier = 15, 
                            user_specified_currency_extra_pax_modifier = 15, 
                            source_extra_child_modifier = 15, 
                            internal_extra_child_modifier = 15, 
                            user_specified_currency_extra_child_modifier = 15, 
                            source_single_occupant_modifier = -15, 
                            internal_single_occupant_modifier = -15, 
                            user_specified_currency_single_occupant_modifier = -15, 
                            source_promotional_modifier = -40, 
                            internal_promotional_modifier = -40, 
                            user_specified_currency_promotional_modifier = -40, 
                            source_premium_modifier = 40, 
                            internal_premium_modifier = 40, 
                            user_specified_currency_premium_modifier = 40, 
                            source_channel_modifier = -10, 
                            internal_channel_modifier = -10, 
                            user_specified_currency_channel_modifier = -10, 
                            quantity = 56, 
                            min_occupancy = 56, 
                            max_occupancy = 56, 
                            rate_source = '', 
                            promotional_discount_percent = 1.337, 
                            channel_discount_percent = 1.337, 
                            premium_percent = 1.337, 
                            available = True, 
                            source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                source = '0', 
                                target = '0', 
                                exchange_rate = 1.337, 
                                timestamp = 56, ), 
                            source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                source = '0', 
                                target = '0', 
                                exchange_rate = 1.337, 
                                timestamp = 56, ), 
                            offer_details = [
                                wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                    description = 'This is a longer description in the specified language.', 
                                    language = 'en', )
                                ], 
                            promotional_codes = [
                                ''
                                ], 
                            user_specified_currency_total = , 
                            source_total = , 
                            internal_total = , 
                            user_specified_currency_average_price_per_night = , 
                            internal_average_price_per_night = , 
                            source_average_price_per_night = , 
                            total_discount_percent = 1.337, ), 
                        extra_charges = wink_sdk_inventory.models.extra_charges_non_authenticated_entity.ExtraCharges_Non_Authenticated_Entity(
                            items = [
                                wink_sdk_inventory.models.extra_charge_non_authenticated_entity.ExtraCharge_Non_Authenticated_Entity(
                                    rate_plan_level_fee = wink_sdk_inventory.models.rate_plan_level_fee_non_authenticated_entity.RatePlanLevelFee_Non_Authenticated_Entity(
                                        descriptions = [
                                            wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                                description = 'This is a longer description in the specified language.', 
                                                language = 'en', )
                                            ], 
                                        fixed_amount = , 
                                        type = 'PER_DAY', ), 
                                    unit_price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                        source_to_user_currency_quote = , 
                                        source_to_internal_currency_quote = , 
                                        user_specified_currency_base_total = , 
                                        source_base_total = , 
                                        internal_base_total = , 
                                        user_specified_currency_promotional_modifier = -40, 
                                        source_promotional_modifier = -40, 
                                        internal_promotional_modifier = -40, 
                                        user_specified_currency_premium_modifier = 40, 
                                        source_premium_modifier = 40, 
                                        internal_premium_modifier = 40, 
                                        user_specified_currency_channel_modifier = -10, 
                                        source_channel_modifier = -10, 
                                        internal_channel_modifier = -10, 
                                        quantity = 56, 
                                        promotional_discount_percent = 1.337, 
                                        channel_discount_percent = 1.337, 
                                        premium_percent = 1.337, 
                                        has_premium = True, 
                                        has_promotion = True, 
                                        total_discount_percent = 1.337, 
                                        has_channel_discount = True, ), )
                                ], ), 
                        configuration = wink_sdk_inventory.models.room_configuration_non_authenticated_entity.RoomConfiguration_Non_Authenticated_Entity(
                            adults = 2, 
                            children = [
                                wink_sdk_inventory.models.child_non_authenticated_entity.Child_Non_Authenticated_Entity(
                                    quantity = 1, 
                                    age = 0, )
                                ], ), 
                        add_on_offers = [
                            null
                            ], 
                        perk_value = 56, 
                        active_cancellation_policy = , 
                        room_nights = 56, 
                        list = [
                            wink_sdk_inventory.models.localized_transactional_travel_inventory_non_authenticated_entity.LocalizedTransactionalTravelInventory_Non_Authenticated_Entity(
                                identifier = 'travel-blocking-1', 
                                name = '1', 
                                descriptions = [
                                    wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                        name = 'An example title', 
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', )
                                    ], 
                                pricing_type = 'PER_STAY', 
                                price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                    source_to_user_currency_quote = , 
                                    source_to_internal_currency_quote = , 
                                    user_specified_currency_base_total = , 
                                    source_base_total = , 
                                    internal_base_total = , 
                                    user_specified_currency_promotional_modifier = -40, 
                                    source_promotional_modifier = -40, 
                                    internal_promotional_modifier = -40, 
                                    user_specified_currency_premium_modifier = 40, 
                                    source_premium_modifier = 40, 
                                    internal_premium_modifier = 40, 
                                    user_specified_currency_channel_modifier = -10, 
                                    source_channel_modifier = -10, 
                                    internal_channel_modifier = -10, 
                                    quantity = 56, 
                                    promotional_discount_percent = 1.337, 
                                    channel_discount_percent = 1.337, 
                                    premium_percent = 1.337, 
                                    has_premium = True, 
                                    has_promotion = True, 
                                    total_discount_percent = 1.337, 
                                    has_channel_discount = True, ), 
                                multimedias = [
                                    wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                        multimedia_identifier = 'image-1', 
                                        identifier = 'cloudinary-image-1', 
                                        type = 'IMAGE', 
                                        source = 'CLOUDINARY', 
                                        sort = 10, 
                                        angle = '-90', 
                                        width = 2560, 
                                        height = 1600, 
                                        published = True, 
                                        category = '1', 
                                        lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                        attribution = [
                                            wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                                url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                                name = 'Samuel Adams', )
                                            ], 
                                        is_landscape = True, )
                                    ], 
                                min_pax = 2, 
                                max_pax = 10, 
                                promotion = '', )
                            ], 
                        channel_inventory_identifier = '', 
                        commissionable = True, 
                        commission = 0.1, 
                        direct = True, 
                        price_list = [
                            null
                            ], 
                        available = True, 
                        rate_source = '', 
                        source_total = , 
                        user_specified_currency_total = , 
                        internal_total = , ), 
                    perk_value = 56, 
                    available = True, 
                    sort = 56, ),
                room_type_list = [
                    wink_sdk_inventory.models.guest_room_lightweight_non_authenticated_entity.GuestRoomLightweight_Non_Authenticated_Entity(
                        identifier = 'document-1', 
                        hotel_identifier = 'hotel-1', 
                        featured_ind = False, 
                        lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                        location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                        descriptions = [
                            wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                name = 'An example title', 
                                description = 'This is a longer description in the specified language.', 
                                language = 'en', )
                            ], 
                        multimedias = [
                            wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                multimedia_identifier = 'image-1', 
                                identifier = 'cloudinary-image-1', 
                                type = 'IMAGE', 
                                source = 'CLOUDINARY', 
                                sort = 10, 
                                angle = '-90', 
                                width = 2560, 
                                height = 1600, 
                                published = True, 
                                category = '1', 
                                lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                attribution = [
                                    wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                        url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                        name = 'Samuel Adams', )
                                    ], 
                                is_landscape = True, )
                            ], 
                        contact = wink_sdk_inventory.models.contact_non_authenticated_entity.Contact_Non_Authenticated_Entity(
                            first_name = 'John', 
                            last_name = 'Smith', 
                            email = 'johnsmith@email.com', 
                            secondary_email = 'johnsmith2@email.com', 
                            phone_number = '+12125551212', 
                            full_name = 'John Smith', 
                            summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                        address = wink_sdk_inventory.models.simple_address_non_authenticated_entity.SimpleAddress_Non_Authenticated_Entity(
                            address1 = '234', 
                            address2 = 'Pebble #5001', 
                            state = 'CA', 
                            postal_code = '90210', 
                            county = 'Alameda county', 
                            city = '0', 
                            country_code = '0', 
                            country = 'United States', 
                            full_address = '11', ), 
                        commissionable = True, 
                        name = 'Archery lesson', 
                        proximity_code = '1', 
                        sort = 1, 
                        min_age_appropriate_code = '1', 
                        bookable = True, 
                        active = True, 
                        disability_features = [
                            ''
                            ], 
                        security_features = [
                            ''
                            ], 
                        socials = [
                            wink_sdk_inventory.models.social_non_authenticated_entity.Social_Non_Authenticated_Entity(
                                type = 'FACEBOOK', 
                                location = '', )
                            ], 
                        price_point = 'THREE', 
                        recognition_list = [
                            wink_sdk_inventory.models.travel_inventory_recognition_non_authenticated_entity.TravelInventoryRecognition_Non_Authenticated_Entity(
                                identifier = 'recognition-1', 
                                category = 'AWARD', 
                                type = 'PERCENT_RATING', 
                                provider = 'Michelin', 
                                rating = 8.5, 
                                max_rating = 10, 
                                date = '2020-10-24', 
                                official_appointment_ind = True, 
                                rating_symbol = '*', )
                            ], 
                        max_occupancy = 2, 
                        min_occupancy = 1, 
                        quantity = 40, 
                        non_smoking = True, 
                        bedroom_configuration_list = [
                            wink_sdk_inventory.models.bedroom_configuration_non_authenticated_entity.BedroomConfiguration_Non_Authenticated_Entity(
                                identifier = '0', 
                                name = '0', 
                                bedroom_list = [
                                    wink_sdk_inventory.models.bedroom_non_authenticated_entity.Bedroom_Non_Authenticated_Entity(
                                        type = 'MASTER', 
                                        bed_list = [
                                            wink_sdk_inventory.models.bed_non_authenticated_entity.Bed_Non_Authenticated_Entity(
                                                bed_type_code = '1', 
                                                quantity = 10, )
                                            ], )
                                    ], )
                            ], 
                        size = 55, 
                        max_adult_occupancy = 1, 
                        max_child_occupancy = 0, 
                        bathroom_count = 0, 
                        living_room_count = 0, 
                        max_rollaways = 0, 
                        room_category = '1', 
                        floor = '', 
                        room_location_code = '1', 
                        room_view_code = '1', 
                        composite = False, 
                        composite_count = 2, 
                        room_classification_code = '1', 
                        room_architecture_code = '1', 
                        room_gender = 'Unknown', 
                        shared_room_ind = False, 
                        max_cribs = 1, 
                        amenities = [
                            ''
                            ], 
                        included_adult_occupancy = 2, 
                        included_child_occupancy = 0, )
                    ],
                price_list = [
                    wink_sdk_inventory.models.room_type_best_price_non_authenticated_entity.RoomTypeBestPrice_Non_Authenticated_Entity(
                        room_type_identifier = '', 
                        price = wink_sdk_inventory.models.room_configuration_price_non_authenticated_entity.RoomConfigurationPrice_Non_Authenticated_Entity(
                            adults = 56, 
                            children = 56, 
                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            room_rate_identifier = '', 
                            room_rate_internal_name = '', 
                            rate_plan = wink_sdk_inventory.models.room_configuration_price_rate_plan_non_authenticated_entity.RoomConfigurationPriceRatePlan_Non_Authenticated_Entity(
                                identifier = '0', 
                                name = 'BAR 1', 
                                breakfast = False, 
                                brunch = False, 
                                lunch = False, 
                                dinner = False, 
                                all_inclusive = False, 
                                all_inclusive_plus_alcohol = False, 
                                early_check_in_charge = null, 
                                late_check_out_charge = null, 
                                cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                    identifier = '', 
                                    hotel_identifier = '', 
                                    refundable = False, 
                                    advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                    refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                    no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                    non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                    non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                    non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                    policy_code = '', ), 
                                cancellation_policy_exceptions = wink_sdk_inventory.models.cancellation_policy_exceptions_non_authenticated_entity.CancellationPolicyExceptions_Non_Authenticated_Entity(
                                    list = [
                                        wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity.CancellationPolicyException_Non_Authenticated_Entity(
                                            cancellation_policy_identifier = '0', 
                                            cancellation_policy = wink_sdk_inventory.models.cancellation_policy_lightweight_non_authenticated_entity.CancellationPolicyLightweight_Non_Authenticated_Entity(
                                                identifier = '', 
                                                hotel_identifier = '', 
                                                refundable = False, 
                                                advance_cancellation_free_of_charge = 'UNTIL_EIGHTEEN_HUNDRED_HOURS_ON_DAY_OF_ARRIVAL', 
                                                refundable_cancellation_charge = 'FIFTY_PERCENT', 
                                                no_show_charge = 'SAME_AS_CANCELLATION_FEE', 
                                                non_refundable_cancellation_charge = 'SEVENTY_PERCENT', 
                                                non_refundable_deadline = 'SEVEN_DAYS_BEFORE_ARRIVAL', 
                                                non_refundable_after_deadline_cancellation_charge = 'ONE_HUNDRED_PERCENT', 
                                                policy_code = '', ), 
                                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                            end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                                        ], ), ), 
                            perk_types = [
                                null
                                ], 
                            price = wink_sdk_inventory.models.stay_rate_non_authenticated_entity.StayRate_Non_Authenticated_Entity(
                                user_specified_currency_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                    amount = 1.337, 
                                    currency = '0', ), 
                                source_base_total = wink_sdk_inventory.models.custom_monetary_amount.CustomMonetaryAmount(
                                    amount = 1.337, 
                                    currency = '0', ), 
                                internal_base_total = , 
                                source_extra_pax_modifier = 15, 
                                internal_extra_pax_modifier = 15, 
                                user_specified_currency_extra_pax_modifier = 15, 
                                source_extra_child_modifier = 15, 
                                internal_extra_child_modifier = 15, 
                                user_specified_currency_extra_child_modifier = 15, 
                                source_single_occupant_modifier = -15, 
                                internal_single_occupant_modifier = -15, 
                                user_specified_currency_single_occupant_modifier = -15, 
                                source_promotional_modifier = -40, 
                                internal_promotional_modifier = -40, 
                                user_specified_currency_promotional_modifier = -40, 
                                source_premium_modifier = 40, 
                                internal_premium_modifier = 40, 
                                user_specified_currency_premium_modifier = 40, 
                                source_channel_modifier = -10, 
                                internal_channel_modifier = -10, 
                                user_specified_currency_channel_modifier = -10, 
                                quantity = 56, 
                                min_occupancy = 56, 
                                max_occupancy = 56, 
                                rate_source = '', 
                                promotional_discount_percent = 1.337, 
                                channel_discount_percent = 1.337, 
                                premium_percent = 1.337, 
                                available = True, 
                                source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                offer_details = [
                                    wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', )
                                    ], 
                                promotional_codes = [
                                    ''
                                    ], 
                                user_specified_currency_total = , 
                                source_total = , 
                                internal_total = , 
                                user_specified_currency_average_price_per_night = , 
                                internal_average_price_per_night = , 
                                source_average_price_per_night = , 
                                total_discount_percent = 1.337, ), 
                            extra_charges = wink_sdk_inventory.models.extra_charges_non_authenticated_entity.ExtraCharges_Non_Authenticated_Entity(
                                items = [
                                    wink_sdk_inventory.models.extra_charge_non_authenticated_entity.ExtraCharge_Non_Authenticated_Entity(
                                        rate_plan_level_fee = wink_sdk_inventory.models.rate_plan_level_fee_non_authenticated_entity.RatePlanLevelFee_Non_Authenticated_Entity(
                                            descriptions = [
                                                wink_sdk_inventory.models.localized_description_non_authenticated_entity.LocalizedDescription_Non_Authenticated_Entity(
                                                    description = 'This is a longer description in the specified language.', 
                                                    language = 'en', )
                                                ], 
                                            fixed_amount = , 
                                            type = 'PER_DAY', ), 
                                        unit_price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                            source_to_user_currency_quote = , 
                                            source_to_internal_currency_quote = , 
                                            user_specified_currency_base_total = , 
                                            source_base_total = , 
                                            internal_base_total = , 
                                            user_specified_currency_promotional_modifier = -40, 
                                            source_promotional_modifier = -40, 
                                            internal_promotional_modifier = -40, 
                                            user_specified_currency_premium_modifier = 40, 
                                            source_premium_modifier = 40, 
                                            internal_premium_modifier = 40, 
                                            user_specified_currency_channel_modifier = -10, 
                                            source_channel_modifier = -10, 
                                            internal_channel_modifier = -10, 
                                            quantity = 56, 
                                            promotional_discount_percent = 1.337, 
                                            channel_discount_percent = 1.337, 
                                            premium_percent = 1.337, 
                                            has_premium = True, 
                                            has_promotion = True, 
                                            total_discount_percent = 1.337, 
                                            has_channel_discount = True, ), )
                                    ], ), 
                            configuration = wink_sdk_inventory.models.room_configuration_non_authenticated_entity.RoomConfiguration_Non_Authenticated_Entity(
                                adults = 2, 
                                children = [
                                    wink_sdk_inventory.models.child_non_authenticated_entity.Child_Non_Authenticated_Entity(
                                        quantity = 1, 
                                        age = 0, )
                                    ], ), 
                            add_on_offers = [
                                null
                                ], 
                            perk_value = 56, 
                            active_cancellation_policy = , 
                            room_nights = 56, 
                            list = [
                                wink_sdk_inventory.models.localized_transactional_travel_inventory_non_authenticated_entity.LocalizedTransactionalTravelInventory_Non_Authenticated_Entity(
                                    identifier = 'travel-blocking-1', 
                                    name = '1', 
                                    descriptions = [
                                        wink_sdk_inventory.models.simple_description_non_authenticated_entity.SimpleDescription_Non_Authenticated_Entity(
                                            name = 'An example title', 
                                            description = 'This is a longer description in the specified language.', 
                                            language = 'en', )
                                        ], 
                                    pricing_type = 'PER_STAY', 
                                    price = wink_sdk_inventory.models.localized_price_non_authenticated_entity.LocalizedPrice_Non_Authenticated_Entity(
                                        source_to_user_currency_quote = , 
                                        source_to_internal_currency_quote = , 
                                        user_specified_currency_base_total = , 
                                        source_base_total = , 
                                        internal_base_total = , 
                                        user_specified_currency_promotional_modifier = -40, 
                                        source_promotional_modifier = -40, 
                                        internal_promotional_modifier = -40, 
                                        user_specified_currency_premium_modifier = 40, 
                                        source_premium_modifier = 40, 
                                        internal_premium_modifier = 40, 
                                        user_specified_currency_channel_modifier = -10, 
                                        source_channel_modifier = -10, 
                                        internal_channel_modifier = -10, 
                                        quantity = 56, 
                                        promotional_discount_percent = 1.337, 
                                        channel_discount_percent = 1.337, 
                                        premium_percent = 1.337, 
                                        has_premium = True, 
                                        has_promotion = True, 
                                        total_discount_percent = 1.337, 
                                        has_channel_discount = True, ), 
                                    multimedias = [
                                        wink_sdk_inventory.models.simple_multimedia_non_authenticated_entity.SimpleMultimedia_Non_Authenticated_Entity(
                                            multimedia_identifier = 'image-1', 
                                            identifier = 'cloudinary-image-1', 
                                            type = 'IMAGE', 
                                            source = 'CLOUDINARY', 
                                            sort = 10, 
                                            angle = '-90', 
                                            width = 2560, 
                                            height = 1600, 
                                            published = True, 
                                            category = '1', 
                                            lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                            attribution = [
                                                wink_sdk_inventory.models.image_attribution_non_authenticated_entity.ImageAttribution_Non_Authenticated_Entity(
                                                    url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                                    name = 'Samuel Adams', )
                                                ], 
                                            is_landscape = True, )
                                        ], 
                                    min_pax = 2, 
                                    max_pax = 10, 
                                    promotion = '', )
                                ], 
                            channel_inventory_identifier = '', 
                            commissionable = True, 
                            commission = 0.1, 
                            direct = True, 
                            available = True, 
                            rate_source = '', 
                            source_total = , 
                            user_specified_currency_total = , 
                            internal_total = , ), 
                        perk_value = 56, 
                        available = True, 
                        sort = 56, )
                    ],
                potential_channel_discount_percent = 1.337,
                source_to_user_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                    source = '0', 
                    target = '0', 
                    exchange_rate = 1.337, 
                    timestamp = 56, ),
                source_to_internal_currency_quote = wink_sdk_inventory.models.quote_lightweight_non_authenticated_entity.QuoteLightweight_Non_Authenticated_Entity(
                    source = '0', 
                    target = '0', 
                    exchange_rate = 1.337, 
                    timestamp = 56, ),
        )
        """

    def testPropertyWithBestPriceNonAuthenticatedEntity(self):
        """Test PropertyWithBestPriceNonAuthenticatedEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
