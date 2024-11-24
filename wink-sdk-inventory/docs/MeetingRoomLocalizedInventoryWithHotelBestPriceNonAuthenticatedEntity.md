# MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

Populated only when the type of grid item is `MEETING_ROOM`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**MeetingRoomLocalizedInventoryNonAuthenticatedEntity**](MeetingRoomLocalizedInventoryNonAuthenticatedEntity.md) |  | [optional] 
**hotel_with_best_price** | [**HotelWithBestPriceNonAuthenticatedEntity**](HotelWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity import MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(meeting_room_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


