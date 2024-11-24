# ChartValueAxisLabelsNonAuthenticatedEntity

The axis labels configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format for displaying the labels. Uses the format method of IntlService. Contains one placeholder (&#x60;{0}&#x60;) which represents the category value. | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_value_axis_labels_non_authenticated_entity import ChartValueAxisLabelsNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartValueAxisLabelsNonAuthenticatedEntity from a JSON string
chart_value_axis_labels_non_authenticated_entity_instance = ChartValueAxisLabelsNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartValueAxisLabelsNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_value_axis_labels_non_authenticated_entity_dict = chart_value_axis_labels_non_authenticated_entity_instance.to_dict()
# create an instance of ChartValueAxisLabelsNonAuthenticatedEntity from a dict
chart_value_axis_labels_non_authenticated_entity_from_dict = ChartValueAxisLabelsNonAuthenticatedEntity.from_dict(chart_value_axis_labels_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


