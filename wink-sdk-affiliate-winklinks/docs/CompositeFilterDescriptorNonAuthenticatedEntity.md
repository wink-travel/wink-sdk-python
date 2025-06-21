# CompositeFilterDescriptorNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorNonAuthenticatedEntity]**](FilterDescriptorNonAuthenticatedEntity.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.composite_filter_descriptor_non_authenticated_entity import CompositeFilterDescriptorNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorNonAuthenticatedEntity from a JSON string
composite_filter_descriptor_non_authenticated_entity_instance = CompositeFilterDescriptorNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorNonAuthenticatedEntity.to_json())

# convert the object into a dict
composite_filter_descriptor_non_authenticated_entity_dict = composite_filter_descriptor_non_authenticated_entity_instance.to_dict()
# create an instance of CompositeFilterDescriptorNonAuthenticatedEntity from a dict
composite_filter_descriptor_non_authenticated_entity_from_dict = CompositeFilterDescriptorNonAuthenticatedEntity.from_dict(composite_filter_descriptor_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


