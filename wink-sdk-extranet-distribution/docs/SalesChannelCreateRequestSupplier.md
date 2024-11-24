# SalesChannelCreateRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_identifier** | **str** | Owner identifier, in this context, is the unique company record identifier. | 
**supplier_identifier** | **str** | Supplier identifier is the entity that owns the ivnentory. | 

## Example

```python
from wink_sdk_extranet_distribution.models.sales_channel_create_request_supplier import SalesChannelCreateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelCreateRequestSupplier from a JSON string
sales_channel_create_request_supplier_instance = SalesChannelCreateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(SalesChannelCreateRequestSupplier.to_json())

# convert the object into a dict
sales_channel_create_request_supplier_dict = sales_channel_create_request_supplier_instance.to_dict()
# create an instance of SalesChannelCreateRequestSupplier from a dict
sales_channel_create_request_supplier_from_dict = SalesChannelCreateRequestSupplier.from_dict(sales_channel_create_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


