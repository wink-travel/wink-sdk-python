# ConfigurableGeoJsonCircleAffiliate

A way to persist a GeoJSON circle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **float** | Circle radius from center | 
**point** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Circle center point | 

## Example

```python
from wink_sdk_affiliate_inventory.models.configurable_geo_json_circle_affiliate import ConfigurableGeoJsonCircleAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurableGeoJsonCircleAffiliate from a JSON string
configurable_geo_json_circle_affiliate_instance = ConfigurableGeoJsonCircleAffiliate.from_json(json)
# print the JSON string representation of the object
print(ConfigurableGeoJsonCircleAffiliate.to_json())

# convert the object into a dict
configurable_geo_json_circle_affiliate_dict = configurable_geo_json_circle_affiliate_instance.to_dict()
# create an instance of ConfigurableGeoJsonCircleAffiliate from a dict
configurable_geo_json_circle_affiliate_from_dict = ConfigurableGeoJsonCircleAffiliate.from_dict(configurable_geo_json_circle_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


