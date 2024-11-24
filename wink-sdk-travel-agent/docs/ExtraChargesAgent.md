# ExtraChargesAgent

Rate plan-level extra charges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeAgent]**](ExtraChargeAgent.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.extra_charges_agent import ExtraChargesAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesAgent from a JSON string
extra_charges_agent_instance = ExtraChargesAgent.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesAgent.to_json())

# convert the object into a dict
extra_charges_agent_dict = extra_charges_agent_instance.to_dict()
# create an instance of ExtraChargesAgent from a dict
extra_charges_agent_from_dict = ExtraChargesAgent.from_dict(extra_charges_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


