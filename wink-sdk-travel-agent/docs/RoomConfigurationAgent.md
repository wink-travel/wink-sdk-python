# RoomConfigurationAgent

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildAgent]**](ChildAgent.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.room_configuration_agent import RoomConfigurationAgent

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationAgent from a JSON string
room_configuration_agent_instance = RoomConfigurationAgent.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationAgent.to_json())

# convert the object into a dict
room_configuration_agent_dict = room_configuration_agent_instance.to_dict()
# create an instance of RoomConfigurationAgent from a dict
room_configuration_agent_from_dict = RoomConfigurationAgent.from_dict(room_configuration_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


