# InventorySupplierAggregateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_channel** | [**SalesChannelLightweightAffiliate**](SalesChannelLightweightAffiliate.md) | Parent sales channel | 
**hotel** | [**PropertyAggregateLightweightAffiliate**](PropertyAggregateLightweightAffiliate.md) | Combined property data. | 
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Best price of the room type or facility ancillary in platform currency | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.inventory_supplier_aggregate_lightweight_affiliate import InventorySupplierAggregateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySupplierAggregateLightweightAffiliate from a JSON string
inventory_supplier_aggregate_lightweight_affiliate_instance = InventorySupplierAggregateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventorySupplierAggregateLightweightAffiliate.to_json())

# convert the object into a dict
inventory_supplier_aggregate_lightweight_affiliate_dict = inventory_supplier_aggregate_lightweight_affiliate_instance.to_dict()
# create an instance of InventorySupplierAggregateLightweightAffiliate from a dict
inventory_supplier_aggregate_lightweight_affiliate_from_dict = InventorySupplierAggregateLightweightAffiliate.from_dict(inventory_supplier_aggregate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


