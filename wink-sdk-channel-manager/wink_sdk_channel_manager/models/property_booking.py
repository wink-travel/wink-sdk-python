# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None   # Channel Manager API Wink exposes a secured REST-based, JSON API to its channel manager partners. The connection is \"channel-wide\". Partners are free to integrate with the REST-based API using any programming language.  # Intended Audience This document is intended for external channel partners who wish to integrate with Wink.  # Requirements - Active account with Wink. Sign up for your Channel Manager account:    - Staging: [https://staging-studio.wink.travel](https://staging-studio.wink.travel).    - Production: [https://studio.wink.travel](https://studio.wink.travel). - Active application. An application provides you with Oauth2 credentials you can pass to our endpoints. One is already created for you upon account creation. - Your production IP numbers. They need to be whitelisted before you can talk to our production environment.  # Performance A particular attention to performance should be given when integrating with this API. A few things to be aware of: - Enable gzip compression to make payloads smaller. - Fewer large REST calls are preferred to many small ones. E.g. It is better to update many dates instead of individual dates. - It is possible to update both rate and availability with a single request. - Request only date ranges that you will use. There is no need to request an entire year if you will only be working with the first seven days.  ## Reservation notification (PUSH) Wink supports PUSH notifications to communicate reservations. We also support BASIC AUTH to your endpoint. If you want to enable PUSH, add your PUSH endpoint and credentials (optional) to your account.

    The version of the OpenAPI document: 30.31.5
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class PropertyBooking(BaseModel):
    """
    PropertyBooking
    """ # noqa: E501
    booking_identifier: UUID = Field(description="Booking ID", alias="bookingIdentifier")
    property_identifier: UUID = Field(description="Property ID", alias="propertyIdentifier")
    room_rate_identifier: UUID = Field(description="Master Rate ID", alias="roomRateIdentifier")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Master Rate name")
    guest_room_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Guest room name", alias="guestRoomName")
    rate_plan_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Rate plan name", alias="ratePlanName")
    rooms: StrictInt = Field(description="Number of rooms")
    guests: StrictInt = Field(description="Number of guests")
    adults: StrictInt = Field(description="Number of adults")
    children: StrictInt = Field(description="Number of children")
    first_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="First name of traveler", alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Last name of traveler", alias="lastName")
    email: Annotated[str, Field(min_length=1, strict=True)] = Field(description="E-mail of traveler")
    amount: Union[StrictFloat, StrictInt] = Field(description="Total booking amount")
    currency_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Supplier currency", alias="currencyCode")
    booking_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Ref. code for traveler", alias="bookingCode")
    start_date: date = Field(description="Arrival date", alias="startDate")
    end_date: date = Field(description="Departure date", alias="endDate")
    created_date: datetime = Field(description="Created date", alias="createdDate")
    cancelled: StrictBool = Field(description="Whether booking is cancelled or not")
    cancel_date: Optional[datetime] = Field(default=None, description="Cancellation date if booking was cancelled", alias="cancelDate")
    payment_method_type: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Payment method", alias="paymentMethodType")
    payment_wallet_type: Optional[StrictStr] = Field(default=None, description="Optional payment wallet type", alias="paymentWalletType")
    payment_method_status: StrictStr = Field(description="Status of payment", alias="paymentMethodStatus")
    sales_channel_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Sales channel name", alias="salesChannelName")
    sales_channel_identifier: UUID = Field(description="Sales channel ID", alias="salesChannelIdentifier")
    __properties: ClassVar[List[str]] = ["bookingIdentifier", "propertyIdentifier", "roomRateIdentifier", "name", "guestRoomName", "ratePlanName", "rooms", "guests", "adults", "children", "firstName", "lastName", "email", "amount", "currencyCode", "bookingCode", "startDate", "endDate", "createdDate", "cancelled", "cancelDate", "paymentMethodType", "paymentWalletType", "paymentMethodStatus", "salesChannelName", "salesChannelIdentifier"]

    @field_validator('payment_method_status')
    def payment_method_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['INITIALIZED', 'PROCESSING', 'SUCCEEDED', 'FAILED']):
            raise ValueError("must be one of enum values ('INITIALIZED', 'PROCESSING', 'SUCCEEDED', 'FAILED')")
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
        """Create an instance of PropertyBooking from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropertyBooking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bookingIdentifier": obj.get("bookingIdentifier"),
            "propertyIdentifier": obj.get("propertyIdentifier"),
            "roomRateIdentifier": obj.get("roomRateIdentifier"),
            "name": obj.get("name"),
            "guestRoomName": obj.get("guestRoomName"),
            "ratePlanName": obj.get("ratePlanName"),
            "rooms": obj.get("rooms"),
            "guests": obj.get("guests"),
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "email": obj.get("email"),
            "amount": obj.get("amount"),
            "currencyCode": obj.get("currencyCode"),
            "bookingCode": obj.get("bookingCode"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "createdDate": obj.get("createdDate"),
            "cancelled": obj.get("cancelled"),
            "cancelDate": obj.get("cancelDate"),
            "paymentMethodType": obj.get("paymentMethodType"),
            "paymentWalletType": obj.get("paymentWalletType"),
            "paymentMethodStatus": obj.get("paymentMethodStatus"),
            "salesChannelName": obj.get("salesChannelName"),
            "salesChannelIdentifier": obj.get("salesChannelIdentifier")
        })
        return _obj


