# PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

Populated only when the type of grid item is `PLACE`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**PlaceLocalizedInventoryNonAuthenticatedEntity**](PlaceLocalizedInventoryNonAuthenticatedEntity.md) |  | [optional] 
**hotel_with_best_price** | [**HotelWithBestPriceNonAuthenticatedEntity**](HotelWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.place_localized_inventory_with_hotel_best_price_non_authenticated_entity import PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
place_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
place_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = place_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
place_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(place_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


