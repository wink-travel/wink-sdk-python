# ChartValueAxisNonAuthenticatedEntity

The configuration options of the value axis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**ChartValueAxisLabelsNonAuthenticatedEntity**](ChartValueAxisLabelsNonAuthenticatedEntity.md) |  | [optional] 
**line** | [**ChartValueAxisLineNonAuthenticatedEntity**](ChartValueAxisLineNonAuthenticatedEntity.md) |  | [optional] 
**axis_crossing_value** | **int** | - (Only for objects) The value at which the category axis crosses this axis. - (Only for arrays) The value indices at which the category axes cross the value axis. - (Only for dates) The date at which the category axis crosses this axis. | [optional] 
**major_unit** | **float** | The interval between major divisions. If &#x60;valueAxis.type&#x60; is set to &#x60;log&#x60;, the majorUnit value is used for the base of the logarithm. | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_value_axis_non_authenticated_entity import ChartValueAxisNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartValueAxisNonAuthenticatedEntity from a JSON string
chart_value_axis_non_authenticated_entity_instance = ChartValueAxisNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartValueAxisNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_value_axis_non_authenticated_entity_dict = chart_value_axis_non_authenticated_entity_instance.to_dict()
# create an instance of ChartValueAxisNonAuthenticatedEntity from a dict
chart_value_axis_non_authenticated_entity_from_dict = ChartValueAxisNonAuthenticatedEntity.from_dict(chart_value_axis_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


