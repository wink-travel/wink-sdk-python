# SyndicatedItemAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **UUID** | Creator of entry | 
**owner_identifier** | **UUID** | The user&#39;s owner company this entry associates with | 
**title** | **str** | The site name of this entry | 
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**status** | **str** | This can change if it&#39;s linked to travel inventory that is no longer available. | 
**type** | **str** | The syndication entry type | 
**metadata** | **Dict[str, object]** | Extended metadata | [optional] 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Localized descriptions describing inventory. | 
**tags** | [**List[KeyValuePairAffiliate]**](KeyValuePairAffiliate.md) | Optional user categories | [optional] 
**multimedias** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) | The main multimedias for this entry. | [optional] 
**display** | **str** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**disabled** | **bool** | Whether author wants to disable the post. | [optional] [default to False]
**publish_date** | **datetime** | An optional date for when this post will be displayed. | [optional] 
**publish_status** | **str** | Publish status of post. | [optional] [default to 'PUBLISHED']
**lock_code** | **str** | Optional code the author can require be entered by the user in order to see the post. | [optional] 
**unique_id** | **str** | Optional unique code that can be used to access this record. | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**hash_tags** | **List[str]** |  | [optional] 

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


