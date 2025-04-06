# FacebookEmbedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.facebook_embed_non_authenticated_entity import FacebookEmbedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookEmbedNonAuthenticatedEntity from a JSON string
facebook_embed_non_authenticated_entity_instance = FacebookEmbedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(FacebookEmbedNonAuthenticatedEntity.to_json())

# convert the object into a dict
facebook_embed_non_authenticated_entity_dict = facebook_embed_non_authenticated_entity_instance.to_dict()
# create an instance of FacebookEmbedNonAuthenticatedEntity from a dict
facebook_embed_non_authenticated_entity_from_dict = FacebookEmbedNonAuthenticatedEntity.from_dict(facebook_embed_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


