# SellerMediaNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**alt_text** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_media_non_authenticated_entity import SellerMediaNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaNonAuthenticatedEntity from a JSON string
seller_media_non_authenticated_entity_instance = SellerMediaNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerMediaNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_media_non_authenticated_entity_dict = seller_media_non_authenticated_entity_instance.to_dict()
# create an instance of SellerMediaNonAuthenticatedEntity from a dict
seller_media_non_authenticated_entity_from_dict = SellerMediaNonAuthenticatedEntity.from_dict(seller_media_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


