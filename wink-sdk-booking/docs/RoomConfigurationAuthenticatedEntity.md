# RoomConfigurationAuthenticatedEntity

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildAuthenticatedEntity]**](ChildAuthenticatedEntity.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_booking.models.room_configuration_authenticated_entity import RoomConfigurationAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationAuthenticatedEntity from a JSON string
room_configuration_authenticated_entity_instance = RoomConfigurationAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationAuthenticatedEntity.to_json())

# convert the object into a dict
room_configuration_authenticated_entity_dict = room_configuration_authenticated_entity_instance.to_dict()
# create an instance of RoomConfigurationAuthenticatedEntity from a dict
room_configuration_authenticated_entity_from_dict = RoomConfigurationAuthenticatedEntity.from_dict(room_configuration_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


