# SellableInventoryPlaceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](PlaceLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced place record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_inventory_place_non_authenticated_entity import SellableInventoryPlaceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableInventoryPlaceNonAuthenticatedEntity from a JSON string
sellable_inventory_place_non_authenticated_entity_instance = SellableInventoryPlaceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableInventoryPlaceNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_inventory_place_non_authenticated_entity_dict = sellable_inventory_place_non_authenticated_entity_instance.to_dict()
# create an instance of SellableInventoryPlaceNonAuthenticatedEntity from a dict
sellable_inventory_place_non_authenticated_entity_from_dict = SellableInventoryPlaceNonAuthenticatedEntity.from_dict(sellable_inventory_place_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


