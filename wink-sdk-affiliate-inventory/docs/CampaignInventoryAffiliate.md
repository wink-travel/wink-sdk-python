# CampaignInventoryAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**layout** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**placeholder_image_url** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.campaign_inventory_affiliate import CampaignInventoryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignInventoryAffiliate from a JSON string
campaign_inventory_affiliate_instance = CampaignInventoryAffiliate.from_json(json)
# print the JSON string representation of the object
print(CampaignInventoryAffiliate.to_json())

# convert the object into a dict
campaign_inventory_affiliate_dict = campaign_inventory_affiliate_instance.to_dict()
# create an instance of CampaignInventoryAffiliate from a dict
campaign_inventory_affiliate_from_dict = CampaignInventoryAffiliate.from_dict(campaign_inventory_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


