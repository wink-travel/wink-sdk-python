# PerkLightweightSupplier

The perks associated with this master rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Enum identifier identifier for this perk. Makes the persistent version backwards compatible. | 
**guaranteed** | **bool** | Whether perk is guaranteed or not. | [optional] 
**level** | **int** | The platform value of this perk. | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) | Localized description for this perk | 
**sort** | **int** | This is how perks get sorted when in a list | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.perk_lightweight_supplier import PerkLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PerkLightweightSupplier from a JSON string
perk_lightweight_supplier_instance = PerkLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(PerkLightweightSupplier.to_json())

# convert the object into a dict
perk_lightweight_supplier_dict = perk_lightweight_supplier_instance.to_dict()
# create an instance of PerkLightweightSupplier from a dict
perk_lightweight_supplier_from_dict = PerkLightweightSupplier.from_dict(perk_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


