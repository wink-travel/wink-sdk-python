# AnnouncementSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**hotel_identifier** | **str** | Hotel identifier manager has access to. | 
**start_date** | **date** | Start date for when announcement is valid | [optional] 
**end_date** | **date** | End date for when announcement is no longer valid | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) |  | 
**show_title** | **bool** | When enabled, the property does not want the title to be displayed | [optional] [default to False]
**show_always** | **bool** | When enabled, the property wants this announcement always to be displayed | [optional] [default to False]

## Example

```python
from wink_sdk_extranet_property.models.announcement_supplier import AnnouncementSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementSupplier from a JSON string
announcement_supplier_instance = AnnouncementSupplier.from_json(json)
# print the JSON string representation of the object
print(AnnouncementSupplier.to_json())

# convert the object into a dict
announcement_supplier_dict = announcement_supplier_instance.to_dict()
# create an instance of AnnouncementSupplier from a dict
announcement_supplier_from_dict = AnnouncementSupplier.from_dict(announcement_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


