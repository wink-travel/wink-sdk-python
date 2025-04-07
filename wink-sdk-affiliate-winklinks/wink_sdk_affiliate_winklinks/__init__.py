# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # WinkLinks API The WinkLinks API exposes endpoints to manage WinkLink entries, categories and settings. This API lets you:  1. Entries: Manage WinkLinks entries. 2. Categories: Manage WinkLinks tags. 2. Settings: Configure WinkLinks account.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.15.2
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.20"

# import apis into sdk package
from wink_sdk_affiliate_winklinks.api.syndication_consumer_api import SyndicationConsumerApi
from wink_sdk_affiliate_winklinks.api.syndication_publisher_api import SyndicationPublisherApi

# import ApiClient
from wink_sdk_affiliate_winklinks.api_response import ApiResponse
from wink_sdk_affiliate_winklinks.api_client import ApiClient
from wink_sdk_affiliate_winklinks.configuration import Configuration
from wink_sdk_affiliate_winklinks.exceptions import OpenApiException
from wink_sdk_affiliate_winklinks.exceptions import ApiTypeError
from wink_sdk_affiliate_winklinks.exceptions import ApiValueError
from wink_sdk_affiliate_winklinks.exceptions import ApiKeyError
from wink_sdk_affiliate_winklinks.exceptions import ApiAttributeError
from wink_sdk_affiliate_winklinks.exceptions import ApiException

# import models into sdk package
from wink_sdk_affiliate_winklinks.models.aggregate_descriptor_non_authenticated_entity import AggregateDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity import ApplicationContextNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader import ApplicationContextNonAuthenticatedEntityClassLoader
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent import ApplicationContextNonAuthenticatedEntityClassLoaderParent
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent_unnamed_module import ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModule
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent_unnamed_module_class_loader import ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModuleClassLoader
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent_unnamed_module_class_loader_defined_packages_inner import ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModuleClassLoaderDefinedPackagesInner
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent_unnamed_module_descriptor import ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModuleDescriptor
from wink_sdk_affiliate_winklinks.models.boolean_response_non_authenticated_entity import BooleanResponseNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.composite_filter_descriptor_non_authenticated_entity import CompositeFilterDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.consumable_syndication_entry_non_authenticated_entity import ConsumableSyndicationEntryNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.consume_external_url_request_affiliate import ConsumeExternalUrlRequestAffiliate
from wink_sdk_affiliate_winklinks.models.environment_non_authenticated_entity import EnvironmentNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.facebook_embed_non_authenticated_entity import FacebookEmbedNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.filter_descriptor_non_authenticated_entity import FilterDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.filter_registration_non_authenticated_entity import FilterRegistrationNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.generic_error_message import GenericErrorMessage
from wink_sdk_affiliate_winklinks.models.group_descriptor_non_authenticated_entity import GroupDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.http_status_code_non_authenticated_entity import HttpStatusCodeNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.image_attribution_affiliate import ImageAttributionAffiliate
from wink_sdk_affiliate_winklinks.models.image_attribution_non_authenticated_entity import ImageAttributionNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.instagram_embed_non_authenticated_entity import InstagramEmbedNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.jsp_config_descriptor_non_authenticated_entity import JspConfigDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.jsp_property_group_descriptor_non_authenticated_entity import JspPropertyGroupDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.key_value_pair_affiliate import KeyValuePairAffiliate
from wink_sdk_affiliate_winklinks.models.key_value_pair_non_authenticated_entity import KeyValuePairNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.online_presence_non_authenticated_entity import OnlinePresenceNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.open_graph_media_affiliate import OpenGraphMediaAffiliate
from wink_sdk_affiliate_winklinks.models.open_graph_media_non_authenticated_entity import OpenGraphMediaNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.page_consumable_syndication_entry_non_authenticated_entity import PageConsumableSyndicationEntryNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.pageable_object_non_authenticated_entity import PageableObjectNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.redirect_view_non_authenticated_entity import RedirectViewNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.servlet_context_non_authenticated_entity import ServletContextNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.servlet_registration_non_authenticated_entity import ServletRegistrationNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.session_cookie_config_non_authenticated_entity import SessionCookieConfigNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.show_syndication_settings400_response import ShowSyndicationSettings400Response
from wink_sdk_affiliate_winklinks.models.simple_description_affiliate import SimpleDescriptionAffiliate
from wink_sdk_affiliate_winklinks.models.simple_description_non_authenticated_entity import SimpleDescriptionNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.simple_multimedia_affiliate import SimpleMultimediaAffiliate
from wink_sdk_affiliate_winklinks.models.simple_multimedia_non_authenticated_entity import SimpleMultimediaNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.sort_descriptor_non_authenticated_entity import SortDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.sort_object import SortObject
from wink_sdk_affiliate_winklinks.models.sorted_affiliate import SortedAffiliate
from wink_sdk_affiliate_winklinks.models.spotify_embed_non_authenticated_entity import SpotifyEmbedNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.state_non_authenticated_entity import StateNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.syndication_account_non_authenticated_entity import SyndicationAccountNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.syndication_category_affiliate import SyndicationCategoryAffiliate
from wink_sdk_affiliate_winklinks.models.syndication_entry_affiliate import SyndicationEntryAffiliate
from wink_sdk_affiliate_winklinks.models.syndication_settings_affiliate import SyndicationSettingsAffiliate
from wink_sdk_affiliate_winklinks.models.taglib_descriptor_non_authenticated_entity import TaglibDescriptorNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.twitter_embed_non_authenticated_entity import TwitterEmbedNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.upsert_syndication_category_affiliate import UpsertSyndicationCategoryAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_entry_affiliate import UpsertSyndicationEntryAffiliate
from wink_sdk_affiliate_winklinks.models.upsert_syndication_settings_affiliate import UpsertSyndicationSettingsAffiliate
