# UpsertSalesChannelRelationshipRequestRequest

A request for relationship between two parties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | type of relationship request | 
**supplier_identifier** | **str** | Specific identifier for the company / corporation / travel agency that is retrieving the rates | 
**introductory_message** | **str** | Owner / affiliate writes an intro to request a connection. | 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.upsert_sales_channel_relationship_request_request import UpsertSalesChannelRelationshipRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSalesChannelRelationshipRequestRequest from a JSON string
upsert_sales_channel_relationship_request_request_instance = UpsertSalesChannelRelationshipRequestRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertSalesChannelRelationshipRequestRequest.to_json())

# convert the object into a dict
upsert_sales_channel_relationship_request_request_dict = upsert_sales_channel_relationship_request_request_instance.to_dict()
# create an instance of UpsertSalesChannelRelationshipRequestRequest from a dict
upsert_sales_channel_relationship_request_request_from_dict = UpsertSalesChannelRelationshipRequestRequest.from_dict(upsert_sales_channel_relationship_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


