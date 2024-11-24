# AnnouncementSupplier

Announcement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique announcement identifier. | 
**hotel_identifier** | **str** | Hotel identifier manager has access to. | 
**start_date** | **date** | Start date for when announcement is valid | [optional] 
**end_date** | **date** | End date for when announcement is no longer valid | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) | List of all localized announcements. | 
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


