# PageQuoteNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[QuoteNonAuthenticatedEntity]**](QuoteNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_reference.models.page_quote_non_authenticated_entity import PageQuoteNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageQuoteNonAuthenticatedEntity from a JSON string
page_quote_non_authenticated_entity_instance = PageQuoteNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageQuoteNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_quote_non_authenticated_entity_dict = page_quote_non_authenticated_entity_instance.to_dict()
# create an instance of PageQuoteNonAuthenticatedEntity from a dict
page_quote_non_authenticated_entity_from_dict = PageQuoteNonAuthenticatedEntity.from_dict(page_quote_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


