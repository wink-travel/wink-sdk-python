# SpecialRateBundleSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | **List[object]** |  | 
**modifier_override** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**is_valid** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionSupplier]**](LocalizedDescriptionSupplier.md) |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.special_rate_bundle_supplier import SpecialRateBundleSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialRateBundleSupplier from a JSON string
special_rate_bundle_supplier_instance = SpecialRateBundleSupplier.from_json(json)
# print the JSON string representation of the object
print(SpecialRateBundleSupplier.to_json())

# convert the object into a dict
special_rate_bundle_supplier_dict = special_rate_bundle_supplier_instance.to_dict()
# create an instance of SpecialRateBundleSupplier from a dict
special_rate_bundle_supplier_from_dict = SpecialRateBundleSupplier.from_dict(special_rate_bundle_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


