# ImproveRoomTypeRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Descriptive title | [optional] 
**description** | **str** | Descriptive text | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.improve_room_type_request_supplier import ImproveRoomTypeRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ImproveRoomTypeRequestSupplier from a JSON string
improve_room_type_request_supplier_instance = ImproveRoomTypeRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(ImproveRoomTypeRequestSupplier.to_json())

# convert the object into a dict
improve_room_type_request_supplier_dict = improve_room_type_request_supplier_instance.to_dict()
# create an instance of ImproveRoomTypeRequestSupplier from a dict
improve_room_type_request_supplier_from_dict = ImproveRoomTypeRequestSupplier.from_dict(improve_room_type_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


