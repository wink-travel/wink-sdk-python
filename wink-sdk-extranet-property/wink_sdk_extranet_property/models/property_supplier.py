# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None   # Extranet Property API This part of the documentation concerns itself with basic property management. It can:  1. Property: List existing properties. Manage property status. Change name and similar. 2. Notification: Read internal messages sent from Wink to your properties. 3. Announcement: Show pertinent messages to travelers in a pop-up window. 4. Geo-location: Set property geo-location. 5. Green Index: Answer eco-related questions regarding the property's recycling practices and much more. 6. Lifestyles: Manage lifestyles the property caters to. 7. Photos / Videos: Manage property media. 8. Policy: Manage property policy. I.e. Children, pets, wi-fi, parking etc. 9. Reputation: Manage awards, online / offline ratings etc. 10. Services: Manage property amenities. 11. Social media: Manage property social media networks. 12. Welcome text: Manage property descriptions  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.31.2
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from wink_sdk_extranet_property.models.contact_supplier import ContactSupplier
from wink_sdk_extranet_property.models.general_manager_supplier import GeneralManagerSupplier
from wink_sdk_extranet_property.models.geo_json_point_supplier import GeoJsonPointSupplier
from wink_sdk_extranet_property.models.geo_name_lightweight_supplier import GeoNameLightweightSupplier
from wink_sdk_extranet_property.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_property.models.managed_by_entity_supplier import ManagedByEntitySupplier
from wink_sdk_extranet_property.models.managing_entity_manager_supplier import ManagingEntityManagerSupplier
from wink_sdk_extranet_property.models.property_aggregate_green_index_answers_supplier import PropertyAggregateGreenIndexAnswersSupplier
from wink_sdk_extranet_property.models.property_policy_supplier import PropertyPolicySupplier
from wink_sdk_extranet_property.models.simple_address_supplier import SimpleAddressSupplier
from wink_sdk_extranet_property.models.simple_description_supplier import SimpleDescriptionSupplier
from wink_sdk_extranet_property.models.simple_multimedia_supplier import SimpleMultimediaSupplier
from wink_sdk_extranet_property.models.social_supplier import SocialSupplier
from wink_sdk_extranet_property.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
from typing import Optional, Set
from typing_extensions import Self

