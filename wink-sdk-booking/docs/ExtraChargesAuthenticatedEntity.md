# ExtraChargesAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeAuthenticatedEntity]**](ExtraChargeAuthenticatedEntity.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.extra_charges_authenticated_entity import ExtraChargesAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesAuthenticatedEntity from a JSON string
extra_charges_authenticated_entity_instance = ExtraChargesAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesAuthenticatedEntity.to_json())

# convert the object into a dict
extra_charges_authenticated_entity_dict = extra_charges_authenticated_entity_instance.to_dict()
# create an instance of ExtraChargesAuthenticatedEntity from a dict
extra_charges_authenticated_entity_from_dict = ExtraChargesAuthenticatedEntity.from_dict(extra_charges_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


