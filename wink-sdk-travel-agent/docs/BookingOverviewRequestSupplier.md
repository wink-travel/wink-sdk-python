# BookingOverviewRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of time series that should be used | 
**units** | **int** | How many units of the timeseries type should be used | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_overview_request_supplier import BookingOverviewRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingOverviewRequestSupplier from a JSON string
booking_overview_request_supplier_instance = BookingOverviewRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingOverviewRequestSupplier.to_json())

# convert the object into a dict
booking_overview_request_supplier_dict = booking_overview_request_supplier_instance.to_dict()
# create an instance of BookingOverviewRequestSupplier from a dict
booking_overview_request_supplier_from_dict = BookingOverviewRequestSupplier.from_dict(booking_overview_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


