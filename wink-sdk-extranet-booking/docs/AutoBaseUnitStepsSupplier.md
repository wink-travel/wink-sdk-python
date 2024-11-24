# AutoBaseUnitStepsSupplier

The time-interval steps when `baseUnit` is set either to `fit` or `auto`. The axis will try to divide the active period into the smallest possible units that yield `maxDateGroups` or less discrete intervals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milliseconds** | **float** |  | [optional] 
**seconds** | **float** |  | [optional] 
**minutes** | **float** |  | [optional] 
**hours** | **float** |  | [optional] 
**days** | **float** |  | [optional] 
**weeks** | **float** |  | [optional] 
**months** | **float** |  | [optional] 
**years** | **float** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.auto_base_unit_steps_supplier import AutoBaseUnitStepsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AutoBaseUnitStepsSupplier from a JSON string
auto_base_unit_steps_supplier_instance = AutoBaseUnitStepsSupplier.from_json(json)
# print the JSON string representation of the object
print(AutoBaseUnitStepsSupplier.to_json())

# convert the object into a dict
auto_base_unit_steps_supplier_dict = auto_base_unit_steps_supplier_instance.to_dict()
# create an instance of AutoBaseUnitStepsSupplier from a dict
auto_base_unit_steps_supplier_from_dict = AutoBaseUnitStepsSupplier.from_dict(auto_base_unit_steps_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


