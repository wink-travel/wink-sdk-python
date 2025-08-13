# RoomTypeWithPriceConfigurationsNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**GuestRoomLightweightNonAuthenticatedEntity**](GuestRoomLightweightNonAuthenticatedEntity.md) | The room type. | 
**price_configurations** | **List[object]** |  | 
**lowest_price** | [**RoomConfigurationPriceNonAuthenticatedEntity**](RoomConfigurationPriceNonAuthenticatedEntity.md) |  | [optional] 
**available** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.room_type_with_price_configurations_non_authenticated_entity import RoomTypeWithPriceConfigurationsNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeWithPriceConfigurationsNonAuthenticatedEntity from a JSON string
room_type_with_price_configurations_non_authenticated_entity_instance = RoomTypeWithPriceConfigurationsNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeWithPriceConfigurationsNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_with_price_configurations_non_authenticated_entity_dict = room_type_with_price_configurations_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeWithPriceConfigurationsNonAuthenticatedEntity from a dict
room_type_with_price_configurations_non_authenticated_entity_from_dict = RoomTypeWithPriceConfigurationsNonAuthenticatedEntity.from_dict(room_type_with_price_configurations_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


