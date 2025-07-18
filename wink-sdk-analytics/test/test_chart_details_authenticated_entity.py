# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [UserLightweight Settings](/user-settings): The UserLightweight Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md   # Analytics API Welcome to the Affiliate API - A programmer-friendly way to get insight into platform-level activities and bookings.  

    The version of the OpenAPI document: 30.17.0
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wink_sdk_analytics.models.chart_details_authenticated_entity import ChartDetailsAuthenticatedEntity

class TestChartDetailsAuthenticatedEntity(unittest.TestCase):
    """ChartDetailsAuthenticatedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChartDetailsAuthenticatedEntity:
        """Test ChartDetailsAuthenticatedEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChartDetailsAuthenticatedEntity`
        """
        model = ChartDetailsAuthenticatedEntity()
        if include_optional:
            return ChartDetailsAuthenticatedEntity(
                series = 'HOUR',
                time_series_units = 24,
                start_date = '2017-12-22T03:07:58.742+0000',
                end_date = '2017-12-23T03:07:58.742+0000',
                filter_on_hotel_identifier = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_channel_sub_type = 'APPLICATION',
                filter_on_owner_identifier = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_engine_country_geo_name_id = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_engine_city_geo_name_id = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_engine_continent_code = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_engine_configuration_identifier = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_country_geo_name_id = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_city_geo_name_id = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_continent_code = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                filter_on_user_identifier = wink_sdk_analytics.models.key_value_pair_authenticated_entity.KeyValuePair_Authenticated_Entity(
                    value = 'id-1', 
                    label = 'Readable text label', ),
                sort_on_page_visits = True,
                sort_on_map_marker_visits = False,
                sort_on_card_visits = False,
                sort_on_bookings = False,
                sort_on_cancellations = False,
                sort_on_room_nights = False,
                sort_on_meeting_rooms = False,
                sort_on_meeting_rooms_revenue = False,
                sort_on_restaurants = False,
                sort_on_restaurants_revenue = False,
                sort_on_spas = False,
                sort_on_spas_revenue = False,
                sort_on_activities = False,
                sort_on_activities_revenue = False,
                sort_on_attractions = False,
                sort_on_attractions_revenue = False,
                sort_on_places = False,
                sort_on_places_revenue = False,
                sort_on_room_type_ancillaries = False,
                sort_on_room_type_ancillaries_revenue = False,
                sort_on_add_ons = False,
                sort_on_addons_revenue = False,
                sort_on_total_room_revenue = False,
                sort_on_total_ancillaries_revenue = False,
                sort_on_total_net_revenue = False,
                sort_on_cancelled_room_nights = False,
                sort_on_cancelled_meeting_rooms = False,
                sort_on_cancelled_meeting_rooms_revenue = False,
                sort_on_cancelled_restaurants = False,
                sort_on_cancelled_restaurants_revenue = False,
                sort_on_cancelled_spas = False,
                sort_on_cancelled_spas_revenue = False,
                sort_on_cancelled_activities = False,
                sort_on_cancelled_activities_revenue = False,
                sort_on_cancelled_attractions = False,
                sort_on_cancelled_attractions_revenue = False,
                sort_on_cancelled_places = False,
                sort_on_cancelled_places_revenue = False,
                sort_on_cancelled_total_room_revenue = False,
                sort_on_cancelled_total_ancillaries_revenue = False,
                sort_on_cancelled_room_type_ancillaries = False,
                sort_on_cancelled_room_type_ancillaries_revenue = False,
                sort_on_cancelled_add_ons = False,
                sort_on_cancelled_addons_revenue = False,
                sort_on_cancelled_total_net_revenue = False,
                include_page_visits = False,
                include_map_marker_visits = False,
                include_card_visits = False,
                include_bookings = False,
                include_cancellations = False,
                include_room_nights = False,
                include_meeting_rooms = False,
                include_meeting_rooms_revenue = False,
                include_restaurants = False,
                include_restaurants_revenue = False,
                include_spas = False,
                include_spas_revenue = False,
                include_activities = False,
                include_activities_revenue = False,
                include_attractions = False,
                include_attractions_revenue = False,
                include_places = False,
                include_places_revenue = False,
                include_room_type_ancillaries = False,
                include_room_type_ancillaries_revenue = False,
                include_add_ons = False,
                include_add_ons_revenue = False,
                include_total_room_revenue = False,
                include_average_room_rate = False,
                include_total_ancillaries_revenue = False,
                include_total_net_revenue = False,
                include_cancelled_room_nights = False,
                include_cancelled_meeting_rooms = False,
                include_cancelled_meeting_rooms_revenue = False,
                include_cancelled_restaurants = False,
                include_cancelled_restaurants_revenue = False,
                include_cancelled_spas = False,
                include_cancelled_spas_revenue = False,
                include_cancelled_activities = False,
                include_cancelled_activities_revenue = False,
                include_cancelled_attractions = False,
                include_cancelled_attractions_revenue = False,
                include_cancelled_places = False,
                include_cancelled_places_revenue = False,
                include_cancelled_room_type_ancillaries = False,
                include_cancelled_room_type_ancillaries_revenue = False,
                include_cancelled_add_ons = False,
                include_cancelled_add_ons_revenue = False,
                include_cancelled_total_room_revenue = False,
                include_cancelled_total_ancillaries_revenue = False,
                include_cancelled_total_net_revenue = False,
                group_on_channel_sub_type = False,
                group_on_owner_identifier = False,
                group_on_engine_country_geo_name_id = False,
                group_on_engine_city_geo_name_id = False,
                group_on_engine_continent_code = False,
                group_on_engine_configuration_identifier = False,
                group_on_country_geo_name_id = False,
                group_on_city_geo_name_id = False,
                group_on_continent_code = False,
                group_on_hotel_identifier = False,
                group_on_user_identifier = False,
                currency_code = 'USD'
            )
        else:
            return ChartDetailsAuthenticatedEntity(
                series = 'HOUR',
        )
        """

    def testChartDetailsAuthenticatedEntity(self):
        """Test ChartDetailsAuthenticatedEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
