# ChartSeriesDefaultsNonAuthenticatedEntity

The default options of all series.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The default type of the series.  The supported values are:  - area - bar - bubble - bullet - candlestick - column - donut - funnel - line - ohlc - pie - polarArea - polarLine - polarScatter - radarArea - radarColumn - radarLine - rangeArea - rangeBar - rangeColumn - scatter - scatterLine - verticalArea - verticalBullet - verticalLine - verticalRangeArea - waterfall | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_series_defaults_non_authenticated_entity import ChartSeriesDefaultsNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSeriesDefaultsNonAuthenticatedEntity from a JSON string
chart_series_defaults_non_authenticated_entity_instance = ChartSeriesDefaultsNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartSeriesDefaultsNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_series_defaults_non_authenticated_entity_dict = chart_series_defaults_non_authenticated_entity_instance.to_dict()
# create an instance of ChartSeriesDefaultsNonAuthenticatedEntity from a dict
chart_series_defaults_non_authenticated_entity_from_dict = ChartSeriesDefaultsNonAuthenticatedEntity.from_dict(chart_series_defaults_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


