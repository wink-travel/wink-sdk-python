# ChartAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**owner_identifier** | **str** | Owner of this chart | 
**name** | **str** | Chart name as named by creator | 
**sort** | **int** | Sort a list of charts by this sort value. | [optional] [default to -1]
**details** | [**ChartDetailsAuthenticatedEntity**](ChartDetailsAuthenticatedEntity.md) | Chart settings | 

## Example

```python
from wink_sdk_analytics.models.chart_authenticated_entity import ChartAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartAuthenticatedEntity from a JSON string
chart_authenticated_entity_instance = ChartAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartAuthenticatedEntity.to_json())

# convert the object into a dict
chart_authenticated_entity_dict = chart_authenticated_entity_instance.to_dict()
# create an instance of ChartAuthenticatedEntity from a dict
chart_authenticated_entity_from_dict = ChartAuthenticatedEntity.from_dict(chart_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


