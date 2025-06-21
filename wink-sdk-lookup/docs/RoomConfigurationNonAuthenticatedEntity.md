# RoomConfigurationNonAuthenticatedEntity

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildNonAuthenticatedEntity]**](ChildNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.room_configuration_non_authenticated_entity import RoomConfigurationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationNonAuthenticatedEntity from a JSON string
room_configuration_non_authenticated_entity_instance = RoomConfigurationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_configuration_non_authenticated_entity_dict = room_configuration_non_authenticated_entity_instance.to_dict()
# create an instance of RoomConfigurationNonAuthenticatedEntity from a dict
room_configuration_non_authenticated_entity_from_dict = RoomConfigurationNonAuthenticatedEntity.from_dict(room_configuration_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


