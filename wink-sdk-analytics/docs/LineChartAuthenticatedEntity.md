# LineChartAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique line chart identifier | [optional] 
**title** | [**ChartTitleAuthenticatedEntity**](ChartTitleAuthenticatedEntity.md) | The configuration options for the chart title | [optional] 
**legend** | [**ChartLegendAuthenticatedEntity**](ChartLegendAuthenticatedEntity.md) | The configuration options for the chart legend. | [optional] 
**series** | [**List[ChartSeriesAuthenticatedEntity]**](ChartSeriesAuthenticatedEntity.md) | The configuration of the chart series. The series type is determined by the value of the type field. If a type value is missing, the chart renders the type that is specified in &#x60;seriesDefaults&#x60;. Some options accept functions as arguments. These arguments are evaluated for each point which is supplied as a parameter. If no value is returned, the chart uses the &#x60;theme&#x60; or &#x60;seriesDefaults&#x60; values. | [optional] 
**x_axis** | [**ChartCategoryAxisAuthenticatedEntity**](ChartCategoryAxisAuthenticatedEntity.md) | The configuration options of the category axis. | [optional] 
**xaxis** | [**ChartCategoryAxisAuthenticatedEntity**](ChartCategoryAxisAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.line_chart_authenticated_entity import LineChartAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LineChartAuthenticatedEntity from a JSON string
line_chart_authenticated_entity_instance = LineChartAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LineChartAuthenticatedEntity.to_json())

# convert the object into a dict
line_chart_authenticated_entity_dict = line_chart_authenticated_entity_instance.to_dict()
# create an instance of LineChartAuthenticatedEntity from a dict
line_chart_authenticated_entity_from_dict = LineChartAuthenticatedEntity.from_dict(line_chart_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


