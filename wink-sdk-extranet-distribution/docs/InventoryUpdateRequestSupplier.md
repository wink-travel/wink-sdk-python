# InventoryUpdateRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique record identifier | 
**enabled** | **bool** | Flag the supplier can use to enable / disable this blocking | [default to True]

## Example

```python
from wink_sdk_extranet_distribution.models.inventory_update_request_supplier import InventoryUpdateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateRequestSupplier from a JSON string
inventory_update_request_supplier_instance = InventoryUpdateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateRequestSupplier.to_json())

# convert the object into a dict
inventory_update_request_supplier_dict = inventory_update_request_supplier_instance.to_dict()
# create an instance of InventoryUpdateRequestSupplier from a dict
inventory_update_request_supplier_from_dict = InventoryUpdateRequestSupplier.from_dict(inventory_update_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


