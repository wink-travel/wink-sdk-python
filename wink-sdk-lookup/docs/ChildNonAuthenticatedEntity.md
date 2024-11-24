# ChildNonAuthenticatedEntity

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_lookup.models.child_non_authenticated_entity import ChildNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChildNonAuthenticatedEntity from a JSON string
child_non_authenticated_entity_instance = ChildNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChildNonAuthenticatedEntity.to_json())

# convert the object into a dict
child_non_authenticated_entity_dict = child_non_authenticated_entity_instance.to_dict()
# create an instance of ChildNonAuthenticatedEntity from a dict
child_non_authenticated_entity_from_dict = ChildNonAuthenticatedEntity.from_dict(child_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


