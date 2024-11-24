# ConfigurableGeoJsonPolygonAffiliate

A way to persist a GeoJSON polygon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polygon** | [**GeoJsonPolygonAffiliate**](GeoJsonPolygonAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_inventory.models.configurable_geo_json_polygon_affiliate import ConfigurableGeoJsonPolygonAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableGeoJsonPolygonAffiliate from a JSON string
configurable_geo_json_polygon_affiliate_instance = ConfigurableGeoJsonPolygonAffiliate.from_json(json)
# print the JSON string representation of the object
print(ConfigurableGeoJsonPolygonAffiliate.to_json())

# convert the object into a dict
configurable_geo_json_polygon_affiliate_dict = configurable_geo_json_polygon_affiliate_instance.to_dict()
# create an instance of ConfigurableGeoJsonPolygonAffiliate from a dict
configurable_geo_json_polygon_affiliate_from_dict = ConfigurableGeoJsonPolygonAffiliate.from_dict(configurable_geo_json_polygon_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


