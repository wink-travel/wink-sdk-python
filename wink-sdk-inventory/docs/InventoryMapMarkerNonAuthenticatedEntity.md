# InventoryMapMarkerNonAuthenticatedEntity

Inventory map marker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_inventory_identifier** | **str** | Identifier of the list, channel blocking or search | 
**point** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 
**supplier_identifier** | **str** | Hotel identifier | 
**supplier_name** | **str** | Hotel name | 
**supplier_url_name** | **str** | Hotel url name | 
**inventory_identifier** | **str** | Actual blocking identifier | 
**inventory_type** | **str** | Type of blocking | 
**inventory_name** | **str** | Name of blocking | 
**lowest_display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 

## Example

```python
from wink_sdk_inventory.models.inventory_map_marker_non_authenticated_entity import InventoryMapMarkerNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMapMarkerNonAuthenticatedEntity from a JSON string
inventory_map_marker_non_authenticated_entity_instance = InventoryMapMarkerNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryMapMarkerNonAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_map_marker_non_authenticated_entity_dict = inventory_map_marker_non_authenticated_entity_instance.to_dict()
# create an instance of InventoryMapMarkerNonAuthenticatedEntity from a dict
inventory_map_marker_non_authenticated_entity_from_dict = InventoryMapMarkerNonAuthenticatedEntity.from_dict(inventory_map_marker_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


