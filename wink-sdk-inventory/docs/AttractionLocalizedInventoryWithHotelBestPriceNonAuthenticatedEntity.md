# AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

Populated only when the type of grid item is `ATTRACTION`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**AttractionLocalizedInventoryNonAuthenticatedEntity**](AttractionLocalizedInventoryNonAuthenticatedEntity.md) |  | [optional] 
**hotel_with_best_price** | [**HotelWithBestPriceNonAuthenticatedEntity**](HotelWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity import AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(attraction_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


