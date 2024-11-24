# AnnouncementNonAuthenticatedEntity

List of property announcements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique announcement identifier. | 
**hotel_identifier** | **str** | Hotel identifier manager has access to. | 
**start_date** | **date** | Start date for when announcement is valid | [optional] 
**end_date** | **date** | End date for when announcement is no longer valid | [optional] 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | List of all localized announcements. | 
**show_title** | **bool** | When enabled, the property does not want the title to be displayed | [optional] [default to False]
**show_always** | **bool** | When enabled, the property wants this announcement always to be displayed | [optional] [default to False]

## Example

```python
from wink_sdk_inventory.models.announcement_non_authenticated_entity import AnnouncementNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementNonAuthenticatedEntity from a JSON string
announcement_non_authenticated_entity_instance = AnnouncementNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AnnouncementNonAuthenticatedEntity.to_json())

# convert the object into a dict
announcement_non_authenticated_entity_dict = announcement_non_authenticated_entity_instance.to_dict()
# create an instance of AnnouncementNonAuthenticatedEntity from a dict
announcement_non_authenticated_entity_from_dict = AnnouncementNonAuthenticatedEntity.from_dict(announcement_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


