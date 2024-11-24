# GeoJsonPolygonNonAuthenticatedEntity

Map bounds the user is looking. Bounds provided by map provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[PointNonAuthenticatedEntity]**](PointNonAuthenticatedEntity.md) |  | [optional] 
**coordinates** | [**List[GeoJsonLineStringNonAuthenticatedEntity]**](GeoJsonLineStringNonAuthenticatedEntity.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.geo_json_polygon_non_authenticated_entity import GeoJsonPolygonNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPolygonNonAuthenticatedEntity from a JSON string
geo_json_polygon_non_authenticated_entity_instance = GeoJsonPolygonNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPolygonNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_json_polygon_non_authenticated_entity_dict = geo_json_polygon_non_authenticated_entity_instance.to_dict()
# create an instance of GeoJsonPolygonNonAuthenticatedEntity from a dict
geo_json_polygon_non_authenticated_entity_from_dict = GeoJsonPolygonNonAuthenticatedEntity.from_dict(geo_json_polygon_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


