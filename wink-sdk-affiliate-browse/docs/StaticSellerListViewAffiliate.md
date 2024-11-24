# StaticSellerListViewAffiliate

Curated list object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**static_seller_list** | [**StaticSellerListAffiliate**](StaticSellerListAffiliate.md) |  | 

## Example

```python
from wink_sdk_affiliate_browse.models.static_seller_list_view_affiliate import StaticSellerListViewAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSellerListViewAffiliate from a JSON string
static_seller_list_view_affiliate_instance = StaticSellerListViewAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticSellerListViewAffiliate.to_json())

# convert the object into a dict
static_seller_list_view_affiliate_dict = static_seller_list_view_affiliate_instance.to_dict()
# create an instance of StaticSellerListViewAffiliate from a dict
static_seller_list_view_affiliate_from_dict = StaticSellerListViewAffiliate.from_dict(static_seller_list_view_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


