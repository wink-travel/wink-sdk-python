# LeaderboardRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Which page to access in the record set | [default to 0]
**size** | **int** | Number of result set to retrieve | [default to 100]
**currency_code** | **str** | Display leaderboard values in this currency | [default to 'USD']
**type** | **str** | The type of leaderboard to display | [default to 'GLOBAL']
**grouping_identifier** | **str** | Can be &#x60;continent&#x60;, &#x60;country.geoNameId&#x60; or &#x60;city.geoNameId&#x60; | [optional] 

## Example

```python
from wink_sdk_analytics.models.leaderboard_request_non_authenticated_entity import LeaderboardRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardRequestNonAuthenticatedEntity from a JSON string
leaderboard_request_non_authenticated_entity_instance = LeaderboardRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LeaderboardRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
leaderboard_request_non_authenticated_entity_dict = leaderboard_request_non_authenticated_entity_instance.to_dict()
# create an instance of LeaderboardRequestNonAuthenticatedEntity from a dict
leaderboard_request_non_authenticated_entity_from_dict = LeaderboardRequestNonAuthenticatedEntity.from_dict(leaderboard_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


