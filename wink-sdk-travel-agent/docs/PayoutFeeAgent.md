# PayoutFeeAgent

Fees incurred when making the withdrawal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Type of fee | 
**candidate** | **str** | Who pays for this fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_travel_agent.models.payout_fee_agent import PayoutFeeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutFeeAgent from a JSON string
payout_fee_agent_instance = PayoutFeeAgent.from_json(json)
# print the JSON string representation of the object
print(PayoutFeeAgent.to_json())

# convert the object into a dict
payout_fee_agent_dict = payout_fee_agent_instance.to_dict()
# create an instance of PayoutFeeAgent from a dict
payout_fee_agent_from_dict = PayoutFeeAgent.from_dict(payout_fee_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


