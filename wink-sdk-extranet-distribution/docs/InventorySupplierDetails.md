# InventorySupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Inventory identifier | 
**sales_channel** | [**SalesChannelSupplierDetails**](SalesChannelSupplierDetails.md) |  | 
**inventory_type** | **str** | Inventory type | 
**inventory_identifier** | **str** | Inventory type identifier | 
**inventory_name** | **str** | Name of blocking as hotel is seeing it | 
**inventory_name_in_english** | **str** | Name of blocking as traveler is seeing it | 
**enabled** | **bool** | Whether this blocking is enabled or not | [default to True]
**image_identifier** | **str** | Main image of blocking | 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**location** | [**GeoJsonPointSupplierDetails**](GeoJsonPointSupplierDetails.md) |  | 
**address** | [**AddressSupplierDetails**](AddressSupplierDetails.md) |  | 
**quantity** | **int** | quantity | [default to 0]
**commissionable** | **bool** | Whether this is commissionable or not | [default to False]
**bookable** | **bool** | Whether blocking can be booked | [default to True]
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**hotel** | [**HotelOnMapSupplierDetails**](HotelOnMapSupplierDetails.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.inventory_supplier_details import InventorySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySupplierDetails from a JSON string
inventory_supplier_details_instance = InventorySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(InventorySupplierDetails.to_json())

# convert the object into a dict
inventory_supplier_details_dict = inventory_supplier_details_instance.to_dict()
# create an instance of InventorySupplierDetails from a dict
inventory_supplier_details_from_dict = InventorySupplierDetails.from_dict(inventory_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


