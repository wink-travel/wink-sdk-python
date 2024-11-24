# ChartRequestAuthenticatedEntity

Chart properties allow you to choose how to visualize available data points. Choose how you want to:   - filter your data  - sort your data  - group your data  - include data in your data sets  - display currency amounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | **str** | The time series to visualize | 
**time_series_units** | **int** | How many units of the time series type to visualize. Only required if start / end date not populated. | [optional] 
**start_date** | **datetime** | Fixed date to start visualizations on | [optional] 
**end_date** | **datetime** | Fixed date to end visualizations on | [optional] 
**filter_on_hotel_identifier** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_channel_sub_type** | **str** | Filter on channel sub type. What channel sub-type helped make the booking. | [optional] 
**filter_on_owner_identifier** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_engine_country_geo_name_id** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_engine_city_geo_name_id** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_engine_continent_code** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_engine_configuration_identifier** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_country_geo_name_id** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_city_geo_name_id** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_continent_code** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**filter_on_user_identifier** | [**KeyValuePairAuthenticatedEntity**](KeyValuePairAuthenticatedEntity.md) |  | [optional] 
**sort_on_page_visits** | **bool** | Sort on page visits | [optional] [default to False]
**sort_on_map_marker_visits** | **bool** | Sort on map marker visits | [optional] [default to False]
**sort_on_card_visits** | **bool** | Sort on card visits | [optional] [default to False]
**sort_on_bookings** | **bool** | Sort on bookings | [optional] [default to False]
**sort_on_cancellations** | **bool** | Sort on cancellations | [optional] [default to False]
**sort_on_room_nights** | **bool** | Sort on room nights | [optional] [default to False]
**sort_on_meeting_rooms** | **bool** | Sort on meeting rooms | [optional] [default to False]
**sort_on_meeting_rooms_revenue** | **bool** | Sort on meeting rooms revenue | [optional] [default to False]
**sort_on_restaurants** | **bool** | Sort on restaurants | [optional] [default to False]
**sort_on_restaurants_revenue** | **bool** | Sort on restaurants revenue | [optional] [default to False]
**sort_on_spas** | **bool** | Sort on spas | [optional] [default to False]
**sort_on_spas_revenue** | **bool** | Sort on spas revenue | [optional] [default to False]
**sort_on_activities** | **bool** | Sort on activities | [optional] [default to False]
**sort_on_activities_revenue** | **bool** | Sort on activities revenue | [optional] [default to False]
**sort_on_attractions** | **bool** | Sort on attractions | [optional] [default to False]
**sort_on_attractions_revenue** | **bool** | Sort on attractions revenue | [optional] [default to False]
**sort_on_places** | **bool** | Sort on places | [optional] [default to False]
**sort_on_places_revenue** | **bool** | Sort on places revenue | [optional] [default to False]
**sort_on_room_type_ancillaries** | **bool** | Sort on room type ancillaries | [optional] [default to False]
**sort_on_room_type_ancillaries_revenue** | **bool** | Sort on room type ancillaries revenue | [optional] [default to False]
**sort_on_add_ons** | **bool** | Sort on add-ons | [optional] [default to False]
**sort_on_addons_revenue** | **bool** | Sort on add-on revenue | [optional] [default to False]
**sort_on_total_room_revenue** | **bool** | Sort on total room revenue | [optional] [default to False]
**sort_on_total_ancillaries_revenue** | **bool** | Sort on aggregate ancillaries revenue | [optional] [default to False]
**sort_on_total_net_revenue** | **bool** | Sort on total net revenue | [optional] [default to False]
**sort_on_cancelled_room_nights** | **bool** | Sort on cancelled room nights | [optional] [default to False]
**sort_on_cancelled_meeting_rooms** | **bool** | Sort on cancelled meeting rooms | [optional] [default to False]
**sort_on_cancelled_meeting_rooms_revenue** | **bool** | Sort on cancelled meeting rooms revenue | [optional] [default to False]
**sort_on_cancelled_restaurants** | **bool** | Sort on cancelled restaurants | [optional] [default to False]
**sort_on_cancelled_restaurants_revenue** | **bool** | Sort on cancelled restaurants revenue | [optional] [default to False]
**sort_on_cancelled_spas** | **bool** | Sort on cancelled spas | [optional] [default to False]
**sort_on_cancelled_spas_revenue** | **bool** | Sort on cancelled spas revenue | [optional] [default to False]
**sort_on_cancelled_activities** | **bool** | Sort on cancelled activities | [optional] [default to False]
**sort_on_cancelled_activities_revenue** | **bool** | Sort on cancelled activities revenue | [optional] [default to False]
**sort_on_cancelled_attractions** | **bool** | Sort on cancelled attractions | [optional] [default to False]
**sort_on_cancelled_attractions_revenue** | **bool** | Sort on cancelled attractions revenue | [optional] [default to False]
**sort_on_cancelled_places** | **bool** | Sort on cancelled places | [optional] [default to False]
**sort_on_cancelled_places_revenue** | **bool** | Sort on cancelled places revenue | [optional] [default to False]
**sort_on_cancelled_total_room_revenue** | **bool** | Sort on cancelled total room revenue | [optional] [default to False]
**sort_on_cancelled_total_ancillaries_revenue** | **bool** | Sort on cancelled aggregate total ancillaries revenue | [optional] [default to False]
**sort_on_cancelled_room_type_ancillaries** | **bool** | Sort on cancelled room type ancillaries | [optional] [default to False]
**sort_on_cancelled_room_type_ancillaries_revenue** | **bool** | Sort on cancelled room type ancillaries revenue | [optional] [default to False]
**sort_on_cancelled_add_ons** | **bool** | Sort on cancelled add-ons | [optional] [default to False]
**sort_on_cancelled_addons_revenue** | **bool** | Sort on cancelled add-o revenue | [optional] [default to False]
**sort_on_cancelled_total_net_revenue** | **bool** | Sort on cancelled total net revenue | [optional] [default to False]
**include_page_visits** | **bool** | Include page visits | [optional] [default to False]
**include_map_marker_visits** | **bool** | Include map marker visits | [optional] [default to False]
**include_card_visits** | **bool** | Include card visits | [optional] [default to False]
**include_bookings** | **bool** | Include bookings | [optional] [default to False]
**include_cancellations** | **bool** | Include cancellations | [optional] [default to False]
**include_room_nights** | **bool** | Include room nights | [optional] [default to False]
**include_meeting_rooms** | **bool** | Include meeting rooms | [optional] [default to False]
**include_meeting_rooms_revenue** | **bool** | Include meeting rooms revenue | [optional] [default to False]
**include_restaurants** | **bool** | Include restaurants | [optional] [default to False]
**include_restaurants_revenue** | **bool** | Include restaurants revenue | [optional] [default to False]
**include_spas** | **bool** | Include spas | [optional] [default to False]
**include_spas_revenue** | **bool** | Include spas revenue | [optional] [default to False]
**include_activities** | **bool** | Include activities | [optional] [default to False]
**include_activities_revenue** | **bool** | Include activities revenue | [optional] [default to False]
**include_attractions** | **bool** | Include attractions | [optional] [default to False]
**include_attractions_revenue** | **bool** | Include attractions revenue | [optional] [default to False]
**include_places** | **bool** | Include places | [optional] [default to False]
**include_places_revenue** | **bool** | Include places revenue | [optional] [default to False]
**include_room_type_ancillaries** | **bool** | Include room type ancillaries | [optional] [default to False]
**include_room_type_ancillaries_revenue** | **bool** | Include packages revenue | [optional] [default to False]
**include_add_ons** | **bool** | Include add-ons | [optional] [default to False]
**include_add_ons_revenue** | **bool** | Include add-ons revenue | [optional] [default to False]
**include_total_room_revenue** | **bool** | Include total room revenue | [optional] [default to False]
**include_average_room_rate** | **bool** | Include average room rate | [optional] [default to False]
**include_total_ancillaries_revenue** | **bool** | Include combined packages and add-os revenue | [optional] [default to False]
**include_total_net_revenue** | **bool** | Include total net revenue | [optional] [default to False]
**include_cancelled_room_nights** | **bool** | Include cancelled room nights | [optional] [default to False]
**include_cancelled_meeting_rooms** | **bool** | Include cancelled meeting rooms | [optional] [default to False]
**include_cancelled_meeting_rooms_revenue** | **bool** | Include cancelled meeting rooms revenue | [optional] [default to False]
**include_cancelled_restaurants** | **bool** | Include cancelled restaurants | [optional] [default to False]
**include_cancelled_restaurants_revenue** | **bool** | Include cancelled restaurants revenue | [optional] [default to False]
**include_cancelled_spas** | **bool** | Include cancelled spas | [optional] [default to False]
**include_cancelled_spas_revenue** | **bool** | Include cancelled spas revenue | [optional] [default to False]
**include_cancelled_activities** | **bool** | Include cancelled activities | [optional] [default to False]
**include_cancelled_activities_revenue** | **bool** | Include cancelled activities revenue | [optional] [default to False]
**include_cancelled_attractions** | **bool** | Include cancelled attractions | [optional] [default to False]
**include_cancelled_attractions_revenue** | **bool** | Include cancelled attractions revenue | [optional] [default to False]
**include_cancelled_places** | **bool** | Include cancelled places | [optional] [default to False]
**include_cancelled_places_revenue** | **bool** | Include cancelled places revenue | [optional] [default to False]
**include_cancelled_room_type_ancillaries** | **bool** | Include cancelled packages | [optional] [default to False]
**include_cancelled_room_type_ancillaries_revenue** | **bool** | Include cancelled packages revenue | [optional] [default to False]
**include_cancelled_add_ons** | **bool** | Include cancelled add-ons | [optional] [default to False]
**include_cancelled_add_ons_revenue** | **bool** | Include cancelled add-ons revenue | [optional] [default to False]
**include_cancelled_total_room_revenue** | **bool** | Include cancelled total room revenue | [optional] [default to False]
**include_cancelled_total_ancillaries_revenue** | **bool** | Include combined cancelled package and add-on revenue | [optional] [default to False]
**include_cancelled_total_net_revenue** | **bool** | Include cancelled total net revenue | [optional] [default to False]
**group_on_channel_sub_type** | **bool** | Group on  channel sub type | [optional] [default to False]
**group_on_owner_identifier** | **bool** | Group on owner identifier | [optional] [default to False]
**group_on_engine_country_geo_name_id** | **bool** | Group on application country geoNameId | [optional] [default to False]
**group_on_engine_city_geo_name_id** | **bool** | Group on application city geoNameId | [optional] [default to False]
**group_on_engine_continent_code** | **bool** | Group on application continent code | [optional] [default to False]
**group_on_engine_configuration_identifier** | **bool** | Group on customization identifier | [optional] [default to False]
**group_on_country_geo_name_id** | **bool** | Group on country geoNameId | [optional] [default to False]
**group_on_city_geo_name_id** | **bool** | Group on city geoNameId | [optional] [default to False]
**group_on_continent_code** | **bool** | Group on continent code | [optional] [default to False]
**group_on_hotel_identifier** | **bool** | Group on hotel identifier | [optional] [default to False]
**group_on_user_identifier** | **bool** | Group on user identifier | [optional] [default to False]
**currency_code** | **str** | Currency code | [optional] [default to 'USD']

## Example

```python
from wink_sdk_analytics.models.chart_request_authenticated_entity import ChartRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChartRequestAuthenticatedEntity from a JSON string
chart_request_authenticated_entity_instance = ChartRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChartRequestAuthenticatedEntity.to_json())

# convert the object into a dict
chart_request_authenticated_entity_dict = chart_request_authenticated_entity_instance.to_dict()
# create an instance of ChartRequestAuthenticatedEntity from a dict
chart_request_authenticated_entity_from_dict = ChartRequestAuthenticatedEntity.from_dict(chart_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


