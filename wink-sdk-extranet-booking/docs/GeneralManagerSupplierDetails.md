# GeneralManagerSupplierDetails

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaSupplierDetails**](SimpleMultimediaSupplierDetails.md) | Cloudinary image identifier of GM currently managing the property. | [optional] 
**descriptions** | [**List[LocalizedDescriptionSupplierDetails]**](LocalizedDescriptionSupplierDetails.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.general_manager_supplier_details import GeneralManagerSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerSupplierDetails from a JSON string
general_manager_supplier_details_instance = GeneralManagerSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerSupplierDetails.to_json())

# convert the object into a dict
general_manager_supplier_details_dict = general_manager_supplier_details_instance.to_dict()
# create an instance of GeneralManagerSupplierDetails from a dict
general_manager_supplier_details_from_dict = GeneralManagerSupplierDetails.from_dict(general_manager_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


