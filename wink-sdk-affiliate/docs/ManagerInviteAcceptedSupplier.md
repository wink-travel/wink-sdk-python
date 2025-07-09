# ManagerInviteAcceptedSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | AffiliateAccount ID | 
**type** | **str** | Type of account | 

## Example

```python
from wink_sdk_affiliate.models.manager_invite_accepted_supplier import ManagerInviteAcceptedSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerInviteAcceptedSupplier from a JSON string
manager_invite_accepted_supplier_instance = ManagerInviteAcceptedSupplier.from_json(json)
# print the JSON string representation of the object
print(ManagerInviteAcceptedSupplier.to_json())

# convert the object into a dict
manager_invite_accepted_supplier_dict = manager_invite_accepted_supplier_instance.to_dict()
# create an instance of ManagerInviteAcceptedSupplier from a dict
manager_invite_accepted_supplier_from_dict = ManagerInviteAcceptedSupplier.from_dict(manager_invite_accepted_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


