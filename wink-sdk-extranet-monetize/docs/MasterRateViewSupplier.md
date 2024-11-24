# MasterRateViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**master_rate** | [**MasterRateSupplier**](MasterRateSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_monetize.models.master_rate_view_supplier import MasterRateViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of MasterRateViewSupplier from a JSON string
master_rate_view_supplier_instance = MasterRateViewSupplier.from_json(json)
# print the JSON string representation of the object
print(MasterRateViewSupplier.to_json())

# convert the object into a dict
master_rate_view_supplier_dict = master_rate_view_supplier_instance.to_dict()
# create an instance of MasterRateViewSupplier from a dict
master_rate_view_supplier_from_dict = MasterRateViewSupplier.from_dict(master_rate_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


