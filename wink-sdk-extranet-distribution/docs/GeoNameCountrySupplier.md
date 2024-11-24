# GeoNameCountrySupplier

country to restrict on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**continent_name** | **str** |  | [optional] 
**country_iso_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.geo_name_country_supplier import GeoNameCountrySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameCountrySupplier from a JSON string
geo_name_country_supplier_instance = GeoNameCountrySupplier.from_json(json)
# print the JSON string representation of the object
print(GeoNameCountrySupplier.to_json())

# convert the object into a dict
geo_name_country_supplier_dict = geo_name_country_supplier_instance.to_dict()
# create an instance of GeoNameCountrySupplier from a dict
geo_name_country_supplier_from_dict = GeoNameCountrySupplier.from_dict(geo_name_country_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


