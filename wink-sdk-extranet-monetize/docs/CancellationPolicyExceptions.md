# CancellationPolicyExceptions

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyException]**](CancellationPolicyException.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_extranet_monetize.models.cancellation_policy_exceptions import CancellationPolicyExceptions

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptions from a JSON string
cancellation_policy_exceptions_instance = CancellationPolicyExceptions.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptions.to_json())

# convert the object into a dict
cancellation_policy_exceptions_dict = cancellation_policy_exceptions_instance.to_dict()
# create an instance of CancellationPolicyExceptions from a dict
cancellation_policy_exceptions_from_dict = CancellationPolicyExceptions.from_dict(cancellation_policy_exceptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


