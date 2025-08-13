# DynamicSellerListRequestAffiliate

Paginated search for travel inventory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**UpsertDynamicSellerListRequestAffiliate**](UpsertDynamicSellerListRequestAffiliate.md) | Contains the caller&#39;s search criteria. | 
**page** | **int** | Which page to view out of total search results. | [default to 0]
**size** | **int** | How many result set to return at the time. | [default to 24]
**display_currency** | **str** | Which currency to display the prices in. | [optional] [default to 'USD']

## Example

```python
from wink_sdk_affiliate_browse.models.dynamic_seller_list_request_affiliate import DynamicSellerListRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicSellerListRequestAffiliate from a JSON string
dynamic_seller_list_request_affiliate_instance = DynamicSellerListRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(DynamicSellerListRequestAffiliate.to_json())

# convert the object into a dict
dynamic_seller_list_request_affiliate_dict = dynamic_seller_list_request_affiliate_instance.to_dict()
# create an instance of DynamicSellerListRequestAffiliate from a dict
dynamic_seller_list_request_affiliate_from_dict = DynamicSellerListRequestAffiliate.from_dict(dynamic_seller_list_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


