# BookingAnalyticsSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charts** | [**List[LineChartSupplier]**](LineChartSupplier.md) | Interesting property-level chart data overview | 

## Example

```python
from wink_sdk_extranet_booking.models.booking_analytics_supplier import BookingAnalyticsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingAnalyticsSupplier from a JSON string
booking_analytics_supplier_instance = BookingAnalyticsSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingAnalyticsSupplier.to_json())

# convert the object into a dict
booking_analytics_supplier_dict = booking_analytics_supplier_instance.to_dict()
# create an instance of BookingAnalyticsSupplier from a dict
booking_analytics_supplier_from_dict = BookingAnalyticsSupplier.from_dict(booking_analytics_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


