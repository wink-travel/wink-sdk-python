# PageBookingViewBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingViewBooker]**](BookingViewBooker.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectBooker**](PageableObjectBooker.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectBooker**](SortObjectBooker.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.page_booking_view_booker import PageBookingViewBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingViewBooker from a JSON string
page_booking_view_booker_instance = PageBookingViewBooker.from_json(json)
# print the JSON string representation of the object
print(PageBookingViewBooker.to_json())

# convert the object into a dict
page_booking_view_booker_dict = page_booking_view_booker_instance.to_dict()
# create an instance of PageBookingViewBooker from a dict
page_booking_view_booker_from_dict = PageBookingViewBooker.from_dict(page_booking_view_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


