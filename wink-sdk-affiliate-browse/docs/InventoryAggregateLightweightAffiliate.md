# InventoryAggregateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**sales_channel** | [**SalesChannelLightweightAffiliate**](SalesChannelLightweightAffiliate.md) | Parent sales channel | 
**inventory_type** | **str** | Inventory type | 
**inventory_identifier** | **str** | Inventory type identifier | 
**inventory_name** | **str** | Name of blocking as hotel is seeing it | 
**inventory_name_in_english** | **str** | Name of blocking as traveler is seeing it | 
**enabled** | **bool** | Whether this blocking is enabled or not | [default to True]
**image_identifier** | **str** | Main image of blocking | 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Location | 
**address** | [**InventoryAddressAffiliate**](InventoryAddressAffiliate.md) | Defaults to property address. | 
**quantity** | **int** | quantity | [default to 0]
**commissionable** | **bool** | Whether this is commissionable or not | [default to False]
**bookable** | **bool** | Whether blocking can be booked | [default to True]
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary in platform currency | [optional] 
**hotel** | [**PropertyAggregateLightweightAffiliate**](PropertyAggregateLightweightAffiliate.md) | Linked hotel | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.inventory_aggregate_lightweight_affiliate import InventoryAggregateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAggregateLightweightAffiliate from a JSON string
inventory_aggregate_lightweight_affiliate_instance = InventoryAggregateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventoryAggregateLightweightAffiliate.to_json())

# convert the object into a dict
inventory_aggregate_lightweight_affiliate_dict = inventory_aggregate_lightweight_affiliate_instance.to_dict()
# create an instance of InventoryAggregateLightweightAffiliate from a dict
inventory_aggregate_lightweight_affiliate_from_dict = InventoryAggregateLightweightAffiliate.from_dict(inventory_aggregate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


