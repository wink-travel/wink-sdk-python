# SortDescriptorAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_analytics.models.sort_descriptor_authenticated_entity import SortDescriptorAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorAuthenticatedEntity from a JSON string
sort_descriptor_authenticated_entity_instance = SortDescriptorAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorAuthenticatedEntity.to_json())

# convert the object into a dict
sort_descriptor_authenticated_entity_dict = sort_descriptor_authenticated_entity_instance.to_dict()
# create an instance of SortDescriptorAuthenticatedEntity from a dict
sort_descriptor_authenticated_entity_from_dict = SortDescriptorAuthenticatedEntity.from_dict(sort_descriptor_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


