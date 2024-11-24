# RateModifierBundleAuthenticatedEntity

Promotion bundles for this channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | [**List[RateModifierAuthenticatedEntity]**](RateModifierAuthenticatedEntity.md) |  | 
**modifier_override** | **object** |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionAuthenticatedEntity]**](LocalizedDescriptionAuthenticatedEntity.md) |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_user_settings.models.rate_modifier_bundle_authenticated_entity import RateModifierBundleAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RateModifierBundleAuthenticatedEntity from a JSON string
rate_modifier_bundle_authenticated_entity_instance = RateModifierBundleAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RateModifierBundleAuthenticatedEntity.to_json())

# convert the object into a dict
rate_modifier_bundle_authenticated_entity_dict = rate_modifier_bundle_authenticated_entity_instance.to_dict()
# create an instance of RateModifierBundleAuthenticatedEntity from a dict
rate_modifier_bundle_authenticated_entity_from_dict = RateModifierBundleAuthenticatedEntity.from_dict(rate_modifier_bundle_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


