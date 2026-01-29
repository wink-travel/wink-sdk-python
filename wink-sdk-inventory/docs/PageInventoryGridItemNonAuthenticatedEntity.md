# PageInventoryGridItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[InventoryGridItemNonAuthenticatedEntity]**](InventoryGridItemNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.page_inventory_grid_item_non_authenticated_entity import PageInventoryGridItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageInventoryGridItemNonAuthenticatedEntity from a JSON string
page_inventory_grid_item_non_authenticated_entity_instance = PageInventoryGridItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageInventoryGridItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_inventory_grid_item_non_authenticated_entity_dict = page_inventory_grid_item_non_authenticated_entity_instance.to_dict()
# create an instance of PageInventoryGridItemNonAuthenticatedEntity from a dict
page_inventory_grid_item_non_authenticated_entity_from_dict = PageInventoryGridItemNonAuthenticatedEntity.from_dict(page_inventory_grid_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


