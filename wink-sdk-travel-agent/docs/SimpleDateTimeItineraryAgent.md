# SimpleDateTimeItineraryAgent

SimpleDateTimeItinerary outlines stay dates, number of adults and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date | 
**end_date** | **datetime** | End date | 
**adults** | **int** | Number of adults | 
**children** | **int** | Number of children | 
**hours** | **int** | Number of hours between start and end dates. Used for itineraries that require bookings that occur within hours and not days. E.g. Meeting room reservation. | [optional] [readonly] 
**guests** | **int** | Total number of adults and children | [optional] [readonly] 
**nights** | **int** | Total number of room nights | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.simple_date_time_itinerary_agent import SimpleDateTimeItineraryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDateTimeItineraryAgent from a JSON string
simple_date_time_itinerary_agent_instance = SimpleDateTimeItineraryAgent.from_json(json)
# print the JSON string representation of the object
print(SimpleDateTimeItineraryAgent.to_json())

# convert the object into a dict
simple_date_time_itinerary_agent_dict = simple_date_time_itinerary_agent_instance.to_dict()
# create an instance of SimpleDateTimeItineraryAgent from a dict
simple_date_time_itinerary_agent_from_dict = SimpleDateTimeItineraryAgent.from_dict(simple_date_time_itinerary_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


