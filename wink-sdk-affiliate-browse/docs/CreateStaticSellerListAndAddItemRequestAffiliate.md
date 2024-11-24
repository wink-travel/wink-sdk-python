# CreateStaticSellerListAndAddItemRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of curated list | 
**channel_inventory_identifiers** | **List[str]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.create_static_seller_list_and_add_item_request_affiliate import CreateStaticSellerListAndAddItemRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaticSellerListAndAddItemRequestAffiliate from a JSON string
create_static_seller_list_and_add_item_request_affiliate_instance = CreateStaticSellerListAndAddItemRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateStaticSellerListAndAddItemRequestAffiliate.to_json())

# convert the object into a dict
create_static_seller_list_and_add_item_request_affiliate_dict = create_static_seller_list_and_add_item_request_affiliate_instance.to_dict()
# create an instance of CreateStaticSellerListAndAddItemRequestAffiliate from a dict
create_static_seller_list_and_add_item_request_affiliate_from_dict = CreateStaticSellerListAndAddItemRequestAffiliate.from_dict(create_static_seller_list_and_add_item_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


