# ProfileNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserNonAuthenticatedEntity**](ProfileUserNonAuthenticatedEntity.md) |  | 
**personal** | [**PersonalNonAuthenticatedEntity**](PersonalNonAuthenticatedEntity.md) |  | 
**preferences** | [**PreferencesNonAuthenticatedEntity**](PreferencesNonAuthenticatedEntity.md) |  | 

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


