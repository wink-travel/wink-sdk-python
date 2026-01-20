# PetInfoLightweightSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_extranet_booking.models.pet_info_lightweight_supplier_details import PetInfoLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoLightweightSupplierDetails from a JSON string
pet_info_lightweight_supplier_details_instance = PetInfoLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PetInfoLightweightSupplierDetails.to_json())

# convert the object into a dict
pet_info_lightweight_supplier_details_dict = pet_info_lightweight_supplier_details_instance.to_dict()
# create an instance of PetInfoLightweightSupplierDetails from a dict
pet_info_lightweight_supplier_details_from_dict = PetInfoLightweightSupplierDetails.from_dict(pet_info_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


