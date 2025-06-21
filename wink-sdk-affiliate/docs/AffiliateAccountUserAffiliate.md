# AffiliateAccountUserAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**status** | **str** | Contact phone number | [optional] 
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**profile_picture_url** | **str** | Profile picture is available | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.affiliate_account_user_affiliate import AffiliateAccountUserAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateAccountUserAffiliate from a JSON string
affiliate_account_user_affiliate_instance = AffiliateAccountUserAffiliate.from_json(json)
# print the JSON string representation of the object
print(AffiliateAccountUserAffiliate.to_json())

# convert the object into a dict
affiliate_account_user_affiliate_dict = affiliate_account_user_affiliate_instance.to_dict()
# create an instance of AffiliateAccountUserAffiliate from a dict
affiliate_account_user_affiliate_from_dict = AffiliateAccountUserAffiliate.from_dict(affiliate_account_user_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


