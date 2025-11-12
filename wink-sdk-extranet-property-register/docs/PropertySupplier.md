# PropertySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**name** | **str** | Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique). | 
**hotel_code** | **str** | A shorter unique code to refer to the hotel. Country Code + 5 digit number | 
**local_name** | **str** | Name of the hotel in its local language if you use it for domestic guests. | [optional] 
**legal_name** | **str** | Legal name of your hotel as it is registered. | 
**url_name** | **str** | Unique url-friendly slug to identify property | 
**unique_id** | **str** | Event shorter name | 
**currency_code** | **str** | Currency code | 
**status** | **str** | wink.travel sets this status as the hotel moves through the payment workflow and manually for approval. | [default to 'APPROVED']
**external_status** | **str** | Property goes active by changing externalStatus. | [default to 'ACTIVE']
**multimedias** | [**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md) |  | [optional] 
**recognition_list** | [**List[TravelInventoryRecognitionSupplier]**](TravelInventoryRecognitionSupplier.md) |  | [optional] 
**location_category** | **str** | Supported OTA specification &#x60;LOC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**segment_category** | **str** | Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**hotel_category** | **str** | Supported OTA specification &#x60;PCT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**architectural_style** | **str** | Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**when_built** | **str** | Year the property was constructed. | [optional] 
**hotel_chain** | **str** | Hotel chain name if property is part of that chain. | [optional] 
**hotel_brand** | **str** | Hotel brand name if property is part of that brand. | [optional] 
**other_channel_manager** | **str** | If the property is currently using a channel manager but it isn&#39;t yet part of our list, chose &#39;OTHER_CHANNEL_MANAGER&#39; as channelManager and fill in the name of the channel manager here | [optional] 
**license_number** | **str** | If the property has a valid license number to run a hotel in their country, add it here. | [optional] 
**stars** | **int** | Hotel star rating. | [optional] 
**general_manager** | [**GeneralManagerSupplier**](GeneralManagerSupplier.md) |  | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) | Localized short and long welcome text of property. | [optional] 
**hotel_amenity_codes** | **List[str]** | Supported OTA specification &#x60;HAC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | [optional] 
**property_accessibility_codes** | **List[str]** | Supported OTA specification &#x60;PHY&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | [optional] 
**property_security_codes** | **List[str]** | Supported OTA specification &#x60;SEC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory). | [optional] 
**location_point** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) | GeoJSON point containing latitude and longitude of property. &#x60;Note: x &#x3D; longitude, y &#x3D; latitude&#x60;. | [optional] 
**policy** | [**PropertyPolicySupplier**](PropertyPolicySupplier.md) | Property policies such as pets and children, early and late checkout and more | [optional] 
**socials** | [**List[SocialSupplier]**](SocialSupplier.md) | List of all social network account property has. | [optional] 
**owner_contact** | [**ContactSupplier**](ContactSupplier.md) | Owner contact information | [optional] 
**reservations_contact** | [**ContactSupplier**](ContactSupplier.md) | Reservation desk contact information | [optional] 
**revenue_contact** | [**ContactSupplier**](ContactSupplier.md) | Accounting contact information | [optional] 
**marketing_contact** | [**ContactSupplier**](ContactSupplier.md) | Accounting contact address | [optional] 
**lifestyle_types** | **List[object]** |  | [optional] 
**green_index_scores** | [**PropertyAggregateGreenIndexAnswersSupplier**](PropertyAggregateGreenIndexAnswersSupplier.md) | Properties that answered the Green Index questionnaire [full or partial], will have aggregate scores available. | [optional] 
**agreement_accepted** | **bool** | Property has accepted our terms and conditions. | 
**marketing_optin_allowed** | **bool** | Property agreed to let the payment use its logo and images for marketing purposes (with proper credits). | [optional] 
**logo** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md) | Property logo | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for property | 
**address** | [**AddressSupplier**](AddressSupplier.md) | Property address. | [optional] 
**reservation_desk_start_time** | **str** | If the reservation desk does not operate 24 hours, enter a start time. | [optional] 
**reservation_desk_end_time** | **str** | If the reservation desk does not operate 24 hours, enter an end time. | [optional] 
**website** | **str** | Property brand.com website. | [optional] 
**google_maps_url** | **str** | Google Maps URL of the place | [optional] 
**metadata** | **Dict[str, object]** | Place to put stuff into | [optional] 
**rate_provider** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) | This can be an enum for external channel managers or an identifier for a Wink company rate provider | [optional] 
**previous_url_name_list** | **List[object]** |  | [optional] 
**active** | **bool** | Property is both approved and activated. | [optional] 
**contract_signer_full_name** | **str** | Concatenated name of contract signer into one string. | [optional] 
**full_address** | **str** | Concatenated address into a single string | [optional] 
**property_active** | **bool** | Property activated itself and went live. | [optional] 
**platform_active** | **bool** | Platform approved property. | [optional] 
**social_networks** | **bool** | Whether property has any social networks associated with her profile. | [optional] 
**lifestyles** | **bool** | Whether property has any lifestyles associated with her profile. | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.property_supplier import PropertySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySupplier from a JSON string
property_supplier_instance = PropertySupplier.from_json(json)
# print the JSON string representation of the object
print(PropertySupplier.to_json())

# convert the object into a dict
property_supplier_dict = property_supplier_instance.to_dict()
# create an instance of PropertySupplier from a dict
property_supplier_from_dict = PropertySupplier.from_dict(property_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


