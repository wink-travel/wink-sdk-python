# PerkLightweightNonAuthenticatedEntity

Perks that accompany the master rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Enum identifier identifier for this perk. Makes the persistent version backwards compatible. | 
**guaranteed** | **bool** | Whether perk is guaranteed or not. | [optional] 
**level** | **int** | The platform value of this perk. | [optional] 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Localized description for this perk | 
**sort** | **int** | This is how perks get sorted when in a list | [optional] 

## Example

```python
from wink_sdk_inventory.models.perk_lightweight_non_authenticated_entity import PerkLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PerkLightweightNonAuthenticatedEntity from a JSON string
perk_lightweight_non_authenticated_entity_instance = PerkLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PerkLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
perk_lightweight_non_authenticated_entity_dict = perk_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of PerkLightweightNonAuthenticatedEntity from a dict
perk_lightweight_non_authenticated_entity_from_dict = PerkLightweightNonAuthenticatedEntity.from_dict(perk_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


