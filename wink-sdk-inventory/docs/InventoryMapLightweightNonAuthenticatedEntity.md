# InventoryMapLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Map identifier | 
**owner_identifier** | **str** | Map owner identifier | 
**customization_identifier** | **str** | Customization identifier | 
**name** | **str** | Name of map | 
**type_identifier** | **str** | Inventory type identifier. Either a single channel inventory identifier, a list identifier or a dynamic search identifier. | 
**type** | **str** | Type of blocking | 
**center** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) | Map center point | 
**draggable** | **bool** | User can move around / pan the map | [default to True]
**zoomable** | **bool** | User can zoom in/out of the map | [default to True]
**initial_zoom_level** | **int** | Valid Google maps zoom level | 
**map_style** | **str** | Map style | 
**map_marker_color** | **str** | Map marker color | 
**map_height** | **int** | Map height in pixels | 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']
**circles** | [**List[ConfigurableGeoJsonCircleNonAuthenticatedEntity]**](ConfigurableGeoJsonCircleNonAuthenticatedEntity.md) |  | [optional] 
**rectangles** | **List[object]** |  | [optional] 
**markers** | **List[object]** |  | [optional] 
**polygons** | **List[object]** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.inventory_map_lightweight_non_authenticated_entity import InventoryMapLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMapLightweightNonAuthenticatedEntity from a JSON string
inventory_map_lightweight_non_authenticated_entity_instance = InventoryMapLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryMapLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_map_lightweight_non_authenticated_entity_dict = inventory_map_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of InventoryMapLightweightNonAuthenticatedEntity from a dict
inventory_map_lightweight_non_authenticated_entity_from_dict = InventoryMapLightweightNonAuthenticatedEntity.from_dict(inventory_map_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


