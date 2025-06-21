# SyndicatedItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | Creator of entry | 
**owner_identifier** | **str** | The user&#39;s owner company this entry associates with | 
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**status** | **str** | The syndication entry status | 
**type** | **str** | The syndication entry type | 
**image_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The image list | [optional] 
**video_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The video list | [optional] 
**audio_list** | [**List[OpenGraphMediaAffiliate]**](OpenGraphMediaAffiliate.md) | The audio list | [optional] 
**metadata** | [**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md) | Extended metadata | [optional] 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) |  | 
**og_type** | **str** | The open graph content type | [optional] 
**tags** | [**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md) | Optional user categories | [optional] 
**media** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) | The main media for this entry. | [optional] 
**intelligent** | **bool** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.syndicated_item_affiliate import SyndicatedItemAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SyndicatedItemAffiliate from a JSON string
syndicated_item_affiliate_instance = SyndicatedItemAffiliate.from_json(json)
# print the JSON string representation of the object
print(SyndicatedItemAffiliate.to_json())

# convert the object into a dict
syndicated_item_affiliate_dict = syndicated_item_affiliate_instance.to_dict()
# create an instance of SyndicatedItemAffiliate from a dict
syndicated_item_affiliate_from_dict = SyndicatedItemAffiliate.from_dict(syndicated_item_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


