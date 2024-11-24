# CompanyDetailsBookingSalesMetricsSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**DisplayCompanySupplier**](DisplayCompanySupplier.md) |  | [optional] 
**total** | [**GroupedBookingSalesMetricsSupplier**](GroupedBookingSalesMetricsSupplier.md) |  | [optional] 
**by_property_list** | [**List[GroupedBookingSalesMetricsSupplier]**](GroupedBookingSalesMetricsSupplier.md) |  | [optional] 
**by_country_list** | [**List[GroupedBookingSalesMetricsSupplier]**](GroupedBookingSalesMetricsSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.company_details_booking_sales_metrics_supplier import CompanyDetailsBookingSalesMetricsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetailsBookingSalesMetricsSupplier from a JSON string
company_details_booking_sales_metrics_supplier_instance = CompanyDetailsBookingSalesMetricsSupplier.from_json(json)
# print the JSON string representation of the object
print(CompanyDetailsBookingSalesMetricsSupplier.to_json())

# convert the object into a dict
company_details_booking_sales_metrics_supplier_dict = company_details_booking_sales_metrics_supplier_instance.to_dict()
# create an instance of CompanyDetailsBookingSalesMetricsSupplier from a dict
company_details_booking_sales_metrics_supplier_from_dict = CompanyDetailsBookingSalesMetricsSupplier.from_dict(company_details_booking_sales_metrics_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


