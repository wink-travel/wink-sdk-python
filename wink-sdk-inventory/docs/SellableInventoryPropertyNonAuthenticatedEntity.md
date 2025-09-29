# SellableInventoryPropertyNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best price this property has to offer. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_inventory_property_non_authenticated_entity import SellableInventoryPropertyNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableInventoryPropertyNonAuthenticatedEntity from a JSON string
sellable_inventory_property_non_authenticated_entity_instance = SellableInventoryPropertyNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableInventoryPropertyNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_inventory_property_non_authenticated_entity_dict = sellable_inventory_property_non_authenticated_entity_instance.to_dict()
# create an instance of SellableInventoryPropertyNonAuthenticatedEntity from a dict
sellable_inventory_property_non_authenticated_entity_from_dict = SellableInventoryPropertyNonAuthenticatedEntity.from_dict(sellable_inventory_property_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


