# RateSupplier

Holds all the information for one rate date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**hotel_identifier** | **str** | Owner of daily rate. | 
**rate_source** | **str** | Indicate where this rate originated from. Leave as TRAVELIKO unless you are a channel manager and responsible for the property&#39;s rates externally of this platform. | [default to 'TRAVELIKO']
**rate_plan_identifier** | **str** | Rate plan associated with this daily rate. | 
**guest_room_identifier** | **str** | Guest room associated with this daily rate. | 
**rate** | **float** | Guest room associated with this daily rate. | 
**currency_code** | **str** | The currencyCode property operates in. | 
**master** | **bool** | This flag indicates whether this rate is available for this date. | [default to True]
**closed_on_arrival** | **bool** | This flag indicates whether a guest can arrive at the property on this date. | [default to False]
**closed_on_departure** | **bool** | This flag indicates whether a guest can leave the property on this date. | [default to False]
**day** | **int** | Day of month | [optional] 
**month** | **int** | Month | [optional] 
**year** | **int** | Year | [optional] 
**quantity** | **int** | Amount of rooms available for this date. | [optional] [default to 0]
**min_length_of_stay** | **int** | Control the minimum length of stay at the day-level. This means that a guest arriving within this date range is required to stay at least these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] [default to -1]
**max_length_of_stay** | **int** | Control the maximum length of stay at the day-level. This means that a guest arriving within this date range is required to stay no longer than these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] [default to -1]
**single_occupancy_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**ttl** | **datetime** | When this rate can be safely removed. | 
**available** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.rate_supplier import RateSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RateSupplier from a JSON string
rate_supplier_instance = RateSupplier.from_json(json)
# print the JSON string representation of the object
print(RateSupplier.to_json())

# convert the object into a dict
rate_supplier_dict = rate_supplier_instance.to_dict()
# create an instance of RateSupplier from a dict
rate_supplier_from_dict = RateSupplier.from_dict(rate_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


