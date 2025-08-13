# SellerInventoryActivityNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](ActivityLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) | Property details along with the priced activity record. | [optional] 
**configuration** | [**SellableItemLightweightNonAuthenticatedEntity**](SellableItemLightweightNonAuthenticatedEntity.md) | Identifier inventory record | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_activity_non_authenticated_entity import SellerInventoryActivityNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryActivityNonAuthenticatedEntity from a JSON string
seller_inventory_activity_non_authenticated_entity_instance = SellerInventoryActivityNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryActivityNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_activity_non_authenticated_entity_dict = seller_inventory_activity_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryActivityNonAuthenticatedEntity from a dict
seller_inventory_activity_non_authenticated_entity_from_dict = SellerInventoryActivityNonAuthenticatedEntity.from_dict(seller_inventory_activity_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


