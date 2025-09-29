# SellableInventoryGuestRoomNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best room type price. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_inventory_guest_room_non_authenticated_entity import SellableInventoryGuestRoomNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableInventoryGuestRoomNonAuthenticatedEntity from a JSON string
sellable_inventory_guest_room_non_authenticated_entity_instance = SellableInventoryGuestRoomNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableInventoryGuestRoomNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_inventory_guest_room_non_authenticated_entity_dict = sellable_inventory_guest_room_non_authenticated_entity_instance.to_dict()
# create an instance of SellableInventoryGuestRoomNonAuthenticatedEntity from a dict
sellable_inventory_guest_room_non_authenticated_entity_from_dict = SellableInventoryGuestRoomNonAuthenticatedEntity.from_dict(sellable_inventory_guest_room_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


