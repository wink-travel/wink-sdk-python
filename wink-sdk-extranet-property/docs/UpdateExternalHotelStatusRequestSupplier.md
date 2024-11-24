# UpdateExternalHotelStatusRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_status_code** | **str** | Via OTA spec: 1 &#x3D; Active, 6 &#x3D; Inactive. This status can be changed by the hotel. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.update_external_hotel_status_request_supplier import UpdateExternalHotelStatusRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalHotelStatusRequestSupplier from a JSON string
update_external_hotel_status_request_supplier_instance = UpdateExternalHotelStatusRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalHotelStatusRequestSupplier.to_json())

# convert the object into a dict
update_external_hotel_status_request_supplier_dict = update_external_hotel_status_request_supplier_instance.to_dict()
# create an instance of UpdateExternalHotelStatusRequestSupplier from a dict
update_external_hotel_status_request_supplier_from_dict = UpdateExternalHotelStatusRequestSupplier.from_dict(update_external_hotel_status_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


