# UpsertStaticListRequestAffiliate

Use this object to update the name of your curated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of curated list | 

## Example

```python
from wink_sdk_affiliate_browse.models.upsert_static_list_request_affiliate import UpsertStaticListRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertStaticListRequestAffiliate from a JSON string
upsert_static_list_request_affiliate_instance = UpsertStaticListRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertStaticListRequestAffiliate.to_json())

# convert the object into a dict
upsert_static_list_request_affiliate_dict = upsert_static_list_request_affiliate_instance.to_dict()
# create an instance of UpsertStaticListRequestAffiliate from a dict
upsert_static_list_request_affiliate_from_dict = UpsertStaticListRequestAffiliate.from_dict(upsert_static_list_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


