# MapRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | [optional] 
**bounds** | [**GeoJsonPolygonNonAuthenticatedEntity**](GeoJsonPolygonNonAuthenticatedEntity.md) |  | [optional] 
**search_filters** | [**SearchFiltersNonAuthenticatedEntity**](SearchFiltersNonAuthenticatedEntity.md) |  | [optional] 
**inventory_types** | **List[str]** |  | [optional] 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [optional] [default to 0]
**size** | **int** | The result size to return. | [optional] [default to 10]

## Example

```python
from wink_sdk_lookup.models.map_request_non_authenticated_entity import MapRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MapRequestNonAuthenticatedEntity from a JSON string
map_request_non_authenticated_entity_instance = MapRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(MapRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
map_request_non_authenticated_entity_dict = map_request_non_authenticated_entity_instance.to_dict()
# create an instance of MapRequestNonAuthenticatedEntity from a dict
map_request_non_authenticated_entity_from_dict = MapRequestNonAuthenticatedEntity.from_dict(map_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


