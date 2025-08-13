# BookingAncillaryBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Ancillary identifier | 
**hotel_identifier** | **str** | Hotel identifier | 
**type_identifier** | **str** | Travel inventory identifier | 
**transactional_travel_inventory_identifier** | **str** | Travel inventory identifier | 
**name** | **str** | Name of inventory | 
**pricing_type** | **str** | Pricing type | 
**type** | **str** | Inventory type | 
**price** | [**LocalizedPriceBooker**](LocalizedPriceBooker.md) | Pricing information for this ancillary. | 
**start_date** | **datetime** | Date start time when reservation was made for. | 
**end_date** | **datetime** | Date end time when reservation was made for. | 
**attendees** | **int** | Number of guests that are part of this reservation. | [default to 1]
**image_identifier** | **str** | Cloudinary image identifier | 
**image_url** | **str** | Absolute URL to image of inventory | 
**localized_name** | **str** | Name of travel inventory in traveler language (if available). Defaults to English. | 
**localized_description** | **str** | Description of travel blocking in traveler language (if available). Defaults to English. | 
**contact** | [**ContactBooker**](ContactBooker.md) | Travel blocking contact (if applicable) | 
**address** | [**SimpleAddressBooker**](SimpleAddressBooker.md) | Travel blocking address (if applicable) | 
**commissionable** | **bool** |  | 
**mandatory** | **bool** |  | 
**commission** | **float** |  | 

## Example

```python
from wink_sdk_booking.models.booking_ancillary_booker import BookingAncillaryBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BookingAncillaryBooker from a JSON string
booking_ancillary_booker_instance = BookingAncillaryBooker.from_json(json)
# print the JSON string representation of the object
print(BookingAncillaryBooker.to_json())

# convert the object into a dict
booking_ancillary_booker_dict = booking_ancillary_booker_instance.to_dict()
# create an instance of BookingAncillaryBooker from a dict
booking_ancillary_booker_from_dict = BookingAncillaryBooker.from_dict(booking_ancillary_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


