# RateModifierBundleAffiliate

Promotion bundles for this channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | [**List[RateModifierAffiliate]**](RateModifierAffiliate.md) |  | 
**modifier_override** | **object** |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionAffiliate]**](LocalizedDescriptionAffiliate.md) |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.rate_modifier_bundle_affiliate import RateModifierBundleAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of RateModifierBundleAffiliate from a JSON string
rate_modifier_bundle_affiliate_instance = RateModifierBundleAffiliate.from_json(json)
# print the JSON string representation of the object
print(RateModifierBundleAffiliate.to_json())

# convert the object into a dict
rate_modifier_bundle_affiliate_dict = rate_modifier_bundle_affiliate_instance.to_dict()
# create an instance of RateModifierBundleAffiliate from a dict
rate_modifier_bundle_affiliate_from_dict = RateModifierBundleAffiliate.from_dict(rate_modifier_bundle_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


