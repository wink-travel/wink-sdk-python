# SpaSellableItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced spa record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.spa_sellable_item_non_authenticated_entity import SpaSellableItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SpaSellableItemNonAuthenticatedEntity from a JSON string
spa_sellable_item_non_authenticated_entity_instance = SpaSellableItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SpaSellableItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
spa_sellable_item_non_authenticated_entity_dict = spa_sellable_item_non_authenticated_entity_instance.to_dict()
# create an instance of SpaSellableItemNonAuthenticatedEntity from a dict
spa_sellable_item_non_authenticated_entity_from_dict = SpaSellableItemNonAuthenticatedEntity.from_dict(spa_sellable_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


