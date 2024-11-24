# CancellationPolicyExceptionsBooker

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyExceptionBooker]**](CancellationPolicyExceptionBooker.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_booking.models.cancellation_policy_exceptions_booker import CancellationPolicyExceptionsBooker

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionsBooker from a JSON string
cancellation_policy_exceptions_booker_instance = CancellationPolicyExceptionsBooker.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionsBooker.to_json())

# convert the object into a dict
cancellation_policy_exceptions_booker_dict = cancellation_policy_exceptions_booker_instance.to_dict()
# create an instance of CancellationPolicyExceptionsBooker from a dict
cancellation_policy_exceptions_booker_from_dict = CancellationPolicyExceptionsBooker.from_dict(cancellation_policy_exceptions_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


