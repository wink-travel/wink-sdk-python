# StaticListLightweightAffiliate

A curated list is a bucket that holds any type of travel inventory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**owner_identifier** | **str** | List creator | 
**name** | **str** | Name of curated list | 
**type** | **str** | Every affiliate starts out with a &#x60;Favorite&#x60; list. All other lists will be of type &#x60;NORMAL&#x60; | 

## Example

```python
from wink_sdk_affiliate_browse.models.static_list_lightweight_affiliate import StaticListLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticListLightweightAffiliate from a JSON string
static_list_lightweight_affiliate_instance = StaticListLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(StaticListLightweightAffiliate.to_json())

# convert the object into a dict
static_list_lightweight_affiliate_dict = static_list_lightweight_affiliate_instance.to_dict()
# create an instance of StaticListLightweightAffiliate from a dict
static_list_lightweight_affiliate_from_dict = StaticListLightweightAffiliate.from_dict(static_list_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


