# GeoJsonLineStringAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[PointAffiliate]**](PointAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.geo_json_line_string_affiliate import GeoJsonLineStringAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonLineStringAffiliate from a JSON string
geo_json_line_string_affiliate_instance = GeoJsonLineStringAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoJsonLineStringAffiliate.to_json())

# convert the object into a dict
geo_json_line_string_affiliate_dict = geo_json_line_string_affiliate_instance.to_dict()
# create an instance of GeoJsonLineStringAffiliate from a dict
geo_json_line_string_affiliate_from_dict = GeoJsonLineStringAffiliate.from_dict(geo_json_line_string_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


