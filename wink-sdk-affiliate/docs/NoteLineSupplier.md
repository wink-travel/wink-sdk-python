# NoteLineSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.note_line_supplier import NoteLineSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of NoteLineSupplier from a JSON string
note_line_supplier_instance = NoteLineSupplier.from_json(json)
# print the JSON string representation of the object
print(NoteLineSupplier.to_json())

# convert the object into a dict
note_line_supplier_dict = note_line_supplier_instance.to_dict()
# create an instance of NoteLineSupplier from a dict
note_line_supplier_from_dict = NoteLineSupplier.from_dict(note_line_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


