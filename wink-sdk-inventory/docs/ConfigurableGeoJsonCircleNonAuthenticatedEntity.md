# ConfigurableGeoJsonCircleNonAuthenticatedEntity

A way to persist a GeoJSON circle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **float** | Circle radius from center | 
**point** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) | Circle center point | 

## Example

```python
from wink_sdk_inventory.models.configurable_geo_json_circle_non_authenticated_entity import ConfigurableGeoJsonCircleNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableGeoJsonCircleNonAuthenticatedEntity from a JSON string
configurable_geo_json_circle_non_authenticated_entity_instance = ConfigurableGeoJsonCircleNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConfigurableGeoJsonCircleNonAuthenticatedEntity.to_json())

# convert the object into a dict
configurable_geo_json_circle_non_authenticated_entity_dict = configurable_geo_json_circle_non_authenticated_entity_instance.to_dict()
# create an instance of ConfigurableGeoJsonCircleNonAuthenticatedEntity from a dict
configurable_geo_json_circle_non_authenticated_entity_from_dict = ConfigurableGeoJsonCircleNonAuthenticatedEntity.from_dict(configurable_geo_json_circle_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


