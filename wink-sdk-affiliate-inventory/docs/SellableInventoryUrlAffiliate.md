# SellableInventoryUrlAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **UUID** | Creator of entry | 
**owner_identifier** | **UUID** | AffiliateAccount identifier | 
**name** | **str** | Descriptive name of this url for seller use only | 
**customization_identifier** | **UUID** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) |  | 
**multimedias** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**unique_id** | **str** | Unique link id | 
**twitter_account** | **str** | Twitter account is used with OpenGraph data | [optional] 
**facebook_app_id** | **str** | Facebook APP ID is used with OpenGraph data | [optional] 
**theme** | **str** | Url theme controls the look and feel of the ad banner. | 
**status** | **str** | Url sell status | 
**inventory_status** | **str** | Url sell status | 
**inventory_type** | **str** | Inventory type | 
**channel_inventory_type** | **str** | Channel inventory type is a subset of inventory type in that it does not include the &#x60;HOTEL&#x60; type. THe way it works is, as a seller you might want to sell a guest room but instead of showing the price of that guest room, you would like to display the best room type price for the property. | 
**supplier_identifier** | **str** | The entity supplying the inventory. Usually a hotel. | 
**channel_inventory_identifier** | **str** | Selected inventory record | 
**transactional_item_identifier** | **str** | In use by ancillary items only. Not used room type or property. The transactional item on the ancillary to retrieve pricing for. If left empty, will find the cheapest priced item. | [optional] 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Animation delay in milliseconds | [optional] [default to -1]

## Example

```python
from wink_sdk_affiliate_inventory.models.sellable_inventory_url_affiliate import SellableInventoryUrlAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellableInventoryUrlAffiliate from a JSON string
sellable_inventory_url_affiliate_instance = SellableInventoryUrlAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellableInventoryUrlAffiliate.to_json())

# convert the object into a dict
sellable_inventory_url_affiliate_dict = sellable_inventory_url_affiliate_instance.to_dict()
# create an instance of SellableInventoryUrlAffiliate from a dict
sellable_inventory_url_affiliate_from_dict = SellableInventoryUrlAffiliate.from_dict(sellable_inventory_url_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


