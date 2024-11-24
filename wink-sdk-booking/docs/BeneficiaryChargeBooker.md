# BeneficiaryChargeBooker

A variable charge can be a fixed amount or a percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of charge | 
**percent** | **float** | A percentage of the total stay amount for an early checkin or late checkout | [optional] 

## Example

```python
from wink_sdk_booking.models.beneficiary_charge_booker import BeneficiaryChargeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryChargeBooker from a JSON string
beneficiary_charge_booker_instance = BeneficiaryChargeBooker.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryChargeBooker.to_json())

# convert the object into a dict
beneficiary_charge_booker_dict = beneficiary_charge_booker_instance.to_dict()
# create an instance of BeneficiaryChargeBooker from a dict
beneficiary_charge_booker_from_dict = BeneficiaryChargeBooker.from_dict(beneficiary_charge_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


