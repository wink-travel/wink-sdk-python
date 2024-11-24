# BookingUserRequestAuthenticatedEntity

User object contains details of the person that made the booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.booking_user_request_authenticated_entity import BookingUserRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserRequestAuthenticatedEntity from a JSON string
booking_user_request_authenticated_entity_instance = BookingUserRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BookingUserRequestAuthenticatedEntity.to_json())

# convert the object into a dict
booking_user_request_authenticated_entity_dict = booking_user_request_authenticated_entity_instance.to_dict()
# create an instance of BookingUserRequestAuthenticatedEntity from a dict
booking_user_request_authenticated_entity_from_dict = BookingUserRequestAuthenticatedEntity.from_dict(booking_user_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


