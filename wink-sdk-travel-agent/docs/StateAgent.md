# StateAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorAgent]**](SortDescriptorAgent.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorAgent**](CompositeFilterDescriptorAgent.md) |  | [optional] 
**group** | [**List[GroupDescriptorAgent]**](GroupDescriptorAgent.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.state_agent import StateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of StateAgent from a JSON string
state_agent_instance = StateAgent.from_json(json)
# print the JSON string representation of the object
print(StateAgent.to_json())

# convert the object into a dict
state_agent_dict = state_agent_instance.to_dict()
# create an instance of StateAgent from a dict
state_agent_from_dict = StateAgent.from_dict(state_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


