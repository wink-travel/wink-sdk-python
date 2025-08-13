# FilterDescriptorAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** |  | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from wink_sdk_analytics.models.filter_descriptor_authenticated_entity import FilterDescriptorAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorAuthenticatedEntity from a JSON string
filter_descriptor_authenticated_entity_instance = FilterDescriptorAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorAuthenticatedEntity.to_json())

# convert the object into a dict
filter_descriptor_authenticated_entity_dict = filter_descriptor_authenticated_entity_instance.to_dict()
# create an instance of FilterDescriptorAuthenticatedEntity from a dict
filter_descriptor_authenticated_entity_from_dict = FilterDescriptorAuthenticatedEntity.from_dict(filter_descriptor_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


