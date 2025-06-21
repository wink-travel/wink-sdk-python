# ChartSeriesSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Chart series which is visible in the legend. | [optional] 
**data** | **List[float]** | The array of data items which represent the series data.  You can set it to:  - Array of numbers. Supported when the series.type option is set to &#x60;area&#x60;, &#x60;bar&#x60;, &#x60;column&#x60;, &#x60;donut&#x60;, &#x60;pie&#x60;, &#x60;line&#x60;, or &#x60;waterfall&#x60;. The Bubble series need arrays of three values—X value, Y value, and Size value—for example, [1, 1, 10]. The Scatter and ScatterLine series need arrays of two values—X value and Y value. The OHLC and Candlestick series need arrays of four values—open, high, low, and close. The RangeBar and RangeArea series need arrays of two values—the from and to value. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.chart_series_supplier import ChartSeriesSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSeriesSupplier from a JSON string
chart_series_supplier_instance = ChartSeriesSupplier.from_json(json)
# print the JSON string representation of the object
print(ChartSeriesSupplier.to_json())

# convert the object into a dict
chart_series_supplier_dict = chart_series_supplier_instance.to_dict()
# create an instance of ChartSeriesSupplier from a dict
chart_series_supplier_from_dict = ChartSeriesSupplier.from_dict(chart_series_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


