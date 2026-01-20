# FeeAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Fee amount | 
**type** | **str** | Type of fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_travel_agent.models.fee_agent import FeeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of FeeAgent from a JSON string
fee_agent_instance = FeeAgent.from_json(json)
# print the JSON string representation of the object
print(FeeAgent.to_json())

# convert the object into a dict
fee_agent_dict = fee_agent_instance.to_dict()
# create an instance of FeeAgent from a dict
fee_agent_from_dict = FeeAgent.from_dict(fee_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


