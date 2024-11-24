# CompositeFilterDescriptorAgent

Descriptors used for filtering result set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorAgent]**](FilterDescriptorAgent.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.composite_filter_descriptor_agent import CompositeFilterDescriptorAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorAgent from a JSON string
composite_filter_descriptor_agent_instance = CompositeFilterDescriptorAgent.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorAgent.to_json())

# convert the object into a dict
composite_filter_descriptor_agent_dict = composite_filter_descriptor_agent_instance.to_dict()
# create an instance of CompositeFilterDescriptorAgent from a dict
composite_filter_descriptor_agent_from_dict = CompositeFilterDescriptorAgent.from_dict(composite_filter_descriptor_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


