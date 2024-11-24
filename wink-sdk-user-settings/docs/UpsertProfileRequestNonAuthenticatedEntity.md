# UpsertProfileRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserNonAuthenticatedEntity**](ProfileUserNonAuthenticatedEntity.md) |  | 
**personal** | [**PersonalNonAuthenticatedEntity**](PersonalNonAuthenticatedEntity.md) |  | 
**preferences** | [**PreferencesNonAuthenticatedEntity**](PreferencesNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_user_settings.models.upsert_profile_request_non_authenticated_entity import UpsertProfileRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertProfileRequestNonAuthenticatedEntity from a JSON string
upsert_profile_request_non_authenticated_entity_instance = UpsertProfileRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpsertProfileRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
upsert_profile_request_non_authenticated_entity_dict = upsert_profile_request_non_authenticated_entity_instance.to_dict()
# create an instance of UpsertProfileRequestNonAuthenticatedEntity from a dict
upsert_profile_request_non_authenticated_entity_from_dict = UpsertProfileRequestNonAuthenticatedEntity.from_dict(upsert_profile_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


