# ExtraChargesSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeSupplier]**](ExtraChargeSupplier.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.extra_charges_supplier import ExtraChargesSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesSupplier from a JSON string
extra_charges_supplier_instance = ExtraChargesSupplier.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesSupplier.to_json())

# convert the object into a dict
extra_charges_supplier_dict = extra_charges_supplier_instance.to_dict()
# create an instance of ExtraChargesSupplier from a dict
extra_charges_supplier_from_dict = ExtraChargesSupplier.from_dict(extra_charges_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


