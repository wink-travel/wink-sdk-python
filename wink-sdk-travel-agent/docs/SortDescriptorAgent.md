# SortDescriptorAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.sort_descriptor_agent import SortDescriptorAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorAgent from a JSON string
sort_descriptor_agent_instance = SortDescriptorAgent.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorAgent.to_json())

# convert the object into a dict
sort_descriptor_agent_dict = sort_descriptor_agent_instance.to_dict()
# create an instance of SortDescriptorAgent from a dict
sort_descriptor_agent_from_dict = SortDescriptorAgent.from_dict(sort_descriptor_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


