# InventoryUsageSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_identifier** | **str** | Inventory type identifier | 
**name** | **str** | Name of the blocking | 
**type** | **str** | Inventory type | 
**item_list** | [**List[InventoryUsageItemSupplier]**](InventoryUsageItemSupplier.md) | How the inventoryIdentifier is currently being used | 
**referenced** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.inventory_usage_supplier import InventoryUsageSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUsageSupplier from a JSON string
inventory_usage_supplier_instance = InventoryUsageSupplier.from_json(json)
# print the JSON string representation of the object
print(InventoryUsageSupplier.to_json())

# convert the object into a dict
inventory_usage_supplier_dict = inventory_usage_supplier_instance.to_dict()
# create an instance of InventoryUsageSupplier from a dict
inventory_usage_supplier_from_dict = InventoryUsageSupplier.from_dict(inventory_usage_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


