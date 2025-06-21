# SalesChannelRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**status** | **str** | status of relationship request | 
**request_type** | **str** | type of relationship request | 
**supplier_identifier** | **str** | Request goes to this supplier identifier. | 
**supplier_name** | **str** | Request goes to this supplier name. | 
**sub_type** | **str** | What type of segment of channel is this. | 
**owner_identifier** | **str** | Specific identifier for the company / corporation / travel agency that is retrieving the rates | 
**owner_name** | **str** | Name of the owner / affiliate. | 
**introductory_message** | **str** | Owner / affiliate writes an intro to request a connection. | 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.sales_channel_request_affiliate import SalesChannelRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelRequestAffiliate from a JSON string
sales_channel_request_affiliate_instance = SalesChannelRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(SalesChannelRequestAffiliate.to_json())

# convert the object into a dict
sales_channel_request_affiliate_dict = sales_channel_request_affiliate_instance.to_dict()
# create an instance of SalesChannelRequestAffiliate from a dict
sales_channel_request_affiliate_from_dict = SalesChannelRequestAffiliate.from_dict(sales_channel_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


