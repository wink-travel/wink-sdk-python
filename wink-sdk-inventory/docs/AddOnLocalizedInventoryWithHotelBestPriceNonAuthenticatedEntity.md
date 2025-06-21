# AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**AddOnLocalizedInventoryNonAuthenticatedEntity**](AddOnLocalizedInventoryNonAuthenticatedEntity.md) | Add-on details | [optional] 
**hotel_with_best_price** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best room type price this property has to offer. | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity import AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(add_on_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


