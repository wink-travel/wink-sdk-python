# GeoNameLightweightSupplierDetails

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoNameLightweight type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointSupplierDetails**](GeoJsonPointSupplierDetails.md) | Coordinate points of the city | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryLightweightSupplierDetails**](CountryLightweightSupplierDetails.md) | Country | [optional] 
**sub_country** | [**SubCountryLightweightSupplierDetails**](SubCountryLightweightSupplierDetails.md) | Country sub division | [optional] 
**sub_sub_country** | [**SubSubCountryLightweightSupplierDetails**](SubSubCountryLightweightSupplierDetails.md) | Country sub sub division | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.geo_name_lightweight_supplier_details import GeoNameLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameLightweightSupplierDetails from a JSON string
geo_name_lightweight_supplier_details_instance = GeoNameLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GeoNameLightweightSupplierDetails.to_json())

# convert the object into a dict
geo_name_lightweight_supplier_details_dict = geo_name_lightweight_supplier_details_instance.to_dict()
# create an instance of GeoNameLightweightSupplierDetails from a dict
geo_name_lightweight_supplier_details_from_dict = GeoNameLightweightSupplierDetails.from_dict(geo_name_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


