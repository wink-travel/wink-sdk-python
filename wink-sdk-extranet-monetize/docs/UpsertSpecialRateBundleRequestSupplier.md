# UpsertSpecialRateBundleRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**item_identifiers** | **List[object]** |  | 
**modifier_override** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_special_rate_bundle_request_supplier import UpsertSpecialRateBundleRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSpecialRateBundleRequestSupplier from a JSON string
upsert_special_rate_bundle_request_supplier_instance = UpsertSpecialRateBundleRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertSpecialRateBundleRequestSupplier.to_json())

# convert the object into a dict
upsert_special_rate_bundle_request_supplier_dict = upsert_special_rate_bundle_request_supplier_instance.to_dict()
# create an instance of UpsertSpecialRateBundleRequestSupplier from a dict
upsert_special_rate_bundle_request_supplier_from_dict = UpsertSpecialRateBundleRequestSupplier.from_dict(upsert_special_rate_bundle_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


