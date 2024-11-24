# CancellationPolicyRemovableResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removable** | **bool** |  | [optional] 
**rate_plans** | [**List[IdentifierNamePairSupplier]**](IdentifierNamePairSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.cancellation_policy_removable_response_supplier import CancellationPolicyRemovableResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyRemovableResponseSupplier from a JSON string
cancellation_policy_removable_response_supplier_instance = CancellationPolicyRemovableResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyRemovableResponseSupplier.to_json())

# convert the object into a dict
cancellation_policy_removable_response_supplier_dict = cancellation_policy_removable_response_supplier_instance.to_dict()
# create an instance of CancellationPolicyRemovableResponseSupplier from a dict
cancellation_policy_removable_response_supplier_from_dict = CancellationPolicyRemovableResponseSupplier.from_dict(cancellation_policy_removable_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


