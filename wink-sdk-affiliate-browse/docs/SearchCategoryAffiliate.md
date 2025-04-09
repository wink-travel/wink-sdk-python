# SearchCategoryAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of search category. | 
**key** | **str** | Usually the OTA inventory code. | 
**value** | **str** | Usually the OTA inventory code value. | 
**count** | **int** | Quantity of items in this category. | [optional] 
**identifier** | **str** | UUID. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.search_category_affiliate import SearchCategoryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCategoryAffiliate from a JSON string
search_category_affiliate_instance = SearchCategoryAffiliate.from_json(json)
# print the JSON string representation of the object
print(SearchCategoryAffiliate.to_json())

# convert the object into a dict
search_category_affiliate_dict = search_category_affiliate_instance.to_dict()
# create an instance of SearchCategoryAffiliate from a dict
search_category_affiliate_from_dict = SearchCategoryAffiliate.from_dict(search_category_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


