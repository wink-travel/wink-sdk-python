# AxisTicksSupplier

The configuration of the category axis minor ticks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**size** | **float** |  | [optional] 
**step** | **float** |  | [optional] 
**skip** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.axis_ticks_supplier import AxisTicksSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AxisTicksSupplier from a JSON string
axis_ticks_supplier_instance = AxisTicksSupplier.from_json(json)
# print the JSON string representation of the object
print(AxisTicksSupplier.to_json())

# convert the object into a dict
axis_ticks_supplier_dict = axis_ticks_supplier_instance.to_dict()
# create an instance of AxisTicksSupplier from a dict
axis_ticks_supplier_from_dict = AxisTicksSupplier.from_dict(axis_ticks_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


