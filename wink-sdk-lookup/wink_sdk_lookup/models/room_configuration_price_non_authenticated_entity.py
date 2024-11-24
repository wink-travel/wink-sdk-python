# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Lookup API The Lookup API exposes endpoints to search for blocking by region, type. It's the entryway to bookable blocking when you don't yet know what you are looking for.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from wink_sdk_lookup.models.add_on_localized_inventory_non_authenticated_entity import AddOnLocalizedInventoryNonAuthenticatedEntity
from wink_sdk_lookup.models.cancellation_policy_non_authenticated_entity import CancellationPolicyNonAuthenticatedEntity
from wink_sdk_lookup.models.custom_monetary_amount import CustomMonetaryAmount
from wink_sdk_lookup.models.extra_charges_non_authenticated_entity import ExtraChargesNonAuthenticatedEntity
from wink_sdk_lookup.models.localized_transactional_travel_inventory_non_authenticated_entity import LocalizedTransactionalTravelInventoryNonAuthenticatedEntity
from wink_sdk_lookup.models.rate_plan_non_authenticated_entity import RatePlanNonAuthenticatedEntity
from wink_sdk_lookup.models.room_configuration_non_authenticated_entity import RoomConfigurationNonAuthenticatedEntity
from wink_sdk_lookup.models.stay_rate_non_authenticated_entity import StayRateNonAuthenticatedEntity
from typing import Optional, Set
from typing_extensions import Self

