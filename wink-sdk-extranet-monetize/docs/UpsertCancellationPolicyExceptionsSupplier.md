# UpsertCancellationPolicyExceptionsSupplier

Allows a property to dynamically use another cancellation policy for a specific date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[UpsertCancellationPolicyExceptionSupplier]**](UpsertCancellationPolicyExceptionSupplier.md) | List of cancellation policy exceptions | 

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_cancellation_policy_exceptions_supplier import UpsertCancellationPolicyExceptionsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCancellationPolicyExceptionsSupplier from a JSON string
upsert_cancellation_policy_exceptions_supplier_instance = UpsertCancellationPolicyExceptionsSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertCancellationPolicyExceptionsSupplier.to_json())

# convert the object into a dict
upsert_cancellation_policy_exceptions_supplier_dict = upsert_cancellation_policy_exceptions_supplier_instance.to_dict()
# create an instance of UpsertCancellationPolicyExceptionsSupplier from a dict
upsert_cancellation_policy_exceptions_supplier_from_dict = UpsertCancellationPolicyExceptionsSupplier.from_dict(upsert_cancellation_policy_exceptions_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


