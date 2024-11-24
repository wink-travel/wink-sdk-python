# ReportingExtraChargeAgent

Displays extra charge accounting details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gross_amount** | **float** |  | [optional] 
**net_amount** | **float** |  | [optional] 
**net_amount_with_refund** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.reporting_extra_charge_agent import ReportingExtraChargeAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingExtraChargeAgent from a JSON string
reporting_extra_charge_agent_instance = ReportingExtraChargeAgent.from_json(json)
# print the JSON string representation of the object
print(ReportingExtraChargeAgent.to_json())

# convert the object into a dict
reporting_extra_charge_agent_dict = reporting_extra_charge_agent_instance.to_dict()
# create an instance of ReportingExtraChargeAgent from a dict
reporting_extra_charge_agent_from_dict = ReportingExtraChargeAgent.from_dict(reporting_extra_charge_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


