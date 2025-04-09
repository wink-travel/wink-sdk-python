# PageConsumableSyndicationEntryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ConsumableSyndicationEntryNonAuthenticatedEntity]**](ConsumableSyndicationEntryNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.page_consumable_syndication_entry_non_authenticated_entity import PageConsumableSyndicationEntryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageConsumableSyndicationEntryNonAuthenticatedEntity from a JSON string
page_consumable_syndication_entry_non_authenticated_entity_instance = PageConsumableSyndicationEntryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageConsumableSyndicationEntryNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_consumable_syndication_entry_non_authenticated_entity_dict = page_consumable_syndication_entry_non_authenticated_entity_instance.to_dict()
# create an instance of PageConsumableSyndicationEntryNonAuthenticatedEntity from a dict
page_consumable_syndication_entry_non_authenticated_entity_from_dict = PageConsumableSyndicationEntryNonAuthenticatedEntity.from_dict(page_consumable_syndication_entry_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