class PropertySupplier(BaseModel):
    """
    PropertySupplier
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Document UUID")
    created_date: Optional[datetime] = Field(default=None, description="Datetime this record was first created", alias="createdDate")
    last_update: Optional[datetime] = Field(default=None, description="Datetime this record was last updated", alias="lastUpdate")
    version: Optional[StrictInt] = Field(default=None, description="Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception.")
    user_identifier: UUID = Field(description="User owner ID.", alias="userIdentifier")
    managing_entity_identifier: UUID = Field(description="Parent ID. Because it's all 1-1, it should be the same ID.", alias="managingEntityIdentifier")
    owner_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The App owner that created this record.", alias="ownerIdentifier")
    managers: Annotated[List[ManagingEntityManagerSupplier], Field(min_length=1)]
    managed_by: Optional[ManagedByEntitySupplier] = Field(default=None, description="If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking.", alias="managedBy")
    owner_type: StrictStr = Field(description="Type of entity this is.", alias="ownerType")
    type: StrictStr = Field(description="Type of sales channel")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique).")
    legal_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Legal name of your hotel as it is registered.", alias="legalName")
    url_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Unique url-friendly slug to identify property", alias="urlName")
    unique_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Event shorter name", alias="uniqueId")
    currency_code: StrictStr = Field(description="Currency code", alias="currencyCode")
    status: StrictStr = Field(description="wink.travel sets this status as the hotel moves through the payment workflow and manually for approval.")
    city: GeoNameLightweightSupplier = Field(description="City location")
    address: Optional[SimpleAddressSupplier] = None
    place_id: Optional[StrictStr] = Field(default=None, description="Optional Google placeId for properties with a Google Business account.", alias="placeId")
    hotel_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="A shorter unique code to refer to the hotel. Country Code + 5 digit number", alias="hotelCode")
    local_name: Optional[StrictStr] = Field(default=None, description="Name of the hotel in its local language if you use it for domestic guests.", alias="localName")
    external_status: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Property goes active by changing externalStatus.", alias="externalStatus")
    multimedias: Optional[List[SimpleMultimediaSupplier]] = Field(default=None, description="List of images / videos of property.")
    recognition_list: Optional[List[TravelInventoryRecognitionSupplier]] = Field(default=None, description="Inventory-level recognition.", alias="recognitionList")
    location_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `LOC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="locationCategory")
    segment_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `SEG` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="segmentCategory")
    hotel_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `PCT` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="hotelCategory")
    architectural_style: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `ARC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="architecturalStyle")
    when_built: Optional[StrictStr] = Field(default=None, description="Year the property was constructed.", alias="whenBuilt")
    hotel_chain: Optional[StrictStr] = Field(default=None, description="Hotel chain name if property is part of that chain.", alias="hotelChain")
    hotel_brand: Optional[StrictStr] = Field(default=None, description="Hotel brand name if property is part of that brand.", alias="hotelBrand")
    other_channel_manager: Optional[StrictStr] = Field(default=None, description="If the property is currently using a channel manager but it isn't yet part of our list, chose 'OTHER_CHANNEL_MANAGER' as channelManager and fill in the name of the channel manager here", alias="otherChannelManager")
    license_number: Optional[StrictStr] = Field(default=None, description="If the property has a valid license number to run a hotel in their country, add it here.", alias="licenseNumber")
    stars: Optional[Annotated[int, Field(le=6, strict=True, ge=0)]] = Field(default=None, description="Hotel star rating.")
    general_manager: Optional[GeneralManagerSupplier] = Field(default=None, alias="generalManager")
    descriptions: Optional[List[SimpleDescriptionSupplier]] = Field(default=None, description="Localized short and long welcome text of property.")
    hotel_amenity_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `HAC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory).", alias="hotelAmenityCodes")
    property_accessibility_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `PHY` code. See [OTA geoname data](#operation/showAvailableCodesForCategory).", alias="propertyAccessibilityCodes")
    property_security_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `SEC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory).", alias="propertySecurityCodes")
    location_point: Optional[GeoJsonPointSupplier] = Field(default=None, description="GeoJSON point containing latitude and longitude of property. `Note: x = longitude, y = latitude`.", alias="locationPoint")
    policy: Optional[PropertyPolicySupplier] = Field(default=None, description="Property policies such as pets and children, early and late checkout and more")
    socials: Optional[List[SocialSupplier]] = Field(default=None, description="List of all social network account property has.")
    reservations_contact: Optional[ContactSupplier] = Field(default=None, description="Reservation desk contact information", alias="reservationsContact")
    revenue_contact: Optional[ContactSupplier] = Field(default=None, description="Accounting contact information", alias="revenueContact")
    marketing_contact: Optional[ContactSupplier] = Field(default=None, description="Accounting contact address", alias="marketingContact")
    lifestyle_types: Optional[List[StrictStr]] = Field(default=None, alias="lifestyleTypes")
    green_index_scores: Optional[PropertyAggregateGreenIndexAnswersSupplier] = Field(default=None, description="Properties that answered the Green Index questionnaire [full or partial], will have aggregate scores available.", alias="greenIndexScores")
    number_of_rooms: Annotated[int, Field(strict=True, ge=0)] = Field(description="Number of rooms / keys for property", alias="numberOfRooms")
    reservation_desk_start_time: Optional[StrictStr] = Field(default=None, description="If the reservation desk does not operate 24 hours, enter a start time.", alias="reservationDeskStartTime")
    reservation_desk_end_time: Optional[StrictStr] = Field(default=None, description="If the reservation desk does not operate 24 hours, enter an end time.", alias="reservationDeskEndTime")
    website: Optional[StrictStr] = Field(default=None, description="Property brand.com website.")
    google_maps_url: Optional[StrictStr] = Field(default=None, description="Google Maps URL of the place", alias="googleMapsUrl")
    rate_provider: Optional[KeyValuePairSupplier] = Field(default=None, description="This can be an enum for external channel managers or an identifier for a Wink company rate provider", alias="rateProvider")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Place to put stuff into")
    active: Optional[StrictBool] = Field(default=None, description="Property is both approved and activated.")
    property_active: Optional[StrictBool] = Field(default=None, description="Property activated itself and went live.", alias="propertyActive")
    platform_active: Optional[StrictBool] = Field(default=None, description="Platform approved property.", alias="platformActive")
    social_networks: Optional[StrictBool] = Field(default=None, description="Whether property has any social networks associated with her profile.", alias="socialNetworks")
    lifestyles: Optional[StrictBool] = Field(default=None, description="Whether property has any lifestyles associated with her profile.")
    __properties: ClassVar[List[str]] = ["id", "createdDate", "lastUpdate", "version", "userIdentifier", "managingEntityIdentifier", "ownerIdentifier", "managers", "managedBy", "ownerType", "type", "name", "legalName", "urlName", "uniqueId", "currencyCode", "status", "city", "address", "placeId", "hotelCode", "localName", "externalStatus", "multimedias", "recognitionList", "locationCategory", "segmentCategory", "hotelCategory", "architecturalStyle", "whenBuilt", "hotelChain", "hotelBrand", "otherChannelManager", "licenseNumber", "stars", "generalManager", "descriptions", "hotelAmenityCodes", "propertyAccessibilityCodes", "propertySecurityCodes", "locationPoint", "policy", "socials", "reservationsContact", "revenueContact", "marketingContact", "lifestyleTypes", "greenIndexScores", "numberOfRooms", "reservationDeskStartTime", "reservationDeskEndTime", "website", "googleMapsUrl", "rateProvider", "metadata", "active", "propertyActive", "platformActive", "socialNetworks", "lifestyles"]

    @field_validator('owner_type')
    def owner_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COMPANY', 'INDIVIDUAL']):
            raise ValueError("must be one of enum values ('COMPANY', 'INDIVIDUAL')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TRIP_PAY', 'FACILITATOR', 'DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER', 'OTHER']):
            raise ValueError("must be one of enum values ('TRIP_PAY', 'FACILITATOR', 'DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER', 'OTHER')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PENDING_APPROVAL', 'ACTIVE', 'INACTIVE', 'UNDER_REVIEW', 'SUSPENDED', 'REJECTED', 'REMOVED']):
            raise ValueError("must be one of enum values ('PENDING_APPROVAL', 'ACTIVE', 'INACTIVE', 'UNDER_REVIEW', 'SUSPENDED', 'REJECTED', 'REMOVED')")
        return value

    @field_validator('external_status')
    def external_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE')")
        return value

    @field_validator('lifestyle_types')
    def lifestyle_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO']):
                raise ValueError("each list item must be one of ('LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PropertySupplier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in managers (list)
        _items = []
        if self.managers:
            for _item_managers in self.managers:
                if _item_managers:
                    _items.append(_item_managers.to_dict())
            _dict['managers'] = _items
        # override the default output from pydantic by calling `to_dict()` of managed_by
        if self.managed_by:
            _dict['managedBy'] = self.managed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict['city'] = self.city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in multimedias (list)
        _items = []
        if self.multimedias:
            for _item_multimedias in self.multimedias:
                if _item_multimedias:
                    _items.append(_item_multimedias.to_dict())
            _dict['multimedias'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recognition_list (list)
        _items = []
        if self.recognition_list:
            for _item_recognition_list in self.recognition_list:
                if _item_recognition_list:
                    _items.append(_item_recognition_list.to_dict())
            _dict['recognitionList'] = _items
        # override the default output from pydantic by calling `to_dict()` of general_manager
        if self.general_manager:
            _dict['generalManager'] = self.general_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in descriptions (list)
        _items = []
        if self.descriptions:
            for _item_descriptions in self.descriptions:
                if _item_descriptions:
                    _items.append(_item_descriptions.to_dict())
            _dict['descriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of location_point
        if self.location_point:
            _dict['locationPoint'] = self.location_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in socials (list)
        _items = []
        if self.socials:
            for _item_socials in self.socials:
                if _item_socials:
                    _items.append(_item_socials.to_dict())
            _dict['socials'] = _items
        # override the default output from pydantic by calling `to_dict()` of reservations_contact
        if self.reservations_contact:
            _dict['reservationsContact'] = self.reservations_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revenue_contact
        if self.revenue_contact:
            _dict['revenueContact'] = self.revenue_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marketing_contact
        if self.marketing_contact:
            _dict['marketingContact'] = self.marketing_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of green_index_scores
        if self.green_index_scores:
            _dict['greenIndexScores'] = self.green_index_scores.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_provider
        if self.rate_provider:
            _dict['rateProvider'] = self.rate_provider.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropertySupplier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdDate": obj.get("createdDate"),
            "lastUpdate": obj.get("lastUpdate"),
            "version": obj.get("version"),
            "userIdentifier": obj.get("userIdentifier"),
            "managingEntityIdentifier": obj.get("managingEntityIdentifier"),
            "ownerIdentifier": obj.get("ownerIdentifier"),
            "managers": [ManagingEntityManagerSupplier.from_dict(_item) for _item in obj["managers"]] if obj.get("managers") is not None else None,
            "managedBy": ManagedByEntitySupplier.from_dict(obj["managedBy"]) if obj.get("managedBy") is not None else None,
            "ownerType": obj.get("ownerType"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "legalName": obj.get("legalName"),
            "urlName": obj.get("urlName"),
            "uniqueId": obj.get("uniqueId"),
            "currencyCode": obj.get("currencyCode"),
            "status": obj.get("status") if obj.get("status") is not None else APPROVED,
            "city": GeoNameLightweightSupplier.from_dict(obj["city"]) if obj.get("city") is not None else None,
            "address": SimpleAddressSupplier.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "placeId": obj.get("placeId"),
            "hotelCode": obj.get("hotelCode"),
            "localName": obj.get("localName"),
            "externalStatus": obj.get("externalStatus") if obj.get("externalStatus") is not None else 'ACTIVE',
            "multimedias": [SimpleMultimediaSupplier.from_dict(_item) for _item in obj["multimedias"]] if obj.get("multimedias") is not None else None,
            "recognitionList": [TravelInventoryRecognitionSupplier.from_dict(_item) for _item in obj["recognitionList"]] if obj.get("recognitionList") is not None else None,
            "locationCategory": obj.get("locationCategory"),
            "segmentCategory": obj.get("segmentCategory"),
            "hotelCategory": obj.get("hotelCategory"),
            "architecturalStyle": obj.get("architecturalStyle"),
            "whenBuilt": obj.get("whenBuilt"),
            "hotelChain": obj.get("hotelChain"),
            "hotelBrand": obj.get("hotelBrand"),
            "otherChannelManager": obj.get("otherChannelManager"),
            "licenseNumber": obj.get("licenseNumber"),
            "stars": obj.get("stars"),
            "generalManager": GeneralManagerSupplier.from_dict(obj["generalManager"]) if obj.get("generalManager") is not None else None,
            "descriptions": [SimpleDescriptionSupplier.from_dict(_item) for _item in obj["descriptions"]] if obj.get("descriptions") is not None else None,
            "hotelAmenityCodes": obj.get("hotelAmenityCodes"),
            "propertyAccessibilityCodes": obj.get("propertyAccessibilityCodes"),
            "propertySecurityCodes": obj.get("propertySecurityCodes"),
            "locationPoint": GeoJsonPointSupplier.from_dict(obj["locationPoint"]) if obj.get("locationPoint") is not None else None,
            "policy": PropertyPolicySupplier.from_dict(obj["policy"]) if obj.get("policy") is not None else None,
            "socials": [SocialSupplier.from_dict(_item) for _item in obj["socials"]] if obj.get("socials") is not None else None,
            "reservationsContact": ContactSupplier.from_dict(obj["reservationsContact"]) if obj.get("reservationsContact") is not None else None,
            "revenueContact": ContactSupplier.from_dict(obj["revenueContact"]) if obj.get("revenueContact") is not None else None,
            "marketingContact": ContactSupplier.from_dict(obj["marketingContact"]) if obj.get("marketingContact") is not None else None,
            "lifestyleTypes": obj.get("lifestyleTypes"),
            "greenIndexScores": PropertyAggregateGreenIndexAnswersSupplier.from_dict(obj["greenIndexScores"]) if obj.get("greenIndexScores") is not None else None,
            "numberOfRooms": obj.get("numberOfRooms"),
            "reservationDeskStartTime": obj.get("reservationDeskStartTime"),
            "reservationDeskEndTime": obj.get("reservationDeskEndTime"),
            "website": obj.get("website"),
            "googleMapsUrl": obj.get("googleMapsUrl"),
            "rateProvider": KeyValuePairSupplier.from_dict(obj["rateProvider"]) if obj.get("rateProvider") is not None else None,
            "metadata": obj.get("metadata"),
            "active": obj.get("active"),
            "propertyActive": obj.get("propertyActive"),
            "platformActive": obj.get("platformActive"),
            "socialNetworks": obj.get("socialNetworks"),
            "lifestyles": obj.get("lifestyles")
        })
        return _obj


