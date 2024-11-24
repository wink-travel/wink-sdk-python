# ChartValueAxisLabelsSupplier

The axis labels configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format for displaying the labels. Uses the format method of IntlService. Contains one placeholder (&#x60;{0}&#x60;) which represents the category value. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.chart_value_axis_labels_supplier import ChartValueAxisLabelsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChartValueAxisLabelsSupplier from a JSON string
chart_value_axis_labels_supplier_instance = ChartValueAxisLabelsSupplier.from_json(json)
# print the JSON string representation of the object
print(ChartValueAxisLabelsSupplier.to_json())

# convert the object into a dict
chart_value_axis_labels_supplier_dict = chart_value_axis_labels_supplier_instance.to_dict()
# create an instance of ChartValueAxisLabelsSupplier from a dict
chart_value_axis_labels_supplier_from_dict = ChartValueAxisLabelsSupplier.from_dict(chart_value_axis_labels_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


