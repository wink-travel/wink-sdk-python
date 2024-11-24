# RoomTypeWithBestPriceNonAuthenticatedEntity

Best-priced room at property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_with_price_configuration** | [**RoomTypeWithPriceConfigurationNonAuthenticatedEntity**](RoomTypeWithPriceConfigurationNonAuthenticatedEntity.md) |  | [optional] 
**perk_value** | **int** | The sum of all perks the master rate had made available. | [optional] 
**available** | **bool** | Whether this room type is available with this configuration | [optional] 
**sort** | **int** | When this room type is displayed in conjunction with many others, this sort property will often times be populated to indicate how the room types should be sorted and displayed. | [optional] 

## Example

```python
from wink_sdk_inventory.models.room_type_with_best_price_non_authenticated_entity import RoomTypeWithBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeWithBestPriceNonAuthenticatedEntity from a JSON string
room_type_with_best_price_non_authenticated_entity_instance = RoomTypeWithBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeWithBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_with_best_price_non_authenticated_entity_dict = room_type_with_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeWithBestPriceNonAuthenticatedEntity from a dict
room_type_with_best_price_non_authenticated_entity_from_dict = RoomTypeWithBestPriceNonAuthenticatedEntity.from_dict(room_type_with_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


