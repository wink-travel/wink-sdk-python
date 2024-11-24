# BookingLeaderboardEntryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_identifier** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_geo_name_id** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**city_geo_name_id** | **str** |  | [optional] 
**bookings** | **int** |  | [optional] 
**total_price_amount** | **float** |  | [optional] 
**average_booking_amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.booking_leaderboard_entry_non_authenticated_entity import BookingLeaderboardEntryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BookingLeaderboardEntryNonAuthenticatedEntity from a JSON string
booking_leaderboard_entry_non_authenticated_entity_instance = BookingLeaderboardEntryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BookingLeaderboardEntryNonAuthenticatedEntity.to_json())

# convert the object into a dict
booking_leaderboard_entry_non_authenticated_entity_dict = booking_leaderboard_entry_non_authenticated_entity_instance.to_dict()
# create an instance of BookingLeaderboardEntryNonAuthenticatedEntity from a dict
booking_leaderboard_entry_non_authenticated_entity_from_dict = BookingLeaderboardEntryNonAuthenticatedEntity.from_dict(booking_leaderboard_entry_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


