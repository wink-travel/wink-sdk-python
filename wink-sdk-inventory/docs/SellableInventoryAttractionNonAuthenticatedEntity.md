# SellableInventoryAttractionNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AttractionLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced attraction record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_inventory_attraction_non_authenticated_entity import SellableInventoryAttractionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableInventoryAttractionNonAuthenticatedEntity from a JSON string
sellable_inventory_attraction_non_authenticated_entity_instance = SellableInventoryAttractionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableInventoryAttractionNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_inventory_attraction_non_authenticated_entity_dict = sellable_inventory_attraction_non_authenticated_entity_instance.to_dict()
# create an instance of SellableInventoryAttractionNonAuthenticatedEntity from a dict
sellable_inventory_attraction_non_authenticated_entity_from_dict = SellableInventoryAttractionNonAuthenticatedEntity.from_dict(sellable_inventory_attraction_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


