# CancellationPolicyExceptionsAuthenticatedEntity

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyExceptionAuthenticatedEntity]**](CancellationPolicyExceptionAuthenticatedEntity.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_booking.models.cancellation_policy_exceptions_authenticated_entity import CancellationPolicyExceptionsAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionsAuthenticatedEntity from a JSON string
cancellation_policy_exceptions_authenticated_entity_instance = CancellationPolicyExceptionsAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionsAuthenticatedEntity.to_json())

# convert the object into a dict
cancellation_policy_exceptions_authenticated_entity_dict = cancellation_policy_exceptions_authenticated_entity_instance.to_dict()
# create an instance of CancellationPolicyExceptionsAuthenticatedEntity from a dict
cancellation_policy_exceptions_authenticated_entity_from_dict = CancellationPolicyExceptionsAuthenticatedEntity.from_dict(cancellation_policy_exceptions_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


