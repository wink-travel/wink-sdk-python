# PageExchangeRateViewNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ExchangeRateViewNonAuthenticatedEntity]**](ExchangeRateViewNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_reference.models.page_exchange_rate_view_non_authenticated_entity import PageExchangeRateViewNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageExchangeRateViewNonAuthenticatedEntity from a JSON string
page_exchange_rate_view_non_authenticated_entity_instance = PageExchangeRateViewNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageExchangeRateViewNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_exchange_rate_view_non_authenticated_entity_dict = page_exchange_rate_view_non_authenticated_entity_instance.to_dict()
# create an instance of PageExchangeRateViewNonAuthenticatedEntity from a dict
page_exchange_rate_view_non_authenticated_entity_from_dict = PageExchangeRateViewNonAuthenticatedEntity.from_dict(page_exchange_rate_view_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


