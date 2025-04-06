# ConsumableSyndicationEntryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | 
**owner_identifier** | **str** | Owner ID | 
**created_date** | **datetime** | Datetime this record was first created | 
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**type** | **str** | The syndication entry type | 
**image_list** | [**List[OpenGraphMediaNonAuthenticatedEntity]**](OpenGraphMediaNonAuthenticatedEntity.md) | The image list | [optional] 
**video_list** | [**List[OpenGraphMediaNonAuthenticatedEntity]**](OpenGraphMediaNonAuthenticatedEntity.md) | The video list | [optional] 
**audio_list** | [**List[OpenGraphMediaNonAuthenticatedEntity]**](OpenGraphMediaNonAuthenticatedEntity.md) | The audio list | [optional] 
**metadata** | [**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md) | Extended metadata | [optional] 
**title** | **str** | The title of this entry | 
**description** | **str** | The description of this entry | 
**og_type** | **str** | The open graph content type | 
**tags** | [**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md) | Optional user categories | 
**media** | [**SimpleMultimediaNonAuthenticatedEntity**](SimpleMultimediaNonAuthenticatedEntity.md) |  | [optional] 
**intelligent** | **bool** | Settings flag for whether to infuse this entry with intelligence | 
**initial_display_type** | **str** | Which way to display the list when WinkLinks first loads | [optional] [default to 'LIST']
**profile_picture_geometry** | **str** | Controls how to display profile picture | [optional] [default to 'CIRCLE']
**configuration_id** | **str** | Customization identifier | 
**client_id** | **str** | The registered user&#39;s default clientId | 

## Example

```python
from wink_sdk_affiliate_winklinks.models.consumable_syndication_entry_non_authenticated_entity import ConsumableSyndicationEntryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumableSyndicationEntryNonAuthenticatedEntity from a JSON string
consumable_syndication_entry_non_authenticated_entity_instance = ConsumableSyndicationEntryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConsumableSyndicationEntryNonAuthenticatedEntity.to_json())

# convert the object into a dict
consumable_syndication_entry_non_authenticated_entity_dict = consumable_syndication_entry_non_authenticated_entity_instance.to_dict()
# create an instance of ConsumableSyndicationEntryNonAuthenticatedEntity from a dict
consumable_syndication_entry_non_authenticated_entity_from_dict = ConsumableSyndicationEntryNonAuthenticatedEntity.from_dict(consumable_syndication_entry_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


