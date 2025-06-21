# SellerInventorySpaNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](SpaLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced spa record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier blocking record | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_spa_non_authenticated_entity import SellerInventorySpaNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventorySpaNonAuthenticatedEntity from a JSON string
seller_inventory_spa_non_authenticated_entity_instance = SellerInventorySpaNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventorySpaNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_spa_non_authenticated_entity_dict = seller_inventory_spa_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventorySpaNonAuthenticatedEntity from a dict
seller_inventory_spa_non_authenticated_entity_from_dict = SellerInventorySpaNonAuthenticatedEntity.from_dict(seller_inventory_spa_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


