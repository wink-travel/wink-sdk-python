# AffiliateAccountAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **UUID** | User owner ID. | 
**managing_entity_identifier** | **UUID** | Parent ID. Because it&#39;s all 1-1, it should be the same ID. | 
**owner_identifier** | **str** | The App owner that created this record. | 
**managers** | [**List[ManagingEntityManagerAgent]**](ManagingEntityManagerAgent.md) |  | 
**managed_by** | [**ManagedByEntityAgent**](ManagedByEntityAgent.md) | If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking. | [optional] 
**owner_type** | **str** | Type of entity this is. | 
**type** | **str** | Type of sales channel | 
**name** | **str** | Name of company | 
**url_name** | **str** | Url slug of company name | 
**unique_id** | **str** | Event shorter name | 
**description** | **str** | Account description. | [optional] 
**currency_code** | **str** | Account&#39;s main currency. | 
**city** | [**GeoNameLightweightAgent**](GeoNameLightweightAgent.md) |  | 
**place_id** | **str** | Optional Google placeId for properties with a Google Business account. | [optional] 
**profile_picture** | [**SimpleMultimediaAgent**](SimpleMultimediaAgent.md) | Customize account with a custom profile picture. | [optional] 
**status** | **str** | Status of entity. | 
**logo** | [**SimpleMultimediaAgent**](SimpleMultimediaAgent.md) | Customize account with a custom logo / profile picture. | [optional] 
**online_presence** | [**List[OnlinePresenceAgent]**](OnlinePresenceAgent.md) |  | [optional] 
**annual_travel_spend_in_dollars** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | How much user or company spends on travel per year. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.affiliate_account_affiliate import AffiliateAccountAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateAccountAffiliate from a JSON string
affiliate_account_affiliate_instance = AffiliateAccountAffiliate.from_json(json)
# print the JSON string representation of the object
print(AffiliateAccountAffiliate.to_json())

# convert the object into a dict
affiliate_account_affiliate_dict = affiliate_account_affiliate_instance.to_dict()
# create an instance of AffiliateAccountAffiliate from a dict
affiliate_account_affiliate_from_dict = AffiliateAccountAffiliate.from_dict(affiliate_account_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


