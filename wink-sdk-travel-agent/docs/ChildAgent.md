# ChildAgent

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_travel_agent.models.child_agent import ChildAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAgent from a JSON string
child_agent_instance = ChildAgent.from_json(json)
# print the JSON string representation of the object
print(ChildAgent.to_json())

# convert the object into a dict
child_agent_dict = child_agent_instance.to_dict()
# create an instance of ChildAgent from a dict
child_agent_from_dict = ChildAgent.from_dict(child_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


