# SalesChannelRelationshipRequestSupplier

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
from wink_sdk_extranet_distribution.models.sales_channel_relationship_request_supplier import SalesChannelRelationshipRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelRelationshipRequestSupplier from a JSON string
sales_channel_relationship_request_supplier_instance = SalesChannelRelationshipRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(SalesChannelRelationshipRequestSupplier.to_json())

# convert the object into a dict
sales_channel_relationship_request_supplier_dict = sales_channel_relationship_request_supplier_instance.to_dict()
# create an instance of SalesChannelRelationshipRequestSupplier from a dict
sales_channel_relationship_request_supplier_from_dict = SalesChannelRelationshipRequestSupplier.from_dict(sales_channel_relationship_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


