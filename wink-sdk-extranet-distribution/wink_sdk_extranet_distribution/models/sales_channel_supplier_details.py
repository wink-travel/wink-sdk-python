# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Extranet Distribution API The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink. This API lets you:  1. Verifier: Test your availability and promotions and create test bookings to simulate the entire booking workflow. 2. Sales Channels: Manage your sales channels. 3. Explore Network: Find new affiliates to work with. 4. Inventory: Manage blocking at the sales channel-level. 5. Calendars: Manage availability calendars for all your blocking.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wink_sdk_extranet_distribution.models.rate_modifier_bundle_supplier_details import RateModifierBundleSupplierDetails
from wink_sdk_extranet_distribution.models.rate_modifier_supplier_details import RateModifierSupplierDetails
from typing import Optional, Set
from typing_extensions import Self

class SalesChannelSupplierDetails(BaseModel):
    """
    Parent sales channel
    """ # noqa: E501
    identifier: StrictStr = Field(description="Unique record identifier of this segment / account")
    supplier_identifier: StrictStr = Field(description="Channel is owned by this supplier identifier.", alias="supplierIdentifier")
    supplier_name: StrictStr = Field(description="Name of property / supplier that owns this channel", alias="supplierName")
    supplier_available: Optional[StrictBool] = Field(default=True, description="Flag when supplier not available. E.g. Hotel disables property", alias="supplierAvailable")
    sub_type: StrictStr = Field(description="What type of segment of channel is this.", alias="subType")
    owner_identifier: StrictStr = Field(description="A specific identifier for the company / corporation / travel agency that is retrieving the rates", alias="ownerIdentifier")
    owner_name: StrictStr = Field(description="Name of the owner / affiliate. `Hotel booking engine` when it's the booking engine.", alias="ownerName")
    enabled: Optional[StrictBool] = Field(default=True, description="Flag the supplier can use to enable / disable this channel")
    channel_disabled: Optional[StrictBool] = Field(default=None, description="System override by reactive to disable. E.g. Platform disables supplier.", alias="channelDisabled")
    blacklisted: StrictBool = Field(description="A way to blacklist a specific channel a property doesn't want to send blocking to.")
    percent_discount: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="Percent discount on this channel and all its children [unless configured at the child level].", alias="percentDiscount")
    commission: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="Amount of sales commission earned through this channel and all its children [unless configured at the child level].")
    rate_modifiers: Optional[List[RateModifierSupplierDetails]] = Field(default=None, description="Promotions for this channel", alias="rateModifiers")
    rate_modifier_bundles: Optional[List[RateModifierBundleSupplierDetails]] = Field(default=None, description="Promotion bundles for this channel", alias="rateModifierBundles")
    __properties: ClassVar[List[str]] = ["identifier", "supplierIdentifier", "supplierName", "supplierAvailable", "subType", "ownerIdentifier", "ownerName", "enabled", "channelDisabled", "blacklisted", "percentDiscount", "commission", "rateModifiers", "rateModifierBundles"]

    @field_validator('sub_type')
    def sub_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER']):
            raise ValueError("must be one of enum values ('DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER')")
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
        """Create an instance of SalesChannelSupplierDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rate_modifiers (list)
        _items = []
        if self.rate_modifiers:
            for _item_rate_modifiers in self.rate_modifiers:
                if _item_rate_modifiers:
                    _items.append(_item_rate_modifiers.to_dict())
            _dict['rateModifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rate_modifier_bundles (list)
        _items = []
        if self.rate_modifier_bundles:
            for _item_rate_modifier_bundles in self.rate_modifier_bundles:
                if _item_rate_modifier_bundles:
                    _items.append(_item_rate_modifier_bundles.to_dict())
            _dict['rateModifierBundles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SalesChannelSupplierDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "supplierIdentifier": obj.get("supplierIdentifier"),
            "supplierName": obj.get("supplierName"),
            "supplierAvailable": obj.get("supplierAvailable") if obj.get("supplierAvailable") is not None else True,
            "subType": obj.get("subType"),
            "ownerIdentifier": obj.get("ownerIdentifier"),
            "ownerName": obj.get("ownerName"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "channelDisabled": obj.get("channelDisabled"),
            "blacklisted": obj.get("blacklisted"),
            "percentDiscount": obj.get("percentDiscount"),
            "commission": obj.get("commission"),
            "rateModifiers": [RateModifierSupplierDetails.from_dict(_item) for _item in obj["rateModifiers"]] if obj.get("rateModifiers") is not None else None,
            "rateModifierBundles": [RateModifierBundleSupplierDetails.from_dict(_item) for _item in obj["rateModifierBundles"]] if obj.get("rateModifierBundles") is not None else None
        })
        return _obj


