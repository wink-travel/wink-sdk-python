# ReportingAncillaryAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of ancillary in English. | [optional] 
**type** | **str** | The type | [optional] 
**gross_amount** | **float** | The gross amount. | [optional] 
**net_amount** | **float** | The gross amount minus fees and commissions. | [optional] 
**net_amount_with_refund** | **float** | The gross amount minus fees and commissions. | [optional] 
**currency** | **str** | The currency for these amounts. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.reporting_ancillary_agent import ReportingAncillaryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingAncillaryAgent from a JSON string
reporting_ancillary_agent_instance = ReportingAncillaryAgent.from_json(json)
# print the JSON string representation of the object
print(ReportingAncillaryAgent.to_json())

# convert the object into a dict
reporting_ancillary_agent_dict = reporting_ancillary_agent_instance.to_dict()
# create an instance of ReportingAncillaryAgent from a dict
reporting_ancillary_agent_from_dict = ReportingAncillaryAgent.from_dict(reporting_ancillary_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


