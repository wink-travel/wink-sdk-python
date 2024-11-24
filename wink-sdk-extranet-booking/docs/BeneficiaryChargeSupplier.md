# BeneficiaryChargeSupplier

A variable charge can be a fixed amount or a percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of charge | 
**percent** | **float** | A percentage of the total stay amount for an early checkin or late checkout | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.beneficiary_charge_supplier import BeneficiaryChargeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryChargeSupplier from a JSON string
beneficiary_charge_supplier_instance = BeneficiaryChargeSupplier.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryChargeSupplier.to_json())

# convert the object into a dict
beneficiary_charge_supplier_dict = beneficiary_charge_supplier_instance.to_dict()
# create an instance of BeneficiaryChargeSupplier from a dict
beneficiary_charge_supplier_from_dict = BeneficiaryChargeSupplier.from_dict(beneficiary_charge_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


