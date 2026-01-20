# CreateSellableItemSyndicatedItemRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | ID of seller inventory item to create a syndication entry from | 

## Example

```python
from wink_sdk_affiliate_inventory.models.create_sellable_item_syndicated_item_request_affiliate import CreateSellableItemSyndicatedItemRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSellableItemSyndicatedItemRequestAffiliate from a JSON string
create_sellable_item_syndicated_item_request_affiliate_instance = CreateSellableItemSyndicatedItemRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateSellableItemSyndicatedItemRequestAffiliate.to_json())

# convert the object into a dict
create_sellable_item_syndicated_item_request_affiliate_dict = create_sellable_item_syndicated_item_request_affiliate_instance.to_dict()
# create an instance of CreateSellableItemSyndicatedItemRequestAffiliate from a dict
create_sellable_item_syndicated_item_request_affiliate_from_dict = CreateSellableItemSyndicatedItemRequestAffiliate.from_dict(create_sellable_item_syndicated_item_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


