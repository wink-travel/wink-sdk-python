# QuoteLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_reference.models.quote_lightweight_non_authenticated_entity import QuoteLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLightweightNonAuthenticatedEntity from a JSON string
quote_lightweight_non_authenticated_entity_instance = QuoteLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(QuoteLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
quote_lightweight_non_authenticated_entity_dict = quote_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of QuoteLightweightNonAuthenticatedEntity from a dict
quote_lightweight_non_authenticated_entity_from_dict = QuoteLightweightNonAuthenticatedEntity.from_dict(quote_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


