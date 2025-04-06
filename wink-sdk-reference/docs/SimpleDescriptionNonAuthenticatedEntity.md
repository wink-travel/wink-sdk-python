# SimpleDescriptionNonAuthenticatedEntity

Localized description for this perk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | [optional] 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_reference.models.simple_description_non_authenticated_entity import SimpleDescriptionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionNonAuthenticatedEntity from a JSON string
simple_description_non_authenticated_entity_instance = SimpleDescriptionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionNonAuthenticatedEntity.to_json())

# convert the object into a dict
simple_description_non_authenticated_entity_dict = simple_description_non_authenticated_entity_instance.to_dict()
# create an instance of SimpleDescriptionNonAuthenticatedEntity from a dict
simple_description_non_authenticated_entity_from_dict = SimpleDescriptionNonAuthenticatedEntity.from_dict(simple_description_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


