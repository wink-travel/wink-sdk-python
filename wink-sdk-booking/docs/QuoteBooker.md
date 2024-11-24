# QuoteBooker

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
from wink_sdk_booking.models.quote_booker import QuoteBooker

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteBooker from a JSON string
quote_booker_instance = QuoteBooker.from_json(json)
# print the JSON string representation of the object
print(QuoteBooker.to_json())

# convert the object into a dict
quote_booker_dict = quote_booker_instance.to_dict()
# create an instance of QuoteBooker from a dict
quote_booker_from_dict = QuoteBooker.from_dict(quote_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


