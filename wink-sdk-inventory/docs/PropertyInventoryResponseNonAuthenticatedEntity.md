# PropertyInventoryResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique property identifier to retrieve inventory for. | [optional] 
**url_name** | **str** | Unique url-friendly record identifier of property. | [optional] 
**hotel** | [**PropertyAggregateLightweightNonAuthenticatedEntity**](PropertyAggregateLightweightNonAuthenticatedEntity.md) | Property details | [optional] 
**green_index_scores** | [**PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity**](PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity.md) | Detailed Green Index scores on hoe the property scores by category | [optional] 
**room_types** | [**List[RoomTypeWithPriceConfigurationsNonAuthenticatedEntity]**](RoomTypeWithPriceConfigurationsNonAuthenticatedEntity.md) | List of room types with price configurations based on the itinerary that was passed on the user session. | [optional] 
**meeting_rooms** | [**List[MeetingRoomLocalizedInventoryNonAuthenticatedEntity]**](MeetingRoomLocalizedInventoryNonAuthenticatedEntity.md) | List of property meeting rooms on and off the premises. | [optional] 
**restaurants** | [**List[RestaurantLocalizedInventoryNonAuthenticatedEntity]**](RestaurantLocalizedInventoryNonAuthenticatedEntity.md) | List of property restaurants on and off the premises. | [optional] 
**spas** | [**List[SpaLocalizedInventoryNonAuthenticatedEntity]**](SpaLocalizedInventoryNonAuthenticatedEntity.md) | List of property spas on and off the premises. | [optional] 
**activities** | [**List[ActivityLocalizedInventoryNonAuthenticatedEntity]**](ActivityLocalizedInventoryNonAuthenticatedEntity.md) | List of property activities on and off the premises. | [optional] 
**attractions** | [**List[AttractionLocalizedInventoryNonAuthenticatedEntity]**](AttractionLocalizedInventoryNonAuthenticatedEntity.md) | List of property attractions on and off the premises. | [optional] 
**places** | [**List[PlaceLocalizedInventoryNonAuthenticatedEntity]**](PlaceLocalizedInventoryNonAuthenticatedEntity.md) | List of property places on and off the premises. | [optional] 
**metadata** | [**List[MetaDataNonAuthenticatedEntity]**](MetaDataNonAuthenticatedEntity.md) | List of property meta data. | [optional] 
**images** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | List of property images | [optional] 
**videos** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | List of property videos | [optional] 
**recognitions** | [**List[TravelInventoryRecognitionNonAuthenticatedEntity]**](TravelInventoryRecognitionNonAuthenticatedEntity.md) | List of property recognitions | [optional] 
**announcements** | [**List[AnnouncementLightweightNonAuthenticatedEntity]**](AnnouncementLightweightNonAuthenticatedEntity.md) | List of property announcements | [optional] 
**reviews** | [**List[UserReviewNonAuthenticatedEntity]**](UserReviewNonAuthenticatedEntity.md) | List of property reviews | [optional] 
**sales_channel** | [**SalesChannelInfoNonAuthenticatedEntity**](SalesChannelInfoNonAuthenticatedEntity.md) | Sales channel that owns this booking | [optional] 
**cheapest_room_types** | [**List[RoomTypeWithPriceConfigurationNonAuthenticatedEntity]**](RoomTypeWithPriceConfigurationNonAuthenticatedEntity.md) | Uses the content from roomTypes and displays the lowest price for each room type that is available. | [optional] 
**available** | **bool** |  | [optional] 
**lowest_price** | [**RoomTypeWithPriceConfigurationNonAuthenticatedEntity**](RoomTypeWithPriceConfigurationNonAuthenticatedEntity.md) | Uses the content from roomTypes and shows the room type with the lowest price. | [optional] 

## Example

```python
from wink_sdk_inventory.models.property_inventory_response_non_authenticated_entity import PropertyInventoryResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyInventoryResponseNonAuthenticatedEntity from a JSON string
property_inventory_response_non_authenticated_entity_instance = PropertyInventoryResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PropertyInventoryResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
property_inventory_response_non_authenticated_entity_dict = property_inventory_response_non_authenticated_entity_instance.to_dict()
# create an instance of PropertyInventoryResponseNonAuthenticatedEntity from a dict
property_inventory_response_non_authenticated_entity_from_dict = PropertyInventoryResponseNonAuthenticatedEntity.from_dict(property_inventory_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


