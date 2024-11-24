# ChartCategoryAxisNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | The category names. The Chart creates a category for every item of the array. | [optional] 

## Example

```python
from wink_sdk_analytics.models.chart_category_axis_non_authenticated_entity import ChartCategoryAxisNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartCategoryAxisNonAuthenticatedEntity from a JSON string
chart_category_axis_non_authenticated_entity_instance = ChartCategoryAxisNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartCategoryAxisNonAuthenticatedEntity.to_json())

# convert the object into a dict
chart_category_axis_non_authenticated_entity_dict = chart_category_axis_non_authenticated_entity_instance.to_dict()
# create an instance of ChartCategoryAxisNonAuthenticatedEntity from a dict
chart_category_axis_non_authenticated_entity_from_dict = ChartCategoryAxisNonAuthenticatedEntity.from_dict(chart_category_axis_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


