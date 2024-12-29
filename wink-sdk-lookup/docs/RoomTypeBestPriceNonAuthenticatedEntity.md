# RoomTypeBestPriceNonAuthenticatedEntity

Best-priced room types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_identifier** | **str** | Room type identifier. | 
**price** | [**RoomConfigurationPriceNonAuthenticatedEntity**](RoomConfigurationPriceNonAuthenticatedEntity.md) |  | 
**perk_value** | **int** | The sum of all perks the master rate had made available. | 
**available** | **bool** | Whether this room type is available with this configuration | 
**sort** | **int** | When this room type is displayed in conjunction with many others, this sort property will often times be populated to indicate how the room types should be sorted and displayed. | 

## Example

```python
from wink_sdk_lookup.models.room_type_best_price_non_authenticated_entity import RoomTypeBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeBestPriceNonAuthenticatedEntity from a JSON string
room_type_best_price_non_authenticated_entity_instance = RoomTypeBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_best_price_non_authenticated_entity_dict = room_type_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeBestPriceNonAuthenticatedEntity from a dict
room_type_best_price_non_authenticated_entity_from_dict = RoomTypeBestPriceNonAuthenticatedEntity.from_dict(room_type_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


