# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Sales Channel API The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. This API lets you:  1. Sales Channel: Manage existing sales channels. 2. Relationship Request: Manage relationship requests. 3. Available Supplier: Browse available suppliers to connect with.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.17.14
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wink_sdk_affiliate_sales_channel.models.contact_affiliate import ContactAffiliate
from wink_sdk_affiliate_sales_channel.models.general_manager_affiliate import GeneralManagerAffiliate
from wink_sdk_affiliate_sales_channel.models.geo_json_point_affiliate import GeoJsonPointAffiliate
from wink_sdk_affiliate_sales_channel.models.property_policy_affiliate import PropertyPolicyAffiliate
from wink_sdk_affiliate_sales_channel.models.simple_address_affiliate import SimpleAddressAffiliate
from wink_sdk_affiliate_sales_channel.models.simple_description_affiliate import SimpleDescriptionAffiliate
from wink_sdk_affiliate_sales_channel.models.simple_multimedia_affiliate import SimpleMultimediaAffiliate
from wink_sdk_affiliate_sales_channel.models.social_affiliate import SocialAffiliate
from wink_sdk_affiliate_sales_channel.models.travel_inventory_recognition_affiliate import TravelInventoryRecognitionAffiliate
from typing import Optional, Set
from typing_extensions import Self

