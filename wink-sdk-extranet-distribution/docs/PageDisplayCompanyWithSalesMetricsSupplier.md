# PageDisplayCompanyWithSalesMetricsSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[DisplayCompanyWithSalesMetricsSupplier]**](DisplayCompanyWithSalesMetricsSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.page_display_company_with_sales_metrics_supplier import PageDisplayCompanyWithSalesMetricsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageDisplayCompanyWithSalesMetricsSupplier from a JSON string
page_display_company_with_sales_metrics_supplier_instance = PageDisplayCompanyWithSalesMetricsSupplier.from_json(json)
# print the JSON string representation of the object
print(PageDisplayCompanyWithSalesMetricsSupplier.to_json())

# convert the object into a dict
page_display_company_with_sales_metrics_supplier_dict = page_display_company_with_sales_metrics_supplier_instance.to_dict()
# create an instance of PageDisplayCompanyWithSalesMetricsSupplier from a dict
page_display_company_with_sales_metrics_supplier_from_dict = PageDisplayCompanyWithSalesMetricsSupplier.from_dict(page_display_company_with_sales_metrics_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


