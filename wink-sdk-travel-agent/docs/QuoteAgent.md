# QuoteAgent

The quote used to create totalCapturePrice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_travel_agent.models.quote_agent import QuoteAgent

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAgent from a JSON string
quote_agent_instance = QuoteAgent.from_json(json)
# print the JSON string representation of the object
print(QuoteAgent.to_json())

# convert the object into a dict
quote_agent_dict = quote_agent_instance.to_dict()
# create an instance of QuoteAgent from a dict
quote_agent_from_dict = QuoteAgent.from_dict(quote_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


