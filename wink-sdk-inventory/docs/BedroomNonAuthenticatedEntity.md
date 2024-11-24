# BedroomNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedNonAuthenticatedEntity]**](BedNonAuthenticatedEntity.md) | A bedroom can have more than one bed type. | 

## Example

```python
from wink_sdk_inventory.models.bedroom_non_authenticated_entity import BedroomNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomNonAuthenticatedEntity from a JSON string
bedroom_non_authenticated_entity_instance = BedroomNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BedroomNonAuthenticatedEntity.to_json())

# convert the object into a dict
bedroom_non_authenticated_entity_dict = bedroom_non_authenticated_entity_instance.to_dict()
# create an instance of BedroomNonAuthenticatedEntity from a dict
bedroom_non_authenticated_entity_from_dict = BedroomNonAuthenticatedEntity.from_dict(bedroom_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


