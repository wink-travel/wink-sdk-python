# PageInventoryAggregateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[InventoryAggregateLightweightAffiliate]**](InventoryAggregateLightweightAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.page_inventory_aggregate_lightweight_affiliate import PageInventoryAggregateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageInventoryAggregateLightweightAffiliate from a JSON string
page_inventory_aggregate_lightweight_affiliate_instance = PageInventoryAggregateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageInventoryAggregateLightweightAffiliate.to_json())

# convert the object into a dict
page_inventory_aggregate_lightweight_affiliate_dict = page_inventory_aggregate_lightweight_affiliate_instance.to_dict()
# create an instance of PageInventoryAggregateLightweightAffiliate from a dict
page_inventory_aggregate_lightweight_affiliate_from_dict = PageInventoryAggregateLightweightAffiliate.from_dict(page_inventory_aggregate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


