# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel blocking on the Wink platform. The API gives you all the tools you need to ready your properties and blocking for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel blocking and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel blocking and get that same blocking out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Test API   - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work Wink.  ### Common APIs  - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consume APIs Consume endpoints are for developers who want to find existing travel blocking and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/engine-client): A single endpoint to retrieve whitelabel + customization information for the booking engine.  - [Lookup](/lookup): All APIs related to locating blocking by region, locale and property flags.  - [Inventory](/blocking): All APIs related to retrieve known travel blocking as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.   ### Produce APIs  Produce endpoints are for developers who want to create and manage travel blocking.   #### Property  - [Property registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink.  - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties.  - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types.  - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities.  - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink.  - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink.  - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.   #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts.  - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and blocking to sell.  - [Inventory](/affiliate/blocking): The Inventory API exposes endpoints for affiliates to manage the blocking they want to sell and how they want to sell it.  - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones.  - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.   #### Rate provider  - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.   ### Taxonomy APIs  Taxonomy endpoints are for developers who want to consume and produce travel blocking and need taxonomies of standard and non-standard codes for blocking types, classes, statuses etc.   - [Reference](/reactive): All APIs related to retrieving platform-supported taxonomies.   ### Insight APIs  Insight endpoints do exactly what the name implies - They offer platform-level insight into the activities of producers and consumers.   - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics.   ### Payment APIs  Payment endpoints are for developers who want to purchase travel blocking. This can be done via the API as a registered Travel Agent or using our API in conjunction with our PCI compliant reactive widget for all other entities.   - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.   ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)   ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.   ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.   ## Release history  - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md    # Extranet Distribution API The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and blocking calendars and more on Wink. This API lets you:  1. Verifier: Test your availability and promotions and create test bookings to simulate the entire booking workflow. 2. Sales Channels: Manage your sales channels. 3. Explore Network: Find new affiliates to work with. 4. Inventory: Manage blocking at the sales channel-level. 5. Calendars: Manage availability calendars for all your blocking.  Browse the endpoints in the left navigation bar to get started.  

    The version of the OpenAPI document: 30.7.10
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier
from wink_sdk_extranet_distribution.models.inventory_view_supplier import InventoryViewSupplier
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier
from wink_sdk_extranet_distribution.models.page_inventory_view_supplier import PageInventoryViewSupplier
from wink_sdk_extranet_distribution.models.selectable_key_value_pair_supplier import SelectableKeyValuePairSupplier
from wink_sdk_extranet_distribution.models.state_supplier import StateSupplier

from wink_sdk_extranet_distribution.api_client import ApiClient, RequestSerialized
from wink_sdk_extranet_distribution.api_response import ApiResponse
from wink_sdk_extranet_distribution.rest import RESTResponseType


class InventoryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def show_channel_activities(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve activities for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Activity Inventories

        Retrieve list of activities for specified property

        :param property_identifier: The property ID to retrieve activities for (required)
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

        _param = self._show_channel_activities_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_activities_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve activities for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Activity Inventories

        Retrieve list of activities for specified property

        :param property_identifier: The property ID to retrieve activities for (required)
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

        _param = self._show_channel_activities_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_activities_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve activities for")],
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
        """Show Activity Inventories

        Retrieve list of activities for specified property

        :param property_identifier: The property ID to retrieve activities for (required)
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

        _param = self._show_channel_activities_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_activities_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/experience/activity/list',
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
    def show_channel_add_ons(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve add-ons for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Add-On Inventories

        Retrieve list of addons for specified property

        :param property_identifier: The property ID to retrieve add-ons for (required)
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

        _param = self._show_channel_add_ons_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_add_ons_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve add-ons for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Add-On Inventories

        Retrieve list of addons for specified property

        :param property_identifier: The property ID to retrieve add-ons for (required)
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

        _param = self._show_channel_add_ons_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_add_ons_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve add-ons for")],
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
        """Show Add-On Inventories

        Retrieve list of addons for specified property

        :param property_identifier: The property ID to retrieve add-ons for (required)
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

        _param = self._show_channel_add_ons_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_add_ons_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/add-on/list',
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
    def show_channel_attractions(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve attractions for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Attraction Inventories

        Retrieve list of attractions for specified property

        :param property_identifier: The property ID to retrieve attractions for (required)
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

        _param = self._show_channel_attractions_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_attractions_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve attractions for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Attraction Inventories

        Retrieve list of attractions for specified property

        :param property_identifier: The property ID to retrieve attractions for (required)
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

        _param = self._show_channel_attractions_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_attractions_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve attractions for")],
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
        """Show Attraction Inventories

        Retrieve list of attractions for specified property

        :param property_identifier: The property ID to retrieve attractions for (required)
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

        _param = self._show_channel_attractions_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_attractions_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/experience/attraction/list',
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
    def show_channel_meeting_rooms(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve meeting rooms for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Meeting Room Inventories

        Retrieve list of meeting room names for specified property

        :param property_identifier: The property ID to retrieve meeting rooms for (required)
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

        _param = self._show_channel_meeting_rooms_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_meeting_rooms_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve meeting rooms for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Meeting Room Inventories

        Retrieve list of meeting room names for specified property

        :param property_identifier: The property ID to retrieve meeting rooms for (required)
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

        _param = self._show_channel_meeting_rooms_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_meeting_rooms_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve meeting rooms for")],
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
        """Show Meeting Room Inventories

        Retrieve list of meeting room names for specified property

        :param property_identifier: The property ID to retrieve meeting rooms for (required)
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

        _param = self._show_channel_meeting_rooms_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_meeting_rooms_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/meeting-room/list',
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
    def show_channel_places(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve places for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Place Inventories

        Retrieve list of places for specified property

        :param property_identifier: The property ID to retrieve places for (required)
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

        _param = self._show_channel_places_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_places_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve places for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Place Inventories

        Retrieve list of places for specified property

        :param property_identifier: The property ID to retrieve places for (required)
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

        _param = self._show_channel_places_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_places_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve places for")],
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
        """Show Place Inventories

        Retrieve list of places for specified property

        :param property_identifier: The property ID to retrieve places for (required)
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

        _param = self._show_channel_places_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_places_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/experience/place/list',
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
    def show_channel_restaurants(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve restaurants for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Restaurant Inventories

        Retrieve list of restaurants for specified property

        :param property_identifier: The property ID to retrieve restaurants for (required)
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

        _param = self._show_channel_restaurants_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_restaurants_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve restaurants for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Restaurant Inventories

        Retrieve list of restaurants for specified property

        :param property_identifier: The property ID to retrieve restaurants for (required)
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

        _param = self._show_channel_restaurants_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_restaurants_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve restaurants for")],
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
        """Show Restaurant Inventories

        Retrieve list of restaurants for specified property

        :param property_identifier: The property ID to retrieve restaurants for (required)
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

        _param = self._show_channel_restaurants_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_restaurants_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/facility/restaurant/list',
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
    def show_channel_spas(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve spas for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Spa Inventories

        Retrieve list of spas for specified property

        :param property_identifier: The property ID to retrieve spas for (required)
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

        _param = self._show_channel_spas_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_spas_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve spas for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Spa Inventories

        Retrieve list of spas for specified property

        :param property_identifier: The property ID to retrieve spas for (required)
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

        _param = self._show_channel_spas_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_channel_spas_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve spas for")],
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
        """Show Spa Inventories

        Retrieve list of spas for specified property

        :param property_identifier: The property ID to retrieve spas for (required)
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

        _param = self._show_channel_spas_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_channel_spas_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/facility/spa/list',
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
    def show_inventory(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve specified blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to retrieve")],
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
    ) -> InventoryViewSupplier:
        """Show Inventory

        Retrieve blocking specified by identifier

        :param property_identifier: The property ID to retrieve specified blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to retrieve (required)
        :type inventory_identifier: str
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

        _param = self._show_inventory_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
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
    def show_inventory_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve specified blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to retrieve")],
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
    ) -> ApiResponse[InventoryViewSupplier]:
        """Show Inventory

        Retrieve blocking specified by identifier

        :param property_identifier: The property ID to retrieve specified blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to retrieve (required)
        :type inventory_identifier: str
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

        _param = self._show_inventory_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
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
    def show_inventory_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve specified blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to retrieve")],
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
        """Show Inventory

        Retrieve blocking specified by identifier

        :param property_identifier: The property ID to retrieve specified blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to retrieve (required)
        :type inventory_identifier: str
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

        _param = self._show_inventory_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_inventory_serialize(
        self,
        property_identifier,
        inventory_identifier,
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
        if inventory_identifier is not None:
            _path_params['inventoryIdentifier'] = inventory_identifier
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/{inventoryIdentifier}',
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
    def show_inventory_list(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve inventories for")],
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
    ) -> List[InventoryViewSupplier]:
        """Show Inventory List

        Retrieve list of blocking for specified property

        :param property_identifier: The property ID to retrieve inventories for (required)
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

        _param = self._show_inventory_list_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
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
    def show_inventory_list_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve inventories for")],
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
    ) -> ApiResponse[List[InventoryViewSupplier]]:
        """Show Inventory List

        Retrieve list of blocking for specified property

        :param property_identifier: The property ID to retrieve inventories for (required)
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

        _param = self._show_inventory_list_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
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
    def show_inventory_list_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve inventories for")],
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
        """Show Inventory List

        Retrieve list of blocking for specified property

        :param property_identifier: The property ID to retrieve inventories for (required)
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

        _param = self._show_inventory_list_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_inventory_list_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/list',
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
    def show_inventory_names(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking names for")],
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
    ) -> List[str]:
        """Show Inventory Names

        Retrieve list of unique blocking names for chosen property.

        :param property_identifier: The property ID to retrieve blocking names for (required)
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

        _param = self._show_inventory_names_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
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
    def show_inventory_names_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking names for")],
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
    ) -> ApiResponse[List[str]]:
        """Show Inventory Names

        Retrieve list of unique blocking names for chosen property.

        :param property_identifier: The property ID to retrieve blocking names for (required)
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

        _param = self._show_inventory_names_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
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
    def show_inventory_names_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking names for")],
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
        """Show Inventory Names

        Retrieve list of unique blocking names for chosen property.

        :param property_identifier: The property ID to retrieve blocking names for (required)
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

        _param = self._show_inventory_names_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_inventory_names_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/name/list',
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
    def show_inventory_types(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking types for")],
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
    ) -> List[str]:
        """Show All Inventory Types

        Retrieve array of all blocking types. E.g. ['GUEST_ROOM', 'MEETING_ROOM'].

        :param property_identifier: The property ID to retrieve blocking types for (required)
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

        _param = self._show_inventory_types_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
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
    def show_inventory_types_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking types for")],
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
    ) -> ApiResponse[List[str]]:
        """Show All Inventory Types

        Retrieve array of all blocking types. E.g. ['GUEST_ROOM', 'MEETING_ROOM'].

        :param property_identifier: The property ID to retrieve blocking types for (required)
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

        _param = self._show_inventory_types_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
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
    def show_inventory_types_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking types for")],
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
        """Show All Inventory Types

        Retrieve array of all blocking types. E.g. ['GUEST_ROOM', 'MEETING_ROOM'].

        :param property_identifier: The property ID to retrieve blocking types for (required)
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

        _param = self._show_inventory_types_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[str]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_inventory_types_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/type/list',
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
    def show_master_rates(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve master rates for")],
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
    ) -> List[KeyValuePairSupplier]:
        """Show Master Rates Inventories

        Retrieve list of master rate names for specified property

        :param property_identifier: The property ID to retrieve master rates for (required)
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

        _param = self._show_master_rates_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_master_rates_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve master rates for")],
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
    ) -> ApiResponse[List[KeyValuePairSupplier]]:
        """Show Master Rates Inventories

        Retrieve list of master rate names for specified property

        :param property_identifier: The property ID to retrieve master rates for (required)
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

        _param = self._show_master_rates_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
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
    def show_master_rates_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve master rates for")],
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
        """Show Master Rates Inventories

        Retrieve list of master rate names for specified property

        :param property_identifier: The property ID to retrieve master rates for (required)
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

        _param = self._show_master_rates_serialize(
            property_identifier=property_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[KeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_master_rates_serialize(
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/master-rate/list',
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
    def show_pageable_channel_inventory(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking grid for")],
        state_supplier: Annotated[StateSupplier, Field(description="Filter grid by state request body")],
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
    ) -> PageInventoryViewSupplier:
        """Search Inventory

        Retrieve page of blocking for specified property.

        :param property_identifier: The property ID to retrieve blocking grid for (required)
        :type property_identifier: str
        :param state_supplier: Filter grid by state request body (required)
        :type state_supplier: StateSupplier
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

        _param = self._show_pageable_channel_inventory_serialize(
            property_identifier=property_identifier,
            state_supplier=state_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "PageInventoryViewSupplier",
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
    def show_pageable_channel_inventory_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking grid for")],
        state_supplier: Annotated[StateSupplier, Field(description="Filter grid by state request body")],
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
    ) -> ApiResponse[PageInventoryViewSupplier]:
        """Search Inventory

        Retrieve page of blocking for specified property.

        :param property_identifier: The property ID to retrieve blocking grid for (required)
        :type property_identifier: str
        :param state_supplier: Filter grid by state request body (required)
        :type state_supplier: StateSupplier
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

        _param = self._show_pageable_channel_inventory_serialize(
            property_identifier=property_identifier,
            state_supplier=state_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "PageInventoryViewSupplier",
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
    def show_pageable_channel_inventory_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve blocking grid for")],
        state_supplier: Annotated[StateSupplier, Field(description="Filter grid by state request body")],
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
        """Search Inventory

        Retrieve page of blocking for specified property.

        :param property_identifier: The property ID to retrieve blocking grid for (required)
        :type property_identifier: str
        :param state_supplier: Filter grid by state request body (required)
        :type state_supplier: StateSupplier
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

        _param = self._show_pageable_channel_inventory_serialize(
            property_identifier=property_identifier,
            state_supplier=state_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "PageInventoryViewSupplier",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_pageable_channel_inventory_serialize(
        self,
        property_identifier,
        state_supplier,
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
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        # process the form parameters
        # process the body parameter
        if state_supplier is not None:
            _body_params = state_supplier


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
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
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/grid',
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
    def show_sales_channel_list_by_inventory(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve sales channels for")],
        inventory_type_identifier: Annotated[StrictStr, Field(description="The blocking type ID to retrieve sales channel for")],
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
    ) -> List[SelectableKeyValuePairSupplier]:
        """Show Inventory as Channels

        Retrieve list of blocking specified by blocking identifier. The list will contain the same blocking available to different sales channels. E.g. Inventory A for Seller A. Inventory A for Seller B etc.

        :param property_identifier: The property ID to retrieve sales channels for (required)
        :type property_identifier: str
        :param inventory_type_identifier: The blocking type ID to retrieve sales channel for (required)
        :type inventory_type_identifier: str
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

        _param = self._show_sales_channel_list_by_inventory_serialize(
            property_identifier=property_identifier,
            inventory_type_identifier=inventory_type_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[SelectableKeyValuePairSupplier]",
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
    def show_sales_channel_list_by_inventory_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve sales channels for")],
        inventory_type_identifier: Annotated[StrictStr, Field(description="The blocking type ID to retrieve sales channel for")],
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
    ) -> ApiResponse[List[SelectableKeyValuePairSupplier]]:
        """Show Inventory as Channels

        Retrieve list of blocking specified by blocking identifier. The list will contain the same blocking available to different sales channels. E.g. Inventory A for Seller A. Inventory A for Seller B etc.

        :param property_identifier: The property ID to retrieve sales channels for (required)
        :type property_identifier: str
        :param inventory_type_identifier: The blocking type ID to retrieve sales channel for (required)
        :type inventory_type_identifier: str
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

        _param = self._show_sales_channel_list_by_inventory_serialize(
            property_identifier=property_identifier,
            inventory_type_identifier=inventory_type_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[SelectableKeyValuePairSupplier]",
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
    def show_sales_channel_list_by_inventory_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to retrieve sales channels for")],
        inventory_type_identifier: Annotated[StrictStr, Field(description="The blocking type ID to retrieve sales channel for")],
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
        """Show Inventory as Channels

        Retrieve list of blocking specified by blocking identifier. The list will contain the same blocking available to different sales channels. E.g. Inventory A for Seller A. Inventory A for Seller B etc.

        :param property_identifier: The property ID to retrieve sales channels for (required)
        :type property_identifier: str
        :param inventory_type_identifier: The blocking type ID to retrieve sales channel for (required)
        :type inventory_type_identifier: str
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

        _param = self._show_sales_channel_list_by_inventory_serialize(
            property_identifier=property_identifier,
            inventory_type_identifier=inventory_type_identifier,
            wink_version=wink_version,
            accept=accept,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[SelectableKeyValuePairSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _show_sales_channel_list_by_inventory_serialize(
        self,
        property_identifier,
        inventory_type_identifier,
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
        if inventory_type_identifier is not None:
            _path_params['inventoryTypeIdentifier'] = inventory_type_identifier
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
                    'text/plain', 
                    '*/*'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/{inventoryTypeIdentifier}/list',
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
    def toggle_inventory_availability(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to update")],
        inventory_update_request_supplier: Annotated[InventoryUpdateRequestSupplier, Field(description="Update blocking request body")],
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
    ) -> InventoryViewSupplier:
        """Update Inventory

        Toggle blocking availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to update (required)
        :type inventory_identifier: str
        :param inventory_update_request_supplier: Update blocking request body (required)
        :type inventory_update_request_supplier: InventoryUpdateRequestSupplier
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

        _param = self._toggle_inventory_availability_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
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
    def toggle_inventory_availability_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to update")],
        inventory_update_request_supplier: Annotated[InventoryUpdateRequestSupplier, Field(description="Update blocking request body")],
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
    ) -> ApiResponse[InventoryViewSupplier]:
        """Update Inventory

        Toggle blocking availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to update (required)
        :type inventory_identifier: str
        :param inventory_update_request_supplier: Update blocking request body (required)
        :type inventory_update_request_supplier: InventoryUpdateRequestSupplier
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

        _param = self._toggle_inventory_availability_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
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
    def toggle_inventory_availability_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_identifier: Annotated[StrictStr, Field(description="The blocking ID to update")],
        inventory_update_request_supplier: Annotated[InventoryUpdateRequestSupplier, Field(description="Update blocking request body")],
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
        """Update Inventory

        Toggle blocking availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_identifier: The blocking ID to update (required)
        :type inventory_identifier: str
        :param inventory_update_request_supplier: Update blocking request body (required)
        :type inventory_update_request_supplier: InventoryUpdateRequestSupplier
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

        _param = self._toggle_inventory_availability_serialize(
            property_identifier=property_identifier,
            inventory_identifier=inventory_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "InventoryViewSupplier",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _toggle_inventory_availability_serialize(
        self,
        property_identifier,
        inventory_identifier,
        inventory_update_request_supplier,
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
        if inventory_identifier is not None:
            _path_params['inventoryIdentifier'] = inventory_identifier
        # process the query parameters
        # process the header parameters
        if wink_version is not None:
            _header_params['Wink-Version'] = wink_version
        # process the form parameters
        # process the body parameter
        if inventory_update_request_supplier is not None:
            _body_params = inventory_update_request_supplier


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
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
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/{inventoryIdentifier}',
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
    def toggle_inventory_list_availability(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_update_request_supplier: Annotated[List[InventoryUpdateRequestSupplier], Field(description="Update inventories request body")],
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
    ) -> List[InventoryViewSupplier]:
        """Update Inventory List

        Toggle blocking list availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_update_request_supplier: Update inventories request body (required)
        :type inventory_update_request_supplier: List[InventoryUpdateRequestSupplier]
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

        _param = self._toggle_inventory_list_availability_serialize(
            property_identifier=property_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
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
    def toggle_inventory_list_availability_with_http_info(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_update_request_supplier: Annotated[List[InventoryUpdateRequestSupplier], Field(description="Update inventories request body")],
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
    ) -> ApiResponse[List[InventoryViewSupplier]]:
        """Update Inventory List

        Toggle blocking list availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_update_request_supplier: Update inventories request body (required)
        :type inventory_update_request_supplier: List[InventoryUpdateRequestSupplier]
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

        _param = self._toggle_inventory_list_availability_serialize(
            property_identifier=property_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
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
    def toggle_inventory_list_availability_without_preload_content(
        self,
        property_identifier: Annotated[StrictStr, Field(description="The property ID to update blocking for")],
        inventory_update_request_supplier: Annotated[List[InventoryUpdateRequestSupplier], Field(description="Update inventories request body")],
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
        """Update Inventory List

        Toggle blocking list availability. Only used to enable / disable blocking.

        :param property_identifier: The property ID to update blocking for (required)
        :type property_identifier: str
        :param inventory_update_request_supplier: Update inventories request body (required)
        :type inventory_update_request_supplier: List[InventoryUpdateRequestSupplier]
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

        _param = self._toggle_inventory_list_availability_serialize(
            property_identifier=property_identifier,
            inventory_update_request_supplier=inventory_update_request_supplier,
            wink_version=wink_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '500': "GenericErrorMessage",
            '403': "GenericErrorMessage",
            '401': "GenericErrorMessage",
            '400': "ShowInventory400Response",
            '200': "List[InventoryViewSupplier]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _toggle_inventory_list_availability_serialize(
        self,
        property_identifier,
        inventory_update_request_supplier,
        wink_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'InventoryUpdateRequestSupplier': '',
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
        # process the form parameters
        # process the body parameter
        if inventory_update_request_supplier is not None:
            _body_params = inventory_update_request_supplier


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/xml', 
                    'text/xml', 
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
            'oauth2ClientCredentials'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/property/{propertyIdentifier}/sales/inventory/list',
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


