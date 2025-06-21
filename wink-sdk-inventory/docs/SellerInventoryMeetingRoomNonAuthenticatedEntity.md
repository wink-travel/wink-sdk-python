# SellerInventoryMeetingRoomNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](MeetingRoomLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced meeting room record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier blocking record | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_meeting_room_non_authenticated_entity import SellerInventoryMeetingRoomNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryMeetingRoomNonAuthenticatedEntity from a JSON string
seller_inventory_meeting_room_non_authenticated_entity_instance = SellerInventoryMeetingRoomNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryMeetingRoomNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_meeting_room_non_authenticated_entity_dict = seller_inventory_meeting_room_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryMeetingRoomNonAuthenticatedEntity from a dict
seller_inventory_meeting_room_non_authenticated_entity_from_dict = SellerInventoryMeetingRoomNonAuthenticatedEntity.from_dict(seller_inventory_meeting_room_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


