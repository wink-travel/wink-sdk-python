# GeneralManagerAuthenticatedEntity

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaAuthenticatedEntity**](SimpleMultimediaAuthenticatedEntity.md) | Cloudinary image identifier of GM currently managing the property. | [optional] 
**descriptions** | [**List[LocalizedDescriptionAuthenticatedEntity]**](LocalizedDescriptionAuthenticatedEntity.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_booking.models.general_manager_authenticated_entity import GeneralManagerAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerAuthenticatedEntity from a JSON string
general_manager_authenticated_entity_instance = GeneralManagerAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerAuthenticatedEntity.to_json())

# convert the object into a dict
general_manager_authenticated_entity_dict = general_manager_authenticated_entity_instance.to_dict()
# create an instance of GeneralManagerAuthenticatedEntity from a dict
general_manager_authenticated_entity_from_dict = GeneralManagerAuthenticatedEntity.from_dict(general_manager_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


