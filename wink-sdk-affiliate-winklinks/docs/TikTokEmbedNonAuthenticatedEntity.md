# TikTokEmbedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_unique_id** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**embed_product_id** | **str** |  | [optional] 
**embed_type** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**width** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**thumbnail_width** | **int** |  | [optional] 
**thumbnail_height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.tik_tok_embed_non_authenticated_entity import TikTokEmbedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokEmbedNonAuthenticatedEntity from a JSON string
tik_tok_embed_non_authenticated_entity_instance = TikTokEmbedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(TikTokEmbedNonAuthenticatedEntity.to_json())

# convert the object into a dict
tik_tok_embed_non_authenticated_entity_dict = tik_tok_embed_non_authenticated_entity_instance.to_dict()
# create an instance of TikTokEmbedNonAuthenticatedEntity from a dict
tik_tok_embed_non_authenticated_entity_from_dict = TikTokEmbedNonAuthenticatedEntity.from_dict(tik_tok_embed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


