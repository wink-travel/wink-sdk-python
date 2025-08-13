# UpsertAffiliateAccountProfileRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of account | 
**description** | **str** | Account description. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.upsert_affiliate_account_profile_request_affiliate import UpsertAffiliateAccountProfileRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAffiliateAccountProfileRequestAffiliate from a JSON string
upsert_affiliate_account_profile_request_affiliate_instance = UpsertAffiliateAccountProfileRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertAffiliateAccountProfileRequestAffiliate.to_json())

# convert the object into a dict
upsert_affiliate_account_profile_request_affiliate_dict = upsert_affiliate_account_profile_request_affiliate_instance.to_dict()
# create an instance of UpsertAffiliateAccountProfileRequestAffiliate from a dict
upsert_affiliate_account_profile_request_affiliate_from_dict = UpsertAffiliateAccountProfileRequestAffiliate.from_dict(upsert_affiliate_account_profile_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


