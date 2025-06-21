# SellerInventoryGuestRoomNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best room type price. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier blocking record | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_guest_room_non_authenticated_entity import SellerInventoryGuestRoomNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryGuestRoomNonAuthenticatedEntity from a JSON string
seller_inventory_guest_room_non_authenticated_entity_instance = SellerInventoryGuestRoomNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryGuestRoomNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_guest_room_non_authenticated_entity_dict = seller_inventory_guest_room_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryGuestRoomNonAuthenticatedEntity from a dict
seller_inventory_guest_room_non_authenticated_entity_from_dict = SellerInventoryGuestRoomNonAuthenticatedEntity.from_dict(seller_inventory_guest_room_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


