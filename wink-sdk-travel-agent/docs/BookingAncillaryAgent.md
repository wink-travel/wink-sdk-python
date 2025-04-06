# BookingAncillaryAgent

Add-on records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Ancillary identifier | 
**hotel_identifier** | **str** | Hotel identifier | 
**type_identifier** | **str** | Travel blocking identifier | 
**transactional_travel_inventory_identifier** | **str** | Travel blocking identifier | 
**name** | **str** | Name of blocking | 
**pricing_type** | **str** | Pricing type | 
**type** | **str** | Inventory type | 
**price** | [**LocalizedPriceAgent**](LocalizedPriceAgent.md) |  | 
**start_date** | **datetime** | Date start time when reservation was made for. | 
**end_date** | **datetime** | Date end time when reservation was made for. | 
**attendees** | **int** | Number of guests that are part of this reservation. | [default to 1]
**image_identifier** | **str** | Cloudinary image identifier | 
**image_url** | **str** | Absolute URL to image of blocking | 
**localized_name** | **str** | Name of travel blocking in traveler language (if available). Defaults to English. | 
**localized_description** | **str** | Description of travel blocking in traveler language (if available). Defaults to English. | 
**contact** | [**ContactAgent**](ContactAgent.md) |  | 
**address** | [**SimpleAddressAgent**](SimpleAddressAgent.md) |  | 
**commissionable** | **bool** |  | 
**mandatory** | **bool** |  | 
**commission** | **float** |  | 

## Example

```python
from wink_sdk_travel_agent.models.booking_ancillary_agent import BookingAncillaryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingAncillaryAgent from a JSON string
booking_ancillary_agent_instance = BookingAncillaryAgent.from_json(json)
# print the JSON string representation of the object
print(BookingAncillaryAgent.to_json())

# convert the object into a dict
booking_ancillary_agent_dict = booking_ancillary_agent_instance.to_dict()
# create an instance of BookingAncillaryAgent from a dict
booking_ancillary_agent_from_dict = BookingAncillaryAgent.from_dict(booking_ancillary_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


