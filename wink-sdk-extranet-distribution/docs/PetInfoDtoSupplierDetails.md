# PetInfoDtoSupplierDetails

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_extranet_distribution.models.pet_info_dto_supplier_details import PetInfoDtoSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDtoSupplierDetails from a JSON string
pet_info_dto_supplier_details_instance = PetInfoDtoSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PetInfoDtoSupplierDetails.to_json())

# convert the object into a dict
pet_info_dto_supplier_details_dict = pet_info_dto_supplier_details_instance.to_dict()
# create an instance of PetInfoDtoSupplierDetails from a dict
pet_info_dto_supplier_details_from_dict = PetInfoDtoSupplierDetails.from_dict(pet_info_dto_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


