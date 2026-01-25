# PageLineChartAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[LineChartAuthenticatedEntity]**](LineChartAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectAuthenticatedEntity**](PageableObjectAuthenticatedEntity.md) |  | [optional] 
**sort** | [**SortObjectAuthenticatedEntity**](SortObjectAuthenticatedEntity.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.page_line_chart_authenticated_entity import PageLineChartAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageLineChartAuthenticatedEntity from a JSON string
page_line_chart_authenticated_entity_instance = PageLineChartAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageLineChartAuthenticatedEntity.to_json())

# convert the object into a dict
page_line_chart_authenticated_entity_dict = page_line_chart_authenticated_entity_instance.to_dict()
# create an instance of PageLineChartAuthenticatedEntity from a dict
page_line_chart_authenticated_entity_from_dict = PageLineChartAuthenticatedEntity.from_dict(page_line_chart_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


