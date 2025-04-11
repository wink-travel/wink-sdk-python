# PageInventoryViewAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[InventoryViewAffiliate]**](InventoryViewAffiliate.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectAffiliate**](PageableObjectAffiliate.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.page_inventory_view_affiliate import PageInventoryViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageInventoryViewAffiliate from a JSON string
page_inventory_view_affiliate_instance = PageInventoryViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageInventoryViewAffiliate.to_json())

# convert the object into a dict
page_inventory_view_affiliate_dict = page_inventory_view_affiliate_instance.to_dict()
# create an instance of PageInventoryViewAffiliate from a dict
page_inventory_view_affiliate_from_dict = PageInventoryViewAffiliate.from_dict(page_inventory_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


