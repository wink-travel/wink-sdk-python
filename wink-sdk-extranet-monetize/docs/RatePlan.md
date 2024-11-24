# RatePlan

An optional rate plan can be applied to the add-on. The rate plan can help to create availability restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Rate plan identifier | 
**hotel_identifier** | **str** | Hotel Identifier | 
**name** | **str** | Provides the name of the rate plan. | 
**prepaid** | **bool** | When true, indicates if the rate is a prepaid rate. | [default to False]
**enabled** | **bool** | Whether rate plan is active or not. | [default to False]
**breakfast** | **bool** | When true, indicates breakfast is included. | [default to False]
**brunch** | **bool** | When true, indicates brunch is included. | [default to False]
**lunch** | **bool** | When true, indicates lunch is included. | [default to False]
**dinner** | **bool** | When true, indicates dinner is included. | [default to False]
**all_inclusive** | **bool** | Everything included except alcohol | [default to False]
**all_inclusive_plus_alcohol** | **bool** | Everything included with alcohol | [default to False]
**sell_start_date** | **date** | Set a start date for when to start selling this rate. When sellStartDate and sellEndDate are set, this rate is only available for sale within that date range. | [optional] 
**sell_end_date** | **date** | Set an end date for when to finish selling this rate. When sellStartDate and sellEndDate are set, this rate is only available for sale within that date range. | [optional] 
**stay_start_date** | **date** | Set a start date for when the guest can visit. When stayStartDate and stayEndDate are set, this rate is only available for stay within that date range. | [optional] 
**stay_end_date** | **date** | Set an end date for when the guest can visit. When stayStartDate and stayEndDate are set, this rate is only available for stay within that date range. | [optional] 
**loyalty_points_accrue** | **bool** | Property honors loyalty points with this rate plan. | [optional] [default to False]
**max_advance_booking_offset** | **int** | Maximum days before the arrival date for which this rate plan may be booked. | [optional] 
**min_advance_booking_offset** | **int** | Minimum days before the arrival date for which this rate plan may be booked. | [optional] 
**min_total_occupancy** | **int** | Defines the minimum number of total occupants required for this rate plan. | [optional] 
**max_total_occupancy** | **int** | Defines the maximum number of total occupants required for this rate plan. | [optional] 
**min_los** | **int** | Indicates the minimum length of stay required for this rate plan. | [optional] 
**max_los** | **int** | Indicates the maximum length of stay. | [optional] 
**min_age** | **int** | The minimum age to qualify for this rate plan. | [optional] 
**max_age** | **int** | The maximum age to qualify for this rate plan. | [optional] 
**rate_plan_level_fees** | [**List[RatePlanLevelFee]**](RatePlanLevelFee.md) | This can be a one-time fee such as a cleaning fee | [optional] 
**available_days_of_week** | [**DowPatternGroup**](DowPatternGroup.md) |  | [optional] 
**arrival_days_of_week** | [**DowPatternGroup**](DowPatternGroup.md) |  | [optional] 
**departure_days_of_week** | [**DowPatternGroup**](DowPatternGroup.md) |  | [optional] 
**required_days_of_week** | [**DowPatternGroup**](DowPatternGroup.md) |  | [optional] 
**early_check_in_charge** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**late_check_out_charge** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**cancellation_policy_identifier** | **str** | The cancellation policy for this rate plan. | 
**cancellation_policy** | [**CancellationPolicy**](CancellationPolicy.md) |  | [optional] 
**cancellation_policy_exceptions** | [**CancellationPolicyExceptions**](CancellationPolicyExceptions.md) |  | [optional] 
**single_occupancy_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.rate_plan import RatePlan

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlan from a JSON string
rate_plan_instance = RatePlan.from_json(json)
# print the JSON string representation of the object
print(RatePlan.to_json())

# convert the object into a dict
rate_plan_dict = rate_plan_instance.to_dict()
# create an instance of RatePlan from a dict
rate_plan_from_dict = RatePlan.from_dict(rate_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


