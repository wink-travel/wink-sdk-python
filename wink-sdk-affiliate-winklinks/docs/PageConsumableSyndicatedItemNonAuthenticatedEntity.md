# PageConsumableSyndicatedItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ConsumableSyndicatedItemNonAuthenticatedEntity]**](ConsumableSyndicatedItemNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.page_consumable_syndicated_item_non_authenticated_entity import PageConsumableSyndicatedItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageConsumableSyndicatedItemNonAuthenticatedEntity from a JSON string
page_consumable_syndicated_item_non_authenticated_entity_instance = PageConsumableSyndicatedItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageConsumableSyndicatedItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_consumable_syndicated_item_non_authenticated_entity_dict = page_consumable_syndicated_item_non_authenticated_entity_instance.to_dict()
# create an instance of PageConsumableSyndicatedItemNonAuthenticatedEntity from a dict
page_consumable_syndicated_item_non_authenticated_entity_from_dict = PageConsumableSyndicatedItemNonAuthenticatedEntity.from_dict(page_consumable_syndicated_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


