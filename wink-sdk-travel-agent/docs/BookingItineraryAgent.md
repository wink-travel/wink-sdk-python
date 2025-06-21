# BookingItineraryAgent

BookingItinerary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of itinerary | 
**end_date** | **date** | Optional end date. If endDate is empty, nights needs to be present. If both are present, nights will take precedence. | [optional] 
**nights** | **int** | Optional number of nights. If nights is empty, endDate needs to be present. If both are present, nights will take precedence. | [optional] 
**items** | [**List[BookingItineraryRoomConfigurationAgent]**](BookingItineraryRoomConfigurationAgent.md) |  | [optional] 
**hours** | **int** | Number of hours between start and end dates. Used for itineraries that require bookings that occur within hours and not days. E.g. Meeting room reservation. | [optional] [readonly] 
**children** | **int** | How many total children for this stay | [optional] 
**rooms** | **int** | How many total rooms for this stay | [optional] 
**guests** | **int** | How many total guests for this stay | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_itinerary_agent import BookingItineraryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryAgent from a JSON string
booking_itinerary_agent_instance = BookingItineraryAgent.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryAgent.to_json())

# convert the object into a dict
booking_itinerary_agent_dict = booking_itinerary_agent_instance.to_dict()
# create an instance of BookingItineraryAgent from a dict
booking_itinerary_agent_from_dict = BookingItineraryAgent.from_dict(booking_itinerary_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


