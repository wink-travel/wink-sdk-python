# ChartValueAxisLineSupplier

The configuration of the axis lines. Also affects the major and minor ticks, but not the grid lines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | If set to true, the Chart displays the axis lines. By default, the axis lines are visible. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.chart_value_axis_line_supplier import ChartValueAxisLineSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChartValueAxisLineSupplier from a JSON string
chart_value_axis_line_supplier_instance = ChartValueAxisLineSupplier.from_json(json)
# print the JSON string representation of the object
print(ChartValueAxisLineSupplier.to_json())

# convert the object into a dict
chart_value_axis_line_supplier_dict = chart_value_axis_line_supplier_instance.to_dict()
# create an instance of ChartValueAxisLineSupplier from a dict
chart_value_axis_line_supplier_from_dict = ChartValueAxisLineSupplier.from_dict(chart_value_axis_line_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


