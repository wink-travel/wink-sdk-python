# StaticSellerListWrapperAffiliate

Contains both the curated list and all its items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**StaticSellerListViewAffiliate**](StaticSellerListViewAffiliate.md) |  | 
**items** | [**List[StaticSellerListItemViewAffiliate]**](StaticSellerListItemViewAffiliate.md) | Travel blocking items contained in list | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.static_seller_list_wrapper_affiliate import StaticSellerListWrapperAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSellerListWrapperAffiliate from a JSON string
static_seller_list_wrapper_affiliate_instance = StaticSellerListWrapperAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticSellerListWrapperAffiliate.to_json())

# convert the object into a dict
static_seller_list_wrapper_affiliate_dict = static_seller_list_wrapper_affiliate_instance.to_dict()
# create an instance of StaticSellerListWrapperAffiliate from a dict
static_seller_list_wrapper_affiliate_from_dict = StaticSellerListWrapperAffiliate.from_dict(static_seller_list_wrapper_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


