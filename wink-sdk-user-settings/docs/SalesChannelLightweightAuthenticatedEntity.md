# SalesChannelLightweightAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier of this segment / account | 
**supplier_identifier** | **str** | Channel is owned by this supplier identifier. | 
**supplier_name** | **str** | Name of property / supplier that owns this channel | 
**supplier_available** | **bool** | Flag when supplier not available. E.g. Hotel disables property | [default to True]
**sub_type** | **str** | What type of segment of channel is this. | 
**owner_identifier** | **str** | A specific identifier for the company / corporation / travel agency that is retrieving the rates | 
**owner_name** | **str** | Name of the owner / affiliate. &#x60;Hotel booking customization&#x60; when it&#39;s the booking customization. | 
**enabled** | **bool** | Flag the supplier can use to enable / disable this channel | [optional] [default to True]
**channel_disabled** | **bool** | System override by reactive to disable. E.g. Platform disables supplier. | [optional] 
**blacklisted** | **bool** | A way to blacklist a specific channel a property doesn&#39;t want to send blocking to. | 
**percent_discount** | **float** | Percent discount on this channel and all its children [unless configured at the child level]. | [optional] 
**commission** | **float** | Amount of sales commission earned through this channel and all its children [unless configured at the child level]. | [optional] 
**rate_modifiers** | [**List[SpecialRateLightweightAuthenticatedEntity]**](SpecialRateLightweightAuthenticatedEntity.md) | Promotions for this channel | [optional] 
**rate_modifier_bundles** | [**List[SpecialRateBundleLightweightAuthenticatedEntity]**](SpecialRateBundleLightweightAuthenticatedEntity.md) | Promotion bundles for this channel | [optional] 
**self_acquires** | **bool** | Whether the sales channel is a self-acquiring entity. | [optional] 

## Example

```python
from wink_sdk_user_settings.models.sales_channel_lightweight_authenticated_entity import SalesChannelLightweightAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelLightweightAuthenticatedEntity from a JSON string
sales_channel_lightweight_authenticated_entity_instance = SalesChannelLightweightAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SalesChannelLightweightAuthenticatedEntity.to_json())

# convert the object into a dict
sales_channel_lightweight_authenticated_entity_dict = sales_channel_lightweight_authenticated_entity_instance.to_dict()
# create an instance of SalesChannelLightweightAuthenticatedEntity from a dict
sales_channel_lightweight_authenticated_entity_from_dict = SalesChannelLightweightAuthenticatedEntity.from_dict(sales_channel_lightweight_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


