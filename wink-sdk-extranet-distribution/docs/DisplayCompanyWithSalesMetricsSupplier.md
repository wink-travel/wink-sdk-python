# DisplayCompanyWithSalesMetricsSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_identifier** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_geo_name_id** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**city_geo_name_id** | **str** |  | [optional] 
**bookings** | **int** |  | [optional] 
**total_price_amount** | **float** |  | [optional] 
**average_booking_amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.display_company_with_sales_metrics_supplier import DisplayCompanyWithSalesMetricsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayCompanyWithSalesMetricsSupplier from a JSON string
display_company_with_sales_metrics_supplier_instance = DisplayCompanyWithSalesMetricsSupplier.from_json(json)
# print the JSON string representation of the object
print(DisplayCompanyWithSalesMetricsSupplier.to_json())

# convert the object into a dict
display_company_with_sales_metrics_supplier_dict = display_company_with_sales_metrics_supplier_instance.to_dict()
# create an instance of DisplayCompanyWithSalesMetricsSupplier from a dict
display_company_with_sales_metrics_supplier_from_dict = DisplayCompanyWithSalesMetricsSupplier.from_dict(display_company_with_sales_metrics_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


