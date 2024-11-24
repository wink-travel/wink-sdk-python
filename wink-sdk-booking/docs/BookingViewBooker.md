# BookingViewBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**booking** | [**BookingBooker**](BookingBooker.md) |  | 

## Example

```python
from wink_sdk_booking.models.booking_view_booker import BookingViewBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BookingViewBooker from a JSON string
booking_view_booker_instance = BookingViewBooker.from_json(json)
# print the JSON string representation of the object
print(BookingViewBooker.to_json())

# convert the object into a dict
booking_view_booker_dict = booking_view_booker_instance.to_dict()
# create an instance of BookingViewBooker from a dict
booking_view_booker_from_dict = BookingViewBooker.from_dict(booking_view_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


