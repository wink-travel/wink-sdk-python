# BeneficiaryChargeAgent

A variable charge can be a fixed amount or a percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of charge | 
**percent** | **float** | A percentage of the total stay amount for an early checkin or late checkout | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.beneficiary_charge_agent import BeneficiaryChargeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryChargeAgent from a JSON string
beneficiary_charge_agent_instance = BeneficiaryChargeAgent.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryChargeAgent.to_json())

# convert the object into a dict
beneficiary_charge_agent_dict = beneficiary_charge_agent_instance.to_dict()
# create an instance of BeneficiaryChargeAgent from a dict
beneficiary_charge_agent_from_dict = BeneficiaryChargeAgent.from_dict(beneficiary_charge_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


