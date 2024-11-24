# UpsertAnnouncementRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date for when announcement is valid | [optional] 
**end_date** | **date** | End date for when announcement is no longer valid | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) | List of all localized announcements. | 
**show_title** | **bool** | When enabled, the property does not want the title to be displayed | [optional] [default to False]
**show_always** | **bool** | When enabled, the property wants this announcement always to be displayed | [optional] [default to False]

## Example

```python
from wink_sdk_extranet_property.models.upsert_announcement_request_supplier import UpsertAnnouncementRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAnnouncementRequestSupplier from a JSON string
upsert_announcement_request_supplier_instance = UpsertAnnouncementRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertAnnouncementRequestSupplier.to_json())

# convert the object into a dict
upsert_announcement_request_supplier_dict = upsert_announcement_request_supplier_instance.to_dict()
# create an instance of UpsertAnnouncementRequestSupplier from a dict
upsert_announcement_request_supplier_from_dict = UpsertAnnouncementRequestSupplier.from_dict(upsert_announcement_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


