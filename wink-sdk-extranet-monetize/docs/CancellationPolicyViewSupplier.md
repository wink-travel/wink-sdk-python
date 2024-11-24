# CancellationPolicyViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document identifier | [optional] [readonly] 
**created_date** | **datetime** | Datetime this record was first created | [optional] [readonly] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] [readonly] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] [readonly] 
**cancellation_policy** | [**CancellationPolicySupplier**](CancellationPolicySupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_monetize.models.cancellation_policy_view_supplier import CancellationPolicyViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyViewSupplier from a JSON string
cancellation_policy_view_supplier_instance = CancellationPolicyViewSupplier.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyViewSupplier.to_json())

# convert the object into a dict
cancellation_policy_view_supplier_dict = cancellation_policy_view_supplier_instance.to_dict()
# create an instance of CancellationPolicyViewSupplier from a dict
cancellation_policy_view_supplier_from_dict = CancellationPolicyViewSupplier.from_dict(cancellation_policy_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


