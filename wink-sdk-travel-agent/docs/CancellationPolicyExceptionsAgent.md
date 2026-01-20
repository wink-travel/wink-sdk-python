# CancellationPolicyExceptionsAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyExceptionAgent]**](CancellationPolicyExceptionAgent.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_travel_agent.models.cancellation_policy_exceptions_agent import CancellationPolicyExceptionsAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionsAgent from a JSON string
cancellation_policy_exceptions_agent_instance = CancellationPolicyExceptionsAgent.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionsAgent.to_json())

# convert the object into a dict
cancellation_policy_exceptions_agent_dict = cancellation_policy_exceptions_agent_instance.to_dict()
# create an instance of CancellationPolicyExceptionsAgent from a dict
cancellation_policy_exceptions_agent_from_dict = CancellationPolicyExceptionsAgent.from_dict(cancellation_policy_exceptions_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


