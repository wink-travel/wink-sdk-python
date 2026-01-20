# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None   # Affiliate API The Affiliate API exposes endpoints to manage affiliate accounts. This API lets you:  1. Create affiliates. 2. Create account managers  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.31.0
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from wink_sdk_affiliate.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_affiliate.models.geo_name_lightweight_agent import GeoNameLightweightAgent
from wink_sdk_affiliate.models.managed_by_entity_agent import ManagedByEntityAgent
from wink_sdk_affiliate.models.managing_entity_manager_agent import ManagingEntityManagerAgent
from wink_sdk_affiliate.models.online_presence_agent import OnlinePresenceAgent
from wink_sdk_affiliate.models.simple_multimedia_agent import SimpleMultimediaAgent
from wink_sdk_affiliate.models.travel_agent_agent import TravelAgentAgent
from typing import Optional, Set
from typing_extensions import Self

class AffiliateAccountAgent(BaseModel):
    """
    AffiliateAccountAgent
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Document UUID")
    created_date: Optional[datetime] = Field(default=None, description="Datetime this record was first created", alias="createdDate")
    last_update: Optional[datetime] = Field(default=None, description="Datetime this record was last updated", alias="lastUpdate")
    version: Optional[StrictInt] = Field(default=None, description="Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception.")
    user_identifier: UUID = Field(description="User owner ID.", alias="userIdentifier")
    managing_entity_identifier: UUID = Field(description="Parent ID. Because it's all 1-1, it should be the same ID.", alias="managingEntityIdentifier")
    owner_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The App owner that created this record.", alias="ownerIdentifier")
    managers: Annotated[List[ManagingEntityManagerAgent], Field(min_length=1)]
    managed_by: Optional[ManagedByEntityAgent] = Field(default=None, description="If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking.", alias="managedBy")
    owner_type: StrictStr = Field(description="Type of entity this is.", alias="ownerType")
    type: StrictStr = Field(description="Type of sales channel")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of company")
    url_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Url slug of company name", alias="urlName")
    unique_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Event shorter name", alias="uniqueId")
    description: Optional[StrictStr] = Field(default=None, description="Account description.")
    currency_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Account's main currency.", alias="currencyCode")
    city: GeoNameLightweightAgent
    place_id: Optional[StrictStr] = Field(default=None, description="Optional Google placeId for properties with a Google Business account.", alias="placeId")
    profile_picture: Optional[SimpleMultimediaAgent] = Field(default=None, description="Customize account with a custom profile picture.", alias="profilePicture")
    status: StrictStr = Field(description="Status of entity.")
    logo: Optional[SimpleMultimediaAgent] = Field(default=None, description="Customize account with a custom logo / profile picture.")
    travel_agent: Optional[TravelAgentAgent] = Field(default=None, description="Optional travel agent details if the affiliate account is a travel agent.", alias="travelAgent")
    online_presence: Optional[List[OnlinePresenceAgent]] = Field(default=None, alias="onlinePresence")
    annual_travel_spend_in_dollars: Optional[CustomMonetaryAmount] = Field(default=None, description="How much user or company spends on travel per year.", alias="annualTravelSpendInDollars")
    __properties: ClassVar[List[str]] = ["id", "createdDate", "lastUpdate", "version", "userIdentifier", "managingEntityIdentifier", "ownerIdentifier", "managers", "managedBy", "ownerType", "type", "name", "urlName", "uniqueId", "description", "currencyCode", "city", "placeId", "profilePicture", "status", "logo", "travelAgent", "onlinePresence", "annualTravelSpendInDollars"]

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
        """Create an instance of AffiliateAccountAgent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of profile_picture
        if self.profile_picture:
            _dict['profilePicture'] = self.profile_picture.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of travel_agent
        if self.travel_agent:
            _dict['travelAgent'] = self.travel_agent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in online_presence (list)
        _items = []
        if self.online_presence:
            for _item_online_presence in self.online_presence:
                if _item_online_presence:
                    _items.append(_item_online_presence.to_dict())
            _dict['onlinePresence'] = _items
        # override the default output from pydantic by calling `to_dict()` of annual_travel_spend_in_dollars
        if self.annual_travel_spend_in_dollars:
            _dict['annualTravelSpendInDollars'] = self.annual_travel_spend_in_dollars.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AffiliateAccountAgent from a dict"""
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
            "managers": [ManagingEntityManagerAgent.from_dict(_item) for _item in obj["managers"]] if obj.get("managers") is not None else None,
            "managedBy": ManagedByEntityAgent.from_dict(obj["managedBy"]) if obj.get("managedBy") is not None else None,
            "ownerType": obj.get("ownerType"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "urlName": obj.get("urlName"),
            "uniqueId": obj.get("uniqueId"),
            "description": obj.get("description"),
            "currencyCode": obj.get("currencyCode"),
            "city": GeoNameLightweightAgent.from_dict(obj["city"]) if obj.get("city") is not None else None,
            "placeId": obj.get("placeId"),
            "profilePicture": SimpleMultimediaAgent.from_dict(obj["profilePicture"]) if obj.get("profilePicture") is not None else None,
            "status": obj.get("status"),
            "logo": SimpleMultimediaAgent.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "travelAgent": TravelAgentAgent.from_dict(obj["travelAgent"]) if obj.get("travelAgent") is not None else None,
            "onlinePresence": [OnlinePresenceAgent.from_dict(_item) for _item in obj["onlinePresence"]] if obj.get("onlinePresence") is not None else None,
            "annualTravelSpendInDollars": CustomMonetaryAmount.from_dict(obj["annualTravelSpendInDollars"]) if obj.get("annualTravelSpendInDollars") is not None else None
        })
        return _obj


