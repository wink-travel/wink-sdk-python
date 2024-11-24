# CancellationPolicyExceptionsSupplier

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[CancellationPolicyExceptionSupplier]**](CancellationPolicyExceptionSupplier.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_extranet_booking.models.cancellation_policy_exceptions_supplier import CancellationPolicyExceptionsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionsSupplier from a JSON string
cancellation_policy_exceptions_supplier_instance = CancellationPolicyExceptionsSupplier.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionsSupplier.to_json())

# convert the object into a dict
cancellation_policy_exceptions_supplier_dict = cancellation_policy_exceptions_supplier_instance.to_dict()
# create an instance of CancellationPolicyExceptionsSupplier from a dict
cancellation_policy_exceptions_supplier_from_dict = CancellationPolicyExceptionsSupplier.from_dict(cancellation_policy_exceptions_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


