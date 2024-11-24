# AggregateGuestRoomRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**engine_configuration_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.aggregate_guest_room_request_non_authenticated_entity import AggregateGuestRoomRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateGuestRoomRequestNonAuthenticatedEntity from a JSON string
aggregate_guest_room_request_non_authenticated_entity_instance = AggregateGuestRoomRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateGuestRoomRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_guest_room_request_non_authenticated_entity_dict = aggregate_guest_room_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateGuestRoomRequestNonAuthenticatedEntity from a dict
aggregate_guest_room_request_non_authenticated_entity_from_dict = AggregateGuestRoomRequestNonAuthenticatedEntity.from_dict(aggregate_guest_room_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


