# LeaderboardOwnerRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Display leaderboard values in this currency | [default to 'USD']
**owner_identifier** | **UUID** | The company you wish to track on a leaderboard | 

## Example

```python
from wink_sdk_analytics.models.leaderboard_owner_request_authenticated_entity import LeaderboardOwnerRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardOwnerRequestAuthenticatedEntity from a JSON string
leaderboard_owner_request_authenticated_entity_instance = LeaderboardOwnerRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LeaderboardOwnerRequestAuthenticatedEntity.to_json())

# convert the object into a dict
leaderboard_owner_request_authenticated_entity_dict = leaderboard_owner_request_authenticated_entity_instance.to_dict()
# create an instance of LeaderboardOwnerRequestAuthenticatedEntity from a dict
leaderboard_owner_request_authenticated_entity_from_dict = LeaderboardOwnerRequestAuthenticatedEntity.from_dict(leaderboard_owner_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


