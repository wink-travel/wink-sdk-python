# SellerInventoryRankedListAffiliate

SellerInventoryRankedList  object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**seller_identifier** | **str** | Company identifier | 
**seller_inventory_ranked_list_name** | **str** | Descriptive name of this list for seller use only | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Contains custom title and description of grid | 
**keywords** | **List[str]** |  | 
**status** | **str** | Status | [default to 'ACTIVE']
**lookup** | [**LookupAffiliate**](LookupAffiliate.md) |  | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. -1 is disabled | [optional] [default to -1]
**sort** | **str** | Determines which badge to show on the Web Component. Is also used to sort properties for search grids. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [optional] [default to 'NATIVE']

## Example

```python
from wink_sdk_affiliate_inventory.models.seller_inventory_ranked_list_affiliate import SellerInventoryRankedListAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryRankedListAffiliate from a JSON string
seller_inventory_ranked_list_affiliate_instance = SellerInventoryRankedListAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryRankedListAffiliate.to_json())

# convert the object into a dict
seller_inventory_ranked_list_affiliate_dict = seller_inventory_ranked_list_affiliate_instance.to_dict()
# create an instance of SellerInventoryRankedListAffiliate from a dict
seller_inventory_ranked_list_affiliate_from_dict = SellerInventoryRankedListAffiliate.from_dict(seller_inventory_ranked_list_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


