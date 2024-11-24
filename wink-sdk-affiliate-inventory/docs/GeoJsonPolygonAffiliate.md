# GeoJsonPolygonAffiliate

A GeoJSON polygon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[PointAffiliate]**](PointAffiliate.md) |  | [optional] 
**coordinates** | [**List[GeoJsonLineStringAffiliate]**](GeoJsonLineStringAffiliate.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.geo_json_polygon_affiliate import GeoJsonPolygonAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPolygonAffiliate from a JSON string
geo_json_polygon_affiliate_instance = GeoJsonPolygonAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPolygonAffiliate.to_json())

# convert the object into a dict
geo_json_polygon_affiliate_dict = geo_json_polygon_affiliate_instance.to_dict()
# create an instance of GeoJsonPolygonAffiliate from a dict
geo_json_polygon_affiliate_from_dict = GeoJsonPolygonAffiliate.from_dict(geo_json_polygon_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


