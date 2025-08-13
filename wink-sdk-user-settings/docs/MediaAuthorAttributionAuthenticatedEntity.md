# MediaAuthorAttributionAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_user_settings.models.media_author_attribution_authenticated_entity import MediaAuthorAttributionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionAuthenticatedEntity from a JSON string
media_author_attribution_authenticated_entity_instance = MediaAuthorAttributionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionAuthenticatedEntity.to_json())

# convert the object into a dict
media_author_attribution_authenticated_entity_dict = media_author_attribution_authenticated_entity_instance.to_dict()
# create an instance of MediaAuthorAttributionAuthenticatedEntity from a dict
media_author_attribution_authenticated_entity_from_dict = MediaAuthorAttributionAuthenticatedEntity.from_dict(media_author_attribution_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


