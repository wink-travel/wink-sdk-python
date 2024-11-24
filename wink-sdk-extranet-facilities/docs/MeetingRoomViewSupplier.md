# MeetingRoomViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**meeting_room** | [**MeetingRoomSupplier**](MeetingRoomSupplier.md) |  | 
**featured_image_identifier** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.meeting_room_view_supplier import MeetingRoomViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingRoomViewSupplier from a JSON string
meeting_room_view_supplier_instance = MeetingRoomViewSupplier.from_json(json)
# print the JSON string representation of the object
print(MeetingRoomViewSupplier.to_json())

# convert the object into a dict
meeting_room_view_supplier_dict = meeting_room_view_supplier_instance.to_dict()
# create an instance of MeetingRoomViewSupplier from a dict
meeting_room_view_supplier_from_dict = MeetingRoomViewSupplier.from_dict(meeting_room_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


