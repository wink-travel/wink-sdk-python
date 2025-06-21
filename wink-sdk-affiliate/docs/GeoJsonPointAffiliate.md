# GeoJsonPointAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.geo_json_point_affiliate import GeoJsonPointAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointAffiliate from a JSON string
geo_json_point_affiliate_instance = GeoJsonPointAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointAffiliate.to_json())

# convert the object into a dict
geo_json_point_affiliate_dict = geo_json_point_affiliate_instance.to_dict()
# create an instance of GeoJsonPointAffiliate from a dict
geo_json_point_affiliate_from_dict = GeoJsonPointAffiliate.from_dict(geo_json_point_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


