# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Extranet Facilities API This part of the documentation concerns itself with the management of facilities, on and off the property. This API lets you create:  1. Guest room: Manage room types on and off the premises. 2. Meeting room: Manage meeting rooms on and off the premises. 3. Restaurant: Manage restaurants on and off the premises. 4. Spa: Manage spas on and off the premises.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.17.14
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wink_sdk_extranet_facilities.models.address_supplier import AddressSupplier
from wink_sdk_extranet_facilities.models.contact_supplier import ContactSupplier
from wink_sdk_extranet_facilities.models.dow_pattern_group_supplier import DowPatternGroupSupplier
from wink_sdk_extranet_facilities.models.geo_json_point_supplier import GeoJsonPointSupplier
from wink_sdk_extranet_facilities.models.simple_description_supplier import SimpleDescriptionSupplier
from wink_sdk_extranet_facilities.models.simple_multimedia_supplier import SimpleMultimediaSupplier
from wink_sdk_extranet_facilities.models.social_supplier import SocialSupplier
from wink_sdk_extranet_facilities.models.transactional_travel_inventory_supplier import TransactionalTravelInventorySupplier
from wink_sdk_extranet_facilities.models.travel_inventory_recognition_supplier import TravelInventoryRecognitionSupplier
from typing import Optional, Set
from typing_extensions import Self

