# SearchFiltersNonAuthenticatedEntity

How user likes to have results displayed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_sounds_like** | **str** | A user can query for a property with a name that sounds like | [optional] 
**radius_in_meters** | **int** | A user can query for blocking that is in a certain proximity to a geo-location. 0 means disabled | [optional] [default to 0]
**lifestyle** | **str** | A user can filter blocking on a lifestyle | [optional] 
**star_rating** | **int** | A user can filter on number of hotel stars | [optional] 
**direct_only** | **bool** | Whether to return blocking that is coming from a supplier with a direct relationship to caller | [optional] 

## Example

```python
from wink_sdk_lookup.models.search_filters_non_authenticated_entity import SearchFiltersNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersNonAuthenticatedEntity from a JSON string
search_filters_non_authenticated_entity_instance = SearchFiltersNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersNonAuthenticatedEntity.to_json())

# convert the object into a dict
search_filters_non_authenticated_entity_dict = search_filters_non_authenticated_entity_instance.to_dict()
# create an instance of SearchFiltersNonAuthenticatedEntity from a dict
search_filters_non_authenticated_entity_from_dict = SearchFiltersNonAuthenticatedEntity.from_dict(search_filters_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


