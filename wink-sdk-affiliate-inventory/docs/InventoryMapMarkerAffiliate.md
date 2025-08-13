# InventoryMapMarkerAffiliate

Inventory map marker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_inventory_identifier** | **str** | Identifier of the list, channel inventory or search | 
**point** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Location of inventory | 
**supplier_identifier** | **str** | Hotel identifier | 
**supplier_name** | **str** | Hotel name | 
**inventory_identifier** | **str** | Actual inventory identifier | 
**inventory_type** | **str** | Type of inventory | 
**inventory_name** | **str** | Name of inventory | 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Lowest price of inventory in desired currency | 

## Example

```python
from wink_sdk_affiliate_inventory.models.inventory_map_marker_affiliate import InventoryMapMarkerAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMapMarkerAffiliate from a JSON string
inventory_map_marker_affiliate_instance = InventoryMapMarkerAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventoryMapMarkerAffiliate.to_json())

# convert the object into a dict
inventory_map_marker_affiliate_dict = inventory_map_marker_affiliate_instance.to_dict()
# create an instance of InventoryMapMarkerAffiliate from a dict
inventory_map_marker_affiliate_from_dict = InventoryMapMarkerAffiliate.from_dict(inventory_map_marker_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


