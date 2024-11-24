# QuoteNonAuthenticatedEntity

Exchange rate quote between the property's source currency and the reactive's currency that was used to populate price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_lookup.models.quote_non_authenticated_entity import QuoteNonAuthenticatedEntity

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


