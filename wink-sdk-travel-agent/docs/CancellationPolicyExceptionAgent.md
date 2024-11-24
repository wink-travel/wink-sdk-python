# CancellationPolicyExceptionAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyAgent**](CancellationPolicyAgent.md) |  | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_travel_agent.models.cancellation_policy_exception_agent import CancellationPolicyExceptionAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionAgent from a JSON string
cancellation_policy_exception_agent_instance = CancellationPolicyExceptionAgent.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionAgent.to_json())

# convert the object into a dict
cancellation_policy_exception_agent_dict = cancellation_policy_exception_agent_instance.to_dict()
# create an instance of CancellationPolicyExceptionAgent from a dict
cancellation_policy_exception_agent_from_dict = CancellationPolicyExceptionAgent.from_dict(cancellation_policy_exception_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


