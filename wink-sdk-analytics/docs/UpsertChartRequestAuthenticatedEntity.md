# UpsertChartRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Chart name as named by creator | 
**sort** | **int** | Sort a list of charts by this sort value. | [optional] [default to -1]
**request** | [**ChartDetailsAuthenticatedEntity**](ChartDetailsAuthenticatedEntity.md) | Chart settings | 

## Example

```python
from wink_sdk_analytics.models.upsert_chart_request_authenticated_entity import UpsertChartRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertChartRequestAuthenticatedEntity from a JSON string
upsert_chart_request_authenticated_entity_instance = UpsertChartRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpsertChartRequestAuthenticatedEntity.to_json())

# convert the object into a dict
upsert_chart_request_authenticated_entity_dict = upsert_chart_request_authenticated_entity_instance.to_dict()
# create an instance of UpsertChartRequestAuthenticatedEntity from a dict
upsert_chart_request_authenticated_entity_from_dict = UpsertChartRequestAuthenticatedEntity.from_dict(upsert_chart_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


