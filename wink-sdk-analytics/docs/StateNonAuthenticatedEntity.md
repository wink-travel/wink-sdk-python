# StateNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorNonAuthenticatedEntity]**](SortDescriptorNonAuthenticatedEntity.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorNonAuthenticatedEntity**](CompositeFilterDescriptorNonAuthenticatedEntity.md) |  | [optional] 
**group** | [**List[GroupDescriptorNonAuthenticatedEntity]**](GroupDescriptorNonAuthenticatedEntity.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_analytics.models.state_non_authenticated_entity import StateNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of StateNonAuthenticatedEntity from a JSON string
state_non_authenticated_entity_instance = StateNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(StateNonAuthenticatedEntity.to_json())

# convert the object into a dict
state_non_authenticated_entity_dict = state_non_authenticated_entity_instance.to_dict()
# create an instance of StateNonAuthenticatedEntity from a dict
state_non_authenticated_entity_from_dict = StateNonAuthenticatedEntity.from_dict(state_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


