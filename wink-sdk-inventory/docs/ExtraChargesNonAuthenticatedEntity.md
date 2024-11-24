# ExtraChargesNonAuthenticatedEntity

Per rate plan level extra charges with localized prices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeNonAuthenticatedEntity]**](ExtraChargeNonAuthenticatedEntity.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.extra_charges_non_authenticated_entity import ExtraChargesNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesNonAuthenticatedEntity from a JSON string
extra_charges_non_authenticated_entity_instance = ExtraChargesNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesNonAuthenticatedEntity.to_json())

# convert the object into a dict
extra_charges_non_authenticated_entity_dict = extra_charges_non_authenticated_entity_instance.to_dict()
# create an instance of ExtraChargesNonAuthenticatedEntity from a dict
extra_charges_non_authenticated_entity_from_dict = ExtraChargesNonAuthenticatedEntity.from_dict(extra_charges_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


