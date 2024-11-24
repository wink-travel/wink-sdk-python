# ChartCategoryAxisSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | The category names. The Chart creates a category for every item of the array. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.chart_category_axis_supplier import ChartCategoryAxisSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChartCategoryAxisSupplier from a JSON string
chart_category_axis_supplier_instance = ChartCategoryAxisSupplier.from_json(json)
# print the JSON string representation of the object
print(ChartCategoryAxisSupplier.to_json())

# convert the object into a dict
chart_category_axis_supplier_dict = chart_category_axis_supplier_instance.to_dict()
# create an instance of ChartCategoryAxisSupplier from a dict
chart_category_axis_supplier_from_dict = ChartCategoryAxisSupplier.from_dict(chart_category_axis_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


