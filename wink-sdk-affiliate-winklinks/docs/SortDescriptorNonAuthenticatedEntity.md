# SortDescriptorNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.sort_descriptor_non_authenticated_entity import SortDescriptorNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorNonAuthenticatedEntity from a JSON string
sort_descriptor_non_authenticated_entity_instance = SortDescriptorNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorNonAuthenticatedEntity.to_json())

# convert the object into a dict
sort_descriptor_non_authenticated_entity_dict = sort_descriptor_non_authenticated_entity_instance.to_dict()
# create an instance of SortDescriptorNonAuthenticatedEntity from a dict
sort_descriptor_non_authenticated_entity_from_dict = SortDescriptorNonAuthenticatedEntity.from_dict(sort_descriptor_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


