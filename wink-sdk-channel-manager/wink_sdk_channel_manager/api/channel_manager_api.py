# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None   # Channel Manager API Wink exposes a secured REST-based, JSON API to its channel manager partners. The connection is \"channel-wide\". Partners are free to integrate with the REST-based API using any programming language.  # Intended Audience This document is intended for external channel partners who wish to integrate with Wink.  # Requirements - Active account with Wink. Sign up for your Channel Manager account:    - Staging: [https://staging-studio.wink.travel](https://staging-studio.wink.travel).    - Production: [https://studio.wink.travel](https://studio.wink.travel). - Active application. An application provides you with Oauth2 credentials you can pass to our endpoints. One is already created for you upon account creation. - Your production IP numbers. They need to be whitelisted before you can talk to our production environment.  # Performance A particular attention to performance should be given when integrating with this API. A few things to be aware of: - Enable gzip compression to make payloads smaller. - Fewer large REST calls are preferred to many small ones. E.g. It is better to update many dates instead of individual dates. - It is possible to update both rate and availability with a single request. - Request only date ranges that you will use. There is no need to request an entire year if you will only be working with the first seven days.  ## Reservation notification (PUSH) Wink supports PUSH notifications to communicate reservations. We also support BASIC AUTH to your endpoint. If you want to enable PUSH, add your PUSH endpoint and credentials (optional) to your account.

    The version of the OpenAPI document: 30.31.1
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from wink_sdk_channel_manager.models.page_channel_manager_property import PageChannelManagerProperty
from wink_sdk_channel_manager.models.ping_response import PingResponse
from wink_sdk_channel_manager.models.property_booking import PropertyBooking
from wink_sdk_channel_manager.models.property_rate import PropertyRate
from wink_sdk_channel_manager.models.property_rate_update_request import PropertyRateUpdateRequest
from wink_sdk_channel_manager.models.property_room_rate_with_rate_list import PropertyRoomRateWithRateList
from wink_sdk_channel_manager.models.property_with_room_rate_list import PropertyWithRoomRateList

from wink_sdk_channel_manager.api_client import ApiClient, RequestSerialized
from wink_sdk_channel_manager.api_response import ApiResponse
from wink_sdk_channel_manager.rest import RESTResponseType


class ChannelManagerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def ping(
        self,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PingResponse:
        """Say Hello

        Test endpoint to validate your credentials.

        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._ping_serialize(
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PingResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def ping_with_http_info(
        self,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PingResponse]:
        """Say Hello

        Test endpoint to validate your credentials.

        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._ping_serialize(
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PingResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def ping_without_preload_content(
        self,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Say Hello

        Test endpoint to validate your credentials.

        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._ping_serialize(
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PingResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _ping_serialize(
        self,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/ping',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def show_properties(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page through all properties owned by your account")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Limit results of records per page")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PageChannelManagerProperty:
        """Show Properties

        The properties endpoint provides the entry point into the listener and is used to list properties you have access to.

        :param page: Page through all properties owned by your account
        :type page: int
        :param size: Limit results of records per page
        :type size: int
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_properties_serialize(
            page=page,
            size=size,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PageChannelManagerProperty",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def show_properties_with_http_info(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page through all properties owned by your account")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Limit results of records per page")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PageChannelManagerProperty]:
        """Show Properties

        The properties endpoint provides the entry point into the listener and is used to list properties you have access to.

        :param page: Page through all properties owned by your account
        :type page: int
        :param size: Limit results of records per page
        :type size: int
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_properties_serialize(
            page=page,
            size=size,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PageChannelManagerProperty",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def show_properties_without_preload_content(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page through all properties owned by your account")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Limit results of records per page")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show Properties

        The properties endpoint provides the entry point into the listener and is used to list properties you have access to.

        :param page: Page through all properties owned by your account
        :type page: int
        :param size: Limit results of records per page
        :type size: int
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_properties_serialize(
            page=page,
            size=size,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PageChannelManagerProperty",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_properties_serialize(
        self,
        page,
        size,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/property/list',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def show_property(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record for this propertyIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PropertyWithRoomRateList:
        """Show Property

        Retrieves property record with master rates included.

        :param property_identifier: Retrieve record for this propertyIdentifier (required)
        :type property_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyWithRoomRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def show_property_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record for this propertyIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PropertyWithRoomRateList]:
        """Show Property

        Retrieves property record with master rates included.

        :param property_identifier: Retrieve record for this propertyIdentifier (required)
        :type property_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyWithRoomRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def show_property_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record for this propertyIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show Property

        Retrieves property record with master rates included.

        :param property_identifier: Retrieve record for this propertyIdentifier (required)
        :type property_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyWithRoomRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_property_serialize(
        self,
        property_identifier,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if property_identifier is not None:
            _path_params['propertyIdentifier'] = property_identifier
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/property/{propertyIdentifier}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def show_property_booking(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by propertyIdentifier")],
        booking_identifier: Annotated[StrictStr, Field(description="Retrieve record for this bookingIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PropertyBooking:
        """Show Booking

        Retrieves a specific booking by property / booking combo.

        :param property_identifier: Retrieve record owned by propertyIdentifier (required)
        :type property_identifier: str
        :param booking_identifier: Retrieve record for this bookingIdentifier (required)
        :type booking_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_booking_serialize(
            property_identifier=property_identifier,
            booking_identifier=booking_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyBooking",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def show_property_booking_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by propertyIdentifier")],
        booking_identifier: Annotated[StrictStr, Field(description="Retrieve record for this bookingIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PropertyBooking]:
        """Show Booking

        Retrieves a specific booking by property / booking combo.

        :param property_identifier: Retrieve record owned by propertyIdentifier (required)
        :type property_identifier: str
        :param booking_identifier: Retrieve record for this bookingIdentifier (required)
        :type booking_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_booking_serialize(
            property_identifier=property_identifier,
            booking_identifier=booking_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyBooking",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def show_property_booking_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by propertyIdentifier")],
        booking_identifier: Annotated[StrictStr, Field(description="Retrieve record for this bookingIdentifier")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show Booking

        Retrieves a specific booking by property / booking combo.

        :param property_identifier: Retrieve record owned by propertyIdentifier (required)
        :type property_identifier: str
        :param booking_identifier: Retrieve record for this bookingIdentifier (required)
        :type booking_identifier: str
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_booking_serialize(
            property_identifier=property_identifier,
            booking_identifier=booking_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyBooking",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_property_booking_serialize(
        self,
        property_identifier,
        booking_identifier,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if property_identifier is not None:
            _path_params['propertyIdentifier'] = property_identifier
        if booking_identifier is not None:
            _path_params['bookingIdentifier'] = booking_identifier
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/property/{propertyIdentifier}/booking/{bookingIdentifier}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def show_property_bookings(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        start_date: Annotated[datetime, Field(description="Limit results on date range starting with")],
        end_date: Annotated[Optional[datetime], Field(description="Limit results on date range ending with")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[PropertyBooking]:
        """Show Bookings

        Retrieves a list of all bookings created for the specified property within the specified date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: datetime
        :param end_date: Limit results on date range ending with
        :type end_date: datetime
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_bookings_serialize(
            property_identifier=property_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyBooking]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def show_property_bookings_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        start_date: Annotated[datetime, Field(description="Limit results on date range starting with")],
        end_date: Annotated[Optional[datetime], Field(description="Limit results on date range ending with")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[PropertyBooking]]:
        """Show Bookings

        Retrieves a list of all bookings created for the specified property within the specified date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: datetime
        :param end_date: Limit results on date range ending with
        :type end_date: datetime
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_bookings_serialize(
            property_identifier=property_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyBooking]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def show_property_bookings_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        start_date: Annotated[datetime, Field(description="Limit results on date range starting with")],
        end_date: Annotated[Optional[datetime], Field(description="Limit results on date range ending with")] = None,
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show Bookings

        Retrieves a list of all bookings created for the specified property within the specified date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: datetime
        :param end_date: Limit results on date range ending with
        :type end_date: datetime
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_bookings_serialize(
            property_identifier=property_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyBooking]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_property_bookings_serialize(
        self,
        property_identifier,
        start_date,
        end_date,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if property_identifier is not None:
            _path_params['propertyIdentifier'] = property_identifier
        # process the query parameters
        if start_date is not None:
            if isinstance(start_date, datetime):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, datetime):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/property/{propertyIdentifier}/booking/list',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def show_property_room_rates(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this masterRateIdentifier")],
        start_date: Annotated[date, Field(description="Limit results on date range starting with")],
        end_date: Annotated[date, Field(description="Limit results on date range ending with")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PropertyRoomRateWithRateList:
        """Show Daily Rates

        Retrieves all daily rates for for property / master rate combo and a date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Retrieve record owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: date
        :param end_date: Limit results on date range ending with (required)
        :type end_date: date
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_room_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyRoomRateWithRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def show_property_room_rates_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this masterRateIdentifier")],
        start_date: Annotated[date, Field(description="Limit results on date range starting with")],
        end_date: Annotated[date, Field(description="Limit results on date range ending with")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PropertyRoomRateWithRateList]:
        """Show Daily Rates

        Retrieves all daily rates for for property / master rate combo and a date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Retrieve record owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: date
        :param end_date: Limit results on date range ending with (required)
        :type end_date: date
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_room_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyRoomRateWithRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def show_property_room_rates_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Retrieve record owned by this masterRateIdentifier")],
        start_date: Annotated[date, Field(description="Limit results on date range starting with")],
        end_date: Annotated[date, Field(description="Limit results on date range ending with")],
        wink_version: Optional[StrictStr] = None,
        accept: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Show Daily Rates

        Retrieves all daily rates for for property / master rate combo and a date range.

        :param property_identifier: Retrieve record owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Retrieve record owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param start_date: Limit results on date range starting with (required)
        :type start_date: date
        :param end_date: Limit results on date range ending with (required)
        :type end_date: date
        :param wink_version:
        :type wink_version: str
        :param accept:
        :type accept: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._show_property_room_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            start_date=start_date,
            end_date=end_date,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "PropertyRoomRateWithRateList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_property_room_rates_serialize(
        self,
        property_identifier,
        master_rate_identifier,
        start_date,
        end_date,
        wink_version,
        accept,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if property_identifier is not None:
            _path_params['propertyIdentifier'] = property_identifier
        if master_rate_identifier is not None:
            _path_params['masterRateIdentifier'] = master_rate_identifier
        # process the query parameters
        if start_date is not None:
            if isinstance(start_date, date):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, date):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        if accept is not None:
            _header_params['Accept'] = accept
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def update_rates(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Update rates owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Update rates owned by this masterRateIdentifier")],
        property_rate_update_request: PropertyRateUpdateRequest,
        wink_version: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[PropertyRate]:
        """Update Daily Rates

        Update daily rate / availability for a property / master rate combo.

        :param property_identifier: Update rates owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Update rates owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param property_rate_update_request: (required)
        :type property_rate_update_request: PropertyRateUpdateRequest
        :param wink_version:
        :type wink_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            property_rate_update_request=property_rate_update_request,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyRate]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def update_rates_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Update rates owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Update rates owned by this masterRateIdentifier")],
        property_rate_update_request: PropertyRateUpdateRequest,
        wink_version: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[PropertyRate]]:
        """Update Daily Rates

        Update daily rate / availability for a property / master rate combo.

        :param property_identifier: Update rates owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Update rates owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param property_rate_update_request: (required)
        :type property_rate_update_request: PropertyRateUpdateRequest
        :param wink_version:
        :type wink_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            property_rate_update_request=property_rate_update_request,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyRate]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def update_rates_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="Update rates owned by this propertyIdentifier")],
        master_rate_identifier: Annotated[StrictStr, Field(description="Update rates owned by this masterRateIdentifier")],
        property_rate_update_request: PropertyRateUpdateRequest,
        wink_version: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update Daily Rates

        Update daily rate / availability for a property / master rate combo.

        :param property_identifier: Update rates owned by this propertyIdentifier (required)
        :type property_identifier: str
        :param master_rate_identifier: Update rates owned by this masterRateIdentifier (required)
        :type master_rate_identifier: str
        :param property_rate_update_request: (required)
        :type property_rate_update_request: PropertyRateUpdateRequest
        :param wink_version:
        :type wink_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_rates_serialize(
            property_identifier=property_identifier,
            master_rate_identifier=master_rate_identifier,
            property_rate_update_request=property_rate_update_request,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "object",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowPropertyRoomRates400Response",
            '200': "List[PropertyRate]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_rates_serialize(
        self,
        property_identifier,
        master_rate_identifier,
        property_rate_update_request,
        wink_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if property_identifier is not None:
            _path_params['propertyIdentifier'] = property_identifier
        if master_rate_identifier is not None:
            _path_params['masterRateIdentifier'] = master_rate_identifier
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        # process the form parameters
        # process the body parameter
        if property_rate_update_request is not None:
            _body_params = property_rate_update_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
                    'text/html', 
                    'text/plain', 
                    '*/*'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oAuth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/channel-manager/property/{propertyIdentifier}/master-rate/{masterRateIdentifier}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


