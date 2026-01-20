# ConfigurableGeoJsonPointAffiliate

A way to persist a GeoJSON map point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | A GeoJSON point | 

## Example

```python
from wink_sdk_affiliate_inventory.models.configurable_geo_json_point_affiliate import ConfigurableGeoJsonPointAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableGeoJsonPointAffiliate from a JSON string
configurable_geo_json_point_affiliate_instance = ConfigurableGeoJsonPointAffiliate.from_json(json)
# print the JSON string representation of the object
print(ConfigurableGeoJsonPointAffiliate.to_json())

# convert the object into a dict
configurable_geo_json_point_affiliate_dict = configurable_geo_json_point_affiliate_instance.to_dict()
# create an instance of ConfigurableGeoJsonPointAffiliate from a dict
configurable_geo_json_point_affiliate_from_dict = ConfigurableGeoJsonPointAffiliate.from_dict(configurable_geo_json_point_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


