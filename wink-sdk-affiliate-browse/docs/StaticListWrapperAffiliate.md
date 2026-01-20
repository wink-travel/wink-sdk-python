# StaticListWrapperAffiliate

Contains both the curated list and all its items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**StaticListAffiliate**](StaticListAffiliate.md) | Curated list object | 
**items** | [**List[StaticListItemAffiliate]**](StaticListItemAffiliate.md) | Travel inventory items contained in list | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.static_list_wrapper_affiliate import StaticListWrapperAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticListWrapperAffiliate from a JSON string
static_list_wrapper_affiliate_instance = StaticListWrapperAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticListWrapperAffiliate.to_json())

# convert the object into a dict
static_list_wrapper_affiliate_dict = static_list_wrapper_affiliate_instance.to_dict()
# create an instance of StaticListWrapperAffiliate from a dict
static_list_wrapper_affiliate_from_dict = StaticListWrapperAffiliate.from_dict(static_list_wrapper_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


