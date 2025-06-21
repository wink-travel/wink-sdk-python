# ImproveRoomTypeResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Indicates the category of the room. Typical values would be Moderate, Standard, or Deluxe. Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**description** | **str** | Floor an which a room is located | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.improve_room_type_response_supplier import ImproveRoomTypeResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ImproveRoomTypeResponseSupplier from a JSON string
improve_room_type_response_supplier_instance = ImproveRoomTypeResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(ImproveRoomTypeResponseSupplier.to_json())

# convert the object into a dict
improve_room_type_response_supplier_dict = improve_room_type_response_supplier_instance.to_dict()
# create an instance of ImproveRoomTypeResponseSupplier from a dict
improve_room_type_response_supplier_from_dict = ImproveRoomTypeResponseSupplier.from_dict(improve_room_type_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


