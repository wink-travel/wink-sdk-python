# VariableCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | When the type is FIXED, fixedAmount is required. When the type is PERCENTAGE, percent is required. | 
**percent** | **float** | A percentage of the total stay amount for an early check-in or late check-out | [optional] 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.variable_charge import VariableCharge

# TODO update the JSON string below
json = "{}"
# create an instance of VariableCharge from a JSON string
variable_charge_instance = VariableCharge.from_json(json)
# print the JSON string representation of the object
print(VariableCharge.to_json())

# convert the object into a dict
variable_charge_dict = variable_charge_instance.to_dict()
# create an instance of VariableCharge from a dict
variable_charge_from_dict = VariableCharge.from_dict(variable_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


