# AnnouncementLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date for when announcement is valid | [optional] 
**end_date** | **date** | End date for when announcement is no longer valid | [optional] 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | List of all localized announcements. | 
**show_title** | **bool** | When enabled, the property does not want the title to be displayed | [optional] [default to False]
**show_always** | **bool** | When enabled, the property wants this announcement always to be displayed | [optional] [default to False]

## Example

```python
from wink_sdk_inventory.models.announcement_lightweight_non_authenticated_entity import AnnouncementLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementLightweightNonAuthenticatedEntity from a JSON string
announcement_lightweight_non_authenticated_entity_instance = AnnouncementLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AnnouncementLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
announcement_lightweight_non_authenticated_entity_dict = announcement_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of AnnouncementLightweightNonAuthenticatedEntity from a dict
announcement_lightweight_non_authenticated_entity_from_dict = AnnouncementLightweightNonAuthenticatedEntity.from_dict(announcement_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


