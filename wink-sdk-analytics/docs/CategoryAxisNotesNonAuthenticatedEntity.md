# CategoryAxisNotesNonAuthenticatedEntity

The configuration of the category axis notes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**line** | [**NoteLineNonAuthenticatedEntity**](NoteLineNonAuthenticatedEntity.md) |  | [optional] 
**position** | **str** |  | [optional] 
**icon** | [**CategoryAxisNotesIconNonAuthenticatedEntity**](CategoryAxisNotesIconNonAuthenticatedEntity.md) |  | [optional] 
**label** | [**CategoryAxisNotesLabelNonAuthenticatedEntity**](CategoryAxisNotesLabelNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.category_axis_notes_non_authenticated_entity import CategoryAxisNotesNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisNotesNonAuthenticatedEntity from a JSON string
category_axis_notes_non_authenticated_entity_instance = CategoryAxisNotesNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisNotesNonAuthenticatedEntity.to_json())

# convert the object into a dict
category_axis_notes_non_authenticated_entity_dict = category_axis_notes_non_authenticated_entity_instance.to_dict()
# create an instance of CategoryAxisNotesNonAuthenticatedEntity from a dict
category_axis_notes_non_authenticated_entity_from_dict = CategoryAxisNotesNonAuthenticatedEntity.from_dict(category_axis_notes_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


