# CompanyDetailsBookingSalesMetricsAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_account** | [**BrowseAffiliateAccountAuthenticatedEntity**](BrowseAffiliateAccountAuthenticatedEntity.md) |  | [optional] 
**total** | [**GroupedBookingSalesMetricsAuthenticatedEntity**](GroupedBookingSalesMetricsAuthenticatedEntity.md) |  | [optional] 
**by_property_list** | [**List[GroupedBookingSalesMetricsAuthenticatedEntity]**](GroupedBookingSalesMetricsAuthenticatedEntity.md) |  | [optional] 
**by_country_list** | [**List[GroupedBookingSalesMetricsAuthenticatedEntity]**](GroupedBookingSalesMetricsAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.company_details_booking_sales_metrics_authenticated_entity import CompanyDetailsBookingSalesMetricsAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetailsBookingSalesMetricsAuthenticatedEntity from a JSON string
company_details_booking_sales_metrics_authenticated_entity_instance = CompanyDetailsBookingSalesMetricsAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CompanyDetailsBookingSalesMetricsAuthenticatedEntity.to_json())

# convert the object into a dict
company_details_booking_sales_metrics_authenticated_entity_dict = company_details_booking_sales_metrics_authenticated_entity_instance.to_dict()
# create an instance of CompanyDetailsBookingSalesMetricsAuthenticatedEntity from a dict
company_details_booking_sales_metrics_authenticated_entity_from_dict = CompanyDetailsBookingSalesMetricsAuthenticatedEntity.from_dict(company_details_booking_sales_metrics_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


