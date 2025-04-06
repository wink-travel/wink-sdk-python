# HotelWithBestPriceNonAuthenticatedEntity

Populated only when the type of grid item is `GUEST_ROOM`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel** | [**HotelOnMapLightweightNonAuthenticatedEntity**](HotelOnMapLightweightNonAuthenticatedEntity.md) |  | 
**lowest_price** | [**RoomTypeBestPriceNonAuthenticatedEntity**](RoomTypeBestPriceNonAuthenticatedEntity.md) |  | 
**room_type_list** | [**List[GuestRoomLightweightNonAuthenticatedEntity]**](GuestRoomLightweightNonAuthenticatedEntity.md) | Unique property room types | 
**price_list** | [**List[RoomTypeBestPriceNonAuthenticatedEntity]**](RoomTypeBestPriceNonAuthenticatedEntity.md) | Best-priced room types | 
**potential_channel_discount_percent** | **float** | The potential discount the user is entitled to if user is a member / authenticated. | 
**source_to_user_currency_quote** | [**QuoteNonAuthenticatedEntity**](QuoteNonAuthenticatedEntity.md) |  | 
**source_to_internal_currency_quote** | [**QuoteNonAuthenticatedEntity**](QuoteNonAuthenticatedEntity.md) |  | 
**available** | **bool** | Flag to indicate whether this blocking is available or not. This data point is identifier to the available flag on the &#x60;price&#x60; child data point. | [optional] 

## Example

```python
from wink_sdk_inventory.models.hotel_with_best_price_non_authenticated_entity import HotelWithBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HotelWithBestPriceNonAuthenticatedEntity from a JSON string
hotel_with_best_price_non_authenticated_entity_instance = HotelWithBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HotelWithBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
hotel_with_best_price_non_authenticated_entity_dict = hotel_with_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of HotelWithBestPriceNonAuthenticatedEntity from a dict
hotel_with_best_price_non_authenticated_entity_from_dict = HotelWithBestPriceNonAuthenticatedEntity.from_dict(hotel_with_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


