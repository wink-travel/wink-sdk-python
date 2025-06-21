# VariableChargeSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | When the type is FIXED, fixedAmount is required. When the type is PERCENTAGE, percent is required. | 
**percent** | **float** | A percentage of the total stay amount for an early check-in or late check-out | [optional] 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | A localized amount | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.variable_charge_supplier import VariableChargeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of VariableChargeSupplier from a JSON string
variable_charge_supplier_instance = VariableChargeSupplier.from_json(json)
# print the JSON string representation of the object
print(VariableChargeSupplier.to_json())

# convert the object into a dict
variable_charge_supplier_dict = variable_charge_supplier_instance.to_dict()
# create an instance of VariableChargeSupplier from a dict
variable_charge_supplier_from_dict = VariableChargeSupplier.from_dict(variable_charge_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


