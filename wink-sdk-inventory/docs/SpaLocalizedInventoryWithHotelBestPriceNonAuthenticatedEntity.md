# SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**SpaLocalizedInventoryNonAuthenticatedEntity**](SpaLocalizedInventoryNonAuthenticatedEntity.md) | Spa details | [optional] 
**hotel_with_best_price** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best room type price this property has to offer. | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.spa_localized_inventory_with_hotel_best_price_non_authenticated_entity import SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
spa_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
spa_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = spa_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
spa_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(spa_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


