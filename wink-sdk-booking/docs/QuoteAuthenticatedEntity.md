# QuoteAuthenticatedEntity

Hotel to wink currency exchange rate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_booking.models.quote_authenticated_entity import QuoteAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAuthenticatedEntity from a JSON string
quote_authenticated_entity_instance = QuoteAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(QuoteAuthenticatedEntity.to_json())

# convert the object into a dict
quote_authenticated_entity_dict = quote_authenticated_entity_instance.to_dict()
# create an instance of QuoteAuthenticatedEntity from a dict
quote_authenticated_entity_from_dict = QuoteAuthenticatedEntity.from_dict(quote_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


