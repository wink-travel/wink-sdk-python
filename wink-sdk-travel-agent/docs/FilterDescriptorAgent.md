# FilterDescriptorAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** |  | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.filter_descriptor_agent import FilterDescriptorAgent

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorAgent from a JSON string
filter_descriptor_agent_instance = FilterDescriptorAgent.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorAgent.to_json())

# convert the object into a dict
filter_descriptor_agent_dict = filter_descriptor_agent_instance.to_dict()
# create an instance of FilterDescriptorAgent from a dict
filter_descriptor_agent_from_dict = FilterDescriptorAgent.from_dict(filter_descriptor_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


