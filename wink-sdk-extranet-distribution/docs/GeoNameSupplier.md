# GeoNameSupplier

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoName type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) |  | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountrySupplier**](CountrySupplier.md) |  | [optional] 
**sub_country** | [**SubCountrySupplier**](SubCountrySupplier.md) |  | [optional] 
**sub_sub_country** | [**SubSubCountrySupplier**](SubSubCountrySupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.geo_name_supplier import GeoNameSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameSupplier from a JSON string
geo_name_supplier_instance = GeoNameSupplier.from_json(json)
# print the JSON string representation of the object
print(GeoNameSupplier.to_json())

# convert the object into a dict
geo_name_supplier_dict = geo_name_supplier_instance.to_dict()
# create an instance of GeoNameSupplier from a dict
geo_name_supplier_from_dict = GeoNameSupplier.from_dict(geo_name_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


