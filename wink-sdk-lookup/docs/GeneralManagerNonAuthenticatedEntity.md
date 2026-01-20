# GeneralManagerNonAuthenticatedEntity

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaNonAuthenticatedEntity**](SimpleMultimediaNonAuthenticatedEntity.md) | Cloudinary image identifier of GM currently managing the property. | [optional] 
**descriptions** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_lookup.models.general_manager_non_authenticated_entity import GeneralManagerNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerNonAuthenticatedEntity from a JSON string
general_manager_non_authenticated_entity_instance = GeneralManagerNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerNonAuthenticatedEntity.to_json())

# convert the object into a dict
general_manager_non_authenticated_entity_dict = general_manager_non_authenticated_entity_instance.to_dict()
# create an instance of GeneralManagerNonAuthenticatedEntity from a dict
general_manager_non_authenticated_entity_from_dict = GeneralManagerNonAuthenticatedEntity.from_dict(general_manager_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


