# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel inventory.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell.  - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel inventory and need taxonomies of standard and non-standard codes for inventory types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel inventory. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # WinkLinks API The WinkLinks API exposes endpoints to manage WinkLink entries, categories and settings. This API lets you:  1. Entries: Manage WinkLinks entries. 2. Categories: Manage WinkLinks tags. 2. Settings: Configure WinkLinks account.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.15.2
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity import ApplicationContextNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.http_status_code_non_authenticated_entity import HttpStatusCodeNonAuthenticatedEntity
from wink_sdk_affiliate_winklinks.models.servlet_context_non_authenticated_entity import ServletContextNonAuthenticatedEntity
from typing import Optional, Set
from typing_extensions import Self

class RedirectViewNonAuthenticatedEntity(BaseModel):
    """
    RedirectViewNonAuthenticatedEntity
    """ # noqa: E501
    application_context: Optional[ApplicationContextNonAuthenticatedEntity] = Field(default=None, alias="applicationContext")
    servlet_context: Optional[ServletContextNonAuthenticatedEntity] = Field(default=None, alias="servletContext")
    content_type: Optional[StrictStr] = Field(default=None, alias="contentType")
    request_context_attribute: Optional[StrictStr] = Field(default=None, alias="requestContextAttribute")
    static_attributes: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="staticAttributes")
    expose_path_variables: Optional[StrictBool] = Field(default=None, alias="exposePathVariables")
    expose_context_beans_as_attributes: Optional[StrictBool] = Field(default=None, alias="exposeContextBeansAsAttributes")
    exposed_context_bean_names: Optional[List[StrictStr]] = Field(default=None, alias="exposedContextBeanNames")
    bean_name: Optional[StrictStr] = Field(default=None, alias="beanName")
    url: Optional[StrictStr] = None
    context_relative: Optional[StrictBool] = Field(default=None, alias="contextRelative")
    http10_compatible: Optional[StrictBool] = Field(default=None, alias="http10Compatible")
    expose_model_attributes: Optional[StrictBool] = Field(default=None, alias="exposeModelAttributes")
    encoding_scheme: Optional[StrictStr] = Field(default=None, alias="encodingScheme")
    status_code: Optional[HttpStatusCodeNonAuthenticatedEntity] = Field(default=None, alias="statusCode")
    expand_uri_template_variables: Optional[StrictBool] = Field(default=None, alias="expandUriTemplateVariables")
    propagate_query_params: Optional[StrictBool] = Field(default=None, alias="propagateQueryParams")
    hosts: Optional[List[StrictStr]] = None
    propagate_query_properties: Optional[StrictBool] = Field(default=None, alias="propagateQueryProperties")
    redirect_view: Optional[StrictBool] = Field(default=None, alias="redirectView")
    attributes: Optional[Dict[str, StrictStr]] = None
    attributes_csv: Optional[StrictStr] = Field(default=None, alias="attributesCSV")
    attributes_map: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="attributesMap")
    __properties: ClassVar[List[str]] = ["applicationContext", "servletContext", "contentType", "requestContextAttribute", "staticAttributes", "exposePathVariables", "exposeContextBeansAsAttributes", "exposedContextBeanNames", "beanName", "url", "contextRelative", "http10Compatible", "exposeModelAttributes", "encodingScheme", "statusCode", "expandUriTemplateVariables", "propagateQueryParams", "hosts", "propagateQueryProperties", "redirectView", "attributes", "attributesCSV", "attributesMap"]

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
        """Create an instance of RedirectViewNonAuthenticatedEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of application_context
        if self.application_context:
            _dict['applicationContext'] = self.application_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of servlet_context
        if self.servlet_context:
            _dict['servletContext'] = self.servlet_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_code
        if self.status_code:
            _dict['statusCode'] = self.status_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedirectViewNonAuthenticatedEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationContext": ApplicationContextNonAuthenticatedEntity.from_dict(obj["applicationContext"]) if obj.get("applicationContext") is not None else None,
            "servletContext": ServletContextNonAuthenticatedEntity.from_dict(obj["servletContext"]) if obj.get("servletContext") is not None else None,
            "contentType": obj.get("contentType"),
            "requestContextAttribute": obj.get("requestContextAttribute"),
            "staticAttributes": obj.get("staticAttributes"),
            "exposePathVariables": obj.get("exposePathVariables"),
            "exposeContextBeansAsAttributes": obj.get("exposeContextBeansAsAttributes"),
            "exposedContextBeanNames": obj.get("exposedContextBeanNames"),
            "beanName": obj.get("beanName"),
            "url": obj.get("url"),
            "contextRelative": obj.get("contextRelative"),
            "http10Compatible": obj.get("http10Compatible"),
            "exposeModelAttributes": obj.get("exposeModelAttributes"),
            "encodingScheme": obj.get("encodingScheme"),
            "statusCode": HttpStatusCodeNonAuthenticatedEntity.from_dict(obj["statusCode"]) if obj.get("statusCode") is not None else None,
            "expandUriTemplateVariables": obj.get("expandUriTemplateVariables"),
            "propagateQueryParams": obj.get("propagateQueryParams"),
            "hosts": obj.get("hosts"),
            "propagateQueryProperties": obj.get("propagateQueryProperties"),
            "redirectView": obj.get("redirectView"),
            "attributes": obj.get("attributes"),
            "attributesCSV": obj.get("attributesCSV"),
            "attributesMap": obj.get("attributesMap")
        })
        return _obj


