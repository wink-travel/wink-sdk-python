# ChartTooltipNonAuthenticatedEntity

The configuration options of the Chart series tooltips. The tooltip of the Chart series is displayed when the `tooltip.visible` option is set to `true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | If set to &#x60;true&#x60;, the Chart displays the series tooltip. By default, the series tooltip is not displayed. | [optional] 
**format** | **str** | The format of the labels. Uses the format method of IntlService. The available format placeholders are:  - Area, Bar, Column, Funnel, Line, and Pie {0} - value - Bubble {0} - x value{1} - y value{2} - size value{3} - category name - Scatter and scatterLine {0} - x value{1} - y value - Candlestick and OHLC {0} - open value{1} - high value{2} - low value{3} - close value{4} - category name | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_tooltip_non_authenticated_entity import ChartTooltipNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartTooltipNonAuthenticatedEntity from a JSON string
chart_tooltip_non_authenticated_entity_instance = ChartTooltipNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartTooltipNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_tooltip_non_authenticated_entity_dict = chart_tooltip_non_authenticated_entity_instance.to_dict()
# create an instance of ChartTooltipNonAuthenticatedEntity from a dict
chart_tooltip_non_authenticated_entity_from_dict = ChartTooltipNonAuthenticatedEntity.from_dict(chart_tooltip_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