class RoomConfigurationPriceNonAuthenticatedEntity(BaseModel):
    """
    RoomConfigurationPriceNonAuthenticatedEntity
    """ # noqa: E501
    adults: StrictInt = Field(description="The actual amount of adults as determined by the hotel's policy")
    children: Optional[StrictInt] = Field(default=None, description="The actual amount of children as determined by the hotel's policy")
    start_date: date = Field(description="SimpleDateTimeItinerary startDate", alias="startDate")
    end_date: date = Field(description="SimpleDateTimeItinerary endDate", alias="endDate")
    room_rate_identifier: StrictStr = Field(description="Specified master rate identifier", alias="roomRateIdentifier")
    room_rate_internal_name: StrictStr = Field(description="Specified master rate internal name", alias="roomRateInternalName")
    rate_plan: RatePlanNonAuthenticatedEntity = Field(alias="ratePlan")
    perk_types: Optional[List[StrictStr]] = Field(default=None, alias="perkTypes")
    price: StayRateNonAuthenticatedEntity
    extra_charges: Optional[ExtraChargesNonAuthenticatedEntity] = Field(default=None, alias="extraCharges")
    configuration: RoomConfigurationNonAuthenticatedEntity
    add_on_offers: Optional[List[AddOnLocalizedInventoryNonAuthenticatedEntity]] = Field(default=None, alias="addOnOffers")
    perk_value: Optional[StrictInt] = Field(default=None, description="The combined value of these perks", alias="perkValue")
    active_cancellation_policy: CancellationPolicyNonAuthenticatedEntity = Field(alias="activeCancellationPolicy")
    room_nights: StrictInt = Field(description="Number of nights the guests will be staying", alias="roomNights")
    list: Optional[List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]] = None
    channel_inventory_identifier: StrictStr = Field(description="Sales channel inventory identifier", alias="channelInventoryIdentifier")
    commissionable: StrictBool = Field(description="Whether this package is commissionable based on the incoming sales channel.")
    commission: Union[StrictFloat, StrictInt] = Field(description="The commission percentage.")
    direct: StrictBool = Field(description="Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking.")
    price_list: Optional[List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]] = Field(default=None, alias="priceList")
    rate_source: Optional[StrictStr] = Field(default=None, alias="rateSource")
    user_specified_currency_total: Optional[CustomMonetaryAmount] = Field(default=None, alias="userSpecifiedCurrencyTotal")
    internal_total: Optional[CustomMonetaryAmount] = Field(default=None, alias="internalTotal")
    source_total: Optional[CustomMonetaryAmount] = Field(default=None, alias="sourceTotal")
    available: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["adults", "children", "startDate", "endDate", "roomRateIdentifier", "roomRateInternalName", "ratePlan", "perkTypes", "price", "extraCharges", "configuration", "addOnOffers", "perkValue", "activeCancellationPolicy", "roomNights", "list", "channelInventoryIdentifier", "commissionable", "commission", "direct", "priceList", "rateSource", "userSpecifiedCurrencyTotal", "internalTotal", "sourceTotal", "available"]

    @field_validator('perk_types')
    def perk_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PERK_LOYALTY_POINTS', 'PERK_WINE', 'PERK_FREE_DRINK_VOUCHER', 'PERK_FREE_MEAL_TWO_PEOPLE', 'PERK_FREE_LUNCH_TWO_PEOPLE', 'PERK_FREE_ONE_HOUR_MASSAGE', 'PERK_FREE_ONE_HOUR_MASSAGE_TWO_PAX', 'PERK_TWENTY_PERCENT_FOOD_BEVERAGE_DISCOUNT', 'PERK_TEN_PERCENT_FOOD_BEVERAGE_DISCOUNT', 'PERK_TWENTY_PERCENT_SPA_DISCOUNT_VOUCHER', 'PERK_TEN_PERCENT_SPA_DISCOUNT_VOUCHER', 'PERK_GUARANTEED_UPGRADE', 'PERK_EARLY_CHECKIN', 'PERK_ROOM_UPGRADE', 'PERK_LATE_CHECKOUT', 'PERK_AIRPORT_TRANSFER', 'PERK_AIRPORT_PICK_UP', 'PERK_BOTTLE_CHAMPAGNE_ON_ARRIVAL', 'PERK_BOTTLE_SPARKLING_WINE_ON_ARRIVAL', 'PERK_BOTTLE_WINE_ON_ARRIVAL', 'PERK_HOTEL_CREDIT_FIVE', 'PERK_HOTEL_CREDIT_TEN', 'PERK_HOTEL_CREDIT_TWELVE', 'PERK_HOTEL_CREDIT_FIFTEEN', 'PERK_HOTEL_CREDIT_TWENTY', 'PERK_HOTEL_CREDIT_TWENTY_FIVE', 'PERK_SPA_CREDIT_FIVE', 'PERK_SPA_CREDIT_TEN', 'PERK_SPA_CREDIT_FIFTEEN', 'PERK_SPA_CREDIT_TWENTY', 'PERK_SPA_CREDIT_TWENTY_FIVE', 'PERK_AFTERNOON_TEA_SET', 'PERK_MEAL_VOUCHER_FIFTEEN', 'PERK_LOUNGE_ACCESS', 'PERK_SHUTTLE_BUS']):
                raise ValueError("each list item must be one of ('PERK_LOYALTY_POINTS', 'PERK_WINE', 'PERK_FREE_DRINK_VOUCHER', 'PERK_FREE_MEAL_TWO_PEOPLE', 'PERK_FREE_LUNCH_TWO_PEOPLE', 'PERK_FREE_ONE_HOUR_MASSAGE', 'PERK_FREE_ONE_HOUR_MASSAGE_TWO_PAX', 'PERK_TWENTY_PERCENT_FOOD_BEVERAGE_DISCOUNT', 'PERK_TEN_PERCENT_FOOD_BEVERAGE_DISCOUNT', 'PERK_TWENTY_PERCENT_SPA_DISCOUNT_VOUCHER', 'PERK_TEN_PERCENT_SPA_DISCOUNT_VOUCHER', 'PERK_GUARANTEED_UPGRADE', 'PERK_EARLY_CHECKIN', 'PERK_ROOM_UPGRADE', 'PERK_LATE_CHECKOUT', 'PERK_AIRPORT_TRANSFER', 'PERK_AIRPORT_PICK_UP', 'PERK_BOTTLE_CHAMPAGNE_ON_ARRIVAL', 'PERK_BOTTLE_SPARKLING_WINE_ON_ARRIVAL', 'PERK_BOTTLE_WINE_ON_ARRIVAL', 'PERK_HOTEL_CREDIT_FIVE', 'PERK_HOTEL_CREDIT_TEN', 'PERK_HOTEL_CREDIT_TWELVE', 'PERK_HOTEL_CREDIT_FIFTEEN', 'PERK_HOTEL_CREDIT_TWENTY', 'PERK_HOTEL_CREDIT_TWENTY_FIVE', 'PERK_SPA_CREDIT_FIVE', 'PERK_SPA_CREDIT_TEN', 'PERK_SPA_CREDIT_FIFTEEN', 'PERK_SPA_CREDIT_TWENTY', 'PERK_SPA_CREDIT_TWENTY_FIVE', 'PERK_AFTERNOON_TEA_SET', 'PERK_MEAL_VOUCHER_FIFTEEN', 'PERK_LOUNGE_ACCESS', 'PERK_SHUTTLE_BUS')")
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
        """Create an instance of RoomConfigurationPriceNonAuthenticatedEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rate_plan
        if self.rate_plan:
            _dict['ratePlan'] = self.rate_plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra_charges
        if self.extra_charges:
            _dict['extraCharges'] = self.extra_charges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in add_on_offers (list)
        _items = []
        if self.add_on_offers:
            for _item_add_on_offers in self.add_on_offers:
                if _item_add_on_offers:
                    _items.append(_item_add_on_offers.to_dict())
            _dict['addOnOffers'] = _items
        # override the default output from pydantic by calling `to_dict()` of active_cancellation_policy
        if self.active_cancellation_policy:
            _dict['activeCancellationPolicy'] = self.active_cancellation_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in list (list)
        _items = []
        if self.list:
            for _item_list in self.list:
                if _item_list:
                    _items.append(_item_list.to_dict())
            _dict['list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in price_list (list)
        _items = []
        if self.price_list:
            for _item_price_list in self.price_list:
                if _item_price_list:
                    _items.append(_item_price_list.to_dict())
            _dict['priceList'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_specified_currency_total
        if self.user_specified_currency_total:
            _dict['userSpecifiedCurrencyTotal'] = self.user_specified_currency_total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal_total
        if self.internal_total:
            _dict['internalTotal'] = self.internal_total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_total
        if self.source_total:
            _dict['sourceTotal'] = self.source_total.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomConfigurationPriceNonAuthenticatedEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "roomRateIdentifier": obj.get("roomRateIdentifier"),
            "roomRateInternalName": obj.get("roomRateInternalName"),
            "ratePlan": RatePlanNonAuthenticatedEntity.from_dict(obj["ratePlan"]) if obj.get("ratePlan") is not None else None,
            "perkTypes": obj.get("perkTypes"),
            "price": StayRateNonAuthenticatedEntity.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "extraCharges": ExtraChargesNonAuthenticatedEntity.from_dict(obj["extraCharges"]) if obj.get("extraCharges") is not None else None,
            "configuration": RoomConfigurationNonAuthenticatedEntity.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "addOnOffers": [AddOnLocalizedInventoryNonAuthenticatedEntity.from_dict(_item) for _item in obj["addOnOffers"]] if obj.get("addOnOffers") is not None else None,
            "perkValue": obj.get("perkValue"),
            "activeCancellationPolicy": CancellationPolicyNonAuthenticatedEntity.from_dict(obj["activeCancellationPolicy"]) if obj.get("activeCancellationPolicy") is not None else None,
            "roomNights": obj.get("roomNights"),
            "list": [LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.from_dict(_item) for _item in obj["list"]] if obj.get("list") is not None else None,
            "channelInventoryIdentifier": obj.get("channelInventoryIdentifier"),
            "commissionable": obj.get("commissionable"),
            "commission": obj.get("commission"),
            "direct": obj.get("direct") if obj.get("direct") is not None else False,
            "priceList": [LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.from_dict(_item) for _item in obj["priceList"]] if obj.get("priceList") is not None else None,
            "rateSource": obj.get("rateSource"),
            "userSpecifiedCurrencyTotal": CustomMonetaryAmount.from_dict(obj["userSpecifiedCurrencyTotal"]) if obj.get("userSpecifiedCurrencyTotal") is not None else None,
            "internalTotal": CustomMonetaryAmount.from_dict(obj["internalTotal"]) if obj.get("internalTotal") is not None else None,
            "sourceTotal": CustomMonetaryAmount.from_dict(obj["sourceTotal"]) if obj.get("sourceTotal") is not None else None,
            "available": obj.get("available")
        })
        return _obj


