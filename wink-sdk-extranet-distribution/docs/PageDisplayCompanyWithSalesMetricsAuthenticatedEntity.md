# PageDisplayCompanyWithSalesMetricsAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[DisplayCompanyWithSalesMetricsAuthenticatedEntity]**](DisplayCompanyWithSalesMetricsAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.page_display_company_with_sales_metrics_authenticated_entity import PageDisplayCompanyWithSalesMetricsAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageDisplayCompanyWithSalesMetricsAuthenticatedEntity from a JSON string
page_display_company_with_sales_metrics_authenticated_entity_instance = PageDisplayCompanyWithSalesMetricsAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageDisplayCompanyWithSalesMetricsAuthenticatedEntity.to_json())

# convert the object into a dict
page_display_company_with_sales_metrics_authenticated_entity_dict = page_display_company_with_sales_metrics_authenticated_entity_instance.to_dict()
# create an instance of PageDisplayCompanyWithSalesMetricsAuthenticatedEntity from a dict
page_display_company_with_sales_metrics_authenticated_entity_from_dict = PageDisplayCompanyWithSalesMetricsAuthenticatedEntity.from_dict(page_display_company_with_sales_metrics_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


