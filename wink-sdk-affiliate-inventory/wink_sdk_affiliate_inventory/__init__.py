# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Inventory API The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it. This API lets you:  1. Manage customizations. 2. Shareable Links: Manage shareable supplier / blocking links. 3. Inventory: Manage individual blocking items. 4. Lists: Manage curated / ranked grids. 5. Maps: Manage maps.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.3"

# import apis into sdk package
from wink_sdk_affiliate_inventory.api.customization_api import CustomizationApi
from wink_sdk_affiliate_inventory.api.embeddable_inventories_api import EmbeddableInventoriesApi
from wink_sdk_affiliate_inventory.api.grids_api import GridsApi
from wink_sdk_affiliate_inventory.api.inventory_links_api import InventoryLinksApi
from wink_sdk_affiliate_inventory.api.items_api import ItemsApi
from wink_sdk_affiliate_inventory.api.maps_api import MapsApi
from wink_sdk_affiliate_inventory.api.ranked_grids_api import RankedGridsApi
from wink_sdk_affiliate_inventory.api.supplier_links_api import SupplierLinksApi

# import ApiClient
from wink_sdk_affiliate_inventory.api_response import ApiResponse
from wink_sdk_affiliate_inventory.api_client import ApiClient
from wink_sdk_affiliate_inventory.configuration import Configuration
from wink_sdk_affiliate_inventory.exceptions import OpenApiException
from wink_sdk_affiliate_inventory.exceptions import ApiTypeError
from wink_sdk_affiliate_inventory.exceptions import ApiValueError
from wink_sdk_affiliate_inventory.exceptions import ApiKeyError
from wink_sdk_affiliate_inventory.exceptions import ApiAttributeError
from wink_sdk_affiliate_inventory.exceptions import ApiException

