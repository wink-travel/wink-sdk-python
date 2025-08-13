# SellerInventoryPropertyNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**PropertyWithBestPriceNonAuthenticatedEntity**](PropertyWithBestPriceNonAuthenticatedEntity.md) | Property details along with the best price this property has to offer. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_property_non_authenticated_entity import SellerInventoryPropertyNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryPropertyNonAuthenticatedEntity from a JSON string
seller_inventory_property_non_authenticated_entity_instance = SellerInventoryPropertyNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryPropertyNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_property_non_authenticated_entity_dict = seller_inventory_property_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryPropertyNonAuthenticatedEntity from a dict
seller_inventory_property_non_authenticated_entity_from_dict = SellerInventoryPropertyNonAuthenticatedEntity.from_dict(seller_inventory_property_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


