# GeoNameLightweightAffiliate

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoNameLightweight type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Coordinate points of the city | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryLightweightAffiliate**](CountryLightweightAffiliate.md) | Country | [optional] 
**sub_country** | [**SubCountryLightweightAffiliate**](SubCountryLightweightAffiliate.md) | Country sub division | [optional] 
**sub_sub_country** | [**SubSubCountryLightweightAffiliate**](SubSubCountryLightweightAffiliate.md) | Country sub sub division | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.geo_name_lightweight_affiliate import GeoNameLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameLightweightAffiliate from a JSON string
geo_name_lightweight_affiliate_instance = GeoNameLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoNameLightweightAffiliate.to_json())

# convert the object into a dict
geo_name_lightweight_affiliate_dict = geo_name_lightweight_affiliate_instance.to_dict()
# create an instance of GeoNameLightweightAffiliate from a dict
geo_name_lightweight_affiliate_from_dict = GeoNameLightweightAffiliate.from_dict(geo_name_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


