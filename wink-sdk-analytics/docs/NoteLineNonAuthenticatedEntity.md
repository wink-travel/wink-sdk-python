# NoteLineNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.note_line_non_authenticated_entity import NoteLineNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of NoteLineNonAuthenticatedEntity from a JSON string
note_line_non_authenticated_entity_instance = NoteLineNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(NoteLineNonAuthenticatedEntity.to_json())

# convert the object into a dict
note_line_non_authenticated_entity_dict = note_line_non_authenticated_entity_instance.to_dict()
# create an instance of NoteLineNonAuthenticatedEntity from a dict
note_line_non_authenticated_entity_from_dict = NoteLineNonAuthenticatedEntity.from_dict(note_line_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


