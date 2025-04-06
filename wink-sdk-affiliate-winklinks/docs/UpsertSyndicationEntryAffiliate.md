# UpsertSyndicationEntryAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**type** | **str** | The syndication entry type | 
**image_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The image list | [optional] 
**video_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The video list | [optional] 
**audio_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The audio list | [optional] 
**metadata** | [**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md) | Extended metadata | [optional] 
**title** | **str** | The title of this entry | [optional] 
**description** | **str** | The description of this entry | [optional] 
**og_type** | **str** | The open graph content ogType | 
**tags** | **List[str]** | Optional user categories | [optional] 
**media** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) |  | [optional] 
**intelligent** | **bool** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.upsert_syndication_entry_affiliate import UpsertSyndicationEntryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSyndicationEntryAffiliate from a JSON string
upsert_syndication_entry_affiliate_instance = UpsertSyndicationEntryAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSyndicationEntryAffiliate.to_json())

# convert the object into a dict
upsert_syndication_entry_affiliate_dict = upsert_syndication_entry_affiliate_instance.to_dict()
# create an instance of UpsertSyndicationEntryAffiliate from a dict
upsert_syndication_entry_affiliate_from_dict = UpsertSyndicationEntryAffiliate.from_dict(upsert_syndication_entry_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


