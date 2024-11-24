# ChartValueAxisLineNonAuthenticatedEntity

The configuration of the axis lines. Also affects the major and minor ticks, but not the grid lines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | If set to true, the Chart displays the axis lines. By default, the axis lines are visible. | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_value_axis_line_non_authenticated_entity import ChartValueAxisLineNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartValueAxisLineNonAuthenticatedEntity from a JSON string
chart_value_axis_line_non_authenticated_entity_instance = ChartValueAxisLineNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartValueAxisLineNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_value_axis_line_non_authenticated_entity_dict = chart_value_axis_line_non_authenticated_entity_instance.to_dict()
# create an instance of ChartValueAxisLineNonAuthenticatedEntity from a dict
chart_value_axis_line_non_authenticated_entity_from_dict = ChartValueAxisLineNonAuthenticatedEntity.from_dict(chart_value_axis_line_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


