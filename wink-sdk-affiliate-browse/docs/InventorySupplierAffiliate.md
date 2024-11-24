# InventorySupplierAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_channel** | [**SalesChannelAffiliate**](SalesChannelAffiliate.md) |  | 
**hotel** | [**HotelOnMapAffiliate**](HotelOnMapAffiliate.md) |  | 
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.inventory_supplier_affiliate import InventorySupplierAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySupplierAffiliate from a JSON string
inventory_supplier_affiliate_instance = InventorySupplierAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventorySupplierAffiliate.to_json())

# convert the object into a dict
inventory_supplier_affiliate_dict = inventory_supplier_affiliate_instance.to_dict()
# create an instance of InventorySupplierAffiliate from a dict
inventory_supplier_affiliate_from_dict = InventorySupplierAffiliate.from_dict(inventory_supplier_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


