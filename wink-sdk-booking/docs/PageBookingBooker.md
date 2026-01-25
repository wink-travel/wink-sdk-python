# PageBookingBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingBooker]**](BookingBooker.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectBooker**](PageableObjectBooker.md) |  | [optional] 
**sort** | [**SortObjectBooker**](SortObjectBooker.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.page_booking_booker import PageBookingBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingBooker from a JSON string
page_booking_booker_instance = PageBookingBooker.from_json(json)
# print the JSON string representation of the object
print(PageBookingBooker.to_json())

# convert the object into a dict
page_booking_booker_dict = page_booking_booker_instance.to_dict()
# create an instance of PageBookingBooker from a dict
page_booking_booker_from_dict = PageBookingBooker.from_dict(page_booking_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


