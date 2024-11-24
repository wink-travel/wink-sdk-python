# GeoJsonRectangleNonAuthenticatedEntity

A GeoJSON rectangle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**south_west** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 
**north_east** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.geo_json_rectangle_non_authenticated_entity import GeoJsonRectangleNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonRectangleNonAuthenticatedEntity from a JSON string
geo_json_rectangle_non_authenticated_entity_instance = GeoJsonRectangleNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoJsonRectangleNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_json_rectangle_non_authenticated_entity_dict = geo_json_rectangle_non_authenticated_entity_instance.to_dict()
# create an instance of GeoJsonRectangleNonAuthenticatedEntity from a dict
geo_json_rectangle_non_authenticated_entity_from_dict = GeoJsonRectangleNonAuthenticatedEntity.from_dict(geo_json_rectangle_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


