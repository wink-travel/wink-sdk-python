# PageBookingLeaderboardEntryAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingLeaderboardEntryAuthenticatedEntity]**](BookingLeaderboardEntryAuthenticatedEntity.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectAuthenticatedEntity**](SortObjectAuthenticatedEntity.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectAuthenticatedEntity**](PageableObjectAuthenticatedEntity.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.page_booking_leaderboard_entry_authenticated_entity import PageBookingLeaderboardEntryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingLeaderboardEntryAuthenticatedEntity from a JSON string
page_booking_leaderboard_entry_authenticated_entity_instance = PageBookingLeaderboardEntryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageBookingLeaderboardEntryAuthenticatedEntity.to_json())

# convert the object into a dict
page_booking_leaderboard_entry_authenticated_entity_dict = page_booking_leaderboard_entry_authenticated_entity_instance.to_dict()
# create an instance of PageBookingLeaderboardEntryAuthenticatedEntity from a dict
page_booking_leaderboard_entry_authenticated_entity_from_dict = PageBookingLeaderboardEntryAuthenticatedEntity.from_dict(page_booking_leaderboard_entry_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


