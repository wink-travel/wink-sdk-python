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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wink_sdk_extranet_distribution.models.beneficiary_charge_supplier_details import BeneficiaryChargeSupplierDetails
from wink_sdk_extranet_distribution.models.pending_refund_supplier_details import PendingRefundSupplierDetails
from typing import Optional, Set
from typing_extensions import Self

class BeneficiarySupplierDetails(BaseModel):
    """
    Beneficiary is a registered account with rights to compensation within a booking.
    """ # noqa: E501
    account_identifier: StrictStr = Field(description="accountIdentifier of beneficiary that can map to an account with us", alias="accountIdentifier")
    account_name: StrictStr = Field(description="accountName of beneficiary that can map to an account with us", alias="accountName")
    account_email: StrictStr = Field(description="accountEmail of beneficiary that can map to an account with us", alias="accountEmail")
    account_url: Optional[StrictStr] = Field(default=None, description="accountUrl of beneficiary that can map to an account with us", alias="accountUrl")
    type: StrictStr = Field(description="The type of beneficiary payment.")
    amount_due: Optional[BeneficiaryChargeSupplierDetails] = Field(default=None, alias="amountDue")
    source_currency: StrictStr = Field(description="The source currency", alias="sourceCurrency")
    display_currency: StrictStr = Field(description="The display currency", alias="displayCurrency")
    supplier_currency: StrictStr = Field(description="The supplier currency", alias="supplierCurrency")
    internal_currency: StrictStr = Field(description="The internal currency", alias="internalCurrency")
    capture_currency: StrictStr = Field(description="The capture currency", alias="captureCurrency")
    source_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Amount in source currency", alias="sourceAmount")
    display_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Amount in display currency", alias="displayAmount")
    supplier_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Amount in supplier currency", alias="supplierAmount")
    internal_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Amount in internal currency", alias="internalAmount")
    capture_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Amount in capture currency", alias="captureAmount")
    source_amount_refund_modifier: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The delta from the original source amount after a refund occurred", alias="sourceAmountRefundModifier")
    display_amount_refund_modifier: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The delta from the original display amount after a refund occurred", alias="displayAmountRefundModifier")
    supplier_amount_refund_modifier: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The delta from the original supplier amount after a refund occurred", alias="supplierAmountRefundModifier")
    internal_amount_refund_modifier: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The delta from the original internal amount after a refund occurred", alias="internalAmountRefundModifier")
    capture_amount_refund_modifier: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The delta from the original capture amount after a refund occurred", alias="captureAmountRefundModifier")
    pending_refunds: Optional[List[PendingRefundSupplierDetails]] = Field(default=None, alias="pendingRefunds")
    net_source_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Source amount minus source modifier.", alias="netSourceAmount")
    net_display_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Display amount minus display modifier.", alias="netDisplayAmount")
    net_supplier_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Supplier amount minus supplier modifier.", alias="netSupplierAmount")
    net_internal_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Internal amount minus internal modifier.", alias="netInternalAmount")
    net_capture_amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Capture amount minus capture modifier.", alias="netCaptureAmount")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Place to add more data related to the beneficiary.")
    __properties: ClassVar[List[str]] = ["accountIdentifier", "accountName", "accountEmail", "accountUrl", "type", "amountDue", "sourceCurrency", "displayCurrency", "supplierCurrency", "internalCurrency", "captureCurrency", "sourceAmount", "displayAmount", "supplierAmount", "internalAmount", "captureAmount", "sourceAmountRefundModifier", "displayAmountRefundModifier", "supplierAmountRefundModifier", "internalAmountRefundModifier", "captureAmountRefundModifier", "pendingRefunds", "netSourceAmount", "netDisplayAmount", "netSupplierAmount", "netInternalAmount", "netCaptureAmount", "metadata"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COMMISSION', 'PLATFORM_FEE', 'TRIP_PAY', 'SALE']):
            raise ValueError("must be one of enum values ('COMMISSION', 'PLATFORM_FEE', 'TRIP_PAY', 'SALE')")
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
        """Create an instance of BeneficiarySupplierDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount_due
        if self.amount_due:
            _dict['amountDue'] = self.amount_due.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pending_refunds (list)
        _items = []
        if self.pending_refunds:
            for _item_pending_refunds in self.pending_refunds:
                if _item_pending_refunds:
                    _items.append(_item_pending_refunds.to_dict())
            _dict['pendingRefunds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BeneficiarySupplierDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountIdentifier": obj.get("accountIdentifier"),
            "accountName": obj.get("accountName"),
            "accountEmail": obj.get("accountEmail"),
            "accountUrl": obj.get("accountUrl"),
            "type": obj.get("type"),
            "amountDue": BeneficiaryChargeSupplierDetails.from_dict(obj["amountDue"]) if obj.get("amountDue") is not None else None,
            "sourceCurrency": obj.get("sourceCurrency"),
            "displayCurrency": obj.get("displayCurrency"),
            "supplierCurrency": obj.get("supplierCurrency"),
            "internalCurrency": obj.get("internalCurrency"),
            "captureCurrency": obj.get("captureCurrency"),
            "sourceAmount": obj.get("sourceAmount"),
            "displayAmount": obj.get("displayAmount"),
            "supplierAmount": obj.get("supplierAmount"),
            "internalAmount": obj.get("internalAmount"),
            "captureAmount": obj.get("captureAmount"),
            "sourceAmountRefundModifier": obj.get("sourceAmountRefundModifier"),
            "displayAmountRefundModifier": obj.get("displayAmountRefundModifier"),
            "supplierAmountRefundModifier": obj.get("supplierAmountRefundModifier"),
            "internalAmountRefundModifier": obj.get("internalAmountRefundModifier"),
            "captureAmountRefundModifier": obj.get("captureAmountRefundModifier"),
            "pendingRefunds": [PendingRefundSupplierDetails.from_dict(_item) for _item in obj["pendingRefunds"]] if obj.get("pendingRefunds") is not None else None,
            "netSourceAmount": obj.get("netSourceAmount"),
            "netDisplayAmount": obj.get("netDisplayAmount"),
            "netSupplierAmount": obj.get("netSupplierAmount"),
            "netInternalAmount": obj.get("netInternalAmount"),
            "netCaptureAmount": obj.get("netCaptureAmount"),
            "metadata": obj.get("metadata")
        })
        return _obj


