# CancellationDetailAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_type** | **str** | Cancellation type | 
**reason** | **str** | Reason for cancellation | 

## Example

```python
from wink_sdk_travel_agent.models.cancellation_detail_agent import CancellationDetailAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationDetailAgent from a JSON string
cancellation_detail_agent_instance = CancellationDetailAgent.from_json(json)
# print the JSON string representation of the object
print(CancellationDetailAgent.to_json())

# convert the object into a dict
cancellation_detail_agent_dict = cancellation_detail_agent_instance.to_dict()
# create an instance of CancellationDetailAgent from a dict
cancellation_detail_agent_from_dict = CancellationDetailAgent.from_dict(cancellation_detail_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


