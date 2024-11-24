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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wink_sdk_extranet_distribution.models.engine_configuration_theme_supplier_details import EngineConfigurationThemeSupplierDetails
from wink_sdk_extranet_distribution.models.geo_name_supplier_details import GeoNameSupplierDetails
from wink_sdk_extranet_distribution.models.room_configuration_supplier_details import RoomConfigurationSupplierDetails
from wink_sdk_extranet_distribution.models.simple_multimedia_supplier_details import SimpleMultimediaSupplierDetails
from typing import Optional, Set
from typing_extensions import Self

class EngineConfigurationBookingReportSupplierDetails(BaseModel):
    """
    Which engine configuration record did the entity application used to facilitate in making this booking happen.
    """ # noqa: E501
    identifier: StrictStr = Field(description="Unique engine configuration identifier")
    name: StrictStr = Field(description="Engine configuration name")
    user_identifier: StrictStr = Field(description="Authenticated user identifier", alias="userIdentifier")
    owner_identifier: StrictStr = Field(description="Engine configuration record creator identifier", alias="ownerIdentifier")
    owner_name: StrictStr = Field(description="Name of company owner.", alias="ownerName")
    sub_type: StrictStr = Field(description="Sales channel sub-type.", alias="subType")
    default_currency: Optional[StrictStr] = Field(default='USD', description="Control which currency your users see prices in initially.", alias="defaultCurrency")
    default_language: Optional[StrictStr] = Field(default='en', description="Control which language your users see text in initially.", alias="defaultLanguage")
    default_lifestyle: Optional[StrictStr] = Field(default=None, description="Control which lifestyle contextx your users see initially.", alias="defaultLifestyle")
    logos: Optional[List[SimpleMultimediaSupplierDetails]] = Field(default=None, description="Customize booking confirmation emails by adding a custom logo to your configuration.")
    hosted_booking_engine_url: Optional[StrictStr] = Field(default='https://ota.wink.travel', description="If you are self-hosting our booking engine, let us know where it is hosted. Note: This url needs to be secured with SSL.", alias="hostedBookingEngineUrl")
    self_hosted: Optional[StrictBool] = Field(default=False, description="Flag to indicate you are self-hosting our booking engine and not using our default booking engine url.", alias="selfHosted")
    theme_colors: Optional[EngineConfigurationThemeSupplierDetails] = Field(default=None, alias="themeColors")
    number_of_advance_days: Optional[StrictInt] = Field(default=None, description="You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long and how many days in advance (this field), of today's date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don't use either of these options, the itinerary will default to today's date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave `startDate` and `endDate` empty.", alias="numberOfAdvanceDays")
    number_of_stay_days: Optional[StrictInt] = Field(default=None, description="You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long (this field) and how many days in advance, of today's date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don't use either of these options, the itinerary will default to today's date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave `startDate` and `endDate` empty.", alias="numberOfStayDays")
    start_date: Optional[date] = Field(default=None, description="Set a fixed itinerary start date. ONLY populate this field if you want to fix the itinerary date. Also, leave `numberOfAdvanceDays` and `numberOfStayDays` empty.", alias="startDate")
    end_date: Optional[date] = Field(default=None, description="Set a fixed itinerary end date ONLY populate this field if you want to fix the itinerary date. Also, leave `numberOfAdvanceDays` and `numberOfStayDays` empty.", alias="endDate")
    room_configurations: Optional[List[RoomConfigurationSupplierDetails]] = Field(default=None, description="Control how many adults / children will be staying and how many rooms. Defaults to: One room, two adults.", alias="roomConfigurations")
    use_days: Optional[StrictBool] = Field(default=None, description="if true, we use numberOfAdvanceDays / numberOfStayDays properties - false, we use startDate / endDate", alias="useDays")
    promotional_codes: Optional[List[StrictStr]] = Field(default=None, description="If you've received special promotional codes from suppliers to give to your audience, you can choose to bake these code directly into the price by entering them here.", alias="promotionalCodes")
    send_booking_notification_emails_to_property: Optional[StrictBool] = Field(default=True, description="An integrator can choose to disable outgoing emails to properties because they want to do that themselves.", alias="sendBookingNotificationEmailsToProperty")
    send_booking_notification_emails_to_booker: Optional[StrictBool] = Field(default=True, description="An integrator can choose to disable outgoing emails to users because they want to do that themselves.", alias="sendBookingNotificationEmailsToBooker")
    send_booking_notification_emails_to_channel_manager: Optional[StrictBool] = Field(default=True, description="An integrator can choose to disable notifying the property's channel manager. Note: This should ONLY be done for testing.", alias="sendBookingNotificationEmailsToChannelManager")
    wc_book_click_action: Optional[StrictStr] = Field(default=None, description="Action to complete once a user clicks on the CTA button on blocking.", alias="wcBookClickAction")
    city: Optional[GeoNameSupplierDetails] = None
    show_unavailable_card: Optional[StrictBool] = Field(default=None, description="Show unavailable blocking card when blocking not currently for sale. Otherwise, it displays a normal card but without the price.", alias="showUnavailableCard")
    show_rankings: Optional[StrictBool] = Field(default=None, description="Whether to display rankings (lifestyle, eco score and reviews) on hotel landing page.", alias="showRankings")
    __properties: ClassVar[List[str]] = ["identifier", "name", "userIdentifier", "ownerIdentifier", "ownerName", "subType", "defaultCurrency", "defaultLanguage", "defaultLifestyle", "logos", "hostedBookingEngineUrl", "selfHosted", "themeColors", "numberOfAdvanceDays", "numberOfStayDays", "startDate", "endDate", "roomConfigurations", "useDays", "promotionalCodes", "sendBookingNotificationEmailsToProperty", "sendBookingNotificationEmailsToBooker", "sendBookingNotificationEmailsToChannelManager", "wcBookClickAction", "city", "showUnavailableCard", "showRankings"]

    @field_validator('sub_type')
    def sub_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER']):
            raise ValueError("must be one of enum values ('DIRECT', 'APPLICATION', 'HOTEL', 'TRAVELIKO', 'CORPORATE', 'TRAVEL_AGENT', 'INFLUENCER', 'BLOGGER', 'DESTINATION', 'CHANNEL_MANAGER', 'PROPERTY_MANAGEMENT_SYSTEM', 'CENTRAL_RESERVATION_SYSTEM', 'GOOGLE_HOTEL_API', 'MANAGEMENT_COMPANY', 'CHAIN', 'BRAND', 'EVENT_ORGANIZER')")
        return value

    @field_validator('default_lifestyle')
    def default_lifestyle_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO']):
            raise ValueError("must be one of enum values ('LIFESTYLE_HEALTH_FITNESS', 'LIFESTYLE_RELAX', 'LIFESTYLE_ADULT_ONLY', 'LIFESTYLE_ADVENTURE', 'LIFESTYLE_BUSINESS', 'LIFESTYLE_LGBT', 'LIFESTYLE_SINGLE_PARENT', 'LIFESTYLE_SOLO_FEMALE', 'LIFESTYLE_BEAUTY', 'LIFESTYLE_FOODIE', 'LIFESTYLE_FAMILY', 'LIFESTYLE_ROMANCE', 'LIFESTYLE_COUPLE', 'LIFESTYLE_SOLO', 'LIFESTYLE_BACKPACKER', 'LIFESTYLE_SHOPPING', 'LIFESTYLE_SPORTS', 'LIFESTYLE_MOUNTAIN', 'LIFESTYLE_BEACH', 'LIFESTYLE_CITY', 'LIFESTYLE_COUNTRY', 'LIFESTYLE_CULTURE', 'LIFESTYLE_ECO')")
        return value

    @field_validator('wc_book_click_action')
    def wc_book_click_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FORWARD_TO_IBE', 'IBE_MODAL']):
            raise ValueError("must be one of enum values ('FORWARD_TO_IBE', 'IBE_MODAL')")
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
        """Create an instance of EngineConfigurationBookingReportSupplierDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in logos (list)
        _items = []
        if self.logos:
            for _item_logos in self.logos:
                if _item_logos:
                    _items.append(_item_logos.to_dict())
            _dict['logos'] = _items
        # override the default output from pydantic by calling `to_dict()` of theme_colors
        if self.theme_colors:
            _dict['themeColors'] = self.theme_colors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in room_configurations (list)
        _items = []
        if self.room_configurations:
            for _item_room_configurations in self.room_configurations:
                if _item_room_configurations:
                    _items.append(_item_room_configurations.to_dict())
            _dict['roomConfigurations'] = _items
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict['city'] = self.city.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EngineConfigurationBookingReportSupplierDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "name": obj.get("name"),
            "userIdentifier": obj.get("userIdentifier"),
            "ownerIdentifier": obj.get("ownerIdentifier"),
            "ownerName": obj.get("ownerName"),
            "subType": obj.get("subType"),
            "defaultCurrency": obj.get("defaultCurrency") if obj.get("defaultCurrency") is not None else 'USD',
            "defaultLanguage": obj.get("defaultLanguage") if obj.get("defaultLanguage") is not None else 'en',
            "defaultLifestyle": obj.get("defaultLifestyle"),
            "logos": [SimpleMultimediaSupplierDetails.from_dict(_item) for _item in obj["logos"]] if obj.get("logos") is not None else None,
            "hostedBookingEngineUrl": obj.get("hostedBookingEngineUrl") if obj.get("hostedBookingEngineUrl") is not None else 'https://ota.wink.travel',
            "selfHosted": obj.get("selfHosted") if obj.get("selfHosted") is not None else False,
            "themeColors": EngineConfigurationThemeSupplierDetails.from_dict(obj["themeColors"]) if obj.get("themeColors") is not None else None,
            "numberOfAdvanceDays": obj.get("numberOfAdvanceDays"),
            "numberOfStayDays": obj.get("numberOfStayDays"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "roomConfigurations": [RoomConfigurationSupplierDetails.from_dict(_item) for _item in obj["roomConfigurations"]] if obj.get("roomConfigurations") is not None else None,
            "useDays": obj.get("useDays"),
            "promotionalCodes": obj.get("promotionalCodes"),
            "sendBookingNotificationEmailsToProperty": obj.get("sendBookingNotificationEmailsToProperty") if obj.get("sendBookingNotificationEmailsToProperty") is not None else True,
            "sendBookingNotificationEmailsToBooker": obj.get("sendBookingNotificationEmailsToBooker") if obj.get("sendBookingNotificationEmailsToBooker") is not None else True,
            "sendBookingNotificationEmailsToChannelManager": obj.get("sendBookingNotificationEmailsToChannelManager") if obj.get("sendBookingNotificationEmailsToChannelManager") is not None else True,
            "wcBookClickAction": obj.get("wcBookClickAction"),
            "city": GeoNameSupplierDetails.from_dict(obj["city"]) if obj.get("city") is not None else None,
            "showUnavailableCard": obj.get("showUnavailableCard"),
            "showRankings": obj.get("showRankings")
        })
        return _obj


