# CancellationPolicyExceptionNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyNonAuthenticatedEntity**](CancellationPolicyNonAuthenticatedEntity.md) |  | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_inventory.models.cancellation_policy_exception_non_authenticated_entity import CancellationPolicyExceptionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionNonAuthenticatedEntity from a JSON string
cancellation_policy_exception_non_authenticated_entity_instance = CancellationPolicyExceptionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionNonAuthenticatedEntity.to_json())

# convert the object into a dict
cancellation_policy_exception_non_authenticated_entity_dict = cancellation_policy_exception_non_authenticated_entity_instance.to_dict()
# create an instance of CancellationPolicyExceptionNonAuthenticatedEntity from a dict
cancellation_policy_exception_non_authenticated_entity_from_dict = CancellationPolicyExceptionNonAuthenticatedEntity.from_dict(cancellation_policy_exception_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


