# ChartRequestWrapperAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**owner_identifier** | **str** | Owner of this chart | 
**name** | **str** | Chart name as named by creator | 
**sort** | **int** | Sort a list of charts by this sort value. | [optional] [default to -1]
**request** | [**ChartRequestAuthenticatedEntity**](ChartRequestAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_analytics.models.chart_request_wrapper_authenticated_entity import ChartRequestWrapperAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartRequestWrapperAuthenticatedEntity from a JSON string
chart_request_wrapper_authenticated_entity_instance = ChartRequestWrapperAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartRequestWrapperAuthenticatedEntity.to_json())

# convert the object into a dict
chart_request_wrapper_authenticated_entity_dict = chart_request_wrapper_authenticated_entity_instance.to_dict()
# create an instance of ChartRequestWrapperAuthenticatedEntity from a dict
chart_request_wrapper_authenticated_entity_from_dict = ChartRequestWrapperAuthenticatedEntity.from_dict(chart_request_wrapper_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


