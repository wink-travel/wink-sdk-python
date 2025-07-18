# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Travel Agent API The Travel Agent API exposes endpoints to manage agent-facilitated bookings. This API lets you:  1. Travel Agent: Manage agent entity. 2. Booking: Create / Manage bookings  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.16.4
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wink_sdk_travel_agent.models.address_agent import AddressAgent
from wink_sdk_travel_agent.models.contact_agent import ContactAgent
from wink_sdk_travel_agent.models.general_manager_agent import GeneralManagerAgent
from wink_sdk_travel_agent.models.geo_json_point_agent import GeoJsonPointAgent
from wink_sdk_travel_agent.models.localized_description_agent import LocalizedDescriptionAgent
from wink_sdk_travel_agent.models.property_policy_agent import PropertyPolicyAgent
from wink_sdk_travel_agent.models.simple_multimedia_agent import SimpleMultimediaAgent
from wink_sdk_travel_agent.models.social_agent import SocialAgent
from wink_sdk_travel_agent.models.travel_inventory_recognition_agent import TravelInventoryRecognitionAgent
from typing import Optional, Set
from typing_extensions import Self

class HotelOnMapAgent(BaseModel):
    """
    Combined property data.
    """ # noqa: E501
    identifier: Optional[StrictStr] = Field(default=None, description="Unique record identifier. This is NOT the same as the unique hotel record identifier.")
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="Unique hotel record identifier.", alias="hotelIdentifier")
    name: Optional[StrictStr] = Field(default=None, description="Hotel trade name")
    local_name: Optional[StrictStr] = Field(default=None, description="Hotel local name if different from the trade name or if it is the local language.", alias="localName")
    chain: Optional[StrictStr] = Field(default=None, description="Name of hotel chain if applicable.")
    brand: Optional[StrictStr] = Field(default=None, description="Name of hotel brand")
    url_name: Optional[StrictStr] = Field(default=None, description="Unique URL-friendly name slug of hotel", alias="urlName")
    star_rating: Optional[Annotated[int, Field(le=6, strict=True, ge=0)]] = Field(default=None, description="Official or self-designated property star rating. Note that in some regions there are 6-star hotels. They are the same as 5-star hotels everywhere else.", alias="starRating")
    bookings: Optional[StrictInt] = Field(default=0, description="Number of bookings for this property on the wink.travel platform.")
    aggregate_review_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.0, description="Aggregate score based on all current user reviews.", alias="aggregateReviewRating")
    location: Optional[GeoJsonPointAgent] = None
    short_descriptions: Optional[List[LocalizedDescriptionAgent]] = Field(default=None, description="A localized list of short property descriptions", alias="shortDescriptions")
    long_descriptions: Optional[List[LocalizedDescriptionAgent]] = Field(default=None, description="A localized list of longer property descriptions", alias="longDescriptions")
    aggregate_greendex_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.0, description="Aggregate Green Index score if the property has answered our questionnaire available in the Extranet.", alias="aggregateGreendexRating")
    lifestyle_types: Optional[List[StrictStr]] = Field(default=None, alias="lifestyleTypes")
    total_reviews: Optional[StrictInt] = Field(default=0, description="Count of total reviews left by users at this property.", alias="totalReviews")
    available: Optional[StrictBool] = Field(default=False, description="Flag indicating whether the reactive has made this property available for sale.")
    hotel_available: Optional[StrictBool] = Field(default=False, description="Flag indicating whether the property has made this property available for sale.", alias="hotelAvailable")
    reservations: Optional[ContactAgent] = None
    socials: Optional[List[SocialAgent]] = Field(default=None, description="Property's social network accounts")
    images: Optional[List[SimpleMultimediaAgent]] = Field(default=None, description="Property images.")
    videos: Optional[List[SimpleMultimediaAgent]] = Field(default=None, description="Property videos.")
    policy: Optional[PropertyPolicyAgent] = None
    third_party_reviews: Optional[List[TravelInventoryRecognitionAgent]] = Field(default=None, description="Array of awards and third party reviews given to property by certified / non-certified providers.", alias="thirdPartyReviews")
    attractions: Optional[StrictInt] = Field(default=0, description="Number of attractions property has listed on its profile.")
    recreations: Optional[StrictInt] = Field(default=0, description="Number of activites property has listed on its profile.")
    pois: Optional[StrictInt] = Field(default=0, description="Number of places property has listed on its profile.")
    restaurants: Optional[StrictInt] = Field(default=0, description="Number of restaurants property has on its profile.")
    meeting_rooms: Optional[StrictInt] = Field(default=0, description="Number of meeting rooms property has on its profile.", alias="meetingRooms")
    spas: Optional[StrictInt] = Field(default=0, description="Number of spas property has on its profile.")
    add_ons: Optional[StrictInt] = Field(default=0, description="Number of add-ons property has on its profile.", alias="addOns")
    general_manager: Optional[GeneralManagerAgent] = Field(default=None, alias="generalManager")
    location_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `LOC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="locationCategory")
    segment_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `SEG` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="segmentCategory")
    hotel_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `PCT` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="hotelCategory")
    architectural_style: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `ARC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="architecturalStyle")
    when_built: Optional[StrictStr] = Field(default=None, description="Year the property was constructed.", alias="whenBuilt")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code for property.", alias="currencyCode")
    membership_rate_discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, description="A property's price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it's there to compare it against other properties.", alias="membershipRateDiscount")
    price_score: Optional[StrictInt] = Field(default=0, description="A property's price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it's there to compare it against other properties.", alias="priceScore")
    perk_score: Optional[StrictInt] = Field(default=0, description="A property's perk score is based on the type of perks that is offered to the guests across all master rates. There is no max score; it's there to compare it against other properties.", alias="perkScore")
    package_score: Optional[StrictInt] = Field(default=0, description="A property's package score is based on general availability and price for all packages and add-ons offered by the property. There is no max score; it's there to compare it against other properties.", alias="packageScore")
    loyalty_score: Optional[StrictInt] = Field(default=0, description="A property's loyalty score is based on calculating how many available rate plans honor loyalty points. There is no max score; it's there to compare it against other properties.", alias="loyaltyScore")
    popular_score: Optional[StrictInt] = Field(default=0, description="A property's popular score is based on calculating number of bookings across room types. There is no max score; it's there to compare it against other properties.", alias="popularScore")
    experience_score: Optional[StrictInt] = Field(default=0, description="A property's experience score is based on how calculating how many types of experiences are available and at what price ranges. There is no max score; it's there to compare it against other properties.", alias="experienceScore")
    availability_score: Optional[StrictInt] = Field(default=0, description="A property's availability score is based on general availability of all room types. If most room types are always unavailable, the attractiveness of this property goes down. We use this as our primary benchmark to decide how and when to feature properties. There is no max score; it's there to compare it against other properties.", alias="availabilityScore")
    hotel_amenity_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `HAC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="hotelAmenityCodes")
    property_accessibility_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `PHY` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="propertyAccessibilityCodes")
    property_security_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `SEC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="propertySecurityCodes")
    number_of_rooms: Optional[StrictInt] = Field(default=0, description="Number of rooms / keys for this property.", alias="numberOfRooms")
    address: Optional[AddressAgent] = None
    active: Optional[StrictBool] = Field(default=None, description="A property is considered active when both available and hotelAvailable flags are true.")
    url_parameters: Optional[StrictStr] = Field(default=None, description="Convenience data point that creates url friendly query parameters of property.", alias="urlParameters")
    __properties: ClassVar[List[str]] = ["identifier", "hotelIdentifier", "name", "localName", "chain", "brand", "urlName", "starRating", "bookings", "aggregateReviewRating", "location", "shortDescriptions", "longDescriptions", "aggregateGreendexRating", "lifestyleTypes", "totalReviews", "available", "hotelAvailable", "reservations", "socials", "images", "videos", "policy", "thirdPartyReviews", "attractions", "recreations", "pois", "restaurants", "meetingRooms", "spas", "addOns", "generalManager", "locationCategory", "segmentCategory", "hotelCategory", "architecturalStyle", "whenBuilt", "currencyCode", "membershipRateDiscount", "priceScore", "perkScore", "packageScore", "loyaltyScore", "popularScore", "experienceScore", "availabilityScore", "hotelAmenityCodes", "propertyAccessibilityCodes", "propertySecurityCodes", "numberOfRooms", "address", "active", "urlParameters"]

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
        """Create an instance of HotelOnMapAgent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in short_descriptions (list)
        _items = []
        if self.short_descriptions:
            for _item_short_descriptions in self.short_descriptions:
                if _item_short_descriptions:
                    _items.append(_item_short_descriptions.to_dict())
            _dict['shortDescriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in long_descriptions (list)
        _items = []
        if self.long_descriptions:
            for _item_long_descriptions in self.long_descriptions:
                if _item_long_descriptions:
                    _items.append(_item_long_descriptions.to_dict())
            _dict['longDescriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of reservations
        if self.reservations:
            _dict['reservations'] = self.reservations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in socials (list)
        _items = []
        if self.socials:
            for _item_socials in self.socials:
                if _item_socials:
                    _items.append(_item_socials.to_dict())
            _dict['socials'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in videos (list)
        _items = []
        if self.videos:
            for _item_videos in self.videos:
                if _item_videos:
                    _items.append(_item_videos.to_dict())
            _dict['videos'] = _items
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in third_party_reviews (list)
        _items = []
        if self.third_party_reviews:
            for _item_third_party_reviews in self.third_party_reviews:
                if _item_third_party_reviews:
                    _items.append(_item_third_party_reviews.to_dict())
            _dict['thirdPartyReviews'] = _items
        # override the default output from pydantic by calling `to_dict()` of general_manager
        if self.general_manager:
            _dict['generalManager'] = self.general_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HotelOnMapAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "hotelIdentifier": obj.get("hotelIdentifier"),
            "name": obj.get("name"),
            "localName": obj.get("localName"),
            "chain": obj.get("chain"),
            "brand": obj.get("brand"),
            "urlName": obj.get("urlName"),
            "starRating": obj.get("starRating"),
            "bookings": obj.get("bookings") if obj.get("bookings") is not None else 0,
            "aggregateReviewRating": obj.get("aggregateReviewRating") if obj.get("aggregateReviewRating") is not None else 0.0,
            "location": GeoJsonPointAgent.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "shortDescriptions": [LocalizedDescriptionAgent.from_dict(_item) for _item in obj["shortDescriptions"]] if obj.get("shortDescriptions") is not None else None,
            "longDescriptions": [LocalizedDescriptionAgent.from_dict(_item) for _item in obj["longDescriptions"]] if obj.get("longDescriptions") is not None else None,
            "aggregateGreendexRating": obj.get("aggregateGreendexRating") if obj.get("aggregateGreendexRating") is not None else 0.0,
            "lifestyleTypes": obj.get("lifestyleTypes"),
            "totalReviews": obj.get("totalReviews") if obj.get("totalReviews") is not None else 0,
            "available": obj.get("available") if obj.get("available") is not None else False,
            "hotelAvailable": obj.get("hotelAvailable") if obj.get("hotelAvailable") is not None else False,
            "reservations": ContactAgent.from_dict(obj["reservations"]) if obj.get("reservations") is not None else None,
            "socials": [SocialAgent.from_dict(_item) for _item in obj["socials"]] if obj.get("socials") is not None else None,
            "images": [SimpleMultimediaAgent.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "videos": [SimpleMultimediaAgent.from_dict(_item) for _item in obj["videos"]] if obj.get("videos") is not None else None,
            "policy": PropertyPolicyAgent.from_dict(obj["policy"]) if obj.get("policy") is not None else None,
            "thirdPartyReviews": [TravelInventoryRecognitionAgent.from_dict(_item) for _item in obj["thirdPartyReviews"]] if obj.get("thirdPartyReviews") is not None else None,
            "attractions": obj.get("attractions") if obj.get("attractions") is not None else 0,
            "recreations": obj.get("recreations") if obj.get("recreations") is not None else 0,
            "pois": obj.get("pois") if obj.get("pois") is not None else 0,
            "restaurants": obj.get("restaurants") if obj.get("restaurants") is not None else 0,
            "meetingRooms": obj.get("meetingRooms") if obj.get("meetingRooms") is not None else 0,
            "spas": obj.get("spas") if obj.get("spas") is not None else 0,
            "addOns": obj.get("addOns") if obj.get("addOns") is not None else 0,
            "generalManager": GeneralManagerAgent.from_dict(obj["generalManager"]) if obj.get("generalManager") is not None else None,
            "locationCategory": obj.get("locationCategory"),
            "segmentCategory": obj.get("segmentCategory"),
            "hotelCategory": obj.get("hotelCategory"),
            "architecturalStyle": obj.get("architecturalStyle"),
            "whenBuilt": obj.get("whenBuilt"),
            "currencyCode": obj.get("currencyCode"),
            "membershipRateDiscount": obj.get("membershipRateDiscount") if obj.get("membershipRateDiscount") is not None else 0,
            "priceScore": obj.get("priceScore") if obj.get("priceScore") is not None else 0,
            "perkScore": obj.get("perkScore") if obj.get("perkScore") is not None else 0,
            "packageScore": obj.get("packageScore") if obj.get("packageScore") is not None else 0,
            "loyaltyScore": obj.get("loyaltyScore") if obj.get("loyaltyScore") is not None else 0,
            "popularScore": obj.get("popularScore") if obj.get("popularScore") is not None else 0,
            "experienceScore": obj.get("experienceScore") if obj.get("experienceScore") is not None else 0,
            "availabilityScore": obj.get("availabilityScore") if obj.get("availabilityScore") is not None else 0,
            "hotelAmenityCodes": obj.get("hotelAmenityCodes"),
            "propertyAccessibilityCodes": obj.get("propertyAccessibilityCodes"),
            "propertySecurityCodes": obj.get("propertySecurityCodes"),
            "numberOfRooms": obj.get("numberOfRooms") if obj.get("numberOfRooms") is not None else 0,
            "address": AddressAgent.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "active": obj.get("active"),
            "urlParameters": obj.get("urlParameters")
        })
        return _obj


