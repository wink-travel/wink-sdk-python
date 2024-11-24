# SalesChannelViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**sales_channel** | [**SalesChannelAffiliate**](SalesChannelAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.sales_channel_view_affiliate import SalesChannelViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelViewAffiliate from a JSON string
sales_channel_view_affiliate_instance = SalesChannelViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(SalesChannelViewAffiliate.to_json())

# convert the object into a dict
sales_channel_view_affiliate_dict = sales_channel_view_affiliate_instance.to_dict()
# create an instance of SalesChannelViewAffiliate from a dict
sales_channel_view_affiliate_from_dict = SalesChannelViewAffiliate.from_dict(sales_channel_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


