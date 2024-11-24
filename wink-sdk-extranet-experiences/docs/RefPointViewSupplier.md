# RefPointViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**ref_point** | [**RefPointSupplier**](RefPointSupplier.md) |  | [optional] 
**featured_image_identifier** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_experiences.models.ref_point_view_supplier import RefPointViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RefPointViewSupplier from a JSON string
ref_point_view_supplier_instance = RefPointViewSupplier.from_json(json)
# print the JSON string representation of the object
print(RefPointViewSupplier.to_json())

# convert the object into a dict
ref_point_view_supplier_dict = ref_point_view_supplier_instance.to_dict()
# create an instance of RefPointViewSupplier from a dict
ref_point_view_supplier_from_dict = RefPointViewSupplier.from_dict(ref_point_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


