# StateAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorSupplier]**](SortDescriptorSupplier.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorSupplier**](CompositeFilterDescriptorSupplier.md) | Descriptors used for filtering result set | [optional] 
**group** | [**List[GroupDescriptorSupplier]**](GroupDescriptorSupplier.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.state_authenticated_entity import StateAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of StateAuthenticatedEntity from a JSON string
state_authenticated_entity_instance = StateAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(StateAuthenticatedEntity.to_json())

# convert the object into a dict
state_authenticated_entity_dict = state_authenticated_entity_instance.to_dict()
# create an instance of StateAuthenticatedEntity from a dict
state_authenticated_entity_from_dict = StateAuthenticatedEntity.from_dict(state_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


