# StaticSellerListAffiliate

A curated list is a bucket that holds any type of travel blocking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**owner_identifier** | **str** | List creator | 
**name** | **str** | Name of curated list | 
**type** | **str** | Static seller list type | 

## Example

```python
from wink_sdk_affiliate_browse.models.static_seller_list_affiliate import StaticSellerListAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSellerListAffiliate from a JSON string
static_seller_list_affiliate_instance = StaticSellerListAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticSellerListAffiliate.to_json())

# convert the object into a dict
static_seller_list_affiliate_dict = static_seller_list_affiliate_instance.to_dict()
# create an instance of StaticSellerListAffiliate from a dict
static_seller_list_affiliate_from_dict = StaticSellerListAffiliate.from_dict(static_seller_list_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


