# SocialNonAuthenticatedEntity

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 
**enabled** | **bool** | Whether social network is available for use. | [optional] 

## Example

```python
from wink_sdk_inventory.models.social_non_authenticated_entity import SocialNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SocialNonAuthenticatedEntity from a JSON string
social_non_authenticated_entity_instance = SocialNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SocialNonAuthenticatedEntity.to_json())

# convert the object into a dict
social_non_authenticated_entity_dict = social_non_authenticated_entity_instance.to_dict()
# create an instance of SocialNonAuthenticatedEntity from a dict
social_non_authenticated_entity_from_dict = SocialNonAuthenticatedEntity.from_dict(social_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


