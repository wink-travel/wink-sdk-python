# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Extranet Experiences API This part of the documentation concerns itself with the management of experiences, on and off the property. This API lets you create:  1. Activities: Manage activities on and off the premises. 2. Attractions: Manage attractions on and off the premises. 3. Places: Manage places on and off the premises.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.3"

# import apis into sdk package
from wink_sdk_extranet_experiences.api.activity_api import ActivityApi
from wink_sdk_extranet_experiences.api.attraction_api import AttractionApi
from wink_sdk_extranet_experiences.api.place_api import PlaceApi

# import ApiClient
from wink_sdk_extranet_experiences.api_response import ApiResponse
from wink_sdk_extranet_experiences.api_client import ApiClient
from wink_sdk_extranet_experiences.configuration import Configuration
from wink_sdk_extranet_experiences.exceptions import OpenApiException
from wink_sdk_extranet_experiences.exceptions import ApiTypeError
from wink_sdk_extranet_experiences.exceptions import ApiValueError
from wink_sdk_extranet_experiences.exceptions import ApiKeyError
from wink_sdk_extranet_experiences.exceptions import ApiAttributeError
from wink_sdk_extranet_experiences.exceptions import ApiException

# import models into sdk package
from wink_sdk_extranet_experiences.models.address import Address
from wink_sdk_extranet_experiences.models.address_supplier import AddressSupplier
from wink_sdk_extranet_experiences.models.attraction import Attraction
from wink_sdk_extranet_experiences.models.attraction_view import AttractionView
from wink_sdk_extranet_experiences.models.contact import Contact
from wink_sdk_extranet_experiences.models.contact_supplier import ContactSupplier
from wink_sdk_extranet_experiences.models.country import Country
from wink_sdk_extranet_experiences.models.country_supplier import CountrySupplier
from wink_sdk_extranet_experiences.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_extranet_experiences.models.dow_pattern_group import DowPatternGroup
from wink_sdk_extranet_experiences.models.dow_pattern_group_supplier import DowPatternGroupSupplier
from wink_sdk_extranet_experiences.models.generic_error_message import GenericErrorMessage
from wink_sdk_extranet_experiences.models.geo_json_point import GeoJsonPoint
from wink_sdk_extranet_experiences.models.geo_json_point_supplier import GeoJsonPointSupplier
from wink_sdk_extranet_experiences.models.geo_name import GeoName
from wink_sdk_extranet_experiences.models.geo_name_supplier import GeoNameSupplier
from wink_sdk_extranet_experiences.models.image_attribution import ImageAttribution
from wink_sdk_extranet_experiences.models.image_attribution_supplier import ImageAttributionSupplier
from wink_sdk_extranet_experiences.models.key_value_pair import KeyValuePair
from wink_sdk_extranet_experiences.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_experiences.models.recreation import Recreation
from wink_sdk_extranet_experiences.models.recreation_view import RecreationView
from wink_sdk_extranet_experiences.models.ref_point_supplier import RefPointSupplier
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier
from wink_sdk_extranet_experiences.models.show_place400_response import ShowPlace400Response
from wink_sdk_extranet_experiences.models.simple_description import SimpleDescription
from wink_sdk_extranet_experiences.models.simple_description_supplier import SimpleDescriptionSupplier
from wink_sdk_extranet_experiences.models.simple_multimedia import SimpleMultimedia
from wink_sdk_extranet_experiences.models.simple_multimedia_supplier import SimpleMultimediaSupplier
from wink_sdk_extranet_experiences.models.social import Social
from wink_sdk_extranet_experiences.models.social_supplier import SocialSupplier
from wink_sdk_extranet_experiences.models.sub_country import SubCountry
from wink_sdk_extranet_experiences.models.sub_country_supplier import SubCountrySupplier
from wink_sdk_extranet_experiences.models.sub_sub_country import SubSubCountry
from wink_sdk_extranet_experiences.models.sub_sub_country_supplier import SubSubCountrySupplier
from wink_sdk_extranet_experiences.models.transactional_travel_inventory import TransactionalTravelInventory
from wink_sdk_extranet_experiences.models.transactional_travel_inventory_supplier import TransactionalTravelInventorySupplier
from wink_sdk_extranet_experiences.models.travel_inventory_recognition import TravelInventoryRecognition
from wink_sdk_extranet_experiences.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
from wink_sdk_extranet_experiences.models.upsert_activity_request import UpsertActivityRequest
from wink_sdk_extranet_experiences.models.upsert_address_request import UpsertAddressRequest
from wink_sdk_extranet_experiences.models.upsert_address_request_supplier import UpsertAddressRequestSupplier
from wink_sdk_extranet_experiences.models.upsert_attraction_request import UpsertAttractionRequest
from wink_sdk_extranet_experiences.models.upsert_place_request_supplier import UpsertPlaceRequestSupplier
