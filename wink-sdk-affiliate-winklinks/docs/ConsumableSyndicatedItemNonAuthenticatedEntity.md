# ConsumableSyndicatedItemNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | 
**owner_identifier** | **str** | Owner ID | 
**created_date** | **datetime** | Datetime this record was first created | 
**title** | **str** | The site name of this entry | 
**content_url** | **str** | The url of this entry | 
**sort** | **int** | How the author wants this entry to get sorted | 
**type** | **str** | The syndication entry type | 
**metadata** | **Dict[str, object]** | Extended metadata | [optional] 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) |  | 
**tags** | [**List[KeyValuePairNonAuthenticatedEntity]**](KeyValuePairNonAuthenticatedEntity.md) | Optional user categories | 
**multimedias** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | The main multimedias for this entry. | [optional] 
**item_display** | **str** | Item indicator for how to display itself | 
**lock_code** | **str** | Optional code the author can require be entered by the user in order to see the post. | [optional] 
**unique_id** | **str** | Optional unique code that can be used to access this record. | [optional] 
**user_tags** | **List[object]** |  | [optional] 
**hash_tags** | **List[object]** |  | [optional] 
**parent_item_display** | **str** | Settings indicator for how to display the item | 
**layout_display** | **str** | Which way to display the list when WinkLinks first loads | [optional] [default to 'LIST']
**profile_picture_geometry** | **str** | Controls how to itemDisplay profile picture | [optional] [default to 'CIRCLE']
**configuration_id** | **str** | Customization identifier | 
**client_id** | **str** | The registered user&#39;s default clientId | 

## Example

```python
from wink_sdk_affiliate_winklinks.models.consumable_syndicated_item_non_authenticated_entity import ConsumableSyndicatedItemNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumableSyndicatedItemNonAuthenticatedEntity from a JSON string
consumable_syndicated_item_non_authenticated_entity_instance = ConsumableSyndicatedItemNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConsumableSyndicatedItemNonAuthenticatedEntity.to_json())

# convert the object into a dict
consumable_syndicated_item_non_authenticated_entity_dict = consumable_syndicated_item_non_authenticated_entity_instance.to_dict()
# create an instance of ConsumableSyndicatedItemNonAuthenticatedEntity from a dict
consumable_syndicated_item_non_authenticated_entity_from_dict = ConsumableSyndicatedItemNonAuthenticatedEntity.from_dict(consumable_syndicated_item_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


