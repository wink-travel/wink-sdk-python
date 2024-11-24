# AnnouncementViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**announcement** | [**AnnouncementSupplier**](AnnouncementSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_property.models.announcement_view_supplier import AnnouncementViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementViewSupplier from a JSON string
announcement_view_supplier_instance = AnnouncementViewSupplier.from_json(json)
# print the JSON string representation of the object
print(AnnouncementViewSupplier.to_json())

# convert the object into a dict
announcement_view_supplier_dict = announcement_view_supplier_instance.to_dict()
# create an instance of AnnouncementViewSupplier from a dict
announcement_view_supplier_from_dict = AnnouncementViewSupplier.from_dict(announcement_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


