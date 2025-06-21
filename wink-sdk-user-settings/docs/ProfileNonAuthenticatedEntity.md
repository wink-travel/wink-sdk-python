# ProfileNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserNonAuthenticatedEntity**](ProfileUserNonAuthenticatedEntity.md) | User details | 
**personal** | [**PersonalNonAuthenticatedEntity**](PersonalNonAuthenticatedEntity.md) | Detailed customer information for this profile | 
**preferences** | [**PreferencesNonAuthenticatedEntity**](PreferencesNonAuthenticatedEntity.md) | Customer preferences | 

## Example

```python
from wink_sdk_user_settings.models.profile_non_authenticated_entity import ProfileNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileNonAuthenticatedEntity from a JSON string
profile_non_authenticated_entity_instance = ProfileNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ProfileNonAuthenticatedEntity.to_json())

# convert the object into a dict
profile_non_authenticated_entity_dict = profile_non_authenticated_entity_instance.to_dict()
# create an instance of ProfileNonAuthenticatedEntity from a dict
profile_non_authenticated_entity_from_dict = ProfileNonAuthenticatedEntity.from_dict(profile_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


