# PayoutFeeBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Fee amount | 
**type** | **str** | Type of fee | 
**candidate** | **str** | Who pays for this fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_booking.models.payout_fee_booker import PayoutFeeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutFeeBooker from a JSON string
payout_fee_booker_instance = PayoutFeeBooker.from_json(json)
# print the JSON string representation of the object
print(PayoutFeeBooker.to_json())

# convert the object into a dict
payout_fee_booker_dict = payout_fee_booker_instance.to_dict()
# create an instance of PayoutFeeBooker from a dict
payout_fee_booker_from_dict = PayoutFeeBooker.from_dict(payout_fee_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


