# UpsertCancellationPolicyExceptionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_cancellation_policy_exception_supplier import UpsertCancellationPolicyExceptionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCancellationPolicyExceptionSupplier from a JSON string
upsert_cancellation_policy_exception_supplier_instance = UpsertCancellationPolicyExceptionSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertCancellationPolicyExceptionSupplier.to_json())

# convert the object into a dict
upsert_cancellation_policy_exception_supplier_dict = upsert_cancellation_policy_exception_supplier_instance.to_dict()
# create an instance of UpsertCancellationPolicyExceptionSupplier from a dict
upsert_cancellation_policy_exception_supplier_from_dict = UpsertCancellationPolicyExceptionSupplier.from_dict(upsert_cancellation_policy_exception_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


