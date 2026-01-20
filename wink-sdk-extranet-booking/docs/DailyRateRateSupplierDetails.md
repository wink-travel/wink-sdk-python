# DailyRateRateSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier. | 
**hotel_identifier** | **UUID** | Owner of daily rate. | 
**rate_source** | **str** | Indicate where this rate originated from. Leave as TRAVELIKO unless you are a channel manager and responsible for the property&#39;s rates externally of this platform. | [default to 'TRAVELIKO']
**rate_plan_identifier** | **UUID** | Rate plan associated with this daily rate. | 
**guest_room_identifier** | **UUID** | Guest room associated with this daily rate. | 
**rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**master** | **bool** | This flag indicates whether this rate is available for this date. | [default to True]
**closed_on_arrival** | **bool** | This flag indicates whether a guest can arrive at the property on this date. | [default to False]
**closed_on_departure** | **bool** | This flag indicates whether a guest can leave the property on this date. | [default to False]
**var_date** | **date** | The date this rate is applicable for. | 
**quantity** | **int** | Amount of rooms available for this date. | [optional] [default to 0]
**min_occupancy** | **int** | Minimum number of guests allowed in a room type. | [default to 1]
**max_occupancy** | **int** | Maximum number of guest allowed in a room type. | [default to 2]
**min_length_of_stay** | **int** | Control the minimum length of stay at the day-level. This means that a guest arriving within this date range is required to stay at least these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] [default to -1]
**max_length_of_stay** | **int** | Control the maximum length of stay at the day-level. This means that a guest arriving within this date range is required to stay no longer than these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] [default to -1]
**single_occupancy_rate_modifier** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.daily_rate_rate_supplier_details import DailyRateRateSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRateRateSupplierDetails from a JSON string
daily_rate_rate_supplier_details_instance = DailyRateRateSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DailyRateRateSupplierDetails.to_json())

# convert the object into a dict
daily_rate_rate_supplier_details_dict = daily_rate_rate_supplier_details_instance.to_dict()
# create an instance of DailyRateRateSupplierDetails from a dict
daily_rate_rate_supplier_details_from_dict = DailyRateRateSupplierDetails.from_dict(daily_rate_rate_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


