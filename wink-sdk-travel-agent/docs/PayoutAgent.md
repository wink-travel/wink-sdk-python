# PayoutAgent

Payout keeps track of all outgoing funds for a certain account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | Name of integration vendor | 
**vendor_identifier** | **str** | Which acquirer account we return fund from. | 
**vendor_name** | **str** | Name of regional acquirer account. | 
**ledger_identifier** | **str** | Unique system ID. | 
**beneficiary_identifier** | **str** | Beneficiary ID. | 
**external_payee_identifier** | **str** | This would be the Wise recipient ID. | 
**type** | **str** | Type of withdrawal. | 
**entry** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**fees** | [**List[PayoutFeeAgent]**](PayoutFeeAgent.md) | Fees incurred when making the withdrawal. | [optional] 
**quote** | [**QuoteAgent**](QuoteAgent.md) |  | [optional] 
**created** | **datetime** | When the payout record was created. | 
**description** | **str** | Textual response from provider | [optional] 
**payout_id** | **str** | The ledgerIdentifier that was generated when scheduling the payout. This will come from the payout provider such as Stripe. | [optional] 
**reference_code** | **str** | The transaction code that was generated when the funds move out of TripPay&#39;s account. This will come from the payout provider such as Stripe. E.g. For VCCs, it will occur when an authorization takes place. | [optional] 
**reference_code_date** | **datetime** | The time the funds were withdrawn | [optional] 
**status** | **str** | Status of withdrawal. | 

## Example

```python
from wink_sdk_travel_agent.models.payout_agent import PayoutAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutAgent from a JSON string
payout_agent_instance = PayoutAgent.from_json(json)
# print the JSON string representation of the object
print(PayoutAgent.to_json())

# convert the object into a dict
payout_agent_dict = payout_agent_instance.to_dict()
# create an instance of PayoutAgent from a dict
payout_agent_from_dict = PayoutAgent.from_dict(payout_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


