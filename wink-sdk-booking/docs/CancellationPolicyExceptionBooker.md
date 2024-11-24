# CancellationPolicyExceptionBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyBooker**](CancellationPolicyBooker.md) |  | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_booking.models.cancellation_policy_exception_booker import CancellationPolicyExceptionBooker

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionBooker from a JSON string
cancellation_policy_exception_booker_instance = CancellationPolicyExceptionBooker.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionBooker.to_json())

# convert the object into a dict
cancellation_policy_exception_booker_dict = cancellation_policy_exception_booker_instance.to_dict()
# create an instance of CancellationPolicyExceptionBooker from a dict
cancellation_policy_exception_booker_from_dict = CancellationPolicyExceptionBooker.from_dict(cancellation_policy_exception_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


