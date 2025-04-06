# SpotifyEmbedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_url** | **int** |  | [optional] 
**thumbnail_height** | **str** |  | [optional] 
**thumbnail_width** | **int** |  | [optional] 
**html** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.spotify_embed_non_authenticated_entity import SpotifyEmbedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SpotifyEmbedNonAuthenticatedEntity from a JSON string
spotify_embed_non_authenticated_entity_instance = SpotifyEmbedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SpotifyEmbedNonAuthenticatedEntity.to_json())

# convert the object into a dict
spotify_embed_non_authenticated_entity_dict = spotify_embed_non_authenticated_entity_instance.to_dict()
# create an instance of SpotifyEmbedNonAuthenticatedEntity from a dict
spotify_embed_non_authenticated_entity_from_dict = SpotifyEmbedNonAuthenticatedEntity.from_dict(spotify_embed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


