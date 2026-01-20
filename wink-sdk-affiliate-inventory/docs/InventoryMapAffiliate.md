# InventoryMapAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**owner_identifier** | **UUID** | Map owner identifier | 
**customization_identifier** | **UUID** | Customization identifier | 
**name** | **str** | Name of map | 
**type_identifier** | **UUID** | Inventory type identifier. Either a single channel inventory identifier, a list identifier or a dynamic search identifier. | 
**type** | **str** | Type of inventory | 
**center** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Map center point | 
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
from wink_sdk_affiliate_inventory.models.inventory_map_affiliate import InventoryMapAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMapAffiliate from a JSON string
inventory_map_affiliate_instance = InventoryMapAffiliate.from_json(json)
# print the JSON string representation of the object
print(InventoryMapAffiliate.to_json())

# convert the object into a dict
inventory_map_affiliate_dict = inventory_map_affiliate_instance.to_dict()
# create an instance of InventoryMapAffiliate from a dict
inventory_map_affiliate_from_dict = InventoryMapAffiliate.from_dict(inventory_map_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


