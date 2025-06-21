# RoomTypeLightweightSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Room type ID | 
**hotel_identifier** | **str** | Hotel ID | 
**featured_ind** | **bool** | Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special. | 
**lifestyle_type** | **str** | Indicate the type of lifestyle this blocking should be associated with. | [optional] 
**location** | [**GeoJsonPointSupplierDetails**](GeoJsonPointSupplierDetails.md) | Geo-location point where blocking takes place. Defaults to location of property. | 
**descriptions** | [**List[SimpleDescriptionSupplierDetails]**](SimpleDescriptionSupplierDetails.md) |  | 
**multimedias** | [**List[SimpleMultimediaSupplierDetails]**](SimpleMultimediaSupplierDetails.md) |  | 
**contact** | [**ContactSupplierDetails**](ContactSupplierDetails.md) | Associate a contact person for this blocking (if applicable). | 
**address** | [**AddressSupplierDetails**](AddressSupplierDetails.md) | Defaults to property address. | 
**commissionable** | **bool** | Indicate whether sales channels receive commission for selling this blocking. | [default to True]
**name** | **str** | Internal name of blocking. | 
**proximity_code** | **str** | Supported OTA specification &#x60;PRX&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**sort** | **int** | Use this property to sort an blocking in a list of activities. | [optional] 
**min_age_appropriate_code** | **str** | Supported OTA specification &#x60;AQC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**bookable** | **bool** | Indicates if this blocking can be added to a booking or if it is read-only marketing material only. | [default to True]
**active** | **bool** | Modify blocking availability with this flag. | [default to True]
**disability_features** | **List[str]** |  | [optional] 
**security_features** | **List[str]** |  | [optional] 
**socials** | [**List[SocialSupplierDetails]**](SocialSupplierDetails.md) |  | [optional] 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**recognition_list** | [**List[TravelInventoryRecognitionSupplierDetails]**](TravelInventoryRecognitionSupplierDetails.md) |  | [optional] 
**transactional_inventory_list** | [**List[TransactionalTravelInventorySupplierDetails]**](TransactionalTravelInventorySupplierDetails.md) |  | [optional] 
**max_occupancy** | **int** | Maximum number of guest allowed in a room type. | [default to 2]
**min_occupancy** | **int** | Minimum number of guests allowed in a room type. | [default to 1]
**quantity** | **int** | Defines the number of rooms of this type | 
**non_smoking** | **bool** | Non-smoking indicator | 
**bedroom_configuration_list** | [**List[BedroomConfigurationSupplierDetails]**](BedroomConfigurationSupplierDetails.md) |  | 
**size** | **float** | Number of square meters that defines the size of this room type. | 
**max_adult_occupancy** | **int** | Maximum number of adults allowed in a room type. | [default to 2]
**max_child_occupancy** | **int** | Maximum number of children allowed in a room type. | [default to 0]
**bathroom_count** | **int** | Number of bathrooms | [default to 1]
**living_room_count** | **int** | Number of living rooms | [default to 1]
**max_rollaways** | **int** | Maximum number of rollaway beds allowed in this room type. | [default to 0]
**room_category** | **str** | Indicates the category of the room. Typical values would be Moderate, Standard, or Deluxe. Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**floor** | **str** | Floor an which a room is located | [optional] 
**room_location_code** | **str** | Indicates the location of the room within the hotel structure. Typical values would be \&quot;Near Exit\&quot;,\&quot;Close to elevator\&quot;, \&quot;Low Floor\&quot; or \&quot;High Floor\&quot;. Supported OTA specification &#x60;RLT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**room_view_code** | **str** | Indicates the view of the room. Typical values would be \&quot;Ocean view\&quot;, \&quot;Pool view\&quot; or \&quot;Garden View\&quot;. Supported OTA specification &#x60;RVT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**composite** | **bool** | Indicates that the room (suite) is a composite of smaller units. | [default to False]
**composite_count** | **int** | Number of rooms of this room type that makes up a larger unit (composite) such as a two bedroom suite could be comprised of two king rooms plus other room types. A 0 means disabled. | [default to 0]
**room_classification_code** | **str** | Specifies the room classification (e.g., cabin, apartment). Supported OTA specification &#x60;GRI&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**room_architecture_code** | **str** | Specifies the architectural style of a room. Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**room_gender** | **str** | Used to request or specify a gender assignment for a room. Note: Typically used by Hosteliers. | [optional] [default to 'Unknown']
**shared_room_ind** | **bool** | If TRUE, the room requires or has sharing available. Note: Typically used by Hosteliers. | [default to False]
**max_cribs** | **int** | Maximum number of cribs allowed in a room type. | [default to 0]
**amenities** | **List[str]** |  | [optional] 
**included_adult_occupancy** | **int** | The number of pax the room price was meant for | [default to 2]
**included_child_occupancy** | **int** | The number of children the room price was meant for | [default to 0]
**base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Typical one night rate during regular remand period | 
**min_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Typical one night rate in a distressed period | 

## Example

```python
from wink_sdk_extranet_distribution.models.room_type_lightweight_supplier_details import RoomTypeLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeLightweightSupplierDetails from a JSON string
room_type_lightweight_supplier_details_instance = RoomTypeLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RoomTypeLightweightSupplierDetails.to_json())

# convert the object into a dict
room_type_lightweight_supplier_details_dict = room_type_lightweight_supplier_details_instance.to_dict()
# create an instance of RoomTypeLightweightSupplierDetails from a dict
room_type_lightweight_supplier_details_from_dict = RoomTypeLightweightSupplierDetails.from_dict(room_type_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


