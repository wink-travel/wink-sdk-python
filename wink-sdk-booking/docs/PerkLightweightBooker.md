# PerkLightweightBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Enum identifier identifier for this perk. Makes the persistent version backwards compatible. | 
**guaranteed** | **bool** | Whether perk is guaranteed or not. | [optional] 
**level** | **int** | The platform value of this perk. | [optional] 
**descriptions** | [**List[SimpleDescriptionBooker]**](SimpleDescriptionBooker.md) | Localized description for this perk | 
**sort** | **int** | This is how perks get sorted when in a list | [optional] 

## Example

```python
from wink_sdk_booking.models.perk_lightweight_booker import PerkLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PerkLightweightBooker from a JSON string
perk_lightweight_booker_instance = PerkLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(PerkLightweightBooker.to_json())

# convert the object into a dict
perk_lightweight_booker_dict = perk_lightweight_booker_instance.to_dict()
# create an instance of PerkLightweightBooker from a dict
perk_lightweight_booker_from_dict = PerkLightweightBooker.from_dict(perk_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


