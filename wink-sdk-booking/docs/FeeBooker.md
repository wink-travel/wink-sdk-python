# FeeBooker

Fees associated with this booking contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Type of fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_booking.models.fee_booker import FeeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBooker from a JSON string
fee_booker_instance = FeeBooker.from_json(json)
# print the JSON string representation of the object
print(FeeBooker.to_json())

# convert the object into a dict
fee_booker_dict = fee_booker_instance.to_dict()
# create an instance of FeeBooker from a dict
fee_booker_from_dict = FeeBooker.from_dict(fee_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


