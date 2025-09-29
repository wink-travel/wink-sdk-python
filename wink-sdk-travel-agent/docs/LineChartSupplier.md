# LineChartSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique line chart identifier | [optional] 
**title** | [**ChartTitleSupplier**](ChartTitleSupplier.md) | The configuration options for the chart title | [optional] 
**legend** | [**ChartLegendSupplier**](ChartLegendSupplier.md) | The configuration options for the chart legend. | [optional] 
**series** | [**List[ChartSeriesSupplier]**](ChartSeriesSupplier.md) | The configuration of the chart series. The series type is determined by the value of the type field. If a type value is missing, the chart renders the type that is specified in &#x60;seriesDefaults&#x60;. Some options accept functions as arguments. These arguments are evaluated for each point which is supplied as a parameter. If no value is returned, the chart uses the &#x60;theme&#x60; or &#x60;seriesDefaults&#x60; values. | [optional] 
**x_axis** | [**ChartCategoryAxisSupplier**](ChartCategoryAxisSupplier.md) | The configuration options of the category axis. | [optional] 
**xaxis** | [**ChartCategoryAxisSupplier**](ChartCategoryAxisSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.line_chart_supplier import LineChartSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of LineChartSupplier from a JSON string
line_chart_supplier_instance = LineChartSupplier.from_json(json)
# print the JSON string representation of the object
print(LineChartSupplier.to_json())

# convert the object into a dict
line_chart_supplier_dict = line_chart_supplier_instance.to_dict()
# create an instance of LineChartSupplier from a dict
line_chart_supplier_from_dict = LineChartSupplier.from_dict(line_chart_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


