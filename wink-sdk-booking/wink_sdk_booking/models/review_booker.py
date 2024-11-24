# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Booking Engine API Welcome to the Booking Engine API - A programmer-friendly way to book blocking that was found on our platform. This API lets you:  1. Shopping Cart: Manage shopping cart. 2. Checkout: Move shopping cart items through the reactive workflow. 3. Booking: Move selected blocking through to booking completion. 4. Review: Leave a review after a completed stay.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wink_sdk_booking.models.review_answer_booker import ReviewAnswerBooker
from wink_sdk_booking.models.review_user_booker import ReviewUserBooker
from typing import Optional, Set
from typing_extensions import Self

class ReviewBooker(BaseModel):
    """
    User review created by the traveler after the booking completed.
    """ # noqa: E501
    identifier: Optional[StrictStr] = Field(default=None, description="Unique review identifier identifying this record.")
    booking_identifier: Optional[StrictStr] = Field(default=None, description="Booking identifier identifier booking this review is associated with.", alias="bookingIdentifier")
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="Hotel identifier this booking is associated with.", alias="hotelIdentifier")
    user: Optional[ReviewUserBooker] = None
    review_date: Optional[datetime] = Field(default=None, description="Date of review.", alias="reviewDate")
    average_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total points divided by number of questions.", alias="averageScore")
    answers: Optional[List[ReviewAnswerBooker]] = Field(default=None, description="List of user review answers.")
    message_from_guest: Optional[StrictStr] = Field(default=None, description="Private message from guest to the hotel. Is not displayed on property profile.", alias="messageFromGuest")
    response_from_hotel: Optional[StrictStr] = Field(default=None, description="Property can response to traveler review. Response goes on public review profile and can be seen by others.", alias="responseFromHotel")
    image_identifier: Optional[StrictStr] = Field(default=None, description="Reviewer can upload her best picture from the property. Cloudinary image identifier.", alias="imageIdentifier")
    text: Optional[StrictStr] = Field(default=None, description="Free text record created by traveler")
    approved_text: Optional[StrictBool] = Field(default=None, description="Hotel allows the review text to be displayed as part of their profile.", alias="approvedText")
    approved_image: Optional[StrictBool] = Field(default=None, description="Hotel allows the user-generated image to be displayed as part of their profile.", alias="approvedImage")
    likes: Optional[List[StrictStr]] = Field(default=None, description="List of member identifiers who liked the textual review")
    room_number: Optional[StrictStr] = Field(default=None, description="Guest's room number during their stay.", alias="roomNumber")
    room_rating: Optional[StrictInt] = Field(default=None, description="Guest's room rating", alias="roomRating")
    responded: Optional[StrictBool] = Field(default=False, description="Returns true if property has responded to the review given by the guest.")
    __properties: ClassVar[List[str]] = ["identifier", "bookingIdentifier", "hotelIdentifier", "user", "reviewDate", "averageScore", "answers", "messageFromGuest", "responseFromHotel", "imageIdentifier", "text", "approvedText", "approvedImage", "likes", "roomNumber", "roomRating", "responded"]

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
        """Create an instance of ReviewBooker from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in answers (list)
        _items = []
        if self.answers:
            for _item_answers in self.answers:
                if _item_answers:
                    _items.append(_item_answers.to_dict())
            _dict['answers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReviewBooker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "bookingIdentifier": obj.get("bookingIdentifier"),
            "hotelIdentifier": obj.get("hotelIdentifier"),
            "user": ReviewUserBooker.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "reviewDate": obj.get("reviewDate"),
            "averageScore": obj.get("averageScore"),
            "answers": [ReviewAnswerBooker.from_dict(_item) for _item in obj["answers"]] if obj.get("answers") is not None else None,
            "messageFromGuest": obj.get("messageFromGuest"),
            "responseFromHotel": obj.get("responseFromHotel"),
            "imageIdentifier": obj.get("imageIdentifier"),
            "text": obj.get("text"),
            "approvedText": obj.get("approvedText"),
            "approvedImage": obj.get("approvedImage"),
            "likes": obj.get("likes"),
            "roomNumber": obj.get("roomNumber"),
            "roomRating": obj.get("roomRating"),
            "responded": obj.get("responded") if obj.get("responded") is not None else False
        })
        return _obj


