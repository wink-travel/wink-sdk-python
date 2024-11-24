# CategoryAxisTitleNonAuthenticatedEntity

Title of axis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**border** | [**BorderNonAuthenticatedEntity**](BorderNonAuthenticatedEntity.md) |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**margin** | [**MarginNonAuthenticatedEntity**](MarginNonAuthenticatedEntity.md) |  | [optional] 
**padding** | [**PaddingNonAuthenticatedEntity**](PaddingNonAuthenticatedEntity.md) |  | [optional] 
**position** | **str** |  | [optional] 
**rotation** | **float** |  | [optional] 
**text** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.category_axis_title_non_authenticated_entity import CategoryAxisTitleNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisTitleNonAuthenticatedEntity from a JSON string
category_axis_title_non_authenticated_entity_instance = CategoryAxisTitleNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisTitleNonAuthenticatedEntity.to_json())

# convert the object into a dict
category_axis_title_non_authenticated_entity_dict = category_axis_title_non_authenticated_entity_instance.to_dict()
# create an instance of CategoryAxisTitleNonAuthenticatedEntity from a dict
category_axis_title_non_authenticated_entity_from_dict = CategoryAxisTitleNonAuthenticatedEntity.from_dict(category_axis_title_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


