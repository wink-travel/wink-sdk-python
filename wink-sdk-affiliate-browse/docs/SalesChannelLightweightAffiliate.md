# SalesChannelLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique record identifier of this segment / account | 
**supplier_identifier** | **UUID** | Channel is owned by this supplier identifier. | 
**supplier_name** | **str** | Name of property / supplier that owns this channel | 
**supplier_available** | **bool** | Flag when supplier not available. E.g. Hotel disables property | [default to True]
**sub_type** | **str** | What type of segment of channel is this. | 
**owner_identifier** | **UUID** | A specific identifier for the company / corporation / travel agency that is retrieving the rates | [optional] 
**owner_name** | **str** | Name of the owner / affiliate. &#x60;Hotel booking customization&#x60; when it&#39;s the booking customization. | [optional] 
**enabled** | **bool** | Flag the supplier can use to enable / disable this channel | [optional] [default to True]
**channel_disabled** | **bool** | System override by supplier to disable channel. E.g. Platform disables supplier. | [optional] 
**blacklisted** | **bool** | A way to blacklist a specific channel a property doesn&#39;t want to send blocking to. | 
**percent_discount** | **float** | Percent discount on this channel and all its children [unless configured at the child level]. | [optional] 
**commission** | **float** | Amount of sales commission earned through this channel and all its children [unless configured at the child level]. | [optional] 
**rate_modifiers** | [**List[SpecialRateLightweightAffiliate]**](SpecialRateLightweightAffiliate.md) | Promotions for this channel | [optional] 
**rate_modifier_bundles** | [**List[SpecialRateBundleLightweightAffiliate]**](SpecialRateBundleLightweightAffiliate.md) | Promotion bundles for this channel | [optional] 
**self_acquires** | **bool** | Whether the sales channel is a self-acquiring entity. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.sales_channel_lightweight_affiliate import SalesChannelLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelLightweightAffiliate from a JSON string
sales_channel_lightweight_affiliate_instance = SalesChannelLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(SalesChannelLightweightAffiliate.to_json())

# convert the object into a dict
sales_channel_lightweight_affiliate_dict = sales_channel_lightweight_affiliate_instance.to_dict()
# create an instance of SalesChannelLightweightAffiliate from a dict
sales_channel_lightweight_affiliate_from_dict = SalesChannelLightweightAffiliate.from_dict(sales_channel_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


