# CancellationPolicyExceptionsNonAuthenticatedEntity

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyExceptionNonAuthenticatedEntity]**](CancellationPolicyExceptionNonAuthenticatedEntity.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_lookup.models.cancellation_policy_exceptions_non_authenticated_entity import CancellationPolicyExceptionsNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionsNonAuthenticatedEntity from a JSON string
cancellation_policy_exceptions_non_authenticated_entity_instance = CancellationPolicyExceptionsNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionsNonAuthenticatedEntity.to_json())

# convert the object into a dict
cancellation_policy_exceptions_non_authenticated_entity_dict = cancellation_policy_exceptions_non_authenticated_entity_instance.to_dict()
# create an instance of CancellationPolicyExceptionsNonAuthenticatedEntity from a dict
cancellation_policy_exceptions_non_authenticated_entity_from_dict = CancellationPolicyExceptionsNonAuthenticatedEntity.from_dict(cancellation_policy_exceptions_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


