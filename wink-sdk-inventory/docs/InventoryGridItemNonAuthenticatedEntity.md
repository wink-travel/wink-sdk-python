# InventoryGridItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | **int** | Sort property indicates how this grid item fits in with the rest of the items in the list. | 
**type** | **str** | The type of blocking this item represents. | 
**identifier** | **str** | Unique blocking identifier | 
**supplier_identifier** | **str** | Supplier identifier referencing blocking owner | 
**activity** | [**ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**attraction** | [**AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**place** | [**PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**room_type** | [**HotelWithBestPriceNonAuthenticatedEntity**](HotelWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**meeting_room** | [**MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**restaurant** | [**RestaurantLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](RestaurantLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**spa** | [**SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**add_on** | [**AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**available** | **bool** | Whether this blocking is available | [optional] 

## Example

```python
from wink_sdk_inventory.models.inventory_grid_item_non_authenticated_entity import InventoryGridItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGridItemNonAuthenticatedEntity from a JSON string
inventory_grid_item_non_authenticated_entity_instance = InventoryGridItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryGridItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_grid_item_non_authenticated_entity_dict = inventory_grid_item_non_authenticated_entity_instance.to_dict()
# create an instance of InventoryGridItemNonAuthenticatedEntity from a dict
inventory_grid_item_non_authenticated_entity_from_dict = InventoryGridItemNonAuthenticatedEntity.from_dict(inventory_grid_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


