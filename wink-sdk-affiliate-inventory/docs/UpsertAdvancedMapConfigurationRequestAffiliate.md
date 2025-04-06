# UpsertAdvancedMapConfigurationRequestAffiliate

Object to save AdvancedMapConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_configuration_identifier** | **str** | Customization identifier | 
**name** | **str** | Name of map | 
**type_identifier** | **str** | Inventory type identifier. Either a single channel inventory identifier, a list identifier or a dynamic search identifier. | 
**type** | **str** | Type of blocking | 
**center** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | 
**draggable** | **bool** | User can move around / pan the map | [default to True]
**zoomable** | **bool** | User can zoom in/out of the map | [default to True]
**initial_zoom_level** | **int** | Valid Google maps zoom level | 
**map_style** | **str** | Map style | 
**map_marker_color** | **str** | Map marker color | 
**map_height** | **int** | Map height in pixels | 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']
**circles** | [**List[ConfigurableGeoJsonCircleAffiliate]**](ConfigurableGeoJsonCircleAffiliate.md) |  | [optional] 
**rectangles** | [**List[ConfigurableGeoJsonRectangleAffiliate]**](ConfigurableGeoJsonRectangleAffiliate.md) |  | [optional] 
**markers** | [**List[ConfigurableGeoJsonPointAffiliate]**](ConfigurableGeoJsonPointAffiliate.md) |  | [optional] 
**polygons** | [**List[ConfigurableGeoJsonPolygonAffiliate]**](ConfigurableGeoJsonPolygonAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.upsert_advanced_map_configuration_request_affiliate import UpsertAdvancedMapConfigurationRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAdvancedMapConfigurationRequestAffiliate from a JSON string
upsert_advanced_map_configuration_request_affiliate_instance = UpsertAdvancedMapConfigurationRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertAdvancedMapConfigurationRequestAffiliate.to_json())

# convert the object into a dict
upsert_advanced_map_configuration_request_affiliate_dict = upsert_advanced_map_configuration_request_affiliate_instance.to_dict()
# create an instance of UpsertAdvancedMapConfigurationRequestAffiliate from a dict
upsert_advanced_map_configuration_request_affiliate_from_dict = UpsertAdvancedMapConfigurationRequestAffiliate.from_dict(upsert_advanced_map_configuration_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


