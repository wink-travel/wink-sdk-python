# UpsertSyndicatedItemAffiliate


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
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) |  | 
**og_type** | **str** | The open graph content ogType | 
**tags** | **List[str]** | Optional user categories | [optional] 
**media** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) | The main media for this entry. | [optional] 
**intelligent** | **bool** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**locale** | **str** |  | [optional] 

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


