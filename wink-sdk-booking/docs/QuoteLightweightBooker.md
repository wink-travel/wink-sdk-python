# QuoteLightweightBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_booking.models.quote_lightweight_booker import QuoteLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLightweightBooker from a JSON string
quote_lightweight_booker_instance = QuoteLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(QuoteLightweightBooker.to_json())

# convert the object into a dict
quote_lightweight_booker_dict = quote_lightweight_booker_instance.to_dict()
# create an instance of QuoteLightweightBooker from a dict
quote_lightweight_booker_from_dict = QuoteLightweightBooker.from_dict(quote_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


