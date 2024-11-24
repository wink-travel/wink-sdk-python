# CategoryAxisNotesLabelSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**border** | [**BorderSupplier**](BorderSupplier.md) |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**rotation** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.category_axis_notes_label_supplier import CategoryAxisNotesLabelSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisNotesLabelSupplier from a JSON string
category_axis_notes_label_supplier_instance = CategoryAxisNotesLabelSupplier.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisNotesLabelSupplier.to_json())

# convert the object into a dict
category_axis_notes_label_supplier_dict = category_axis_notes_label_supplier_instance.to_dict()
# create an instance of CategoryAxisNotesLabelSupplier from a dict
category_axis_notes_label_supplier_from_dict = CategoryAxisNotesLabelSupplier.from_dict(category_axis_notes_label_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


