# BookingItineraryBooker

BookingItinerary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of itinerary | 
**end_date** | **date** | Optional end date. If endDate is empty, nights needs to be present. If both are present, nights will take precedence. | [optional] 
**nights** | **int** | Optional number of nights. If nights is empty, endDate needs to be present. If both are present, nights will take precedence. | [optional] 
**items** | [**List[BookingItineraryRoomConfigurationBooker]**](BookingItineraryRoomConfigurationBooker.md) |  | [optional] 
**hours** | **int** | Number of hours between start and end dates. Used for itineraries that require bookings that occur within hours and not days. E.g. Meeting room reservation. | [optional] [readonly] 
**children** | **int** | How many total children for this stay | [optional] 
**guests** | **int** | How many total guests for this stay | [optional] 
**rooms** | **int** | How many total rooms for this stay | [optional] 

## Example

```python
from wink_sdk_booking.models.booking_itinerary_booker import BookingItineraryBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryBooker from a JSON string
booking_itinerary_booker_instance = BookingItineraryBooker.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryBooker.to_json())

# convert the object into a dict
booking_itinerary_booker_dict = booking_itinerary_booker_instance.to_dict()
# create an instance of BookingItineraryBooker from a dict
booking_itinerary_booker_from_dict = BookingItineraryBooker.from_dict(booking_itinerary_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