class PropertyAggregateLightweightAffiliate(BaseModel):
    """
    PropertyAggregateLightweightAffiliate
    """ # noqa: E501
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="Unique hotel record identifier.", alias="hotelIdentifier")
    name: Optional[StrictStr] = Field(default=None, description="Hotel trade name")
    local_name: Optional[StrictStr] = Field(default=None, description="Hotel local name if different from the trade name or if it is the local language.", alias="localName")
    chain: Optional[StrictStr] = Field(default=None, description="Name of hotel chain if applicable.")
    brand: Optional[StrictStr] = Field(default=None, description="Name of hotel brand")
    url_name: Optional[StrictStr] = Field(default=None, description="Unique URL-friendly name slug of hotel", alias="urlName")
    star_rating: Optional[Annotated[int, Field(le=6, strict=True, ge=0)]] = Field(default=None, description="Official or self-designated property star rating. Note that in some regions there are 6-star hotels. They are the same as 5-star hotels everywhere else.", alias="starRating")
    bookings: Optional[StrictInt] = Field(default=0, description="Number of bookings for this property on the wink.travel platform.")
    aggregate_review_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.0, description="Aggregate score based on all current user reviews.", alias="aggregateReviewRating")
    location: Optional[GeoJsonPointAffiliate] = Field(default=None, description="Geo-location")
    descriptions: Optional[List[SimpleDescriptionAffiliate]] = Field(default=None, description="Short and long welcome text")
    aggregate_greendex_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=0.0, description="Aggregate Green Index score if the property has answered our questionnaire available in the Extranet.", alias="aggregateGreendexRating")
    lifestyle_types: Optional[List[Any]] = Field(default=None, alias="lifestyleTypes")
    total_reviews: Optional[StrictInt] = Field(default=0, description="Count of total reviews left by users at this property.", alias="totalReviews")
    reservations: Optional[ContactAffiliate] = Field(default=None, description="Contact details for reservations desk")
    socials: Optional[List[SocialAffiliate]] = Field(default=None, description="Property's social network accounts")
    images: Optional[List[SimpleMultimediaAffiliate]] = Field(default=None, description="Property images.")
    videos: Optional[List[SimpleMultimediaAffiliate]] = Field(default=None, description="Property videos.")
    policy: Optional[PropertyPolicyAffiliate] = Field(default=None, description="Basic property policy record.")
    third_party_reviews: Optional[List[TravelInventoryRecognitionAffiliate]] = Field(default=None, description="Array of awards and third party reviews given to property by certified / non-certified providers.", alias="thirdPartyReviews")
    attractions: Optional[StrictInt] = Field(default=0, description="Number of attractions property has listed on its profile.")
    activities: Optional[StrictInt] = Field(default=0, description="Number of activites property has listed on its profile.")
    places: Optional[StrictInt] = Field(default=0, description="Number of places property has listed on its profile.")
    restaurants: Optional[StrictInt] = Field(default=0, description="Number of restaurants property has on its profile.")
    meeting_rooms: Optional[StrictInt] = Field(default=0, description="Number of meeting rooms property has on its profile.", alias="meetingRooms")
    spas: Optional[StrictInt] = Field(default=0, description="Number of spas property has on its profile.")
    add_ons: Optional[StrictInt] = Field(default=0, description="Number of add-ons property has on its profile.", alias="addOns")
    general_manager: Optional[GeneralManagerAffiliate] = Field(default=None, alias="generalManager")
    location_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `LOC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="locationCategory")
    segment_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `SEG` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="segmentCategory")
    hotel_category: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `PCT` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="hotelCategory")
    architectural_style: Optional[StrictStr] = Field(default=None, description="Supported OTA specification `ARC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="architecturalStyle")
    when_built: Optional[StrictStr] = Field(default=None, description="Year the property was constructed.", alias="whenBuilt")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code for property.", alias="currencyCode")
    membership_rate_discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, description="A property's price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it's there to compare it against other properties.", alias="membershipRateDiscount")
    price_score: Optional[StrictInt] = Field(default=0, description="A property's price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it's there to compare it against other properties.", alias="priceScore")
    perk_score: Optional[StrictInt] = Field(default=0, description="A property's perk score is based on the type of perks that is offered to the guests across all master rates. There is no max score; it's there to compare it against other properties.", alias="perkScore")
    add_on_score: Optional[StrictInt] = Field(default=0, description="A property's package score is based on general availability and price for all packages and add-ons offered by the property. There is no max score; it's there to compare it against other properties.", alias="addOnScore")
    loyalty_score: Optional[StrictInt] = Field(default=0, description="A property's loyalty score is based on calculating how many available rate plans honor loyalty points. There is no max score; it's there to compare it against other properties.", alias="loyaltyScore")
    popular_score: Optional[StrictInt] = Field(default=0, description="A property's popular score is based on calculating number of bookings across room types. There is no max score; it's there to compare it against other properties.", alias="popularScore")
    experience_score: Optional[StrictInt] = Field(default=0, description="A property's experience score is based on how calculating how many types of experiences are available and at what price ranges. There is no max score; it's there to compare it against other properties.", alias="experienceScore")
    hotel_amenity_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `HAC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="hotelAmenityCodes")
    property_accessibility_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `PHY` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="propertyAccessibilityCodes")
    property_security_codes: Optional[List[StrictStr]] = Field(default=None, description="Supported OTA specification `SEC` code. See [OTA geoname data](#operation/showAvailableCodesForCategory)", alias="propertySecurityCodes")
    number_of_rooms: Optional[StrictInt] = Field(default=0, description="Number of rooms / keys for this property.", alias="numberOfRooms")
    address: Optional[SimpleAddressAffiliate] = Field(default=None, description="Property address.")
    active: Optional[StrictBool] = Field(default=None, description="Whether property is active")
    url_parameters: Optional[StrictStr] = Field(default=None, description="Convenience data point that creates url friendly query parameters of property.", alias="urlParameters")
    __properties: ClassVar[List[str]] = ["hotelIdentifier", "name", "localName", "chain", "brand", "urlName", "starRating", "bookings", "aggregateReviewRating", "location", "descriptions", "aggregateGreendexRating", "lifestyleTypes", "totalReviews", "reservations", "socials", "images", "videos", "policy", "thirdPartyReviews", "attractions", "activities", "places", "restaurants", "meetingRooms", "spas", "addOns", "generalManager", "locationCategory", "segmentCategory", "hotelCategory", "architecturalStyle", "whenBuilt", "currencyCode", "membershipRateDiscount", "priceScore", "perkScore", "addOnScore", "loyaltyScore", "popularScore", "experienceScore", "hotelAmenityCodes", "propertyAccessibilityCodes", "propertySecurityCodes", "numberOfRooms", "address", "active", "urlParameters"]

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
        """Create an instance of PropertyAggregateLightweightAffiliate from a JSON string"""
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
        """Create an instance of PropertyAggregateLightweightAffiliate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hotelIdentifier": obj.get("hotelIdentifier"),
            "name": obj.get("name"),
            "localName": obj.get("localName"),
            "chain": obj.get("chain"),
            "brand": obj.get("brand"),
            "urlName": obj.get("urlName"),
            "starRating": obj.get("starRating"),
            "bookings": obj.get("bookings") if obj.get("bookings") is not None else 0,
            "aggregateReviewRating": obj.get("aggregateReviewRating") if obj.get("aggregateReviewRating") is not None else 0.0,
            "location": GeoJsonPointAffiliate.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "descriptions": [SimpleDescriptionAffiliate.from_dict(_item) for _item in obj["descriptions"]] if obj.get("descriptions") is not None else None,
            "aggregateGreendexRating": obj.get("aggregateGreendexRating") if obj.get("aggregateGreendexRating") is not None else 0.0,
            "lifestyleTypes": obj.get("lifestyleTypes"),
            "totalReviews": obj.get("totalReviews") if obj.get("totalReviews") is not None else 0,
            "reservations": ContactAffiliate.from_dict(obj["reservations"]) if obj.get("reservations") is not None else None,
            "socials": [SocialAffiliate.from_dict(_item) for _item in obj["socials"]] if obj.get("socials") is not None else None,
            "images": [SimpleMultimediaAffiliate.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "videos": [SimpleMultimediaAffiliate.from_dict(_item) for _item in obj["videos"]] if obj.get("videos") is not None else None,
            "policy": PropertyPolicyAffiliate.from_dict(obj["policy"]) if obj.get("policy") is not None else None,
            "thirdPartyReviews": [TravelInventoryRecognitionAffiliate.from_dict(_item) for _item in obj["thirdPartyReviews"]] if obj.get("thirdPartyReviews") is not None else None,
            "attractions": obj.get("attractions") if obj.get("attractions") is not None else 0,
            "activities": obj.get("activities") if obj.get("activities") is not None else 0,
            "places": obj.get("places") if obj.get("places") is not None else 0,
            "restaurants": obj.get("restaurants") if obj.get("restaurants") is not None else 0,
            "meetingRooms": obj.get("meetingRooms") if obj.get("meetingRooms") is not None else 0,
            "spas": obj.get("spas") if obj.get("spas") is not None else 0,
            "addOns": obj.get("addOns") if obj.get("addOns") is not None else 0,
            "generalManager": GeneralManagerAffiliate.from_dict(obj["generalManager"]) if obj.get("generalManager") is not None else None,
            "locationCategory": obj.get("locationCategory"),
            "segmentCategory": obj.get("segmentCategory"),
            "hotelCategory": obj.get("hotelCategory"),
            "architecturalStyle": obj.get("architecturalStyle"),
            "whenBuilt": obj.get("whenBuilt"),
            "currencyCode": obj.get("currencyCode"),
            "membershipRateDiscount": obj.get("membershipRateDiscount") if obj.get("membershipRateDiscount") is not None else 0,
            "priceScore": obj.get("priceScore") if obj.get("priceScore") is not None else 0,
            "perkScore": obj.get("perkScore") if obj.get("perkScore") is not None else 0,
            "addOnScore": obj.get("addOnScore") if obj.get("addOnScore") is not None else 0,
            "loyaltyScore": obj.get("loyaltyScore") if obj.get("loyaltyScore") is not None else 0,
            "popularScore": obj.get("popularScore") if obj.get("popularScore") is not None else 0,
            "experienceScore": obj.get("experienceScore") if obj.get("experienceScore") is not None else 0,
            "hotelAmenityCodes": obj.get("hotelAmenityCodes"),
            "propertyAccessibilityCodes": obj.get("propertyAccessibilityCodes"),
            "propertySecurityCodes": obj.get("propertySecurityCodes"),
            "numberOfRooms": obj.get("numberOfRooms") if obj.get("numberOfRooms") is not None else 0,
            "address": SimpleAddressAffiliate.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "active": obj.get("active"),
            "urlParameters": obj.get("urlParameters")
        })
        return _obj


