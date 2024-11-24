# SellerInventoryListResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_page** | [**PageInventoryGridItemNonAuthenticatedEntity**](PageInventoryGridItemNonAuthenticatedEntity.md) |  | [optional] 
**configuration** | [**SellerInventoryListNonAuthenticatedEntity**](SellerInventoryListNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_inventory_list_response_non_authenticated_entity import SellerInventoryListResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerInventoryListResponseNonAuthenticatedEntity from a JSON string
seller_inventory_list_response_non_authenticated_entity_instance = SellerInventoryListResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerInventoryListResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_inventory_list_response_non_authenticated_entity_dict = seller_inventory_list_response_non_authenticated_entity_instance.to_dict()
# create an instance of SellerInventoryListResponseNonAuthenticatedEntity from a dict
seller_inventory_list_response_non_authenticated_entity_from_dict = SellerInventoryListResponseNonAuthenticatedEntity.from_dict(seller_inventory_list_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


