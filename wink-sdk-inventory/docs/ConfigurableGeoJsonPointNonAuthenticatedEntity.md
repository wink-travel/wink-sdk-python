# ConfigurableGeoJsonPointNonAuthenticatedEntity

A way to persist a GeoJSON map point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.configurable_geo_json_point_non_authenticated_entity import ConfigurableGeoJsonPointNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableGeoJsonPointNonAuthenticatedEntity from a JSON string
configurable_geo_json_point_non_authenticated_entity_instance = ConfigurableGeoJsonPointNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConfigurableGeoJsonPointNonAuthenticatedEntity.to_json())

# convert the object into a dict
configurable_geo_json_point_non_authenticated_entity_dict = configurable_geo_json_point_non_authenticated_entity_instance.to_dict()
# create an instance of ConfigurableGeoJsonPointNonAuthenticatedEntity from a dict
configurable_geo_json_point_non_authenticated_entity_from_dict = ConfigurableGeoJsonPointNonAuthenticatedEntity.from_dict(configurable_geo_json_point_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


