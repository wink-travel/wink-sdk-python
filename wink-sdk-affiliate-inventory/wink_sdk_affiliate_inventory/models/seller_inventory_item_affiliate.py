# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Inventory API The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. This API lets you:  1. Manage customizations. 2. Shareable Links: Manage shareable supplier / inventory links. 3. Inventory: Manage individual inventory items. 4. Lists: Manage curated / ranked grids. 5. Maps: Manage maps.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.16.4
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wink_sdk_affiliate_inventory.models.simple_description_affiliate import SimpleDescriptionAffiliate
from typing import Optional, Set
from typing_extensions import Self

class SellerInventoryItemAffiliate(BaseModel):
    """
    SellerInventoryItem data
    """ # noqa: E501
    identifier: StrictStr = Field(description="Unique identifier")
    seller_identifier: StrictStr = Field(description="Company / Owner identifier", alias="sellerIdentifier")
    seller_inventory_item_name: StrictStr = Field(description="Descriptive name of this item for seller use", alias="sellerInventoryItemName")
    engine_configuration_identifier: StrictStr = Field(description="Which configuration to use with this item", alias="engineConfigurationIdentifier")
    descriptions: Annotated[List[SimpleDescriptionAffiliate], Field(min_length=1, max_length=2147483647)] = Field(description="Title and description of blocking.")
    keywords: Annotated[List[StrictStr], Field(min_length=1, max_length=2147483647)]
    status: StrictStr = Field(description="Availability status")
    inventory_status: StrictStr = Field(description="Url sell status", alias="inventoryStatus")
    inventory_type: StrictStr = Field(description="The type of blocking being offer up for sale", alias="inventoryType")
    channel_inventory_type: StrictStr = Field(description="Channel inventory type is a subset of blocking type in that it does not include the `HOTEL` type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property.", alias="channelInventoryType")
    supplier_identifier: StrictStr = Field(description="Supplier / Hotel identifier that owns this blocking.", alias="supplierIdentifier")
    channel_inventory_identifier: StrictStr = Field(description="The channel inventory record identifier describing the relationship between supplier and seller.", alias="channelInventoryIdentifier")
    multimedia_identifiers: Annotated[List[StrictStr], Field(min_length=1, max_length=2147483647)] = Field(description="Reference identifiers to Cloudinary media assets", alias="multimediaIdentifiers")
    animate: Optional[StrictBool] = Field(default=False, description="Create an animated gif instead of a list of images. Feature currently not available. Feel free to enable and it will become available at a later date.")
    animate_delay: Optional[StrictInt] = Field(default=None, description="Controls animation delay in milliseconds.", alias="animateDelay")
    sort: Optional[StrictStr] = Field(default=None, description="The specific badge to display over the image on the Web Component.")
    display_type: StrictStr = Field(description="Indicate which initial values to display first on the front-facing card", alias="displayType")
    __properties: ClassVar[List[str]] = ["identifier", "sellerIdentifier", "sellerInventoryItemName", "engineConfigurationIdentifier", "descriptions", "keywords", "status", "inventoryStatus", "inventoryType", "channelInventoryType", "supplierIdentifier", "channelInventoryIdentifier", "multimediaIdentifiers", "animate", "animateDelay", "sort", "displayType"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE', 'REMOVED']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'REMOVED')")
        return value

    @field_validator('inventory_status')
    def inventory_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE', 'REMOVED']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'REMOVED')")
        return value

    @field_validator('inventory_type')
    def inventory_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['HOTEL', 'GUEST_ROOM', 'MEETING_ROOM', 'RESTAURANT', 'SPA', 'ADD_ON', 'ATTRACTION', 'ACTIVITY', 'PLACE']):
            raise ValueError("must be one of enum values ('HOTEL', 'GUEST_ROOM', 'MEETING_ROOM', 'RESTAURANT', 'SPA', 'ADD_ON', 'ATTRACTION', 'ACTIVITY', 'PLACE')")
        return value

    @field_validator('channel_inventory_type')
    def channel_inventory_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['GUEST_ROOM', 'ADD_ON', 'MEETING_ROOM', 'RESTAURANT', 'SPA', 'ATTRACTION', 'PLACE', 'ACTIVITY']):
            raise ValueError("must be one of enum values ('GUEST_ROOM', 'ADD_ON', 'MEETING_ROOM', 'RESTAURANT', 'SPA', 'ATTRACTION', 'PLACE', 'ACTIVITY')")
        return value

    @field_validator('sort')
    def sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MEMBER', 'PRICE_LOW_TO_HIGH', 'PRICE_HIGH_TO_LOW', 'PRICE', 'POPULARITY', 'ECO', 'EXPERIENCE', 'PERK', 'LOYALTY', 'PACKAGE']):
            raise ValueError("must be one of enum values ('MEMBER', 'PRICE_LOW_TO_HIGH', 'PRICE_HIGH_TO_LOW', 'PRICE', 'POPULARITY', 'ECO', 'EXPERIENCE', 'PERK', 'LOYALTY', 'PACKAGE')")
        return value

    @field_validator('display_type')
    def display_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NATIVE', 'HOTEL', 'ROOM']):
            raise ValueError("must be one of enum values ('NATIVE', 'HOTEL', 'ROOM')")
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
        """Create an instance of SellerInventoryItemAffiliate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in descriptions (list)
        _items = []
        if self.descriptions:
            for _item_descriptions in self.descriptions:
                if _item_descriptions:
                    _items.append(_item_descriptions.to_dict())
            _dict['descriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SellerInventoryItemAffiliate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "sellerIdentifier": obj.get("sellerIdentifier"),
            "sellerInventoryItemName": obj.get("sellerInventoryItemName"),
            "engineConfigurationIdentifier": obj.get("engineConfigurationIdentifier"),
            "descriptions": [SimpleDescriptionAffiliate.from_dict(_item) for _item in obj["descriptions"]] if obj.get("descriptions") is not None else None,
            "keywords": obj.get("keywords"),
            "status": obj.get("status") if obj.get("status") is not None else 'ACTIVE',
            "inventoryStatus": obj.get("inventoryStatus"),
            "inventoryType": obj.get("inventoryType"),
            "channelInventoryType": obj.get("channelInventoryType"),
            "supplierIdentifier": obj.get("supplierIdentifier"),
            "channelInventoryIdentifier": obj.get("channelInventoryIdentifier"),
            "multimediaIdentifiers": obj.get("multimediaIdentifiers"),
            "animate": obj.get("animate") if obj.get("animate") is not None else False,
            "animateDelay": obj.get("animateDelay"),
            "sort": obj.get("sort"),
            "displayType": obj.get("displayType") if obj.get("displayType") is not None else 'NATIVE'
        })
        return _obj


