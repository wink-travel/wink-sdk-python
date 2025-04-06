# TwitterEmbedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**cache_age** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.twitter_embed_non_authenticated_entity import TwitterEmbedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterEmbedNonAuthenticatedEntity from a JSON string
twitter_embed_non_authenticated_entity_instance = TwitterEmbedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(TwitterEmbedNonAuthenticatedEntity.to_json())

# convert the object into a dict
twitter_embed_non_authenticated_entity_dict = twitter_embed_non_authenticated_entity_instance.to_dict()
# create an instance of TwitterEmbedNonAuthenticatedEntity from a dict
twitter_embed_non_authenticated_entity_from_dict = TwitterEmbedNonAuthenticatedEntity.from_dict(twitter_embed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


