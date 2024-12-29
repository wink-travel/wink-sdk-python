# PageBookingViewAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingViewAgent]**](BookingViewAgent.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectAgent**](PageableObjectAgent.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.page_booking_view_agent import PageBookingViewAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingViewAgent from a JSON string
page_booking_view_agent_instance = PageBookingViewAgent.from_json(json)
# print the JSON string representation of the object
print(PageBookingViewAgent.to_json())

# convert the object into a dict
page_booking_view_agent_dict = page_booking_view_agent_instance.to_dict()
# create an instance of PageBookingViewAgent from a dict
page_booking_view_agent_from_dict = PageBookingViewAgent.from_dict(page_booking_view_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


