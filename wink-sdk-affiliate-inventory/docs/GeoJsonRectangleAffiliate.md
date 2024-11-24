# GeoJsonRectangleAffiliate

A GeoJSON rectangle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**south_west** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | 
**north_east** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_inventory.models.geo_json_rectangle_affiliate import GeoJsonRectangleAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonRectangleAffiliate from a JSON string
geo_json_rectangle_affiliate_instance = GeoJsonRectangleAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoJsonRectangleAffiliate.to_json())

# convert the object into a dict
geo_json_rectangle_affiliate_dict = geo_json_rectangle_affiliate_instance.to_dict()
# create an instance of GeoJsonRectangleAffiliate from a dict
geo_json_rectangle_affiliate_from_dict = GeoJsonRectangleAffiliate.from_dict(geo_json_rectangle_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


