# UpsertAddressRequestSupplier

Light-weight Address object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**city_geo_name_id** | **str** | City geo name ID | 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | 
**county** | **str** | County | [optional] 

## Example

```python
from wink_sdk_extranet_experiences.models.upsert_address_request_supplier import UpsertAddressRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAddressRequestSupplier from a JSON string
upsert_address_request_supplier_instance = UpsertAddressRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertAddressRequestSupplier.to_json())

# convert the object into a dict
upsert_address_request_supplier_dict = upsert_address_request_supplier_instance.to_dict()
# create an instance of UpsertAddressRequestSupplier from a dict
upsert_address_request_supplier_from_dict = UpsertAddressRequestSupplier.from_dict(upsert_address_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


