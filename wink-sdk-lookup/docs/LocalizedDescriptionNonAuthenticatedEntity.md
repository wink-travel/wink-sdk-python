# LocalizedDescriptionNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_lookup.models.localized_description_non_authenticated_entity import LocalizedDescriptionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedDescriptionNonAuthenticatedEntity from a JSON string
localized_description_non_authenticated_entity_instance = LocalizedDescriptionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LocalizedDescriptionNonAuthenticatedEntity.to_json())

# convert the object into a dict
localized_description_non_authenticated_entity_dict = localized_description_non_authenticated_entity_instance.to_dict()
# create an instance of LocalizedDescriptionNonAuthenticatedEntity from a dict
localized_description_non_authenticated_entity_from_dict = LocalizedDescriptionNonAuthenticatedEntity.from_dict(localized_description_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


