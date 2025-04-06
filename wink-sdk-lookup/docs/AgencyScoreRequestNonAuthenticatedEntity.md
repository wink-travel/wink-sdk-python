# AgencyScoreRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_url_name_or_country_code** | **str** | Unique url name for city or country code for country. | [optional] 
**sort** | **str** | Choose the criteria you want the results sorted on. | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [default to 0]
**size** | **int** | The result size to return. | [default to 6]

## Example

```python
from wink_sdk_lookup.models.agency_score_request_non_authenticated_entity import AgencyScoreRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyScoreRequestNonAuthenticatedEntity from a JSON string
agency_score_request_non_authenticated_entity_instance = AgencyScoreRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AgencyScoreRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
agency_score_request_non_authenticated_entity_dict = agency_score_request_non_authenticated_entity_instance.to_dict()
# create an instance of AgencyScoreRequestNonAuthenticatedEntity from a dict
agency_score_request_non_authenticated_entity_from_dict = AgencyScoreRequestNonAuthenticatedEntity.from_dict(agency_score_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


