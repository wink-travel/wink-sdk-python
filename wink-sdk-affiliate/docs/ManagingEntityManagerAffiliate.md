# ManagingEntityManagerAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**status** | **str** | Contact phone number | [optional] 
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**profile_picture** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) | Profile picture is available | [optional] 
**owner** | **bool** | Account owner | [optional] 
**roles** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.managing_entity_manager_affiliate import ManagingEntityManagerAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityManagerAffiliate from a JSON string
managing_entity_manager_affiliate_instance = ManagingEntityManagerAffiliate.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityManagerAffiliate.to_json())

# convert the object into a dict
managing_entity_manager_affiliate_dict = managing_entity_manager_affiliate_instance.to_dict()
# create an instance of ManagingEntityManagerAffiliate from a dict
managing_entity_manager_affiliate_from_dict = ManagingEntityManagerAffiliate.from_dict(managing_entity_manager_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


