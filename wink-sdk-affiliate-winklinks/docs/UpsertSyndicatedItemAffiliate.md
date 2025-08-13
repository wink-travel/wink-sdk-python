# UpsertSyndicatedItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The site name of this entry | 
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**type** | **str** | The syndication entry type | 
**metadata** | **Dict[str, object]** | Extended metadata | [optional] 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) |  | 
**tags** | [**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md) | Optional user categories | [optional] 
**multimedias** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) | The main media for this entry. | [optional] 
**display** | **str** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**disabled** | **bool** | Whether author wants to disable the post. | [optional] [default to False]
**publish_date** | **datetime** | An optional date for when this post will be displayed. | [optional] 
**publish_status** | **str** | Publish status of post. | [optional] [default to 'PUBLISHED']
**lock_code** | **str** | Optional code the author can require be entered by the user in order to see the post. | [optional] 
**unique_id** | **str** | Optional unique code that can be used to access this record. | [optional] 
**user_tags** | **List[object]** |  | [optional] 
**hash_tags** | **List[object]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.upsert_syndicated_item_affiliate import UpsertSyndicatedItemAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSyndicatedItemAffiliate from a JSON string
upsert_syndicated_item_affiliate_instance = UpsertSyndicatedItemAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSyndicatedItemAffiliate.to_json())

# convert the object into a dict
upsert_syndicated_item_affiliate_dict = upsert_syndicated_item_affiliate_instance.to_dict()
# create an instance of UpsertSyndicatedItemAffiliate from a dict
upsert_syndicated_item_affiliate_from_dict = UpsertSyndicatedItemAffiliate.from_dict(upsert_syndicated_item_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