# import models into sdk package
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_affiliate import AdvancedMapConfigurationAffiliate
from wink_sdk_affiliate_inventory.models.advanced_map_configuration_view_affiliate import AdvancedMapConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.boolean_response_affiliate import BooleanResponseAffiliate
from wink_sdk_affiliate_inventory.models.campaign_inventory_affiliate import CampaignInventoryAffiliate
from wink_sdk_affiliate_inventory.models.child_affiliate import ChildAffiliate
from wink_sdk_affiliate_inventory.models.configurable_geo_json_circle_affiliate import ConfigurableGeoJsonCircleAffiliate
from wink_sdk_affiliate_inventory.models.configurable_geo_json_point_affiliate import ConfigurableGeoJsonPointAffiliate
from wink_sdk_affiliate_inventory.models.configurable_geo_json_polygon_affiliate import ConfigurableGeoJsonPolygonAffiliate
from wink_sdk_affiliate_inventory.models.configurable_geo_json_rectangle_affiliate import ConfigurableGeoJsonRectangleAffiliate
from wink_sdk_affiliate_inventory.models.country_affiliate import CountryAffiliate
from wink_sdk_affiliate_inventory.models.create_advanced_map_configuration_syndication_entry_request_affiliate import CreateAdvancedMapConfigurationSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.create_seller_inventory_item_syndication_entry_request_affiliate import CreateSellerInventoryItemSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.create_seller_inventory_ranked_list_syndication_entry_request_affiliate import CreateSellerInventoryRankedListSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.create_seller_url_syndication_entry_request_affiliate import CreateSellerUrlSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.create_static_seller_list_syndication_entry_request_affiliate import CreateStaticSellerListSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.create_supplier_url_syndication_entry_request_affiliate import CreateSupplierUrlSyndicationEntryRequestAffiliate
from wink_sdk_affiliate_inventory.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_affiliate_inventory.models.engine_configuration_affiliate import EngineConfigurationAffiliate
from wink_sdk_affiliate_inventory.models.engine_configuration_theme_affiliate import EngineConfigurationThemeAffiliate
from wink_sdk_affiliate_inventory.models.engine_configuration_view_affiliate import EngineConfigurationViewAffiliate
from wink_sdk_affiliate_inventory.models.generic_error_message import GenericErrorMessage
from wink_sdk_affiliate_inventory.models.geo_json_line_string_affiliate import GeoJsonLineStringAffiliate
from wink_sdk_affiliate_inventory.models.geo_json_point_affiliate import GeoJsonPointAffiliate
from wink_sdk_affiliate_inventory.models.geo_json_polygon_affiliate import GeoJsonPolygonAffiliate
from wink_sdk_affiliate_inventory.models.geo_json_rectangle_affiliate import GeoJsonRectangleAffiliate
from wink_sdk_affiliate_inventory.models.geo_name_affiliate import GeoNameAffiliate
from wink_sdk_affiliate_inventory.models.image_attribution_affiliate import ImageAttributionAffiliate
from wink_sdk_affiliate_inventory.models.inventory_map_marker_affiliate import InventoryMapMarkerAffiliate
from wink_sdk_affiliate_inventory.models.key_value_pair_affiliate import KeyValuePairAffiliate
from wink_sdk_affiliate_inventory.models.lookup_affiliate import LookupAffiliate
from wink_sdk_affiliate_inventory.models.open_graph_media_affiliate import OpenGraphMediaAffiliate
from wink_sdk_affiliate_inventory.models.point_affiliate import PointAffiliate
from wink_sdk_affiliate_inventory.models.room_configuration_affiliate import RoomConfigurationAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_item_affiliate import SellerInventoryItemAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_item_view_affiliate import SellerInventoryItemViewAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_list_affiliate import SellerInventoryListAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_list_view_affiliate import SellerInventoryListViewAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_ranked_list_affiliate import SellerInventoryRankedListAffiliate
from wink_sdk_affiliate_inventory.models.seller_inventory_ranked_list_view_affiliate import SellerInventoryRankedListViewAffiliate
from wink_sdk_affiliate_inventory.models.seller_url_affiliate import SellerUrlAffiliate
from wink_sdk_affiliate_inventory.models.seller_url_view_affiliate import SellerUrlViewAffiliate
from wink_sdk_affiliate_inventory.models.show_supplier_url400_response import ShowSupplierUrl400Response
from wink_sdk_affiliate_inventory.models.simple_description_affiliate import SimpleDescriptionAffiliate
from wink_sdk_affiliate_inventory.models.simple_multimedia_affiliate import SimpleMultimediaAffiliate
from wink_sdk_affiliate_inventory.models.sub_country_affiliate import SubCountryAffiliate
from wink_sdk_affiliate_inventory.models.sub_sub_country_affiliate import SubSubCountryAffiliate
from wink_sdk_affiliate_inventory.models.supplier_url_affiliate import SupplierUrlAffiliate
from wink_sdk_affiliate_inventory.models.supplier_url_view_affiliate import SupplierUrlViewAffiliate
from wink_sdk_affiliate_inventory.models.syndication_entry_affiliate import SyndicationEntryAffiliate
from wink_sdk_affiliate_inventory.models.upsert_advanced_map_configuration_request_affiliate import UpsertAdvancedMapConfigurationRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_engine_configuration_request_affiliate import UpsertEngineConfigurationRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_item_request_affiliate import UpsertSellerInventoryItemRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_list_request_affiliate import UpsertSellerInventoryListRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_ranked_list_request_affiliate import UpsertSellerInventoryRankedListRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_seller_url_request_affiliate import UpsertSellerUrlRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_advanced_map_configuration_request_affiliate import UpsertSupplierAdvancedMapConfigurationRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_seller_inventory_item_request_affiliate import UpsertSupplierSellerInventoryItemRequestAffiliate
from wink_sdk_affiliate_inventory.models.upsert_supplier_url_request_affiliate import UpsertSupplierUrlRequestAffiliate
