# GuestUserBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**profile** | [**ProfileLightweightBooker**](ProfileLightweightBooker.md) | Optional profile record | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_booking.models.guest_user_booker import GuestUserBooker

# TODO update the JSON string below
json = "{}"
# create an instance of GuestUserBooker from a JSON string
guest_user_booker_instance = GuestUserBooker.from_json(json)
# print the JSON string representation of the object
print(GuestUserBooker.to_json())

# convert the object into a dict
guest_user_booker_dict = guest_user_booker_instance.to_dict()
# create an instance of GuestUserBooker from a dict
guest_user_booker_from_dict = GuestUserBooker.from_dict(guest_user_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


