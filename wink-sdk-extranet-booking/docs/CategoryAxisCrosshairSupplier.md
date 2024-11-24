# CategoryAxisCrosshairSupplier

The configuration options of the crosshair. The crosshair is displayed when the `categoryAxis.crosshair.visible` option is set to `true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**opacity** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 
**tooltip** | [**CategoryAxisCrosshairTooltipSupplier**](CategoryAxisCrosshairTooltipSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.category_axis_crosshair_supplier import CategoryAxisCrosshairSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisCrosshairSupplier from a JSON string
category_axis_crosshair_supplier_instance = CategoryAxisCrosshairSupplier.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisCrosshairSupplier.to_json())

# convert the object into a dict
category_axis_crosshair_supplier_dict = category_axis_crosshair_supplier_instance.to_dict()
# create an instance of CategoryAxisCrosshairSupplier from a dict
category_axis_crosshair_supplier_from_dict = CategoryAxisCrosshairSupplier.from_dict(category_axis_crosshair_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


