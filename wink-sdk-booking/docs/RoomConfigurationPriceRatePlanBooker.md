# RoomConfigurationPriceRatePlanBooker

Rate plan used for this stay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Rate plan identifier | 
**name** | **str** | Provides the name of the rate plan. | 
**breakfast** | **bool** | When true, indicates breakfast is included. | [default to False]
**brunch** | **bool** | When true, indicates brunch is included. | [default to False]
**lunch** | **bool** | When true, indicates lunch is included. | [default to False]
**dinner** | **bool** | When true, indicates dinner is included. | [default to False]
**all_inclusive** | **bool** | Everything included except alcohol | [default to False]
**all_inclusive_plus_alcohol** | **bool** | Everything included with alcohol | [default to False]
**early_check_in_charge** | **object** |  | [optional] 
**late_check_out_charge** | **object** |  | [optional] 
**cancellation_policy** | [**CancellationPolicyBooker**](CancellationPolicyBooker.md) |  | [optional] 
**cancellation_policy_exceptions** | [**CancellationPolicyExceptionsBooker**](CancellationPolicyExceptionsBooker.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.room_configuration_price_rate_plan_booker import RoomConfigurationPriceRatePlanBooker

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceRatePlanBooker from a JSON string
room_configuration_price_rate_plan_booker_instance = RoomConfigurationPriceRatePlanBooker.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceRatePlanBooker.to_json())

# convert the object into a dict
room_configuration_price_rate_plan_booker_dict = room_configuration_price_rate_plan_booker_instance.to_dict()
# create an instance of RoomConfigurationPriceRatePlanBooker from a dict
room_configuration_price_rate_plan_booker_from_dict = RoomConfigurationPriceRatePlanBooker.from_dict(room_configuration_price_rate_plan_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


