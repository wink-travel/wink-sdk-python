# SalesChannelAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
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
**rate_modifiers** | [**List[SpecialRateLightweightAffiliate]**](SpecialRateLightweightAffiliate.md) | Promotions for this channel | [optional] 
**rate_modifier_bundles** | [**List[SpecialRateBundleLightweightAffiliate]**](SpecialRateBundleLightweightAffiliate.md) | Promotion bundles for this channel | [optional] 
**self_acquires** | **bool** | Whether the sales channel is a self-acquiring entity. | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.sales_channel_affiliate import SalesChannelAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelAffiliate from a JSON string
sales_channel_affiliate_instance = SalesChannelAffiliate.from_json(json)
# print the JSON string representation of the object
print(SalesChannelAffiliate.to_json())

# convert the object into a dict
sales_channel_affiliate_dict = sales_channel_affiliate_instance.to_dict()
# create an instance of SalesChannelAffiliate from a dict
sales_channel_affiliate_from_dict = SalesChannelAffiliate.from_dict(sales_channel_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


