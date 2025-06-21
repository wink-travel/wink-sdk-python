# GeoJsonPointNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.geo_json_point_non_authenticated_entity import GeoJsonPointNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointNonAuthenticatedEntity from a JSON string
geo_json_point_non_authenticated_entity_instance = GeoJsonPointNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_json_point_non_authenticated_entity_dict = geo_json_point_non_authenticated_entity_instance.to_dict()
# create an instance of GeoJsonPointNonAuthenticatedEntity from a dict
geo_json_point_non_authenticated_entity_from_dict = GeoJsonPointNonAuthenticatedEntity.from_dict(geo_json_point_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


