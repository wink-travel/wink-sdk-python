# UpsertSellerInventoryRankedListRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_inventory_ranked_list_name** | **str** | Descriptive name of this list for seller use only | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Contains custom title and description of grid | 
**keywords** | **List[str]** |  | 
**lookup** | [**LookupAffiliate**](LookupAffiliate.md) |  | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. -1 is disabled | [optional] [default to -1]
**sort** | **str** | Determines which badge to show on the Web Component. Is also used to sort properties for search grids. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [optional] [default to 'NATIVE']

## Example

```python
from wink_sdk_affiliate_inventory.models.upsert_seller_inventory_ranked_list_request_affiliate import UpsertSellerInventoryRankedListRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSellerInventoryRankedListRequestAffiliate from a JSON string
upsert_seller_inventory_ranked_list_request_affiliate_instance = UpsertSellerInventoryRankedListRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSellerInventoryRankedListRequestAffiliate.to_json())

# convert the object into a dict
upsert_seller_inventory_ranked_list_request_affiliate_dict = upsert_seller_inventory_ranked_list_request_affiliate_instance.to_dict()
# create an instance of UpsertSellerInventoryRankedListRequestAffiliate from a dict
upsert_seller_inventory_ranked_list_request_affiliate_from_dict = UpsertSellerInventoryRankedListRequestAffiliate.from_dict(upsert_seller_inventory_ranked_list_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


