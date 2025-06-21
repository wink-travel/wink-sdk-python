# SellableRankedListLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**owner_identifier** | **str** | AffiliateAccountLightweight identifier | 
**name** | **str** | Descriptive name of this list for seller use only | 
**customization_identifier** | **str** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Contains custom title and description of grid | 
**keywords** | **List[object]** |  | 
**status** | **str** | Status | [default to 'ACTIVE']
**lookup** | [**LookupLightweightNonAuthenticatedEntity**](LookupLightweightNonAuthenticatedEntity.md) | The destination to display ranked blocking from. | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. -1 is disabled | [optional] [default to -1]
**sort** | **str** | Determines which badge to show on the Web Component. Is also used to sort properties for search grids. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [optional] [default to 'NATIVE']

## Example

```python
from wink_sdk_inventory.models.sellable_ranked_list_lightweight_non_authenticated_entity import SellableRankedListLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableRankedListLightweightNonAuthenticatedEntity from a JSON string
sellable_ranked_list_lightweight_non_authenticated_entity_instance = SellableRankedListLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableRankedListLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_ranked_list_lightweight_non_authenticated_entity_dict = sellable_ranked_list_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of SellableRankedListLightweightNonAuthenticatedEntity from a dict
sellable_ranked_list_lightweight_non_authenticated_entity_from_dict = SellableRankedListLightweightNonAuthenticatedEntity.from_dict(sellable_ranked_list_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


