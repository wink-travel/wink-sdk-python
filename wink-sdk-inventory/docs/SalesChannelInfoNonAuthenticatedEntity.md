# SalesChannelInfoNonAuthenticatedEntity

Sales channel that owns this booking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of sales channel | 
**channel_discount_percent** | **float** | A percent discount the property gave the sales channel. Value between 0.0 - 1.0. | [optional] [default to 0]
**commission_percent** | **float** | A percent commission the property gave the sales channel. Value between 0.0 - 1.0. | [optional] [default to 0]

## Example

```python
from wink_sdk_inventory.models.sales_channel_info_non_authenticated_entity import SalesChannelInfoNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelInfoNonAuthenticatedEntity from a JSON string
sales_channel_info_non_authenticated_entity_instance = SalesChannelInfoNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SalesChannelInfoNonAuthenticatedEntity.to_json())

# convert the object into a dict
sales_channel_info_non_authenticated_entity_dict = sales_channel_info_non_authenticated_entity_instance.to_dict()
# create an instance of SalesChannelInfoNonAuthenticatedEntity from a dict
sales_channel_info_non_authenticated_entity_from_dict = SalesChannelInfoNonAuthenticatedEntity.from_dict(sales_channel_info_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


