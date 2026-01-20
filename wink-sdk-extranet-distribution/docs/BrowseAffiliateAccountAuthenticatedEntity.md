# BrowseAffiliateAccountAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**city** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | 
**country** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | 
**continent** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | 
**name** | **str** |  | 
**owner_name** | **str** |  | 
**url_name** | **str** |  | 
**unique_id** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**status** | **str** |  | 
**created_date** | **datetime** |  | 
**last_update** | **datetime** |  | 
**travel_agent** | **object** |  | 
**owner_image_id** | **str** | The company image ID | 

## Example

```python
from wink_sdk_extranet_distribution.models.browse_affiliate_account_authenticated_entity import BrowseAffiliateAccountAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseAffiliateAccountAuthenticatedEntity from a JSON string
browse_affiliate_account_authenticated_entity_instance = BrowseAffiliateAccountAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BrowseAffiliateAccountAuthenticatedEntity.to_json())

# convert the object into a dict
browse_affiliate_account_authenticated_entity_dict = browse_affiliate_account_authenticated_entity_instance.to_dict()
# create an instance of BrowseAffiliateAccountAuthenticatedEntity from a dict
browse_affiliate_account_authenticated_entity_from_dict = BrowseAffiliateAccountAuthenticatedEntity.from_dict(browse_affiliate_account_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


