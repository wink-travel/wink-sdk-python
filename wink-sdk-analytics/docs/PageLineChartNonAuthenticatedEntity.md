# PageLineChartNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[LineChartNonAuthenticatedEntity]**](LineChartNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.page_line_chart_non_authenticated_entity import PageLineChartNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageLineChartNonAuthenticatedEntity from a JSON string
page_line_chart_non_authenticated_entity_instance = PageLineChartNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageLineChartNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_line_chart_non_authenticated_entity_dict = page_line_chart_non_authenticated_entity_instance.to_dict()
# create an instance of PageLineChartNonAuthenticatedEntity from a dict
page_line_chart_non_authenticated_entity_from_dict = PageLineChartNonAuthenticatedEntity.from_dict(page_line_chart_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


