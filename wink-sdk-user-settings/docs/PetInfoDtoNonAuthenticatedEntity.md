# PetInfoDtoNonAuthenticatedEntity

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_user_settings.models.pet_info_dto_non_authenticated_entity import PetInfoDtoNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDtoNonAuthenticatedEntity from a JSON string
pet_info_dto_non_authenticated_entity_instance = PetInfoDtoNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PetInfoDtoNonAuthenticatedEntity.to_json())

# convert the object into a dict
pet_info_dto_non_authenticated_entity_dict = pet_info_dto_non_authenticated_entity_instance.to_dict()
# create an instance of PetInfoDtoNonAuthenticatedEntity from a dict
pet_info_dto_non_authenticated_entity_from_dict = PetInfoDtoNonAuthenticatedEntity.from_dict(pet_info_dto_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


