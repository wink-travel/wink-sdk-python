# PageableObjectAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**sort** | [**SortObjectAffiliate**](SortObjectAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.pageable_object_affiliate import PageableObjectAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectAffiliate from a JSON string
pageable_object_affiliate_instance = PageableObjectAffiliate.from_json(json)
# print the JSON string representation of the object
print(PageableObjectAffiliate.to_json())

# convert the object into a dict
pageable_object_affiliate_dict = pageable_object_affiliate_instance.to_dict()
# create an instance of PageableObjectAffiliate from a dict
pageable_object_affiliate_from_dict = PageableObjectAffiliate.from_dict(pageable_object_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


