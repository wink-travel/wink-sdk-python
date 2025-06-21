# UpsertManagedByAgencyRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managing_entity_identifier** | **str** | Existing user account managingEntityIdentifier to make manager | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRulesAffiliate**](ManagedByEntityRulesAffiliate.md) | Optional rules for expiration date etc when agency is no longer managing this entity. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.upsert_managed_by_agency_request_affiliate import UpsertManagedByAgencyRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertManagedByAgencyRequestAffiliate from a JSON string
upsert_managed_by_agency_request_affiliate_instance = UpsertManagedByAgencyRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertManagedByAgencyRequestAffiliate.to_json())

# convert the object into a dict
upsert_managed_by_agency_request_affiliate_dict = upsert_managed_by_agency_request_affiliate_instance.to_dict()
# create an instance of UpsertManagedByAgencyRequestAffiliate from a dict
upsert_managed_by_agency_request_affiliate_from_dict = UpsertManagedByAgencyRequestAffiliate.from_dict(upsert_managed_by_agency_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


