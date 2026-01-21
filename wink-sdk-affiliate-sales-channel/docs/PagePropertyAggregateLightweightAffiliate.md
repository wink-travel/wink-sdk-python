# PagePropertyAggregateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[PropertyAggregateLightweightAffiliate]**](PropertyAggregateLightweightAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.page_property_aggregate_lightweight_affiliate import PagePropertyAggregateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PagePropertyAggregateLightweightAffiliate from a JSON string
page_property_aggregate_lightweight_affiliate_instance = PagePropertyAggregateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(PagePropertyAggregateLightweightAffiliate.to_json())

# convert the object into a dict
page_property_aggregate_lightweight_affiliate_dict = page_property_aggregate_lightweight_affiliate_instance.to_dict()
# create an instance of PagePropertyAggregateLightweightAffiliate from a dict
page_property_aggregate_lightweight_affiliate_from_dict = PagePropertyAggregateLightweightAffiliate.from_dict(page_property_aggregate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


