# PageInventorySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[InventorySupplier]**](InventorySupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.page_inventory_supplier import PageInventorySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageInventorySupplier from a JSON string
page_inventory_supplier_instance = PageInventorySupplier.from_json(json)
# print the JSON string representation of the object
print(PageInventorySupplier.to_json())

# convert the object into a dict
page_inventory_supplier_dict = page_inventory_supplier_instance.to_dict()
# create an instance of PageInventorySupplier from a dict
page_inventory_supplier_from_dict = PageInventorySupplier.from_dict(page_inventory_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


