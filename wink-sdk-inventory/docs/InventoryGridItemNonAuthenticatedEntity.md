# InventoryGridItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | **int** | Sort property indicates how this grid item fits in with the rest of the items in the list. | 
**type** | **str** | The type of inventory this item represents. | 
**identifier** | **str** | Unique inventory identifier | 
**supplier_identifier** | **str** | Supplier identifier referencing inventory owner | 
**activity** | [**ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;ACTIVITY&#x60; | [optional] 
**attraction** | [**AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;ATTRACTION&#x60; | [optional] 
**place** | [**PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;PLACE&#x60; | [optional] 
**room_type** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;GUEST_ROOM&#x60; | [optional] 
**meeting_room** | [**MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;MEETING_ROOM&#x60; | [optional] 
**restaurant** | [**RestaurantLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](RestaurantLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;RESTAURANT&#x60; | [optional] 
**spa** | [**SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;SPA&#x60; | [optional] 
**add_on** | [**AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Populated only when the type of grid item is &#x60;ADD_ON&#x60; | [optional] 
**available** | **bool** | Whether this inventory is available | [optional] 

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


