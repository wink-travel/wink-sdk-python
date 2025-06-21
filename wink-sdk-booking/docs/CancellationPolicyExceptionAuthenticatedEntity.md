# CancellationPolicyExceptionAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyLightweightAuthenticatedEntity**](CancellationPolicyLightweightAuthenticatedEntity.md) | Cancellation policy | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_booking.models.cancellation_policy_exception_authenticated_entity import CancellationPolicyExceptionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionAuthenticatedEntity from a JSON string
cancellation_policy_exception_authenticated_entity_instance = CancellationPolicyExceptionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionAuthenticatedEntity.to_json())

# convert the object into a dict
cancellation_policy_exception_authenticated_entity_dict = cancellation_policy_exception_authenticated_entity_instance.to_dict()
# create an instance of CancellationPolicyExceptionAuthenticatedEntity from a dict
cancellation_policy_exception_authenticated_entity_from_dict = CancellationPolicyExceptionAuthenticatedEntity.from_dict(cancellation_policy_exception_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


