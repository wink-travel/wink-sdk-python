# CompositeFilterDescriptorAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorAuthenticatedEntity]**](FilterDescriptorAuthenticatedEntity.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_analytics.models.composite_filter_descriptor_authenticated_entity import CompositeFilterDescriptorAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorAuthenticatedEntity from a JSON string
composite_filter_descriptor_authenticated_entity_instance = CompositeFilterDescriptorAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorAuthenticatedEntity.to_json())

# convert the object into a dict
composite_filter_descriptor_authenticated_entity_dict = composite_filter_descriptor_authenticated_entity_instance.to_dict()
# create an instance of CompositeFilterDescriptorAuthenticatedEntity from a dict
composite_filter_descriptor_authenticated_entity_from_dict = CompositeFilterDescriptorAuthenticatedEntity.from_dict(composite_filter_descriptor_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


