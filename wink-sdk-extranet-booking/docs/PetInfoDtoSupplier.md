# PetInfoDtoSupplier

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_extranet_booking.models.pet_info_dto_supplier import PetInfoDtoSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDtoSupplier from a JSON string
pet_info_dto_supplier_instance = PetInfoDtoSupplier.from_json(json)
# print the JSON string representation of the object
print(PetInfoDtoSupplier.to_json())

# convert the object into a dict
pet_info_dto_supplier_dict = pet_info_dto_supplier_instance.to_dict()
# create an instance of PetInfoDtoSupplier from a dict
pet_info_dto_supplier_from_dict = PetInfoDtoSupplier.from_dict(pet_info_dto_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


