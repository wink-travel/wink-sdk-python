# SpaViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**spa** | [**SpaSupplier**](SpaSupplier.md) |  | 
**featured_image_identifier** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.spa_view_supplier import SpaViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SpaViewSupplier from a JSON string
spa_view_supplier_instance = SpaViewSupplier.from_json(json)
# print the JSON string representation of the object
print(SpaViewSupplier.to_json())

# convert the object into a dict
spa_view_supplier_dict = spa_view_supplier_instance.to_dict()
# create an instance of SpaViewSupplier from a dict
spa_view_supplier_from_dict = SpaViewSupplier.from_dict(spa_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


