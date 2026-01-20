# UpsertSalesChannelRequestRequestSupplier

A request for relationship between two parties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | type of relationship request | 
**supplier_identifier** | **UUID** | Specific identifier for the company / corporation / travel agency that is retrieving the rates | 
**introductory_message** | **str** | Owner / affiliate writes an intro to request a connection. | 

## Example

```python
from wink_sdk_extranet_distribution.models.upsert_sales_channel_request_request_supplier import UpsertSalesChannelRequestRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSalesChannelRequestRequestSupplier from a JSON string
upsert_sales_channel_request_request_supplier_instance = UpsertSalesChannelRequestRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertSalesChannelRequestRequestSupplier.to_json())

# convert the object into a dict
upsert_sales_channel_request_request_supplier_dict = upsert_sales_channel_request_request_supplier_instance.to_dict()
# create an instance of UpsertSalesChannelRequestRequestSupplier from a dict
upsert_sales_channel_request_request_supplier_from_dict = UpsertSalesChannelRequestRequestSupplier.from_dict(upsert_sales_channel_request_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


