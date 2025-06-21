# GeoJsonPointSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.geo_json_point_supplier_details import GeoJsonPointSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointSupplierDetails from a JSON string
geo_json_point_supplier_details_instance = GeoJsonPointSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointSupplierDetails.to_json())

# convert the object into a dict
geo_json_point_supplier_details_dict = geo_json_point_supplier_details_instance.to_dict()
# create an instance of GeoJsonPointSupplierDetails from a dict
geo_json_point_supplier_details_from_dict = GeoJsonPointSupplierDetails.from_dict(geo_json_point_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


