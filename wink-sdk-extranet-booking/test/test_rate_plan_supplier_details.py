# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant payment widget for all other entities.   - [TripPay](/payment): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md   # Extranet Booking API The Booking API exposes endpoints to manage bookings. This API lets you:  1. Booking: Manage bookings including cancellations. 2. Review: Manage user reviews. 3. Sync w. Calendar: Manage calendar sync with your favorite calendar software  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.5.19
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wink_sdk_extranet_booking.models.rate_plan_supplier_details import RatePlanSupplierDetails

class TestRatePlanSupplierDetails(unittest.TestCase):
    """RatePlanSupplierDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RatePlanSupplierDetails:
        """Test RatePlanSupplierDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RatePlanSupplierDetails`
        """
        model = RatePlanSupplierDetails()
        if include_optional:
            return RatePlanSupplierDetails(
                identifier = '',
                hotel_identifier = '',
                name = 'BAR 1',
                prepaid = False,
                enabled = False,
                breakfast = False,
                brunch = False,
                lunch = False,
                dinner = False,
                all_inclusive = False,
                all_inclusive_plus_alcohol = False,
                sell_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                sell_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                stay_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                stay_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                loyalty_points_accrue = False,
                max_advance_booking_offset = 10,
                min_advance_booking_offset = 3,
                min_total_occupancy = 4,
                max_total_occupancy = 4,
                min_los = 3,
                max_los = 5,
                min_age = 26,
                max_age = 50,
                rate_plan_level_fees = [
                    wink_sdk_extranet_booking.models.rate_plan_level_fee_supplier_details.RatePlanLevelFee_SupplierDetails(
                        descriptions = [
                            wink_sdk_extranet_booking.models.localized_description_supplier_details.LocalizedDescription_SupplierDetails(
                                description = 'This is a longer description in the specified language.', 
                                language = 'en', )
                            ], 
                        fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                            amount = 1.337, 
                            currency = '', ), 
                        type = 'PER_DAY', )
                    ],
                available_days_of_week = wink_sdk_extranet_booking.models.dow_pattern_group_supplier_details.DowPatternGroup_SupplierDetails(
                    mon = True, 
                    tue = True, 
                    wed = True, 
                    thu = True, 
                    fri = True, 
                    sat = True, 
                    sun = True, 
                    disabled = True, ),
                arrival_days_of_week = wink_sdk_extranet_booking.models.dow_pattern_group_supplier_details.DowPatternGroup_SupplierDetails(
                    mon = True, 
                    tue = True, 
                    wed = True, 
                    thu = True, 
                    fri = True, 
                    sat = True, 
                    sun = True, 
                    disabled = True, ),
                departure_days_of_week = wink_sdk_extranet_booking.models.dow_pattern_group_supplier_details.DowPatternGroup_SupplierDetails(
                    mon = True, 
                    tue = True, 
                    wed = True, 
                    thu = True, 
                    fri = True, 
                    sat = True, 
                    sun = True, 
                    disabled = True, ),
                required_days_of_week = wink_sdk_extranet_booking.models.dow_pattern_group_supplier_details.DowPatternGroup_SupplierDetails(
                    mon = True, 
                    tue = True, 
                    wed = True, 
                    thu = True, 
                    fri = True, 
                    sat = True, 
                    sun = True, 
                    disabled = True, ),
                early_check_in_charge = wink_sdk_extranet_booking.models.variable_charge_supplier_details.VariableCharge_SupplierDetails(
                    type = 'FIXED', 
                    percent = 0.25, 
                    fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                        amount = 1.337, 
                        currency = '', ), ),
                late_check_out_charge = wink_sdk_extranet_booking.models.variable_charge_supplier_details.VariableCharge_SupplierDetails(
                    type = 'FIXED', 
                    percent = 0.25, 
                    fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                        amount = 1.337, 
                        currency = '', ), ),
                cancellation_policy_identifier = 'cancellation-policy-1',
                cancellation_policy = wink_sdk_extranet_booking.models.cancellation_policy_supplier_details.CancellationPolicy_SupplierDetails(
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
                cancellation_policy_exceptions = wink_sdk_extranet_booking.models.cancellation_policy_exceptions_supplier_details.CancellationPolicyExceptions_SupplierDetails(
                    list = [
                        wink_sdk_extranet_booking.models.cancellation_policy_exception_supplier_details.CancellationPolicyException_SupplierDetails(
                            cancellation_policy_identifier = '', 
                            cancellation_policy = wink_sdk_extranet_booking.models.cancellation_policy_supplier_details.CancellationPolicy_SupplierDetails(
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
                        ], ),
                single_occupancy_rate_modifier = wink_sdk_extranet_booking.models.variable_charge_supplier_details.VariableCharge_SupplierDetails(
                    type = 'FIXED', 
                    percent = 0.25, 
                    fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                        amount = 1.337, 
                        currency = '', ), ),
                extra_pax_rate_modifier = wink_sdk_extranet_booking.models.variable_charge_supplier_details.VariableCharge_SupplierDetails(
                    type = 'FIXED', 
                    percent = 0.25, 
                    fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                        amount = 1.337, 
                        currency = '', ), ),
                extra_child_rate_modifier = wink_sdk_extranet_booking.models.variable_charge_supplier_details.VariableCharge_SupplierDetails(
                    type = 'FIXED', 
                    percent = 0.25, 
                    fixed_amount = wink_sdk_extranet_booking.models.custom_monetary_amount.CustomMonetaryAmount(
                        amount = 1.337, 
                        currency = '', ), )
            )
        else:
            return RatePlanSupplierDetails(
                identifier = '',
                hotel_identifier = '',
                name = 'BAR 1',
                prepaid = False,
                enabled = False,
                breakfast = False,
                brunch = False,
                lunch = False,
                dinner = False,
                all_inclusive = False,
                all_inclusive_plus_alcohol = False,
                cancellation_policy_identifier = 'cancellation-policy-1',
        )
        """

    def testRatePlanSupplierDetails(self):
        """Test RatePlanSupplierDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
