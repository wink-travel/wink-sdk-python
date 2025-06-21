# UpsertSalesChannelRequestRequest

A request for relationship between two parties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | type of relationship request | 
**supplier_identifier** | **str** | Specific identifier for the company / corporation / travel agency that is retrieving the rates | 
**introductory_message** | **str** | Owner / affiliate writes an intro to request a connection. | 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.upsert_sales_channel_request_request import UpsertSalesChannelRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSalesChannelRequestRequest from a JSON string
upsert_sales_channel_request_request_instance = UpsertSalesChannelRequestRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertSalesChannelRequestRequest.to_json())

# convert the object into a dict
upsert_sales_channel_request_request_dict = upsert_sales_channel_request_request_instance.to_dict()
# create an instance of UpsertSalesChannelRequestRequest from a dict
upsert_sales_channel_request_request_from_dict = UpsertSalesChannelRequestRequest.from_dict(upsert_sales_channel_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


