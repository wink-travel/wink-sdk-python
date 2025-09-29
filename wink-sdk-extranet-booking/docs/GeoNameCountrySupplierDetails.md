# GeoNameCountrySupplierDetails


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
from wink_sdk_extranet_booking.models.geo_name_country_supplier_details import GeoNameCountrySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameCountrySupplierDetails from a JSON string
geo_name_country_supplier_details_instance = GeoNameCountrySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GeoNameCountrySupplierDetails.to_json())

# convert the object into a dict
geo_name_country_supplier_details_dict = geo_name_country_supplier_details_instance.to_dict()
# create an instance of GeoNameCountrySupplierDetails from a dict
geo_name_country_supplier_details_from_dict = GeoNameCountrySupplierDetails.from_dict(geo_name_country_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


