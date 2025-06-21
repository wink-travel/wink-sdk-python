# BedroomAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedAuthenticatedEntity]**](BedAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_booking.models.bedroom_authenticated_entity import BedroomAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomAuthenticatedEntity from a JSON string
bedroom_authenticated_entity_instance = BedroomAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BedroomAuthenticatedEntity.to_json())

# convert the object into a dict
bedroom_authenticated_entity_dict = bedroom_authenticated_entity_instance.to_dict()
# create an instance of BedroomAuthenticatedEntity from a dict
bedroom_authenticated_entity_from_dict = BedroomAuthenticatedEntity.from_dict(bedroom_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


