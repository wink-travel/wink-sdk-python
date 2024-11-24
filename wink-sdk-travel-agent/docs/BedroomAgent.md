# BedroomAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedAgent]**](BedAgent.md) | A bedroom can have more than one bed type. | 

## Example

```python
from wink_sdk_travel_agent.models.bedroom_agent import BedroomAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomAgent from a JSON string
bedroom_agent_instance = BedroomAgent.from_json(json)
# print the JSON string representation of the object
print(BedroomAgent.to_json())

# convert the object into a dict
bedroom_agent_dict = bedroom_agent_instance.to_dict()
# create an instance of BedroomAgent from a dict
bedroom_agent_from_dict = BedroomAgent.from_dict(bedroom_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


