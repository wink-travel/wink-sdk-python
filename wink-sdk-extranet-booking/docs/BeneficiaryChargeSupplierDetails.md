# BeneficiaryChargeSupplierDetails

A variable charge can be a fixed amount or a percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of charge | 
**percent** | **float** | A percentage of the total stay amount for an early checkin or late checkout | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.beneficiary_charge_supplier_details import BeneficiaryChargeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryChargeSupplierDetails from a JSON string
beneficiary_charge_supplier_details_instance = BeneficiaryChargeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryChargeSupplierDetails.to_json())

# convert the object into a dict
beneficiary_charge_supplier_details_dict = beneficiary_charge_supplier_details_instance.to_dict()
# create an instance of BeneficiaryChargeSupplierDetails from a dict
beneficiary_charge_supplier_details_from_dict = BeneficiaryChargeSupplierDetails.from_dict(beneficiary_charge_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


