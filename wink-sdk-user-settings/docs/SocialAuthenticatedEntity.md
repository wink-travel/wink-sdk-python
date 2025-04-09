# SocialAuthenticatedEntity

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 

## Example

```python
from wink_sdk_user_settings.models.social_authenticated_entity import SocialAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAuthenticatedEntity from a JSON string
social_authenticated_entity_instance = SocialAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SocialAuthenticatedEntity.to_json())

# convert the object into a dict
social_authenticated_entity_dict = social_authenticated_entity_instance.to_dict()
# create an instance of SocialAuthenticatedEntity from a dict
social_authenticated_entity_from_dict = SocialAuthenticatedEntity.from_dict(social_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