class RestaurantSupplier(BaseModel):
    """
    RestaurantSupplier
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Document UUID")
    created_date: Optional[datetime] = Field(default=None, description="Datetime this record was first created", alias="createdDate")
    last_update: Optional[datetime] = Field(default=None, description="Datetime this record was last updated", alias="lastUpdate")
    version: Optional[StrictInt] = Field(default=None, description="Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception.")
    hotel_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Hotel identifier.", alias="hotelIdentifier")
    featured_ind: StrictBool = Field(description="Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special.", alias="featuredInd")
    lifestyle_type: Optional[StrictStr] = Field(default=None, description="Indicate the type of lifestyle this blocking should be associated with.", alias="lifestyleType")
    location: GeoJsonPointSupplier = Field(description="Geo-location point where blocking takes place. Defaults to location of property.")
    descriptions: Annotated[List[SimpleDescriptionSupplier], Field(min_length=1)]
    multimedias: Annotated[List[SimpleMultimediaSupplier], Field(min_length=1)]
    contact: ContactSupplier = Field(description="Associate a contact person for this blocking (if applicable).")
    address: AddressSupplier = Field(description="Defaults to property address.")
    commissionable: StrictBool = Field(description="Indicate whether sales channels receive commission for selling this blocking.")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Internal name of blocking.")
    proximity_code: StrictStr = Field(description="Supported OTA specification `PRX` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="proximityCode")
    sort: Optional[StrictInt] = Field(default=None, description="Use this property to sort an blocking in a list of activities.")
    min_age_appropriate_code: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `AQC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="minAgeAppropriateCode")
    bookable: StrictBool = Field(description="Indicates if this blocking can be added to a booking or if it is read-only marketing material only.")
    active: StrictBool = Field(description="Modify blocking availability with this flag.")
    disability_features: Optional[List[StrictStr]] = Field(default=None, alias="disabilityFeatures")
    security_features: Optional[List[StrictStr]] = Field(default=None, alias="securityFeatures")
    socials: Optional[List[SocialSupplier]] = None
    price_point: StrictStr = Field(description="Level of expensiveness.", alias="pricePoint")
    recognition_list: Optional[List[TravelInventoryRecognitionSupplier]] = Field(default=None, alias="recognitionList")
    transactional_inventory_list: Optional[List[TransactionalTravelInventorySupplier]] = Field(default=None, alias="transactionalInventoryList")
    applicable_start: Optional[date] = Field(default=None, description="Start month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a starting date.", alias="applicableStart")
    applicable_end: Optional[date] = Field(default=None, description="End month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a ending date.", alias="applicableEnd")
    reservation_required_ind: Optional[StrictBool] = Field(default=None, description="Indicates whether a reservation is required to participate in this blocking.", alias="reservationRequiredInd")
    opens: Optional[StrictStr] = Field(default=None, description="Opening time of blocking (if applicable). Leave empty if blocking is always available.")
    closes: Optional[StrictStr] = Field(default=None, description="Closing time of blocking (if applicable). Leave empty if blocking is always available.")
    days_of_week: Optional[DowPatternGroupSupplier] = Field(default=None, description="Indicate which days this blocking is open.", alias="daysOfWeek")
    max_seating_capacity: Annotated[int, Field(strict=True, ge=1)] = Field(description="Restaurant supports these many people.", alias="maxSeatingCapacity")
    max_single_party: Annotated[int, Field(strict=True, ge=1)] = Field(description="Largest table at restaurant.", alias="maxSingleParty")
    offer_breakfast: StrictBool = Field(description="Restaurant offers breakfast.", alias="offerBreakfast")
    offer_lunch: StrictBool = Field(description="Restaurant offers lunch.", alias="offerLunch")
    offer_dinner: StrictBool = Field(description="Restaurant offers dinner.", alias="offerDinner")
    offer_brunch: StrictBool = Field(description="Restaurant offers brunch.", alias="offerBrunch")
    amenities: Optional[List[StrictStr]] = None
    info_codes: Optional[List[StrictStr]] = Field(default=None, alias="infoCodes")
    cuisine_codes: Optional[List[StrictStr]] = Field(default=None, alias="cuisineCodes")
    __properties: ClassVar[List[str]] = ["id", "createdDate", "lastUpdate", "version", "hotelIdentifier", "featuredInd", "lifestyleType", "location", "descriptions", "multimedias", "contact", "address", "commissionable", "name", "proximityCode", "sort", "minAgeAppropriateCode", "bookable", "active", "disabilityFeatures", "securityFeatures", "socials", "pricePoint", "recognitionList", "transactionalInventoryList", "applicableStart", "applicableEnd", "reservationRequiredInd", "opens", "closes", "daysOfWeek", "maxSeatingCapacity", "maxSingleParty", "offerBreakfast", "offerLunch", "offerDinner", "offerBrunch", "amenities", "infoCodes", "cuisineCodes"]

    @field_validator('lifestyle_type')
    def lifestyle_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO']):
            raise ValueError("must be one of enum values ('LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO')")
        return value

    @field_validator('price_point')
    def price_point_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['HALF', 'ONE', 'ONE_HALF', 'TWO', 'TWO_HALF', 'THREE', 'THREE_HALF', 'FOUR', 'FOUR_HALF', 'FIVE']):
            raise ValueError("must be one of enum values ('HALF', 'ONE', 'ONE_HALF', 'TWO', 'TWO_HALF', 'THREE', 'THREE_HALF', 'FOUR', 'FOUR_HALF', 'FIVE')")
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
        """Create an instance of RestaurantSupplier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in descriptions (list)
        _items = []
        if self.descriptions:
            for _item_descriptions in self.descriptions:
                if _item_descriptions:
                    _items.append(_item_descriptions.to_dict())
            _dict['descriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in multimedias (list)
        _items = []
        if self.multimedias:
            for _item_multimedias in self.multimedias:
                if _item_multimedias:
                    _items.append(_item_multimedias.to_dict())
            _dict['multimedias'] = _items
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in socials (list)
        _items = []
        if self.socials:
            for _item_socials in self.socials:
                if _item_socials:
                    _items.append(_item_socials.to_dict())
            _dict['socials'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recognition_list (list)
        _items = []
        if self.recognition_list:
            for _item_recognition_list in self.recognition_list:
                if _item_recognition_list:
                    _items.append(_item_recognition_list.to_dict())
            _dict['recognitionList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transactional_inventory_list (list)
        _items = []
        if self.transactional_inventory_list:
            for _item_transactional_inventory_list in self.transactional_inventory_list:
                if _item_transactional_inventory_list:
                    _items.append(_item_transactional_inventory_list.to_dict())
            _dict['transactionalInventoryList'] = _items
        # override the default output from pydantic by calling `to_dict()` of days_of_week
        if self.days_of_week:
            _dict['daysOfWeek'] = self.days_of_week.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestaurantSupplier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdDate": obj.get("createdDate"),
            "lastUpdate": obj.get("lastUpdate"),
            "version": obj.get("version"),
            "hotelIdentifier": obj.get("hotelIdentifier"),
            "featuredInd": obj.get("featuredInd"),
            "lifestyleType": obj.get("lifestyleType"),
            "location": GeoJsonPointSupplier.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "descriptions": [SimpleDescriptionSupplier.from_dict(_item) for _item in obj["descriptions"]] if obj.get("descriptions") is not None else None,
            "multimedias": [SimpleMultimediaSupplier.from_dict(_item) for _item in obj["multimedias"]] if obj.get("multimedias") is not None else None,
            "contact": ContactSupplier.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "address": AddressSupplier.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "commissionable": obj.get("commissionable") if obj.get("commissionable") is not None else True,
            "name": obj.get("name"),
            "proximityCode": obj.get("proximityCode"),
            "sort": obj.get("sort"),
            "minAgeAppropriateCode": obj.get("minAgeAppropriateCode"),
            "bookable": obj.get("bookable") if obj.get("bookable") is not None else True,
            "active": obj.get("active") if obj.get("active") is not None else True,
            "disabilityFeatures": obj.get("disabilityFeatures"),
            "securityFeatures": obj.get("securityFeatures"),
            "socials": [SocialSupplier.from_dict(_item) for _item in obj["socials"]] if obj.get("socials") is not None else None,
            "pricePoint": obj.get("pricePoint") if obj.get("pricePoint") is not None else 'THREE',
            "recognitionList": [TravelInventoryRecognitionSupplier.from_dict(_item) for _item in obj["recognitionList"]] if obj.get("recognitionList") is not None else None,
            "transactionalInventoryList": [TransactionalTravelInventorySupplier.from_dict(_item) for _item in obj["transactionalInventoryList"]] if obj.get("transactionalInventoryList") is not None else None,
            "applicableStart": obj.get("applicableStart"),
            "applicableEnd": obj.get("applicableEnd"),
            "reservationRequiredInd": obj.get("reservationRequiredInd"),
            "opens": obj.get("opens"),
            "closes": obj.get("closes"),
            "daysOfWeek": DowPatternGroupSupplier.from_dict(obj["daysOfWeek"]) if obj.get("daysOfWeek") is not None else None,
            "maxSeatingCapacity": obj.get("maxSeatingCapacity"),
            "maxSingleParty": obj.get("maxSingleParty"),
            "offerBreakfast": obj.get("offerBreakfast") if obj.get("offerBreakfast") is not None else False,
            "offerLunch": obj.get("offerLunch") if obj.get("offerLunch") is not None else False,
            "offerDinner": obj.get("offerDinner") if obj.get("offerDinner") is not None else False,
            "offerBrunch": obj.get("offerBrunch") if obj.get("offerBrunch") is not None else False,
            "amenities": obj.get("amenities"),
            "infoCodes": obj.get("infoCodes"),
            "cuisineCodes": obj.get("cuisineCodes")
        })
        return _obj


