# ExtraChargesSupplierDetails

Per rate plan level extra charges with localized prices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeSupplierDetails]**](ExtraChargeSupplierDetails.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.extra_charges_supplier_details import ExtraChargesSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesSupplierDetails from a JSON string
extra_charges_supplier_details_instance = ExtraChargesSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesSupplierDetails.to_json())

# convert the object into a dict
extra_charges_supplier_details_dict = extra_charges_supplier_details_instance.to_dict()
# create an instance of ExtraChargesSupplierDetails from a dict
extra_charges_supplier_details_from_dict = ExtraChargesSupplierDetails.from_dict(extra_charges_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


