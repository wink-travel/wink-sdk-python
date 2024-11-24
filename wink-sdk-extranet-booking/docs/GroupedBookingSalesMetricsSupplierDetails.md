# GroupedBookingSalesMetricsSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**type_identifier** | **str** |  | [optional] 
**bookings** | **int** |  | [optional] 
**total_price_amount** | **float** |  | [optional] 
**average_booking_amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.grouped_booking_sales_metrics_supplier_details import GroupedBookingSalesMetricsSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedBookingSalesMetricsSupplierDetails from a JSON string
grouped_booking_sales_metrics_supplier_details_instance = GroupedBookingSalesMetricsSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GroupedBookingSalesMetricsSupplierDetails.to_json())

# convert the object into a dict
grouped_booking_sales_metrics_supplier_details_dict = grouped_booking_sales_metrics_supplier_details_instance.to_dict()
# create an instance of GroupedBookingSalesMetricsSupplierDetails from a dict
grouped_booking_sales_metrics_supplier_details_from_dict = GroupedBookingSalesMetricsSupplierDetails.from_dict(grouped_booking_sales_metrics_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


