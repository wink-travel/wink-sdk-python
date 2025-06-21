# ManagedByEntityAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Entity identifier | 
**name** | **str** | Name of entity | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRulesAffiliate**](ManagedByEntityRulesAffiliate.md) | Optional rules for expiration date etc when agency is no longer managing this entity. | [optional] 
**valid** | **bool** | Whether managing entity is eligible a commission. | [optional] [readonly] 

## Example

```python
from wink_sdk_affiliate.models.managed_by_entity_affiliate import ManagedByEntityAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByEntityAffiliate from a JSON string
managed_by_entity_affiliate_instance = ManagedByEntityAffiliate.from_json(json)
# print the JSON string representation of the object
print(ManagedByEntityAffiliate.to_json())

# convert the object into a dict
managed_by_entity_affiliate_dict = managed_by_entity_affiliate_instance.to_dict()
# create an instance of ManagedByEntityAffiliate from a dict
managed_by_entity_affiliate_from_dict = ManagedByEntityAffiliate.from_dict(managed_by_entity_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


