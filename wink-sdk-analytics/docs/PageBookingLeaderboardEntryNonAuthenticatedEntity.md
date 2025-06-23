# PageBookingLeaderboardEntryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingLeaderboardEntryNonAuthenticatedEntity]**](BookingLeaderboardEntryNonAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectNonAuthenticatedEntity**](PageableObjectNonAuthenticatedEntity.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.page_booking_leaderboard_entry_non_authenticated_entity import PageBookingLeaderboardEntryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingLeaderboardEntryNonAuthenticatedEntity from a JSON string
page_booking_leaderboard_entry_non_authenticated_entity_instance = PageBookingLeaderboardEntryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageBookingLeaderboardEntryNonAuthenticatedEntity.to_json())

# convert the object into a dict
page_booking_leaderboard_entry_non_authenticated_entity_dict = page_booking_leaderboard_entry_non_authenticated_entity_instance.to_dict()
# create an instance of PageBookingLeaderboardEntryNonAuthenticatedEntity from a dict
page_booking_leaderboard_entry_non_authenticated_entity_from_dict = PageBookingLeaderboardEntryNonAuthenticatedEntity.from_dict(page_booking_leaderboard_entry_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


