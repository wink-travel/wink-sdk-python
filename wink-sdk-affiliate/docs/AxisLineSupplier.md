# AxisLineSupplier

The configuration of the axis lines. Also affects the major and minor ticks, but not the grid lines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.axis_line_supplier import AxisLineSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AxisLineSupplier from a JSON string
axis_line_supplier_instance = AxisLineSupplier.from_json(json)
# print the JSON string representation of the object
print(AxisLineSupplier.to_json())

# convert the object into a dict
axis_line_supplier_dict = axis_line_supplier_instance.to_dict()
# create an instance of AxisLineSupplier from a dict
axis_line_supplier_from_dict = AxisLineSupplier.from_dict(axis_line_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


