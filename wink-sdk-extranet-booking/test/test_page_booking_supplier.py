# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md   # Extranet Booking API The Booking API exposes endpoints to manage bookings. This API lets you:  1. Booking: Manage bookings including cancellations. 2. Review: Manage user reviews. 3. Sync w. Calendar: Manage calendar sync with your favorite calendar software  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.17.1
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wink_sdk_extranet_booking.models.page_booking_supplier import PageBookingSupplier

class TestPageBookingSupplier(unittest.TestCase):
    """PageBookingSupplier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageBookingSupplier:
        """Test PageBookingSupplier
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageBookingSupplier`
        """
        model = PageBookingSupplier()
        if include_optional:
            return PageBookingSupplier(
                total_elements = 56,
                total_pages = 56,
                size = 56,
                content = [
                    wink_sdk_extranet_booking.models.booking_supplier.Booking_Supplier(
                        id = 'doc-1', 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        version = 12, 
                        creation = 'NORMAL', 
                        group_identifier = 'document-1', 
                        customization = wink_sdk_extranet_booking.models.customization_lightweight_supplier.CustomizationLightweight_Supplier(
                            identifier = 'customization-configuration-1', 
                            name = 'Engine Configuration 1', 
                            user_identifier = 'user-1', 
                            owner_identifier = 'company-1', 
                            owner_name = 'Travel Tech 1', 
                            sub_type = 'APPLICATION', 
                            default_currency = 'USD', 
                            default_language = 'en', 
                            default_lifestyle = 'LIFESTYLE_HEALTH_FITNESS', 
                            logos = [
                                wink_sdk_extranet_booking.models.simple_multimedia_supplier.SimpleMultimedia_Supplier(
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
                                    descriptions = [
                                        wink_sdk_extranet_booking.models.simple_description_supplier.SimpleDescription_Supplier(
                                            name = 'An example title', 
                                            description = 'This is a longer description in the specified language.', 
                                            language = 'en', 
                                            creator = 'USER', 
                                            md5_content_hash = '', 
                                            hash_mismatch = True, )
                                        ], 
                                    lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                    attribution = [
                                        wink_sdk_extranet_booking.models.image_attribution_supplier.ImageAttribution_Supplier(
                                            url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                                            name = 'Samuel Adams', )
                                        ], 
                                    is_landscape = True, )
                                ], 
                            hosted_booking_engine_url = 'https://ota.wink.travel', 
                            self_hosted = True, 
                            theme_colors = wink_sdk_extranet_booking.models.customization_theme_colors_supplier.CustomizationThemeColors_Supplier(
                                primary = '#dc3545', 
                                secondary = '#6c757d', 
                                success = '#28a745', 
                                danger = '#dc3545', 
                                warning = '#ffc107', 
                                info = '#17a2b8', 
                                light = '#f8f9fa', 
                                dark = '#343a40', 
                                body = '#212529', 
                                muted = '#6c757d', 
                                white = '#ffffff', ), 
                            card_layout = 'VERTICAL', 
                            layout = 'INFORMATIONAL', 
                            card_design = 'DEFAULT', 
                            number_of_advance_days = 10, 
                            number_of_stay_days = 2, 
                            start_date = '2021-12-24', 
                            end_date = '2021-12-31', 
                            room_configurations = [
                                wink_sdk_extranet_booking.models.room_configuration_supplier.RoomConfiguration_Supplier(
                                    adults = 2, 
                                    children = [
                                        wink_sdk_extranet_booking.models.child_supplier.Child_Supplier(
                                            quantity = 1, 
                                            age = 0, )
                                        ], )
                                ], 
                            use_days = True, 
                            promotional_codes = [promo-1], 
                            send_booking_notification_emails_to_property = True, 
                            send_booking_notification_emails_to_booker = True, 
                            send_booking_notification_emails_to_channel_manager = True, 
                            wc_book_click_action = 'IBE_MODAL', 
                            city = wink_sdk_extranet_booking.models.geo_name_lightweight_supplier.GeoNameLightweight_Supplier(
                                geo_name_id = '5128581', 
                                type = 'CITY', 
                                name = 'New York City', 
                                url_name = 'new-york-city-united-states', 
                                ascii_name = 'New York City', 
                                location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                                feature_code = '', 
                                country_code = '', 
                                timezone = 'America/New_York', 
                                country = wink_sdk_extranet_booking.models.country_lightweight_supplier.CountryLightweight_Supplier(
                                    iso = 'US', 
                                    name = 'United States', 
                                    capital = 'Washington', 
                                    continent = 'NA', 
                                    currency_code = 'USD', 
                                    currency_name = 'Dollar', 
                                    geo_name_id = '6252001', ), 
                                sub_country = wink_sdk_extranet_booking.models.sub_country_lightweight_supplier.SubCountryLightweight_Supplier(
                                    name = 'New York', 
                                    ascii_name = 'New York', 
                                    geo_name_id = '5128638', ), 
                                sub_sub_country = wink_sdk_extranet_booking.models.sub_sub_country_lightweight_supplier.SubSubCountryLightweight_Supplier(
                                    name = '', 
                                    ascii_name = '', 
                                    geo_name_id = '', ), ), 
                            show_unavailable_card = True, 
                            show_rankings = True, 
                            show_search = True, ), 
                        booking_code = 'ABC1234', 
                        user = wink_sdk_extranet_booking.models.booking_user_supplier.BookingUser_Supplier(
                            user_identifier = '', 
                            first_name = 'John', 
                            last_name = 'Smith', 
                            email = 'john.smith@email.com', 
                            telephone = '+1 212 555 1212', 
                            full_name = 'John Smith', ), 
                        user_session = wink_sdk_extranet_booking.models.booking_user_session_supplier.BookingUserSession_Supplier(
                            itinerary = wink_sdk_extranet_booking.models.booking_itinerary_supplier.BookingItinerary_Supplier(
                                start_date = '2024-01-01', 
                                end_date = '2024-01-02', 
                                nights = 56, 
                                items = [
                                    wink_sdk_extranet_booking.models.booking_itinerary_room_configuration_supplier.BookingItineraryRoomConfiguration_Supplier(
                                        adults = 2, )
                                    ], 
                                hours = 56, 
                                rooms = 56, 
                                guests = 56, ), 
                            language = 'en', 
                            currency = 'USD', 
                            promotional_codes = [
                                null
                                ], 
                            selected_room_configuration_index = 56, 
                            lifestyle = 'LIFESTYLE_HEALTH_FITNESS', ), 
                        server_url = '', 
                        socials = [
                            wink_sdk_extranet_booking.models.social_supplier.Social_Supplier(
                                type = 'FACEBOOK', 
                                location = '', )
                            ], 
                        review = wink_sdk_extranet_booking.models.review_lightweight_supplier.ReviewLightweight_Supplier(
                            identifier = 'review-1', 
                            booking_identifier = 'booking-1', 
                            hotel_identifier = 'hotel-1', 
                            review_date = '2017-12-22T03:07:58.742+0000', 
                            average_score = 8.7, 
                            answers = [
                                wink_sdk_extranet_booking.models.review_answer_supplier.ReviewAnswer_Supplier(
                                    question_identifier = '0', 
                                    category = 'COMFORT', 
                                    sort = 56, 
                                    value = 56, )
                                ], 
                            message_from_guest = 'Dear GM, I would like to say thank you so much for taking the time to show my husband and I around the premises and the secret cave behind the property.', 
                            response_from_hotel = 'It was so great to have you at our hotel. Please recommend your friends and come again soon.', 
                            image_identifier = 'cloudinary-image-1', 
                            text = 'Our stay was amazing! Can recommend highly to all. Felt like home.', 
                            approved_text = True, 
                            approved_image = False, 
                            likes = [
                                ''
                                ], 
                            room_number = '501', 
                            room_rating = 7, 
                            responded = False, ), 
                        email_header_logo_url = '', 
                        logo_identifier = '', 
                        hotel = wink_sdk_extranet_booking.models.property_aggregate_lightweight_supplier.PropertyAggregateLightweight_Supplier(
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
                            aggregate_greendex_rating = 7.0, 
                            lifestyle_types = [
                                null
                                ], 
                            total_reviews = 989, 
                            reservations = wink_sdk_extranet_booking.models.contact_supplier.Contact_Supplier(
                                first_name = 'John', 
                                last_name = 'Smith', 
                                email = 'johnsmith@email.com', 
                                secondary_email = 'johnsmith2@email.com', 
                                phone_number = '+12125551212', 
                                full_name = 'John Smith', 
                                summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                            images = [
                                wink_sdk_extranet_booking.models.simple_multimedia_supplier.SimpleMultimedia_Supplier(
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
                            videos = [
                                
                                ], 
                            policy = wink_sdk_extranet_booking.models.property_policy_supplier.PropertyPolicy_Supplier(
                                children_allowed = True, 
                                children_minimum_age = 6, 
                                internet_availability = 'YES', 
                                internet_connection_type = 'WIFI', 
                                internet_connection_location = 'ENTIRE_PROPERTY', 
                                parking_availability = 'YES', 
                                parking_access = 'PRIVATE', 
                                pets_allowed = True, 
                                pet_max_weight_in_kilos = 10, 
                                pet_charge = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                                    amount = 1.337, 
                                    currency = '0', ), 
                                check_out_time = '10:00', 
                                check_in_time = '14:00', ), 
                            third_party_reviews = [
                                wink_sdk_extranet_booking.models.travel_inventory_recognition_supplier.TravelInventoryRecognition_Supplier(
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
                            general_manager = wink_sdk_extranet_booking.models.general_manager_supplier.GeneralManager_Supplier(
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
                            address = wink_sdk_extranet_booking.models.simple_address_supplier.SimpleAddress_Supplier(
                                address1 = '234', 
                                address2 = 'Pebble #5001', 
                                state = 'CA', 
                                postal_code = '90210', 
                                county = 'Alameda county', 
                                city = '0', 
                                country_code = '0', 
                                full_address = '11', ), 
                            active = True, 
                            url_parameters = '', ), 
                        room_stay = wink_sdk_extranet_booking.models.room_stay_supplier.RoomStay_Supplier(
                            policy = wink_sdk_extranet_booking.models.property_policy_supplier.PropertyPolicy_Supplier(
                                children_allowed = True, 
                                children_minimum_age = 6, 
                                internet_availability = 'YES', 
                                internet_connection_type = 'WIFI', 
                                internet_connection_location = 'ENTIRE_PROPERTY', 
                                parking_availability = 'YES', 
                                parking_access = 'PRIVATE', 
                                pets_allowed = True, 
                                pet_max_weight_in_kilos = 10, 
                                check_out_time = '10:00', 
                                check_in_time = '14:00', ), 
                            room = wink_sdk_extranet_booking.models.guest_room_lightweight_supplier.GuestRoomLightweight_Supplier(
                                identifier = 'document-1', 
                                hotel_identifier = 'hotel-1', 
                                featured_ind = False, 
                                lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                                location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                                descriptions = [
                                    wink_sdk_extranet_booking.models.simple_description_supplier.SimpleDescription_Supplier(
                                        name = 'An example title', 
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', 
                                        creator = 'USER', 
                                        md5_content_hash = '', 
                                        hash_mismatch = True, )
                                    ], 
                                multimedias = [
                                    
                                    ], 
                                contact = wink_sdk_extranet_booking.models.contact_supplier.Contact_Supplier(
                                    first_name = 'John', 
                                    last_name = 'Smith', 
                                    email = 'johnsmith@email.com', 
                                    secondary_email = 'johnsmith2@email.com', 
                                    phone_number = '+12125551212', 
                                    full_name = 'John Smith', 
                                    summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                                address = wink_sdk_extranet_booking.models.simple_address_supplier.SimpleAddress_Supplier(
                                    address1 = '234', 
                                    address2 = 'Pebble #5001', 
                                    state = 'CA', 
                                    postal_code = '90210', 
                                    county = 'Alameda county', 
                                    city = '0', 
                                    country_code = '0', 
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
                                price_point = 'THREE', 
                                recognition_list = [
                                    wink_sdk_extranet_booking.models.travel_inventory_recognition_supplier.TravelInventoryRecognition_Supplier(
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
                                transactional_inventory_list = [
                                    wink_sdk_extranet_booking.models.transactional_travel_inventory_supplier.TransactionalTravelInventory_Supplier(
                                        identifier = 'travel-blocking-1', 
                                        name = '1', 
                                        descriptions = [
                                            
                                            ], 
                                        pricing_type = 'PER_STAY', 
                                        base_price = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                                            amount = 1.337, 
                                            currency = '0', ), 
                                        discounted_price = , 
                                        min_pax = 2, 
                                        max_pax = 10, 
                                        percent_discount = 0.1, 
                                        percent_premium = 0.1, )
                                    ], 
                                max_occupancy = 2, 
                                min_occupancy = 1, 
                                quantity = 40, 
                                non_smoking = True, 
                                bedroom_configuration_list = [
                                    wink_sdk_extranet_booking.models.bedroom_configuration_supplier.BedroomConfiguration_Supplier(
                                        identifier = '0', 
                                        name = '0', 
                                        bedroom_list = [
                                            wink_sdk_extranet_booking.models.bedroom_supplier.Bedroom_Supplier(
                                                type = 'MASTER', 
                                                bed_list = [
                                                    wink_sdk_extranet_booking.models.bed_supplier.Bed_Supplier(
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
                                included_child_occupancy = 0, 
                                base_rate = , 
                                min_rate = , ), 
                            rooms = 1, 
                            bedroom_configuration = wink_sdk_extranet_booking.models.bedroom_configuration_supplier.BedroomConfiguration_Supplier(
                                identifier = '0', 
                                name = '0', 
                                bedroom_list = [
                                    wink_sdk_extranet_booking.models.bedroom_supplier.Bedroom_Supplier(
                                        type = 'MASTER', 
                                        bed_list = [
                                            wink_sdk_extranet_booking.models.bed_supplier.Bed_Supplier(
                                                bed_type_code = '1', 
                                                quantity = 10, )
                                            ], )
                                    ], ), 
                            adults = 2, 
                            children = 0, 
                            start_date = '2021-12-24', 
                            end_date = '2021-12-31', 
                            price = wink_sdk_extranet_booking.models.stay_rate_supplier.StayRate_Supplier(
                                user_specified_currency_base_total = , 
                                source_base_total = , 
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
                                source_to_user_currency_quote = wink_sdk_extranet_booking.models.quote_lightweight_supplier.QuoteLightweight_Supplier(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                source_to_internal_currency_quote = wink_sdk_extranet_booking.models.quote_lightweight_supplier.QuoteLightweight_Supplier(
                                    source = '0', 
                                    target = '0', 
                                    exchange_rate = 1.337, 
                                    timestamp = 56, ), 
                                offer_details = [
                                    wink_sdk_extranet_booking.models.localized_description_supplier.LocalizedDescription_Supplier(
                                        description = 'This is a longer description in the specified language.', 
                                        language = 'en', 
                                        creator = 'USER', 
                                        md5_content_hash = '', 
                                        hash_mismatch = True, )
                                    ], 
                                user_specified_currency_total = , 
                                source_total = , 
                                internal_total = , 
                                user_specified_currency_average_price_per_night = , 
                                internal_average_price_per_night = , 
                                source_average_price_per_night = , 
                                total_discount_percent = 1.337, ), 
                            room_rate_identifier = 'master-rate-1', 
                            room_rate_internal_name = 'Master Rate 1', 
                            rate_plan = wink_sdk_extranet_booking.models.room_configuration_price_rate_plan_supplier.RoomConfigurationPriceRatePlan_Supplier(
                                identifier = '0', 
                                name = 'BAR 1', 
                                breakfast = False, 
                                brunch = False, 
                                lunch = False, 
                                dinner = False, 
                                all_inclusive = False, 
                                all_inclusive_plus_alcohol = False, 
                                early_check_in_charge = wink_sdk_extranet_booking.models.variable_charge_supplier.VariableCharge_Supplier(
                                    type = 'FIXED', 
                                    percent = 0.25, 
                                    fixed_amount = , ), 
                                late_check_out_charge = wink_sdk_extranet_booking.models.variable_charge_supplier.VariableCharge_Supplier(
                                    type = 'FIXED', 
                                    percent = 0.25, ), 
                                cancellation_policy = wink_sdk_extranet_booking.models.cancellation_policy_lightweight_supplier.CancellationPolicyLightweight_Supplier(
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
                                cancellation_policy_exceptions = wink_sdk_extranet_booking.models.cancellation_policy_exceptions_supplier.CancellationPolicyExceptions_Supplier(
                                    list = [
                                        wink_sdk_extranet_booking.models.cancellation_policy_exception_supplier.CancellationPolicyException_Supplier(
                                            cancellation_policy_identifier = '0', 
                                            cancellation_policy = wink_sdk_extranet_booking.models.cancellation_policy_lightweight_supplier.CancellationPolicyLightweight_Supplier(
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
                            perk_types = [PERK_FREE_DRINK_VOUCHER, PERK_EARLY_CHECKIN], 
                            extra_charges = wink_sdk_extranet_booking.models.extra_charges_supplier.ExtraCharges_Supplier(), 
                            active_cancellation_policy = , 
                            room_nights = 2, 
                            guests = 56, 
                            rate_source = '', 
                            source_total = , 
                            user_specified_currency_total = , 
                            internal_total = , 
                            cancellable_by_hotel = True, 
                            cancellable_with_potential_charge = True, 
                            cancellable = True, ), 
                        special_requests = '', 
                        comment = '', 
                        early_check_in_charge = , 
                        late_check_out_charge = , 
                        early_check_in_charge_percent = 0.05, 
                        late_check_out_charge_percent = 0.05, 
                        hotel_image_url = 'https://path.to/property-image.jpg', 
                        room_image_url = 'https://path.to/room-image.jpg', 
                        commission_list = [
                            wink_sdk_extranet_booking.models.commissionable_entry_supplier.CommissionableEntry_Supplier(
                                name = '0', 
                                identifier = '0', 
                                type = 'GUEST_ROOM', 
                                commission_percent = 1.337, )
                            ], 
                        ancillary_list = [
                            wink_sdk_extranet_booking.models.booking_ancillary_supplier.BookingAncillary_Supplier(
                                identifier = 'ancillary-1', 
                                hotel_identifier = 'hotel-1', 
                                type_identifier = 'place-1', 
                                transactional_travel_inventory_identifier = 'place-1', 
                                name = 'Place 1', 
                                pricing_type = 'PER_USE', 
                                type = 'PLACE', 
                                price = wink_sdk_extranet_booking.models.localized_price_supplier.LocalizedPrice_Supplier(
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
                                start_date = '2017-12-22T03:07:58.742+0000', 
                                end_date = '2017-12-22T08:07:58.742+0000', 
                                attendees = 2, 
                                image_identifier = 'cloudinary-image-1', 
                                image_url = 'https://path.to.image.com/this-is-me.jpg', 
                                localized_name = 'Plass 1', 
                                localized_description = 'place-1', 
                                contact = , 
                                address = , 
                                commissionable = True, 
                                mandatory = True, 
                                commission = 1.337, )
                            ], 
                        booking_contract = wink_sdk_extranet_booking.models.booking_contract_supplier.BookingContract_Supplier(
                            booking_contract_identifier = 'doc-1', 
                            created_date = '2017-12-22T03:07:58.742+0000', 
                            last_update = '2017-12-22T03:07:58.742+0000', 
                            federated_organization_identifier = 'owner-1', 
                            federated_organization_name = 'Wink', 
                            user = user-1, 
                            ip_address = '111.222.333.444', 
                            trace_id = 'T-123456', 
                            source_url = 'https://www.traveliko.com', 
                            identifier = 'unique-supplier-booking-contract-1', 
                            supplier_identifier = 'supplier-1', 
                            supplier_name = 'Supplier One', 
                            display_price_quote = , 
                            supplier_price_quote = , 
                            internal_price_quote = , 
                            capture_price_quote = , 
                            item_list = [
                                wink_sdk_extranet_booking.models.booking_contract_item_supplier.BookingContractItem_Supplier(
                                    supplier_item_booking_code = 'TP-ASDFG1234', 
                                    user = wink_sdk_extranet_booking.models.guest_user_supplier.GuestUser_Supplier(
                                        user_identifier = '', 
                                        first_name = 'John', 
                                        last_name = 'Smith', 
                                        email = 'john.smith@email.com', 
                                        telephone = '+1 212 555 1212', 
                                        profile = wink_sdk_extranet_booking.models.profile_lightweight_supplier.ProfileLightweight_Supplier(
                                            profile_identifier = '0', 
                                            user_identifier = '0', 
                                            share = True, 
                                            user = wink_sdk_extranet_booking.models.profile_user_supplier.ProfileUser_Supplier(
                                                first_name = 'Avid', 
                                                last_name = 'Travelman', 
                                                email = 'avid@travelman.com', 
                                                phone = '0123456789', 
                                                profile_picture_url = '', 
                                                full_name = 'John Smith', ), 
                                            personal = wink_sdk_extranet_booking.models.personal_supplier.Personal_Supplier(
                                                gender = 'MALE', 
                                                birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                                marital_status = 'ANNULLED', 
                                                child_quantity = 56, 
                                                citizenship = '', 
                                                address1 = '', 
                                                address2 = '', 
                                                state = '', 
                                                postal_code = '', 
                                                preferred_currency = 'USD', 
                                                language = '', 
                                                contact_person = [
                                                    null
                                                    ], 
                                                phys_chall_name = [
                                                    null
                                                    ], 
                                                pet_info = [
                                                    null
                                                    ], ), 
                                            preferences = wink_sdk_extranet_booking.models.preferences_supplier.Preferences_Supplier(
                                                property_location_pref = '', 
                                                property_type_pref = '', 
                                                hotel_chain_pref = '', 
                                                property_amenity_pref = [
                                                    ''
                                                    ], 
                                                recreation_srvc_pref = [
                                                    ''
                                                    ], 
                                                business_srvc_pref = [
                                                    ''
                                                    ], 
                                                security_feature_pref = [
                                                    ''
                                                    ], 
                                                phys_chal_feature_pref = [
                                                    ''
                                                    ], 
                                                smoking_allowed = True, 
                                                room_location_pref = '', 
                                                bed_type_pref = '', 
                                                food_srvc_pref = '', 
                                                room_amenity_pref = [
                                                    ''
                                                    ], 
                                                guest_type = '', 
                                                meal_pref = '', 
                                                cuisine_pref = '', 
                                                interest_pref = [
                                                    ''
                                                    ], 
                                                beverage_pref = [
                                                    ''
                                                    ], 
                                                food_pref = [
                                                    ''
                                                    ], 
                                                allergies = [
                                                    ''
                                                    ], 
                                                pets_pref = [
                                                    ''
                                                    ], ), ), 
                                        full_name = 'John Smith', ), 
                                    name_in_english = 'Deluxe King', 
                                    description_in_english = 'This is the best deluxe king that money can buy.', 
                                    itinerary = wink_sdk_extranet_booking.models.simple_date_time_itinerary_supplier.SimpleDateTimeItinerary_Supplier(
                                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        adults = 0, 
                                        children = 0, 
                                        hours = 56, 
                                        nights = 56, 
                                        guests = 56, ), 
                                    pricing_type = 'PER_STAY', 
                                    type = 'LODGING', 
                                    beneficiary_list = [
                                        wink_sdk_extranet_booking.models.beneficiary_supplier.Beneficiary_Supplier(
                                            account_identifier = 'account-1', 
                                            account_name = 'Account 1', 
                                            account_email = 'account@one.com', 
                                            account_url = 'https://some.url', 
                                            type = 'TRIP_PAY', 
                                            amount_due = wink_sdk_extranet_booking.models.beneficiary_charge_supplier.BeneficiaryCharge_Supplier(
                                                type = 'PERCENTAGE', 
                                                percent = 1.337, ), 
                                            source_currency = 'USD', 
                                            display_currency = 'USD', 
                                            supplier_currency = 'USD', 
                                            internal_currency = 'USD', 
                                            capture_currency = 'USD', 
                                            source_amount = 50, 
                                            display_amount = 50, 
                                            supplier_amount = 50, 
                                            internal_amount = 50, 
                                            capture_amount = 50, 
                                            source_amount_refund_modifier = 5, 
                                            display_amount_refund_modifier = 5, 
                                            supplier_amount_refund_modifier = 5, 
                                            internal_amount_refund_modifier = 5, 
                                            capture_amount_refund_modifier = 5, 
                                            pending_refunds = [
                                                null
                                                ], 
                                            net_source_amount = 0, 
                                            net_display_amount = 0, 
                                            net_supplier_amount = 0, 
                                            net_internal_amount = 0, 
                                            net_capture_amount = 0, 
                                            reconciled = False, 
                                            metadata = {
                                                'key' : ''
                                                }, )
                                        ], 
                                    payable = 'PREPAY', 
                                    external_identifier = 'room-type-1', 
                                    tokens_earned = 12, 
                                    daily_rate_list = [
                                        null
                                        ], 
                                    cancelled = True, 
                                    source_currency = 'USD', 
                                    display_currency = 'USD', 
                                    supplier_currency = 'USD', 
                                    internal_currency = 'USD', 
                                    capture_currency = 'USD', 
                                    source_amount = 0, 
                                    display_amount = 0, 
                                    supplier_amount = 0, 
                                    internal_amount = 0, 
                                    capture_amount = 0, 
                                    source_amount_refund_modifier = 0, 
                                    display_amount_refund_modifier = 0, 
                                    supplier_amount_refund_modifier = 0, 
                                    internal_amount_refund_modifier = 0, 
                                    capture_amount_refund_modifier = 0, 
                                    net_source_amount = 0, 
                                    net_display_amount = 0, 
                                    net_supplier_amount = 0, 
                                    net_internal_amount = 0, 
                                    net_capture_amount = 0, 
                                    metadata = {
                                        'key' : ''
                                        }, 
                                    cancellable_by_traveler = True, 
                                    cancellable_with_no_charges = True, 
                                    cancellable_with_potential_charges = True, 
                                    cancellable_by_supplier_or_agent = True, )
                                ], 
                            external_supplier_identifier = 'supplier-a', 
                            external_supplier_booking_code = 'external-booking-code-1', 
                            payment = wink_sdk_extranet_booking.models.booking_contract_payment_details_supplier.BookingContractPaymentDetails_Supplier(
                                acquirer_identifier = 'stripe-world', 
                                vendor = 'STRIPE', 
                                transaction_identifier = 'tx-1', 
                                customer_identifier = 'customer-1', 
                                charge_identifier = 'charge-1', 
                                status = 'INITIALIZED', 
                                agent_invoiced_date = '2017-12-22T03:07:58.742+0000', 
                                agent_invoice_identifier = 'invoice-1', 
                                redirect_url = '', 
                                fees = [
                                    null
                                    ], 
                                vendor_specific = {
                                    'key' : ''
                                    }, ), 
                            cancelled = False, 
                            cancelled_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            canceller = 'SALES_CHANNEL', 
                            cancellation_type = 'DUPLICATE', 
                            canceller_user_identifier = '', 
                            cancel_reason = '', 
                            funds_processed = False, 
                            refunds = [
                                wink_sdk_extranet_booking.models.refund_supplier.Refund_Supplier(
                                    identifier = 'refund-1', 
                                    acquirer_refund_identifier = 'r-123456', 
                                    requested_by_identifier = 'user-1', 
                                    refund = , 
                                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    description = 'Customer made a mistake', 
                                    reason_type = 'DUPLICATE', 
                                    cancel_on_refund = 'NONE', 
                                    status_type = 'SUCCEEDED', 
                                    request_type = 'BY_ADMIN', 
                                    request_status = 'APPROVED', 
                                    request_response = 'We have rejected your request. Your cancellation policy does not warrant a manual refund.', 
                                    receipt_url = 'https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xSXcxazVBQ3F2UW9nN1IxKIPqo54GMgbHKn45YQY6LBbCZ62655YzamuWDVeWAaw7uApCrxewxjSsZX4C9Lef5jY9JeYFrOVx3IaI', 
                                    retries = 0, 
                                    allocation = 'EQUAL_DISTRIBUTION', )
                                ], 
                            payouts = [
                                wink_sdk_extranet_booking.models.payout_supplier.Payout_Supplier(
                                    vendor = 'STRIPE', 
                                    vendor_identifier = '0', 
                                    vendor_name = '0', 
                                    ledger_identifier = 'ABC1234', 
                                    beneficiary_identifier = 'account-1', 
                                    external_payee_identifier = 'wise-recipient-1', 
                                    type = 'BANK_TRANSFER', 
                                    entry = , 
                                    quote = , 
                                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    description = 'Card created successfully', 
                                    payout_id = 'stripe-card-1', 
                                    reference_code = 'ABC1234', 
                                    reference_code_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    status = 'SCHEDULED', )
                                ], 
                            source_currency = 'USD', 
                            display_currency = 'USD', 
                            supplier_currency = 'USD', 
                            internal_currency = 'USD', 
                            capture_currency = 'USD', 
                            source_amount = 0, 
                            display_amount = 0, 
                            supplier_amount = 0, 
                            internal_amount = 0, 
                            capture_amount = 0, 
                            source_amount_refund_modifier = 1.337, 
                            display_amount_refund_modifier = 1.337, 
                            supplier_amount_refund_modifier = 1.337, 
                            internal_amount_refund_modifier = 1.337, 
                            capture_amount_refund_modifier = 1.337, 
                            net_source_amount = 1.337, 
                            net_display_amount = 1.337, 
                            net_supplier_amount = 1.337, 
                            net_internal_amount = 1.337, 
                            net_capture_amount = 1.337, 
                            metadata = {
                                'key' : ''
                                }, 
                            net_commissionable_total_source_amount = , 
                            net_commissionable_total_capture_amount = , 
                            net_commissionable_total_display_amount = , 
                            net_commissionable_total_supplier_amount = , 
                            net_commissionable_total_internal_amount = , 
                            net_total_fees_and_commissions_source_amount = , 
                            net_total_fees_and_commissions_capture_amount = , 
                            net_total_fees_and_commissions_display_amount = , 
                            net_total_fees_and_commissions_supplier_amount = , 
                            net_total_fees_and_commissions_internal_amount = , 
                            net_total_fees_source_amount = , 
                            net_total_fees_capture_amount = , 
                            net_total_fees_display_amount = , 
                            net_total_fees_supplier_amount = , 
                            net_total_fees_internal_amount = , 
                            net_total_trip_pay_fee_source_amount = , 
                            net_total_trip_pay_fee_capture_amount = , 
                            net_total_trip_pay_fee_display_amount = , 
                            net_total_trip_pay_fee_supplier_amount = , 
                            net_total_trip_pay_fee_internal_amount = , 
                            net_total_sales_source_amount = , 
                            net_total_sales_capture_amount = , 
                            net_total_sales_display_amount = , 
                            net_total_sales_supplier_amount = , 
                            net_total_sales_internal_amount = , 
                            commissionable_total_source_amount = , 
                            commissionable_total_capture_amount = , 
                            commissionable_total_display_amount = , 
                            commissionable_total_supplier_amount = , 
                            commissionable_total_internal_amount = , 
                            total_fees_and_commissions_source_amount = , 
                            total_fees_and_commissions_capture_amount = , 
                            total_fees_and_commissions_display_amount = , 
                            total_fees_and_commissions_supplier_amount = , 
                            total_fees_and_commissions_internal_amount = , 
                            total_fees_source_amount = , 
                            total_fees_capture_amount = , 
                            total_fees_display_amount = , 
                            total_fees_supplier_amount = , 
                            total_fees_internal_amount = , 
                            total_trip_pay_fee_source_amount = , 
                            total_trip_pay_fee_capture_amount = , 
                            total_trip_pay_fee_display_amount = , 
                            total_trip_pay_fee_supplier_amount = , 
                            total_trip_pay_fee_internal_amount = , 
                            total_sales_source_amount = , 
                            total_sales_capture_amount = , 
                            total_sales_display_amount = , 
                            total_sales_supplier_amount = , 
                            total_sales_internal_amount = , 
                            funds_available_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            total_fees_in_percent_with_refund = 1.337, 
                            total_fees_in_percent = 1.337, 
                            total_trip_pay_fee_in_percent_with_refund = 1.337, 
                            total_trip_pay_fee_in_percent = 1.337, 
                            total_commissions_in_percent_with_refund = 1.337, 
                            total_commissions_in_percent = 1.337, 
                            total_fees_and_commissions_in_percent_with_refund = 1.337, 
                            total_fees_and_commissions_in_percent = 1.337, 
                            original_fees_in_percent = 1.337, 
                            original_affiliate_agency_fees_in_percent = 1.337, 
                            original_supplier_agency_fees_in_percent = 1.337, 
                            original_commissions_in_percent = 1.337, 
                            net_total_customers_source_amount = , 
                            net_total_customers_capture_amount = , 
                            net_total_customers_display_amount = , 
                            net_total_customers_supplier_amount = , 
                            net_total_customers_internal_amount = , 
                            total_affiliate_agency_fees_source_amount = , 
                            total_affiliate_agency_fees_capture_amount = , 
                            total_affiliate_agency_fees_display_amount = , 
                            total_affiliate_agency_fees_supplier_amount = , 
                            total_affiliate_agency_fees_internal_amount = , 
                            total_supplier_agency_fees_source_amount = , 
                            total_supplier_agency_fees_capture_amount = , 
                            total_supplier_agency_fees_display_amount = , 
                            total_supplier_agency_fees_supplier_amount = , 
                            total_supplier_agency_fees_internal_amount = , 
                            net_total_affiliate_agency_fees_source_amount = , 
                            net_total_affiliate_agency_fees_capture_amount = , 
                            net_total_affiliate_agency_fees_display_amount = , 
                            net_total_affiliate_agency_fees_supplier_amount = , 
                            net_total_affiliate_agency_fees_internal_amount = , 
                            net_total_supplier_agency_fees_source_amount = , 
                            net_total_supplier_agency_fees_capture_amount = , 
                            net_total_supplier_agency_fees_display_amount = , 
                            net_total_supplier_agency_fees_supplier_amount = , 
                            net_total_supplier_agency_fees_internal_amount = , 
                            has_refunds = True, 
                            has_successful_refunds = True, 
                            has_pending_refunds = True, 
                            has_failed_refunds = True, 
                            platform_identifier = '', 
                            total_funds_grouped_by_beneficiary = [
                                wink_sdk_extranet_booking.models.beneficiary_supplier.Beneficiary_Supplier(
                                    account_identifier = 'account-1', 
                                    account_name = 'Account 1', 
                                    account_email = 'account@one.com', 
                                    account_url = 'https://some.url', 
                                    type = 'TRIP_PAY', 
                                    source_currency = 'USD', 
                                    display_currency = 'USD', 
                                    supplier_currency = 'USD', 
                                    internal_currency = 'USD', 
                                    capture_currency = 'USD', 
                                    source_amount = 50, 
                                    display_amount = 50, 
                                    supplier_amount = 50, 
                                    internal_amount = 50, 
                                    capture_amount = 50, 
                                    source_amount_refund_modifier = 5, 
                                    display_amount_refund_modifier = 5, 
                                    supplier_amount_refund_modifier = 5, 
                                    internal_amount_refund_modifier = 5, 
                                    capture_amount_refund_modifier = 5, 
                                    net_source_amount = 0, 
                                    net_display_amount = 0, 
                                    net_supplier_amount = 0, 
                                    net_internal_amount = 0, 
                                    net_capture_amount = 0, 
                                    reconciled = False, )
                                ], 
                            total_tokens_earned = 56, 
                            self_acquiring = True, 
                            lodging = wink_sdk_extranet_booking.models.booking_contract_item_supplier.BookingContractItem_Supplier(
                                supplier_item_booking_code = 'TP-ASDFG1234', 
                                user = wink_sdk_extranet_booking.models.guest_user_supplier.GuestUser_Supplier(
                                    user_identifier = '', 
                                    first_name = 'John', 
                                    last_name = 'Smith', 
                                    email = 'john.smith@email.com', 
                                    telephone = '+1 212 555 1212', 
                                    full_name = 'John Smith', ), 
                                name_in_english = 'Deluxe King', 
                                description_in_english = 'This is the best deluxe king that money can buy.', 
                                itinerary = wink_sdk_extranet_booking.models.simple_date_time_itinerary_supplier.SimpleDateTimeItinerary_Supplier(
                                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    adults = 0, 
                                    children = 0, 
                                    hours = 56, 
                                    nights = 56, 
                                    guests = 56, ), 
                                pricing_type = 'PER_STAY', 
                                type = 'LODGING', 
                                beneficiary_list = [
                                    
                                    ], 
                                payable = 'PREPAY', 
                                external_identifier = 'room-type-1', 
                                tokens_earned = 12, 
                                cancelled = True, 
                                source_currency = 'USD', 
                                display_currency = 'USD', 
                                supplier_currency = 'USD', 
                                internal_currency = 'USD', 
                                capture_currency = 'USD', 
                                source_amount = 0, 
                                display_amount = 0, 
                                supplier_amount = 0, 
                                internal_amount = 0, 
                                capture_amount = 0, 
                                source_amount_refund_modifier = 0, 
                                display_amount_refund_modifier = 0, 
                                supplier_amount_refund_modifier = 0, 
                                internal_amount_refund_modifier = 0, 
                                capture_amount_refund_modifier = 0, 
                                net_source_amount = 0, 
                                net_display_amount = 0, 
                                net_supplier_amount = 0, 
                                net_internal_amount = 0, 
                                net_capture_amount = 0, 
                                cancellable_by_traveler = True, 
                                cancellable_with_no_charges = True, 
                                cancellable_with_potential_charges = True, 
                                cancellable_by_supplier_or_agent = True, ), 
                            cancellable_by_agent = True, 
                            cancellable_by_supplier = True, 
                            cancellable_by_traveler = True, 
                            fully_refunded = True, 
                            cancellable_with_no_charges = True, 
                            is_cancellable_with_potential_charges = True, ), 
                        static_map_image_url = 'https://path.to/room-image.jpg', 
                        static_map_url = 'https://path.to/room-image.jpg', 
                        status = 'ACTIVE', 
                        meeting_rooms = [
                            wink_sdk_extranet_booking.models.booking_ancillary_supplier.BookingAncillary_Supplier(
                                identifier = 'ancillary-1', 
                                hotel_identifier = 'hotel-1', 
                                type_identifier = 'place-1', 
                                transactional_travel_inventory_identifier = 'place-1', 
                                name = 'Place 1', 
                                pricing_type = 'PER_USE', 
                                type = 'PLACE', 
                                price = wink_sdk_extranet_booking.models.localized_price_supplier.LocalizedPrice_Supplier(
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
                                start_date = '2017-12-22T03:07:58.742+0000', 
                                end_date = '2017-12-22T08:07:58.742+0000', 
                                attendees = 2, 
                                image_identifier = 'cloudinary-image-1', 
                                image_url = 'https://path.to.image.com/this-is-me.jpg', 
                                localized_name = 'Plass 1', 
                                localized_description = 'place-1', 
                                contact = , 
                                address = , 
                                commissionable = True, 
                                mandatory = True, 
                                commission = 1.337, )
                            ], 
                        restaurants = [
                            
                            ], 
                        spas = [
                            
                            ], 
                        activities = [
                            
                            ], 
                        attractions = [
                            
                            ], 
                        places = [
                            
                            ], 
                        room_type_ancillaries = [
                            
                            ], 
                        add_ons = [
                            
                            ], 
                        rate_source = 'SITEMINDER', 
                        has_add_ons = True, 
                        cancellable_by_agent = True, 
                        cancellable_by_supplier = True, 
                        cancellable_by_traveler = True, 
                        has_breakfast = True, 
                        has_brunch = True, 
                        has_lunch = True, 
                        has_dinner = True, 
                        has_all_inclusive = True, 
                        has_all_inclusive_plus_alcohol = True, 
                        has_room_type_ancillaries = True, 
                        has_food = True, 
                        has_restaurants = True, 
                        has_meeting_rooms = True, 
                        has_spas = True, 
                        has_activities = True, 
                        has_attractions = True, 
                        has_places = True, 
                        reporting_daily_rate_list = [
                            null
                            ], 
                        reporting_ancillary_list = [
                            null
                            ], 
                        reporting_extra_charge_list = [
                            null
                            ], )
                    ],
                number = 56,
                number_of_elements = 56,
                sort = wink_sdk_extranet_booking.models.sort_object_supplier.SortObject_Supplier(
                    empty = True, 
                    sorted = True, 
                    unsorted = True, ),
                pageable = wink_sdk_extranet_booking.models.pageable_object_supplier.PageableObject_Supplier(
                    offset = 56, 
                    unpaged = True, 
                    sort = wink_sdk_extranet_booking.models.sort_object_supplier.SortObject_Supplier(
                        empty = True, 
                        sorted = True, 
                        unsorted = True, ), 
                    paged = True, 
                    page_number = 56, 
                    page_size = 56, ),
                first = True,
                last = True,
                empty = True
            )
        else:
            return PageBookingSupplier(
        )
        """

    def testPageBookingSupplier(self):
        """Test PageBookingSupplier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
