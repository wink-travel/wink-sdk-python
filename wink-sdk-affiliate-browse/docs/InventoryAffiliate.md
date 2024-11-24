# InventoryAffiliate

Channel blocking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Inventory identifier | 
**sales_channel** | [**SalesChannelAffiliate**](SalesChannelAffiliate.md) |  | 
**inventory_type** | **str** | Inventory type | 
**inventory_identifier** | **str** | Inventory type identifier | 
**inventory_name** | **str** | Name of blocking as hotel is seeing it | 
**inventory_name_in_english** | **str** | Name of blocking as traveler is seeing it | 
**enabled** | **bool** | Whether this blocking is enabled or not | [default to True]
**image_identifier** | **str** | Main image of blocking | 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | 
**address** | [**AddressAffiliate**](AddressAffiliate.md) |  | 
**quantity** | **int** | quantity | [default to 0]
**commissionable** | **bool** | Whether this is commissionable or not | [default to False]
**bookable** | **bool** | Whether blocking can be booked | [default to True]
**lowest_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**hotel** | [**HotelOnMapAffiliate**](HotelOnMapAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_browse.models.inventory_affiliate import InventoryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAffiliate from a JSON string
inventory_affiliate_instance = InventoryAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventoryAffiliate.to_json())

# convert the object into a dict
inventory_affiliate_dict = inventory_affiliate_instance.to_dict()
# create an instance of InventoryAffiliate from a dict
inventory_affiliate_from_dict = InventoryAffiliate.from_dict(inventory_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


