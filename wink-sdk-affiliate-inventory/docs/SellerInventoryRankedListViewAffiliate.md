# SellerInventoryRankedListViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**seller_inventory_ranked_list** | [**SellerInventoryRankedListAffiliate**](SellerInventoryRankedListAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_inventory.models.seller_inventory_ranked_list_view_affiliate import SellerInventoryRankedListViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryRankedListViewAffiliate from a JSON string
seller_inventory_ranked_list_view_affiliate_instance = SellerInventoryRankedListViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryRankedListViewAffiliate.to_json())

# convert the object into a dict
seller_inventory_ranked_list_view_affiliate_dict = seller_inventory_ranked_list_view_affiliate_instance.to_dict()
# create an instance of SellerInventoryRankedListViewAffiliate from a dict
seller_inventory_ranked_list_view_affiliate_from_dict = SellerInventoryRankedListViewAffiliate.from_dict(seller_inventory_ranked_list_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


