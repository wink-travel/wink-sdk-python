# ExtraChargeAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeAgent**](RatePlanLevelFeeAgent.md) | What the guest is paying extra for | [optional] 
**unit_price** | [**LocalizedPriceAgent**](LocalizedPriceAgent.md) | The localized unit price of the extra charge | [optional] 
**price** | [**LocalizedPriceAgent**](LocalizedPriceAgent.md) | The localized price of the extra charge | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.extra_charge_agent import ExtraChargeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeAgent from a JSON string
extra_charge_agent_instance = ExtraChargeAgent.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeAgent.to_json())

# convert the object into a dict
extra_charge_agent_dict = extra_charge_agent_instance.to_dict()
# create an instance of ExtraChargeAgent from a dict
extra_charge_agent_from_dict = ExtraChargeAgent.from_dict(extra_charge_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


