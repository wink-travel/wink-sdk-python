# CategoryAxisNotesSupplier

The configuration of the category axis notes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**line** | [**NoteLineSupplier**](NoteLineSupplier.md) |  | [optional] 
**position** | **str** |  | [optional] 
**icon** | [**CategoryAxisNotesIconSupplier**](CategoryAxisNotesIconSupplier.md) |  | [optional] 
**label** | [**CategoryAxisNotesLabelSupplier**](CategoryAxisNotesLabelSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.category_axis_notes_supplier import CategoryAxisNotesSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisNotesSupplier from a JSON string
category_axis_notes_supplier_instance = CategoryAxisNotesSupplier.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisNotesSupplier.to_json())

# convert the object into a dict
category_axis_notes_supplier_dict = category_axis_notes_supplier_instance.to_dict()
# create an instance of CategoryAxisNotesSupplier from a dict
category_axis_notes_supplier_from_dict = CategoryAxisNotesSupplier.from_dict(category_axis_notes_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


