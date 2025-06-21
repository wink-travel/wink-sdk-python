# AggregateDescriptorAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.aggregate_descriptor_agent import AggregateDescriptorAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorAgent from a JSON string
aggregate_descriptor_agent_instance = AggregateDescriptorAgent.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorAgent.to_json())

# convert the object into a dict
aggregate_descriptor_agent_dict = aggregate_descriptor_agent_instance.to_dict()
# create an instance of AggregateDescriptorAgent from a dict
aggregate_descriptor_agent_from_dict = AggregateDescriptorAgent.from_dict(aggregate_descriptor_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


