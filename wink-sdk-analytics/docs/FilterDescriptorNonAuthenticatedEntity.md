# FilterDescriptorNonAuthenticatedEntity

Descriptors used for filtering the result set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** | Value to filter dataset against | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from wink_sdk_analytics.models.filter_descriptor_non_authenticated_entity import FilterDescriptorNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorNonAuthenticatedEntity from a JSON string
filter_descriptor_non_authenticated_entity_instance = FilterDescriptorNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorNonAuthenticatedEntity.to_json())

# convert the object into a dict
filter_descriptor_non_authenticated_entity_dict = filter_descriptor_non_authenticated_entity_instance.to_dict()
# create an instance of FilterDescriptorNonAuthenticatedEntity from a dict
filter_descriptor_non_authenticated_entity_from_dict = FilterDescriptorNonAuthenticatedEntity.from_dict(filter_descriptor_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


