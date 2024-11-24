# StaticSellerListItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identifier | 
**parent** | [**StaticSellerListAffiliate**](StaticSellerListAffiliate.md) |  | 
**inventory** | [**InventoryAffiliate**](InventoryAffiliate.md) |  | 
**sort** | **int** | Sort key | [optional] 
**status** | **str** | Status | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.static_seller_list_item_affiliate import StaticSellerListItemAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSellerListItemAffiliate from a JSON string
static_seller_list_item_affiliate_instance = StaticSellerListItemAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticSellerListItemAffiliate.to_json())

# convert the object into a dict
static_seller_list_item_affiliate_dict = static_seller_list_item_affiliate_instance.to_dict()
# create an instance of StaticSellerListItemAffiliate from a dict
static_seller_list_item_affiliate_from_dict = StaticSellerListItemAffiliate.from_dict(static_seller_list_item_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


