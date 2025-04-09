# PageInventoryViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[InventoryViewSupplier]**](InventoryViewSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.page_inventory_view_supplier import PageInventoryViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageInventoryViewSupplier from a JSON string
page_inventory_view_supplier_instance = PageInventoryViewSupplier.from_json(json)
# print the JSON string representation of the object
print(PageInventoryViewSupplier.to_json())

# convert the object into a dict
page_inventory_view_supplier_dict = page_inventory_view_supplier_instance.to_dict()
# create an instance of PageInventoryViewSupplier from a dict
page_inventory_view_supplier_from_dict = PageInventoryViewSupplier.from_dict(page_inventory_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


