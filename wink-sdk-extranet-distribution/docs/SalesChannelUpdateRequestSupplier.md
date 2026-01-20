# SalesChannelUpdateRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag the supplier can use to enable / disable a sales channel | [default to True]
**blacklisted** | **bool** | Flag the supplier can use to ignore a sales channel | [default to True]
**percent_discount** | **float** | Percent discount on this channel and all its children [unless configured at the child level]. | 
**commission** | **float** | Amount of sales commission earned through this channel and all its children [unless configured at the child level]. | 
**rate_modifier_identifiers** | **List[UUID]** |  | [optional] 
**rate_modifier_bundle_identifiers** | **List[UUID]** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.sales_channel_update_request_supplier import SalesChannelUpdateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelUpdateRequestSupplier from a JSON string
sales_channel_update_request_supplier_instance = SalesChannelUpdateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(SalesChannelUpdateRequestSupplier.to_json())

# convert the object into a dict
sales_channel_update_request_supplier_dict = sales_channel_update_request_supplier_instance.to_dict()
# create an instance of SalesChannelUpdateRequestSupplier from a dict
sales_channel_update_request_supplier_from_dict = SalesChannelUpdateRequestSupplier.from_dict(sales_channel_update_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


