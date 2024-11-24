# SubSubCountrySupplierDetails

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.sub_sub_country_supplier_details import SubSubCountrySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountrySupplierDetails from a JSON string
sub_sub_country_supplier_details_instance = SubSubCountrySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SubSubCountrySupplierDetails.to_json())

# convert the object into a dict
sub_sub_country_supplier_details_dict = sub_sub_country_supplier_details_instance.to_dict()
# create an instance of SubSubCountrySupplierDetails from a dict
sub_sub_country_supplier_details_from_dict = SubSubCountrySupplierDetails.from_dict(sub_sub_country_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


