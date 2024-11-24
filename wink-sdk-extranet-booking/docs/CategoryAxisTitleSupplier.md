# CategoryAxisTitleSupplier

Title of axis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**border** | [**BorderSupplier**](BorderSupplier.md) |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**margin** | [**MarginSupplier**](MarginSupplier.md) |  | [optional] 
**padding** | [**PaddingSupplier**](PaddingSupplier.md) |  | [optional] 
**position** | **str** |  | [optional] 
**rotation** | **float** |  | [optional] 
**text** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.category_axis_title_supplier import CategoryAxisTitleSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisTitleSupplier from a JSON string
category_axis_title_supplier_instance = CategoryAxisTitleSupplier.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisTitleSupplier.to_json())

# convert the object into a dict
category_axis_title_supplier_dict = category_axis_title_supplier_instance.to_dict()
# create an instance of CategoryAxisTitleSupplier from a dict
category_axis_title_supplier_from_dict = CategoryAxisTitleSupplier.from_dict(category_axis_title_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


