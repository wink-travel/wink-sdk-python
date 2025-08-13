# AbstractOpenGraphRedirectUrlNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of document the uniqueId links to | 
**language** | **str** | Which language the seller wanted to use | [default to 'en']
**currency** | **str** | Which currency the seller is using | [optional] [default to 'USD']
**title** | **str** | Link title | 
**description** | **str** | Link description | 
**keywords** | **str** | Comma-separated keyword values that can be used to populate HTML metadata | [optional] 
**unique_id** | **str** | The URL ID that uniquely represents this link | 
**twitter_account** | **str** | Optional X account ID | [optional] 
**facebook_app_id** | **str** | Optional Facebook app ID | [optional] 
**image** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) | The image you want to accompany this link | [optional] 
**video** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) | The video you want to accompany this link | [optional] 
**transact_url** | **str** | The transation url, or where to redirect to when clicking the CTA button. | 

## Example

```python
from wink_sdk_inventory.models.abstract_open_graph_redirect_url_non_authenticated_entity import AbstractOpenGraphRedirectUrlNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractOpenGraphRedirectUrlNonAuthenticatedEntity from a JSON string
abstract_open_graph_redirect_url_non_authenticated_entity_instance = AbstractOpenGraphRedirectUrlNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AbstractOpenGraphRedirectUrlNonAuthenticatedEntity.to_json())

# convert the object into a dict
abstract_open_graph_redirect_url_non_authenticated_entity_dict = abstract_open_graph_redirect_url_non_authenticated_entity_instance.to_dict()
# create an instance of AbstractOpenGraphRedirectUrlNonAuthenticatedEntity from a dict
abstract_open_graph_redirect_url_non_authenticated_entity_from_dict = AbstractOpenGraphRedirectUrlNonAuthenticatedEntity.from_dict(abstract_open_graph_redirect_url_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


