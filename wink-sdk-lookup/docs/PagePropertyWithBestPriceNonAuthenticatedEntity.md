# PagePropertyWithBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[PropertyWithBestPriceNonAuthenticatedEntity]**](PropertyWithBestPriceNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.page_property_with_best_price_non_authenticated_entity import PagePropertyWithBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PagePropertyWithBestPriceNonAuthenticatedEntity from a JSON string
page_property_with_best_price_non_authenticated_entity_instance = PagePropertyWithBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PagePropertyWithBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_property_with_best_price_non_authenticated_entity_dict = page_property_with_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of PagePropertyWithBestPriceNonAuthenticatedEntity from a dict
page_property_with_best_price_non_authenticated_entity_from_dict = PagePropertyWithBestPriceNonAuthenticatedEntity.from_dict(page_property_with_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


