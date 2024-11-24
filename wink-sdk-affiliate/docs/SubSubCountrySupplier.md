# SubSubCountrySupplier

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.sub_sub_country_supplier import SubSubCountrySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountrySupplier from a JSON string
sub_sub_country_supplier_instance = SubSubCountrySupplier.from_json(json)
# print the JSON string representation of the object
print(SubSubCountrySupplier.to_json())

# convert the object into a dict
sub_sub_country_supplier_dict = sub_sub_country_supplier_instance.to_dict()
# create an instance of SubSubCountrySupplier from a dict
sub_sub_country_supplier_from_dict = SubSubCountrySupplier.from_dict(sub_sub_country_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


