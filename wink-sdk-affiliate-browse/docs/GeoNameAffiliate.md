# GeoNameAffiliate

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoName type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) |  | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryAffiliate**](CountryAffiliate.md) |  | [optional] 
**sub_country** | [**SubCountryAffiliate**](SubCountryAffiliate.md) |  | [optional] 
**sub_sub_country** | [**SubSubCountryAffiliate**](SubSubCountryAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.geo_name_affiliate import GeoNameAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameAffiliate from a JSON string
geo_name_affiliate_instance = GeoNameAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeoNameAffiliate.to_json())

# convert the object into a dict
geo_name_affiliate_dict = geo_name_affiliate_instance.to_dict()
# create an instance of GeoNameAffiliate from a dict
geo_name_affiliate_from_dict = GeoNameAffiliate.from_dict(geo_name_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


