# PageSalesChannelViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[SalesChannelViewAffiliate]**](SalesChannelViewAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.page_sales_channel_view_affiliate import PageSalesChannelViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageSalesChannelViewAffiliate from a JSON string
page_sales_channel_view_affiliate_instance = PageSalesChannelViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageSalesChannelViewAffiliate.to_json())

# convert the object into a dict
page_sales_channel_view_affiliate_dict = page_sales_channel_view_affiliate_instance.to_dict()
# create an instance of PageSalesChannelViewAffiliate from a dict
page_sales_channel_view_affiliate_from_dict = PageSalesChannelViewAffiliate.from_dict(page_sales_channel_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


