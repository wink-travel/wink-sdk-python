# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # User Settings API The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink. This API lets you:  1. Application: Manage 3rd party access to Wink. 2. Bucket List: Manage your bucket list on Wink. 3. Webhook: Subscribe to receive Wink events as they occur in realtime. 4. User: Manage user settings.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.3"

# import apis into sdk package
from wink_sdk_user_settings.api.application_api import ApplicationApi
from wink_sdk_user_settings.api.bucket_list_api import BucketListApi
from wink_sdk_user_settings.api.user_settings_api import UserSettingsApi
from wink_sdk_user_settings.api.webhook_api import WebhookApi

# import ApiClient
from wink_sdk_user_settings.api_response import ApiResponse
from wink_sdk_user_settings.api_client import ApiClient
from wink_sdk_user_settings.configuration import Configuration
from wink_sdk_user_settings.exceptions import OpenApiException
from wink_sdk_user_settings.exceptions import ApiTypeError
from wink_sdk_user_settings.exceptions import ApiValueError
from wink_sdk_user_settings.exceptions import ApiKeyError
from wink_sdk_user_settings.exceptions import ApiAttributeError
from wink_sdk_user_settings.exceptions import ApiException

# import models into sdk package
from wink_sdk_user_settings.models.address_authenticated_entity import AddressAuthenticatedEntity
from wink_sdk_user_settings.models.application import Application
from wink_sdk_user_settings.models.boolean_response import BooleanResponse
from wink_sdk_user_settings.models.bucket_list_entry_authenticated_entity import BucketListEntryAuthenticatedEntity
from wink_sdk_user_settings.models.bucket_list_entry_request_authenticated_entity import BucketListEntryRequestAuthenticatedEntity
from wink_sdk_user_settings.models.bucket_list_entry_view_authenticated_entity import BucketListEntryViewAuthenticatedEntity
from wink_sdk_user_settings.models.bucket_list_entry_wrapper_authenticated_entity import BucketListEntryWrapperAuthenticatedEntity
from wink_sdk_user_settings.models.change_password_request import ChangePasswordRequest
from wink_sdk_user_settings.models.contact_authenticated_entity import ContactAuthenticatedEntity
from wink_sdk_user_settings.models.contact_non_authenticated_entity import ContactNonAuthenticatedEntity
from wink_sdk_user_settings.models.country_authenticated_entity import CountryAuthenticatedEntity
from wink_sdk_user_settings.models.create_application_response import CreateApplicationResponse
from wink_sdk_user_settings.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_user_settings.models.general_manager_authenticated_entity import GeneralManagerAuthenticatedEntity
from wink_sdk_user_settings.models.generic_error_message import GenericErrorMessage
from wink_sdk_user_settings.models.geo_json_point_authenticated_entity import GeoJsonPointAuthenticatedEntity
from wink_sdk_user_settings.models.geo_name_authenticated_entity import GeoNameAuthenticatedEntity
from wink_sdk_user_settings.models.hotel_on_map_authenticated_entity import HotelOnMapAuthenticatedEntity
from wink_sdk_user_settings.models.image_attribution import ImageAttribution
from wink_sdk_user_settings.models.image_attribution_authenticated_entity import ImageAttributionAuthenticatedEntity
from wink_sdk_user_settings.models.inventory_authenticated_entity import InventoryAuthenticatedEntity
from wink_sdk_user_settings.models.key_value_pair import KeyValuePair
from wink_sdk_user_settings.models.localized_description_authenticated_entity import LocalizedDescriptionAuthenticatedEntity
from wink_sdk_user_settings.models.managing_entity import ManagingEntity
from wink_sdk_user_settings.models.personal_non_authenticated_entity import PersonalNonAuthenticatedEntity
from wink_sdk_user_settings.models.pet_info_dto_non_authenticated_entity import PetInfoDtoNonAuthenticatedEntity
from wink_sdk_user_settings.models.preferences_non_authenticated_entity import PreferencesNonAuthenticatedEntity
from wink_sdk_user_settings.models.profile_non_authenticated_entity import ProfileNonAuthenticatedEntity
from wink_sdk_user_settings.models.profile_user_non_authenticated_entity import ProfileUserNonAuthenticatedEntity
from wink_sdk_user_settings.models.profile_view_non_authenticated_entity import ProfileViewNonAuthenticatedEntity
from wink_sdk_user_settings.models.property_policy_authenticated_entity import PropertyPolicyAuthenticatedEntity
from wink_sdk_user_settings.models.rate_modifier_authenticated_entity import RateModifierAuthenticatedEntity
from wink_sdk_user_settings.models.rate_modifier_bundle_authenticated_entity import RateModifierBundleAuthenticatedEntity
from wink_sdk_user_settings.models.remove_entry_response import RemoveEntryResponse
from wink_sdk_user_settings.models.revoke_client_id_response import RevokeClientIdResponse
from wink_sdk_user_settings.models.sales_channel_authenticated_entity import SalesChannelAuthenticatedEntity
from wink_sdk_user_settings.models.show_profile400_response import ShowProfile400Response
from wink_sdk_user_settings.models.simple_description import SimpleDescription
from wink_sdk_user_settings.models.simple_description_authenticated_entity import SimpleDescriptionAuthenticatedEntity
from wink_sdk_user_settings.models.simple_multimedia import SimpleMultimedia
from wink_sdk_user_settings.models.simple_multimedia_authenticated_entity import SimpleMultimediaAuthenticatedEntity
from wink_sdk_user_settings.models.social_authenticated_entity import SocialAuthenticatedEntity
from wink_sdk_user_settings.models.sub_country_authenticated_entity import SubCountryAuthenticatedEntity
from wink_sdk_user_settings.models.sub_sub_country_authenticated_entity import SubSubCountryAuthenticatedEntity
from wink_sdk_user_settings.models.travel_inventory_recognition_authenticated_entity import TravelInventoryRecognitionAuthenticatedEntity
from wink_sdk_user_settings.models.update_application_response import UpdateApplicationResponse
from wink_sdk_user_settings.models.upsert_application_request import UpsertApplicationRequest
from wink_sdk_user_settings.models.upsert_profile_request_non_authenticated_entity import UpsertProfileRequestNonAuthenticatedEntity
from wink_sdk_user_settings.models.upsert_user_profile_request import UpsertUserProfileRequest
from wink_sdk_user_settings.models.upsert_user_profile_response import UpsertUserProfileResponse
from wink_sdk_user_settings.models.upsert_webhook_request import UpsertWebhookRequest
from wink_sdk_user_settings.models.webhook import Webhook
