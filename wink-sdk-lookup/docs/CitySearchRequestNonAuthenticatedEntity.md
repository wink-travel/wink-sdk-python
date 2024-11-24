# CitySearchRequestNonAuthenticatedEntity

City search request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier from the [https://geonames.org](https://geonames.org) dataset. | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**search_filters** | [**SearchFiltersNonAuthenticatedEntity**](SearchFiltersNonAuthenticatedEntity.md) |  | [optional] 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [default to 0]
**size** | **int** | The result size to return. | [default to 6]

## Example

```python
from wink_sdk_lookup.models.city_search_request_non_authenticated_entity import CitySearchRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CitySearchRequestNonAuthenticatedEntity from a JSON string
city_search_request_non_authenticated_entity_instance = CitySearchRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CitySearchRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
city_search_request_non_authenticated_entity_dict = city_search_request_non_authenticated_entity_instance.to_dict()
# create an instance of CitySearchRequestNonAuthenticatedEntity from a dict
city_search_request_non_authenticated_entity_from_dict = CitySearchRequestNonAuthenticatedEntity.from_dict(city_search_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


