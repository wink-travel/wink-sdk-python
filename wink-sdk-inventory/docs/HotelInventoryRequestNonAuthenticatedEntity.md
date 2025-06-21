# HotelInventoryRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique property identifier to retrieve inventory for. Either the hotelIdentifier or urlName property is required. | [optional] 
**url_name** | **str** | Unique url-friendly record identifier of property. Either the hotelIdentifier or urlName property is required. | [optional] 
**show_hotel** | **bool** | Flag to indicate whether to return basic property data. If you are loading up property for the first time, this data would be good to include. But there is no need to load that a second time if you are only going for availability data. This field populates &#x60;hotel&#x60; data in response. | [optional] [default to True]
**show_room_types** | **bool** | Flag to indicate whether to return property room type data. This field populates &#x60;roomType&#x60;, &#x60;cheapesRoomTypes&#x60; and &#x60;available&#x60; data in response. | [optional] [default to True]
**show_metadata** | **bool** | Flag to indicate whether to return property meta data. This field populates &#x60;metadata&#x60; data in response. | [optional] [default to True]
**show_videos** | **bool** | Flag to indicate whether to return property video data. This field populates &#x60;videos&#x60; data in response. | [optional] [default to False]
**show_images** | **bool** | Flag to indicate whether to return property image data. This field populates &#x60;images&#x60; data in response. | [optional] [default to False]
**show_add_on_offers** | **bool** | Flag to indicate whether to return property add-on data. This field populates &#x60;roomTypes.priceConfigurations.addOnOffers&#x60; data in response. | [optional] [default to False]
**show_restaurants** | **bool** | Flag to indicate whether to return property restaurant data. This field populates &#x60;restaurants&#x60; data in response. | [optional] [default to False]
**show_meeting_rooms** | **bool** | Flag to indicate whether to return property meeting room data. This field populates &#x60;meetingRooms&#x60; data in response. | [optional] [default to False]
**show_spas** | **bool** | Flag to indicate whether to return property spa data. This field populates &#x60;spas&#x60; data in response. | [optional] [default to False]
**show_attractions** | **bool** | Flag to indicate whether to return property attraction data. This field populates &#x60;attractions&#x60; data in response. | [optional] [default to False]
**show_activities** | **bool** | Flag to indicate whether to return property activity data. This field populates &#x60;activities&#x60; data in response. | [optional] [default to False]
**show_places** | **bool** | Flag to indicate whether to return property place data. This field populates &#x60;places&#x60; data in response. | [optional] [default to False]
**show_recognition** | **bool** | Flag to indicate whether to return property recognition data. This field populates &#x60;recognitions&#x60; data in response. | [optional] [default to False]
**show_aggregate_green_index_scores** | **bool** | Flag to indicate whether to return property green index score data. This field populates &#x60;greenIndexScores&#x60; data in response. Note: You only need to return hotel data to get the overall aggregate Green Index score and not detailed category scores. | [optional] [default to False]
**show_announcements** | **bool** | Flag to indicate whether to return property announcement data. Announcements are messages the property wishes to convey to travelers for certain dates. This field populates &#x60;announcements&#x60; data in response. | [optional] [default to False]
**show_reviews** | **bool** | Flag to indicate whether to return property review data. Note: You only need to return hotel data to get the overall aggregate review score and not the entire list of reviews. This field populates &#x60;reviews&#x60; data in response. | [optional] [default to False]
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | Returns the same user session that was sent by the caller. | 

## Example

```python
from wink_sdk_inventory.models.hotel_inventory_request_non_authenticated_entity import HotelInventoryRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HotelInventoryRequestNonAuthenticatedEntity from a JSON string
hotel_inventory_request_non_authenticated_entity_instance = HotelInventoryRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HotelInventoryRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
hotel_inventory_request_non_authenticated_entity_dict = hotel_inventory_request_non_authenticated_entity_instance.to_dict()
# create an instance of HotelInventoryRequestNonAuthenticatedEntity from a dict
hotel_inventory_request_non_authenticated_entity_from_dict = HotelInventoryRequestNonAuthenticatedEntity.from_dict(hotel_inventory_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


