# RoomConfigurationBooker

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildBooker]**](ChildBooker.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_booking.models.room_configuration_booker import RoomConfigurationBooker

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationBooker from a JSON string
room_configuration_booker_instance = RoomConfigurationBooker.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationBooker.to_json())

# convert the object into a dict
room_configuration_booker_dict = room_configuration_booker_instance.to_dict()
# create an instance of RoomConfigurationBooker from a dict
room_configuration_booker_from_dict = RoomConfigurationBooker.from_dict(room_configuration_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


