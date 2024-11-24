# SellerInventoryAddOnNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity**](AddOnLocalizedInventoryWithHotelBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**configuration** | [**SellerInventoryItemNonAuthenticatedEntity**](SellerInventoryItemNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_add_on_non_authenticated_entity import SellerInventoryAddOnNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryAddOnNonAuthenticatedEntity from a JSON string
seller_inventory_add_on_non_authenticated_entity_instance = SellerInventoryAddOnNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryAddOnNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_add_on_non_authenticated_entity_dict = seller_inventory_add_on_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryAddOnNonAuthenticatedEntity from a dict
seller_inventory_add_on_non_authenticated_entity_from_dict = SellerInventoryAddOnNonAuthenticatedEntity.from_dict(seller_inventory_add_on_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


