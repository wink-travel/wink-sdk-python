# InventoryUsageItemSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **str** | The type of technology using the inventory | 
**count** | **int** |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.inventory_usage_item_supplier import InventoryUsageItemSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUsageItemSupplier from a JSON string
inventory_usage_item_supplier_instance = InventoryUsageItemSupplier.from_json(json)
# print the JSON string representation of the object
print(InventoryUsageItemSupplier.to_json())

# convert the object into a dict
inventory_usage_item_supplier_dict = inventory_usage_item_supplier_instance.to_dict()
# create an instance of InventoryUsageItemSupplier from a dict
inventory_usage_item_supplier_from_dict = InventoryUsageItemSupplier.from_dict(inventory_usage_item_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


