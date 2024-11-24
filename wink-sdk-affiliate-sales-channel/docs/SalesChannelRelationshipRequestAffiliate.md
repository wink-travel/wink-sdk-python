# SalesChannelRelationshipRequestAffiliate

A request for relationship between two parties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
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
from wink_sdk_affiliate_sales_channel.models.sales_channel_relationship_request_affiliate import SalesChannelRelationshipRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelRelationshipRequestAffiliate from a JSON string
sales_channel_relationship_request_affiliate_instance = SalesChannelRelationshipRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(SalesChannelRelationshipRequestAffiliate.to_json())

# convert the object into a dict
sales_channel_relationship_request_affiliate_dict = sales_channel_relationship_request_affiliate_instance.to_dict()
# create an instance of SalesChannelRelationshipRequestAffiliate from a dict
sales_channel_relationship_request_affiliate_from_dict = SalesChannelRelationshipRequestAffiliate.from_dict(sales_channel_relationship_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


