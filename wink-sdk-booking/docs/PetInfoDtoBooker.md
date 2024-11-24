# PetInfoDtoBooker

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_booking.models.pet_info_dto_booker import PetInfoDtoBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDtoBooker from a JSON string
pet_info_dto_booker_instance = PetInfoDtoBooker.from_json(json)
# print the JSON string representation of the object
print(PetInfoDtoBooker.to_json())

# convert the object into a dict
pet_info_dto_booker_dict = pet_info_dto_booker_instance.to_dict()
# create an instance of PetInfoDtoBooker from a dict
pet_info_dto_booker_from_dict = PetInfoDtoBooker.from_dict(pet_info_dto_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


