# CompanyUserAffiliate


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
from wink_sdk_affiliate.models.company_user_affiliate import CompanyUserAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserAffiliate from a JSON string
company_user_affiliate_instance = CompanyUserAffiliate.from_json(json)
# print the JSON string representation of the object
print(CompanyUserAffiliate.to_json())

# convert the object into a dict
company_user_affiliate_dict = company_user_affiliate_instance.to_dict()
# create an instance of CompanyUserAffiliate from a dict
company_user_affiliate_from_dict = CompanyUserAffiliate.from_dict(company_user_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


