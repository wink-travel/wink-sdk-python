# UpsertChartRequestWrapperAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Chart name as named by creator | 
**sort** | **int** | Sort a list of charts by this sort value. | [optional] [default to -1]
**request** | [**ChartRequestAuthenticatedEntity**](ChartRequestAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_analytics.models.upsert_chart_request_wrapper_authenticated_entity import UpsertChartRequestWrapperAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertChartRequestWrapperAuthenticatedEntity from a JSON string
upsert_chart_request_wrapper_authenticated_entity_instance = UpsertChartRequestWrapperAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpsertChartRequestWrapperAuthenticatedEntity.to_json())

# convert the object into a dict
upsert_chart_request_wrapper_authenticated_entity_dict = upsert_chart_request_wrapper_authenticated_entity_instance.to_dict()
# create an instance of UpsertChartRequestWrapperAuthenticatedEntity from a dict
upsert_chart_request_wrapper_authenticated_entity_from_dict = UpsertChartRequestWrapperAuthenticatedEntity.from_dict(upsert_chart_request_wrapper_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


