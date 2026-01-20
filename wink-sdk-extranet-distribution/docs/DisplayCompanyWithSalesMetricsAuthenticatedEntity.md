# DisplayCompanyWithSalesMetricsAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_identifier** | **str** | The company ID. | [optional] 
**type** | **str** | The company type | [optional] 
**owner_name** | **str** | The company name | [optional] 
**url_name** | **str** | The company url slug | [optional] 
**continent** | **str** | The company continent | [optional] 
**country** | **str** | The company country | [optional] 
**country_geo_name_id** | **str** | The company country geo name ID | [optional] 
**city** | **str** | The company city | [optional] 
**city_geo_name_id** | **str** | The company city geo name ID | [optional] 
**owner_image_id** | **str** | The company image ID | [optional] 
**description** | **str** |  | [optional] 
**bookings** | **int** |  | [optional] 
**total_price_amount** | **float** |  | [optional] 
**average_booking_amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.display_company_with_sales_metrics_authenticated_entity import DisplayCompanyWithSalesMetricsAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayCompanyWithSalesMetricsAuthenticatedEntity from a JSON string
display_company_with_sales_metrics_authenticated_entity_instance = DisplayCompanyWithSalesMetricsAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(DisplayCompanyWithSalesMetricsAuthenticatedEntity.to_json())

# convert the object into a dict
display_company_with_sales_metrics_authenticated_entity_dict = display_company_with_sales_metrics_authenticated_entity_instance.to_dict()
# create an instance of DisplayCompanyWithSalesMetricsAuthenticatedEntity from a dict
display_company_with_sales_metrics_authenticated_entity_from_dict = DisplayCompanyWithSalesMetricsAuthenticatedEntity.from_dict(display_company_with_sales_metrics_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


