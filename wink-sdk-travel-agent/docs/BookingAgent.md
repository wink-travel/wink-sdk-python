# BookingAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**creation** | **str** | Communicates whether the booking was created normally or if it failed or was just for testing. | [default to 'NORMAL']
**group_identifier** | **str** | Unique record identifier for the collection of bookings that were made at the same time. | 
**customization** | [**CustomizationLightweightAgent**](CustomizationLightweightAgent.md) | Which customization configuration record did the entity application used to facilitate in making this booking happen. | 
**booking_code** | **str** | Unique user-friendly booking geoname. This code should be used when corresponding with travelers. | 
**user** | [**BookingUserAgent**](BookingUserAgent.md) | User details for the authenticated person that made the booking. | 
**user_session** | [**BookingUserSessionAgent**](BookingUserSessionAgent.md) | User session state as it was when the user made the booking. | 
**server_url** | **str** | The URL the booking occurred | 
**socials** | [**List[SocialAgent]**](SocialAgent.md) | List of all social network account property has for the traveler to get in touch. | [optional] 
**review** | [**ReviewLightweightAgent**](ReviewLightweightAgent.md) | User review created by the traveler after the booking completed. | [optional] 
**email_header_logo_url** | **str** | Full url of the image logo optimized for emails | 
**logo_identifier** | **str** | Logo cloudinary identifier for potential reuse | [optional] 
**hotel** | [**PropertyAggregateLightweightAgent**](PropertyAggregateLightweightAgent.md) | Combined property data. | 
**room_stay** | [**RoomStayAgent**](RoomStayAgent.md) | All information about the room that was booked. | [optional] 
**special_requests** | **str** | Free text where the traveler can add a message to the property. | [optional] 
**comment** | **str** | Internal comment field the platform can add and make available to channel manager partners. | [optional] 
**early_check_in_charge** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Early check-in charge fixed amount that is due if guest checks out early. | [optional] 
**late_check_out_charge** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Late check-out charge fixed amount that is due if guest checks out late. | [optional] 
**early_check_in_charge_percent** | **float** | Early check-in charge calculated in percent of first room night price. | [optional] 
**late_check_out_charge_percent** | **float** | Early check-in charge calculated in percent of first room night price. | [optional] 
**hotel_image_url** | **str** | Absolute URL of hotel image that can be used as-is | 
**room_image_url** | **str** | Absolute URL of room image that can be used as-is | 
**commission_list** | [**List[CommissionableEntryAgent]**](CommissionableEntryAgent.md) | List of all travel inventory entries that are due a commission to the affiliate. | [optional] 
**ancillary_list** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) |  | [optional] 
**booking_contract** | [**BookingContractAgent**](BookingContractAgent.md) | Booking contract created by TripPay | [optional] 
**static_map_image_url** | **str** | Url of map image that can be sent via email | [optional] 
**static_map_url** | **str** | Url of map image location on Google Maps | [optional] 
**status** | **str** | Convenience data point to show which status the booking currently has. | [optional] 
**meeting_rooms** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Meeting room reservation records. | [optional] 
**restaurants** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Restaurant reservation records. | [optional] 
**spas** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Spa reservation records. | [optional] 
**activities** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Activity reservation records. | [optional] 
**attractions** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Attraction reservation records. | [optional] 
**places** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Place reservation records. | [optional] 
**room_type_ancillaries** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Room type ancillary records. | [optional] 
**add_ons** | [**List[BookingAncillaryAgent]**](BookingAncillaryAgent.md) | Add-on records. | [optional] 
**cancellable_by_agent** | **bool** | Whether the booking can still be cancelled completely by the agent. | [optional] 
**rate_source** | **str** | Rate origin. This is usually the property channel manager. | [optional] 
**has_add_ons** | **bool** | Convenience data point to check if any add-on offers are in this booking. | [optional] 
**cancellable_by_supplier** | **bool** | Whether the booking can still be cancelled completely by the supplier. | [optional] 
**cancellable_by_traveler** | **bool** | Whether the booking can still be cancelled completely by the traveller. | [optional] 
**reporting_daily_rate_list** | **List[object]** |  | [optional] 
**reporting_ancillary_list** | **List[object]** |  | [optional] 
**reporting_extra_charge_list** | **List[object]** |  | [optional] 
**has_breakfast** | **bool** | Convenience data point to get to breakfast quickly. | [optional] 
**has_brunch** | **bool** | Convenience data point to get to brunch quickly. | [optional] 
**has_lunch** | **bool** | Convenience data point to get to lunch quickly. | [optional] 
**has_dinner** | **bool** | Convenience data point to get to dinner quickly. | [optional] 
**has_all_inclusive** | **bool** | Convenience data point to get to all-inclusive quickly. | [optional] 
**has_all_inclusive_plus_alcohol** | **bool** | Convenience data point to get to all-inclusive with alcohol quickly. | [optional] 
**has_room_type_ancillaries** | **bool** | Convenience data point to check if any room type ancillaries are in this booking. | [optional] 
**has_food** | **bool** | Convenience data point to check if any food is included in this booking. | [optional] 
**has_restaurants** | **bool** | Convenience data point to check if any restaurant reservations are included in this booking. | [optional] 
**has_meeting_rooms** | **bool** | Convenience data point to check if any meeting room reservations are included in this booking. | [optional] 
**has_spas** | **bool** | Convenience data point to check if any spa reservations are included in this booking. | [optional] 
**has_activities** | **bool** | Convenience data point to check if any activity reservations are included in this booking. | [optional] 
**has_attractions** | **bool** | Convenience data point to check if any attractions reservations are included in this booking. | [optional] 
**has_places** | **bool** | Convenience data point to check if any place reservations are included in this booking. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_agent import BookingAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingAgent from a JSON string
booking_agent_instance = BookingAgent.from_json(json)
# print the JSON string representation of the object
print(BookingAgent.to_json())

# convert the object into a dict
booking_agent_dict = booking_agent_instance.to_dict()
# create an instance of BookingAgent from a dict
booking_agent_from_dict = BookingAgent.from_dict(booking_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


