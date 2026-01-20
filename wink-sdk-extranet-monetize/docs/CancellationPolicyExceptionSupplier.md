# CancellationPolicyExceptionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **UUID** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyLightweightSupplier**](CancellationPolicyLightweightSupplier.md) | Cancellation policy | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_extranet_monetize.models.cancellation_policy_exception_supplier import CancellationPolicyExceptionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionSupplier from a JSON string
cancellation_policy_exception_supplier_instance = CancellationPolicyExceptionSupplier.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionSupplier.to_json())

# convert the object into a dict
cancellation_policy_exception_supplier_dict = cancellation_policy_exception_supplier_instance.to_dict()
# create an instance of CancellationPolicyExceptionSupplier from a dict
cancellation_policy_exception_supplier_from_dict = CancellationPolicyExceptionSupplier.from_dict(cancellation_policy_exception_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


