# CountryScoreRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Unique country code you want to search in as it was given to you in the lookup entry or by using standard country codes as defined here [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | 
**sort** | **str** | Choose the criteria you want the results sorted on. | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | User session is the current search state. SimpleDateTimeItinerary and other data points are all included here. | 
**search_filters** | [**SearchFiltersNonAuthenticatedEntity**](SearchFiltersNonAuthenticatedEntity.md) | How user likes to have results displayed | [optional] 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [default to 0]
**size** | **int** | The result size to return. | [default to 6]

## Example

```python
from wink_sdk_lookup.models.country_score_request_non_authenticated_entity import CountryScoreRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CountryScoreRequestNonAuthenticatedEntity from a JSON string
country_score_request_non_authenticated_entity_instance = CountryScoreRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CountryScoreRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
country_score_request_non_authenticated_entity_dict = country_score_request_non_authenticated_entity_instance.to_dict()
# create an instance of CountryScoreRequestNonAuthenticatedEntity from a dict
country_score_request_non_authenticated_entity_from_dict = CountryScoreRequestNonAuthenticatedEntity.from_dict(country_score_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


