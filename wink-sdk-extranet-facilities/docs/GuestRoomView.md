# GuestRoomView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**guest_room** | [**GuestRoom**](GuestRoom.md) |  | 

## Example

```python
from wink_sdk_extranet_facilities.models.guest_room_view import GuestRoomView

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRoomView from a JSON string
guest_room_view_instance = GuestRoomView.from_json(json)
# print the JSON string representation of the object
print(GuestRoomView.to_json())

# convert the object into a dict
guest_room_view_dict = guest_room_view_instance.to_dict()
# create an instance of GuestRoomView from a dict
guest_room_view_from_dict = GuestRoomView.from_dict(guest_room_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


