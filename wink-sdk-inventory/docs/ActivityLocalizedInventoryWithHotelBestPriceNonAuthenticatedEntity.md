# ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_with_price** | [**ActivityLocalizedInventoryNonAuthenticatedEntity**](ActivityLocalizedInventoryNonAuthenticatedEntity.md) | Activity details | [optional] 
**hotel_with_best_price** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best room type price this property has to offer. | [optional] 
**sort** | **int** | Populated when the record is in the context of static lists. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.activity_localized_inventory_with_hotel_best_price_non_authenticated_entity import ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a JSON string
activity_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance = ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
activity_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict = activity_localized_inventory_with_hotel_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity from a dict
activity_localized_inventory_with_hotel_best_price_non_authenticated_entity_from_dict = ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.from_dict(activity_localized_inventory_with_hotel_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


