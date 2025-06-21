# ExtraChargesBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExtraChargeBooker]**](ExtraChargeBooker.md) | List of extra charges that applies to the rate plan. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.extra_charges_booker import ExtraChargesBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargesBooker from a JSON string
extra_charges_booker_instance = ExtraChargesBooker.from_json(json)
# print the JSON string representation of the object
print(ExtraChargesBooker.to_json())

# convert the object into a dict
extra_charges_booker_dict = extra_charges_booker_instance.to_dict()
# create an instance of ExtraChargesBooker from a dict
extra_charges_booker_from_dict = ExtraChargesBooker.from_dict(extra_charges_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


