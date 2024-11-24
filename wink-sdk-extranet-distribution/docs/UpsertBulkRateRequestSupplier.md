# UpsertBulkRateRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date for where you want to begin updating rates | 
**end_date** | **date** | End date for where you want to stop updating rates | 
**rate_source** | **str** | Indicate where this rate originated from. Leave as TRAVELIKO unless you are a channel manager and responsible for the property&#39;s rates externally of this platform. | [default to 'TRAVELIKO']
**master** | **bool** | This flag indicates whether this rate is available for this date. | [default to True]
**closed_on_arrival** | **bool** | This flag indicates whether a guest can arrive at the property on this date. | [default to False]
**closed_on_departure** | **bool** | This flag indicates whether a guest can leave the property on this date. | [default to False]
**number_of_units** | **int** | Update the amount of rooms available for this date range. Leave empty if you don&#39;t want to update this property. | [optional] 
**rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**min_length_of_stay** | **int** | Control the minimum length of stay at the day-level. This means that a guest arriving within this date range is required to stay at least these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] 
**max_length_of_stay** | **int** | Control the maximum length of stay at the day-level. This means that a guest arriving within this date range is required to stay no longer than these number of days in order to get this rate. Leave empty if you don&#39;t want to update this property. | [optional] 
**single_occupancy_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.upsert_bulk_rate_request_supplier import UpsertBulkRateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBulkRateRequestSupplier from a JSON string
upsert_bulk_rate_request_supplier_instance = UpsertBulkRateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertBulkRateRequestSupplier.to_json())

# convert the object into a dict
upsert_bulk_rate_request_supplier_dict = upsert_bulk_rate_request_supplier_instance.to_dict()
# create an instance of UpsertBulkRateRequestSupplier from a dict
upsert_bulk_rate_request_supplier_from_dict = UpsertBulkRateRequestSupplier.from_dict(upsert_bulk_rate_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


