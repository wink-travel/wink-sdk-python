# AddressSupplierDetails

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**city** | [**GeoNameLightweightSupplierDetails**](GeoNameLightweightSupplierDetails.md) | City geo name object | 
**valid** | **bool** | Whether this address is considered valid by the system or not | [optional] [readonly] 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_distribution.models.address_supplier_details import AddressSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSupplierDetails from a JSON string
address_supplier_details_instance = AddressSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(AddressSupplierDetails.to_json())

# convert the object into a dict
address_supplier_details_dict = address_supplier_details_instance.to_dict()
# create an instance of AddressSupplierDetails from a dict
address_supplier_details_from_dict = AddressSupplierDetails.from_dict(address_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


