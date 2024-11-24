# LanguageNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**display_country** | **str** |  | [optional] 
**display_language** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**display_script** | **str** |  | [optional] 
**display_variant** | **str** |  | [optional] 
**iso3_country** | **str** |  | [optional] 
**iso3_language** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**variant** | **str** |  | [optional] 

## Example

```python
from wink_sdk_reference.models.language_non_authenticated_entity import LanguageNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageNonAuthenticatedEntity from a JSON string
language_non_authenticated_entity_instance = LanguageNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LanguageNonAuthenticatedEntity.to_json())

# convert the object into a dict
language_non_authenticated_entity_dict = language_non_authenticated_entity_instance.to_dict()
# create an instance of LanguageNonAuthenticatedEntity from a dict
language_non_authenticated_entity_from_dict = LanguageNonAuthenticatedEntity.from_dict(language_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


