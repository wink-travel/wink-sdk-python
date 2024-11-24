# GeoJsonPointSupplier

Coordinate points of the city

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.geo_json_point_supplier import GeoJsonPointSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointSupplier from a JSON string
geo_json_point_supplier_instance = GeoJsonPointSupplier.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointSupplier.to_json())

# convert the object into a dict
geo_json_point_supplier_dict = geo_json_point_supplier_instance.to_dict()
# create an instance of GeoJsonPointSupplier from a dict
geo_json_point_supplier_from_dict = GeoJsonPointSupplier.from_dict(geo_json_point_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


