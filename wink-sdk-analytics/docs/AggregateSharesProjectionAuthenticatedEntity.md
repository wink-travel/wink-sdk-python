# AggregateSharesProjectionAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_identifier** | **str** | Affiliate ID. | [optional] 
**views** | **int** |  | [optional] 
**clicks** | **int** |  | [optional] 
**shares** | **int** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.aggregate_shares_projection_authenticated_entity import AggregateSharesProjectionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateSharesProjectionAuthenticatedEntity from a JSON string
aggregate_shares_projection_authenticated_entity_instance = AggregateSharesProjectionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateSharesProjectionAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_shares_projection_authenticated_entity_dict = aggregate_shares_projection_authenticated_entity_instance.to_dict()
# create an instance of AggregateSharesProjectionAuthenticatedEntity from a dict
aggregate_shares_projection_authenticated_entity_from_dict = AggregateSharesProjectionAuthenticatedEntity.from_dict(aggregate_shares_projection_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


