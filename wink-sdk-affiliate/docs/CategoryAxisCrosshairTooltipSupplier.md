# CategoryAxisCrosshairTooltipSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**border** | [**BorderSupplier**](BorderSupplier.md) |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**padding** | [**PaddingSupplier**](PaddingSupplier.md) |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.category_axis_crosshair_tooltip_supplier import CategoryAxisCrosshairTooltipSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisCrosshairTooltipSupplier from a JSON string
category_axis_crosshair_tooltip_supplier_instance = CategoryAxisCrosshairTooltipSupplier.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisCrosshairTooltipSupplier.to_json())

# convert the object into a dict
category_axis_crosshair_tooltip_supplier_dict = category_axis_crosshair_tooltip_supplier_instance.to_dict()
# create an instance of CategoryAxisCrosshairTooltipSupplier from a dict
category_axis_crosshair_tooltip_supplier_from_dict = CategoryAxisCrosshairTooltipSupplier.from_dict(category_axis_crosshair_tooltip_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


