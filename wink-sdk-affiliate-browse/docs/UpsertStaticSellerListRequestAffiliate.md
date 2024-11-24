# UpsertStaticSellerListRequestAffiliate

Use this object to update the name of your curated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of curated list | 

## Example

```python
from wink_sdk_affiliate_browse.models.upsert_static_seller_list_request_affiliate import UpsertStaticSellerListRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertStaticSellerListRequestAffiliate from a JSON string
upsert_static_seller_list_request_affiliate_instance = UpsertStaticSellerListRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertStaticSellerListRequestAffiliate.to_json())

# convert the object into a dict
upsert_static_seller_list_request_affiliate_dict = upsert_static_seller_list_request_affiliate_instance.to_dict()
# create an instance of UpsertStaticSellerListRequestAffiliate from a dict
upsert_static_seller_list_request_affiliate_from_dict = UpsertStaticSellerListRequestAffiliate.from_dict(upsert_static_seller_list_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


