# InstagramEmbedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**thumbnail_width** | **int** |  | [optional] 
**thumbnail_height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.instagram_embed_non_authenticated_entity import InstagramEmbedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramEmbedNonAuthenticatedEntity from a JSON string
instagram_embed_non_authenticated_entity_instance = InstagramEmbedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InstagramEmbedNonAuthenticatedEntity.to_json())

# convert the object into a dict
instagram_embed_non_authenticated_entity_dict = instagram_embed_non_authenticated_entity_instance.to_dict()
# create an instance of InstagramEmbedNonAuthenticatedEntity from a dict
instagram_embed_non_authenticated_entity_from_dict = InstagramEmbedNonAuthenticatedEntity.from_dict(instagram_embed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


