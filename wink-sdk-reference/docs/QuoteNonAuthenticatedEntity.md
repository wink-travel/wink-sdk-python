# QuoteNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_reference.models.quote_non_authenticated_entity import QuoteNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteNonAuthenticatedEntity from a JSON string
quote_non_authenticated_entity_instance = QuoteNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(QuoteNonAuthenticatedEntity.to_json())

# convert the object into a dict
quote_non_authenticated_entity_dict = quote_non_authenticated_entity_instance.to_dict()
# create an instance of QuoteNonAuthenticatedEntity from a dict
quote_non_authenticated_entity_from_dict = QuoteNonAuthenticatedEntity.from_dict(quote_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


