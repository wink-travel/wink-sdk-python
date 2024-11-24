# DuplicateGuestRoomRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Which property to duplicate room type for | 
**guest_room_identifier** | **str** | Which room type to duplicate | 

## Example

```python
from wink_sdk_extranet_facilities.models.duplicate_guest_room_request_supplier import DuplicateGuestRoomRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateGuestRoomRequestSupplier from a JSON string
duplicate_guest_room_request_supplier_instance = DuplicateGuestRoomRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(DuplicateGuestRoomRequestSupplier.to_json())

# convert the object into a dict
duplicate_guest_room_request_supplier_dict = duplicate_guest_room_request_supplier_instance.to_dict()
# create an instance of DuplicateGuestRoomRequestSupplier from a dict
duplicate_guest_room_request_supplier_from_dict = DuplicateGuestRoomRequestSupplier.from_dict(duplicate_guest_room_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


