# GroupDescriptorAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorAgent]**](AggregateDescriptorAgent.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.group_descriptor_agent import GroupDescriptorAgent

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorAgent from a JSON string
group_descriptor_agent_instance = GroupDescriptorAgent.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorAgent.to_json())

# convert the object into a dict
group_descriptor_agent_dict = group_descriptor_agent_instance.to_dict()
# create an instance of GroupDescriptorAgent from a dict
group_descriptor_agent_from_dict = GroupDescriptorAgent.from_dict(group_descriptor_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


