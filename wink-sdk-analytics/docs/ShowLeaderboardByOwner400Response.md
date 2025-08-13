# ShowLeaderboardByOwner400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.show_leaderboard_by_owner400_response import ShowLeaderboardByOwner400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShowLeaderboardByOwner400Response from a JSON string
show_leaderboard_by_owner400_response_instance = ShowLeaderboardByOwner400Response.from_json(json)
# print the JSON string representation of the object
print(ShowLeaderboardByOwner400Response.to_json())

# convert the object into a dict
show_leaderboard_by_owner400_response_dict = show_leaderboard_by_owner400_response_instance.to_dict()
# create an instance of ShowLeaderboardByOwner400Response from a dict
show_leaderboard_by_owner400_response_from_dict = ShowLeaderboardByOwner400Response.from_dict(show_leaderboard_by_owner400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


