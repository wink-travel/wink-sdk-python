# SellableListLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**seller_identifier** | **UUID** | AffiliateAccount identifier | 
**name** | **str** | Descriptive name of this list for seller use only | 
**customization_identifier** | **UUID** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Contains custom title and description of grid | 
**keywords** | **List[str]** | Keywords is meta data for the grid you created that can be used for SEO purposes. | 
**status** | **str** | Status | [default to 'ACTIVE']
**list_type** | **str** | List type | 
**list_identifier** | **UUID** | Depending on the &#x60;listType&#x60;, this is either the list / search / channel inventory identifier. | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. -1 is disabled | [optional] [default to -1]
**sort** | **str** | Determines which badge to show on the Web Component. Is also used to sort properties for search grids. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_inventory.models.sellable_list_lightweight_non_authenticated_entity import SellableListLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableListLightweightNonAuthenticatedEntity from a JSON string
sellable_list_lightweight_non_authenticated_entity_instance = SellableListLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableListLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_list_lightweight_non_authenticated_entity_dict = sellable_list_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of SellableListLightweightNonAuthenticatedEntity from a dict
sellable_list_lightweight_non_authenticated_entity_from_dict = SellableListLightweightNonAuthenticatedEntity.from_dict(sellable_list_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


