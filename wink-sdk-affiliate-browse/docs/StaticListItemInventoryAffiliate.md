# StaticListItemInventoryAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Channel Inventory identifier | 
**sales_channel** | [**SalesChannelLightweightAffiliate**](SalesChannelLightweightAffiliate.md) | Parent sales channel | 
**inventory_type** | **str** | Inventory type | 
**inventory_identifier** | **str** | Inventory type identifier | 
**inventory_name_in_english** | **str** | Name of blocking as traveler is seeing it | 
**enabled** | **bool** | Whether this blocking is enabled or not | [default to True]
**image_identifier** | **str** | Main image of blocking | 
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Location | 
**commissionable** | **bool** | Whether this is commissionable or not | [default to False]
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary in platform currency | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.static_list_item_inventory_affiliate import StaticListItemInventoryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticListItemInventoryAffiliate from a JSON string
static_list_item_inventory_affiliate_instance = StaticListItemInventoryAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticListItemInventoryAffiliate.to_json())

# convert the object into a dict
static_list_item_inventory_affiliate_dict = static_list_item_inventory_affiliate_instance.to_dict()
# create an instance of StaticListItemInventoryAffiliate from a dict
static_list_item_inventory_affiliate_from_dict = StaticListItemInventoryAffiliate.from_dict(static_list_item_inventory_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


