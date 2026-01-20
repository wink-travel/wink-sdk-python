# PageBookingAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingAgent]**](BookingAgent.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectAgent**](SortObjectAgent.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectAgent**](PageableObjectAgent.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.page_booking_agent import PageBookingAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingAgent from a JSON string
page_booking_agent_instance = PageBookingAgent.from_json(json)
# print the JSON string representation of the object
print(PageBookingAgent.to_json())

# convert the object into a dict
page_booking_agent_dict = page_booking_agent_instance.to_dict()
# create an instance of PageBookingAgent from a dict
page_booking_agent_from_dict = PageBookingAgent.from_dict(page_booking_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


