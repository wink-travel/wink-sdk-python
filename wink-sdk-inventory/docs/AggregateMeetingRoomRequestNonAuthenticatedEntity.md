# AggregateMeetingRoomRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | User session containing itinerary and other data by the user | 
**customization_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.aggregate_meeting_room_request_non_authenticated_entity import AggregateMeetingRoomRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateMeetingRoomRequestNonAuthenticatedEntity from a JSON string
aggregate_meeting_room_request_non_authenticated_entity_instance = AggregateMeetingRoomRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateMeetingRoomRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_meeting_room_request_non_authenticated_entity_dict = aggregate_meeting_room_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateMeetingRoomRequestNonAuthenticatedEntity from a dict
aggregate_meeting_room_request_non_authenticated_entity_from_dict = AggregateMeetingRoomRequestNonAuthenticatedEntity.from_dict(aggregate_meeting_room_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


