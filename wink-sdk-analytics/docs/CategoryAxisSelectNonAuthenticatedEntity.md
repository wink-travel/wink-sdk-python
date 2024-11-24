# CategoryAxisSelectNonAuthenticatedEntity

The selected axis range. If set, the axis selection is enabled. The range is index-based, starting from zero. Categories with indexes in the range (`select.from`, `select.to`) will be selected. That is, the last category in the range will not be included in the selection. If the categories are dates, the range has to be also specified with date values. Selection is only supported if the axis is horizontal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **object** |  | [optional] 
**max** | **object** |  | [optional] 
**min** | **object** |  | [optional] 
**mousewheel** | **object** |  | [optional] 
**to** | **object** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.category_axis_select_non_authenticated_entity import CategoryAxisSelectNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisSelectNonAuthenticatedEntity from a JSON string
category_axis_select_non_authenticated_entity_instance = CategoryAxisSelectNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisSelectNonAuthenticatedEntity.to_json())

# convert the object into a dict
category_axis_select_non_authenticated_entity_dict = category_axis_select_non_authenticated_entity_instance.to_dict()
# create an instance of CategoryAxisSelectNonAuthenticatedEntity from a dict
category_axis_select_non_authenticated_entity_from_dict = CategoryAxisSelectNonAuthenticatedEntity.from_dict(category_axis_select_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


