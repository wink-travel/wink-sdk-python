# AdvancedMapConfigurationNonAuthenticatedEntity

Advanced map configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique map identifier | 
**owner_identifier** | **str** | Map owner identifier | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**name** | **str** | Name of map | 
**type_identifier** | **str** | Inventory type identifier. Either a single channel inventory identifier, a list identifier or a dynamic search identifier. | 
**type** | **str** | Type of blocking | 
**center** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 
**draggable** | **bool** | User can move around / pan the map | [default to True]
**zoomable** | **bool** | User can zoom in/out of the map | [default to True]
**initial_zoom_level** | **int** | Valid Google maps zoom level | 
**map_style** | **str** | Map style | 
**map_marker_color** | **str** | Map marker color | 
**map_height** | **int** | Map height in pixels | 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']
**circles** | [**List[ConfigurableGeoJsonCircleNonAuthenticatedEntity]**](ConfigurableGeoJsonCircleNonAuthenticatedEntity.md) |  | [optional] 
**rectangles** | [**List[ConfigurableGeoJsonRectangleNonAuthenticatedEntity]**](ConfigurableGeoJsonRectangleNonAuthenticatedEntity.md) |  | [optional] 
**markers** | [**List[ConfigurableGeoJsonPointNonAuthenticatedEntity]**](ConfigurableGeoJsonPointNonAuthenticatedEntity.md) |  | [optional] 
**polygons** | [**List[ConfigurableGeoJsonPolygonNonAuthenticatedEntity]**](ConfigurableGeoJsonPolygonNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.advanced_map_configuration_non_authenticated_entity import AdvancedMapConfigurationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedMapConfigurationNonAuthenticatedEntity from a JSON string
advanced_map_configuration_non_authenticated_entity_instance = AdvancedMapConfigurationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AdvancedMapConfigurationNonAuthenticatedEntity.to_json())

# convert the object into a dict
advanced_map_configuration_non_authenticated_entity_dict = advanced_map_configuration_non_authenticated_entity_instance.to_dict()
# create an instance of AdvancedMapConfigurationNonAuthenticatedEntity from a dict
advanced_map_configuration_non_authenticated_entity_from_dict = AdvancedMapConfigurationNonAuthenticatedEntity.from_dict(advanced_map_configuration_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


