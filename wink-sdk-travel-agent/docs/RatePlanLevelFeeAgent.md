# RatePlanLevelFeeAgent

What the guest is paying extra for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionAgent]**](LocalizedDescriptionAgent.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_travel_agent.models.rate_plan_level_fee_agent import RatePlanLevelFeeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeAgent from a JSON string
rate_plan_level_fee_agent_instance = RatePlanLevelFeeAgent.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeAgent.to_json())

# convert the object into a dict
rate_plan_level_fee_agent_dict = rate_plan_level_fee_agent_instance.to_dict()
# create an instance of RatePlanLevelFeeAgent from a dict
rate_plan_level_fee_agent_from_dict = RatePlanLevelFeeAgent.from_dict(rate_plan_level_fee_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


