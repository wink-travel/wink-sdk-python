# SimpleDateTimeItinerarySupplierDetails

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
from wink_sdk_extranet_distribution.models.simple_date_time_itinerary_supplier_details import SimpleDateTimeItinerarySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDateTimeItinerarySupplierDetails from a JSON string
simple_date_time_itinerary_supplier_details_instance = SimpleDateTimeItinerarySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SimpleDateTimeItinerarySupplierDetails.to_json())

# convert the object into a dict
simple_date_time_itinerary_supplier_details_dict = simple_date_time_itinerary_supplier_details_instance.to_dict()
# create an instance of SimpleDateTimeItinerarySupplierDetails from a dict
simple_date_time_itinerary_supplier_details_from_dict = SimpleDateTimeItinerarySupplierDetails.from_dict(simple_date_time_itinerary_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


