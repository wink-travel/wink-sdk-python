# PageSalesChannelAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[SalesChannelAffiliate]**](SalesChannelAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.page_sales_channel_affiliate import PageSalesChannelAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageSalesChannelAffiliate from a JSON string
page_sales_channel_affiliate_instance = PageSalesChannelAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageSalesChannelAffiliate.to_json())

# convert the object into a dict
page_sales_channel_affiliate_dict = page_sales_channel_affiliate_instance.to_dict()
# create an instance of PageSalesChannelAffiliate from a dict
page_sales_channel_affiliate_from_dict = PageSalesChannelAffiliate.from_dict(page_sales_channel_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


