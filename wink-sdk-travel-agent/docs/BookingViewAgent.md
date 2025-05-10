# BookingViewAgent

List of all bookings whether they were successful or not

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**booking** | [**BookingAgent**](BookingAgent.md) |  | 

## Example

```python
from wink_sdk_travel_agent.models.booking_view_agent import BookingViewAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingViewAgent from a JSON string
booking_view_agent_instance = BookingViewAgent.from_json(json)
# print the JSON string representation of the object
print(BookingViewAgent.to_json())

# convert the object into a dict
booking_view_agent_dict = booking_view_agent_instance.to_dict()
# create an instance of BookingViewAgent from a dict
booking_view_agent_from_dict = BookingViewAgent.from_dict(booking_view_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


