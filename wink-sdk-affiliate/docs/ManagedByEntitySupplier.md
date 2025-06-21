# ManagedByEntitySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Entity identifier | 
**name** | **str** | Name of entity | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRulesSupplier**](ManagedByEntityRulesSupplier.md) | Optional rules for expiration date etc when agency is no longer managing this entity. | [optional] 
**valid** | **bool** | Whether managing entity is eligible a commission. | [optional] [readonly] 

## Example

```python
from wink_sdk_affiliate.models.managed_by_entity_supplier import ManagedByEntitySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByEntitySupplier from a JSON string
managed_by_entity_supplier_instance = ManagedByEntitySupplier.from_json(json)
# print the JSON string representation of the object
print(ManagedByEntitySupplier.to_json())

# convert the object into a dict
managed_by_entity_supplier_dict = managed_by_entity_supplier_instance.to_dict()
# create an instance of ManagedByEntitySupplier from a dict
managed_by_entity_supplier_from_dict = ManagedByEntitySupplier.from_dict(managed_by_entity_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


