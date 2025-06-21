# ExtraChargeBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeBooker**](RatePlanLevelFeeBooker.md) | What the guest is paying extra for | [optional] 
**unit_price** | [**LocalizedPriceBooker**](LocalizedPriceBooker.md) | The localized unit price of the extra charge | [optional] 
**price** | [**LocalizedPriceBooker**](LocalizedPriceBooker.md) | The localized price of the extra charge | [optional] 

## Example

```python
from wink_sdk_booking.models.extra_charge_booker import ExtraChargeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeBooker from a JSON string
extra_charge_booker_instance = ExtraChargeBooker.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeBooker.to_json())

# convert the object into a dict
extra_charge_booker_dict = extra_charge_booker_instance.to_dict()
# create an instance of ExtraChargeBooker from a dict
extra_charge_booker_from_dict = ExtraChargeBooker.from_dict(extra_charge_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


