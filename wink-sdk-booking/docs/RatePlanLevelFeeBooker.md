# RatePlanLevelFeeBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionBooker]**](LocalizedDescriptionBooker.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Rate plan level fixed fee amount in property currency | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_booking.models.rate_plan_level_fee_booker import RatePlanLevelFeeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeBooker from a JSON string
rate_plan_level_fee_booker_instance = RatePlanLevelFeeBooker.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeBooker.to_json())

# convert the object into a dict
rate_plan_level_fee_booker_dict = rate_plan_level_fee_booker_instance.to_dict()
# create an instance of RatePlanLevelFeeBooker from a dict
rate_plan_level_fee_booker_from_dict = RatePlanLevelFeeBooker.from_dict(rate_plan_level_fee_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


