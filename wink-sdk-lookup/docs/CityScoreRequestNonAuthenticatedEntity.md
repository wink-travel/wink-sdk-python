# CityScoreRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_name** | **str** | Unique url name for city you wish to search in as it was given to you in the lookup entry. | 
**sort** | **str** | Choose the criteria you want the results sorted on. | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**search_filters** | [**SearchFiltersNonAuthenticatedEntity**](SearchFiltersNonAuthenticatedEntity.md) |  | [optional] 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [default to 0]
**size** | **int** | The result size to return. | [default to 6]

## Example

```python
from wink_sdk_lookup.models.city_score_request_non_authenticated_entity import CityScoreRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CityScoreRequestNonAuthenticatedEntity from a JSON string
city_score_request_non_authenticated_entity_instance = CityScoreRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CityScoreRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
city_score_request_non_authenticated_entity_dict = city_score_request_non_authenticated_entity_instance.to_dict()
# create an instance of CityScoreRequestNonAuthenticatedEntity from a dict
city_score_request_non_authenticated_entity_from_dict = CityScoreRequestNonAuthenticatedEntity.from_dict(city_score_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


