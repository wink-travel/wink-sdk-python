# CategoryAxisNotesLabelNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**border** | [**BorderNonAuthenticatedEntity**](BorderNonAuthenticatedEntity.md) |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**rotation** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.category_axis_notes_label_non_authenticated_entity import CategoryAxisNotesLabelNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisNotesLabelNonAuthenticatedEntity from a JSON string
category_axis_notes_label_non_authenticated_entity_instance = CategoryAxisNotesLabelNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisNotesLabelNonAuthenticatedEntity.to_json())

# convert the object into a dict
category_axis_notes_label_non_authenticated_entity_dict = category_axis_notes_label_non_authenticated_entity_instance.to_dict()
# create an instance of CategoryAxisNotesLabelNonAuthenticatedEntity from a dict
category_axis_notes_label_non_authenticated_entity_from_dict = CategoryAxisNotesLabelNonAuthenticatedEntity.from_dict(category_axis_notes_label_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


