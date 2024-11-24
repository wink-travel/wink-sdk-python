# DailyRateSupplier

In case of LODGING, include daily rates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date this rate is applicable for. | 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**supplier_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**internal_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**capture_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 

## Example

```python
from wink_sdk_extranet_booking.models.daily_rate_supplier import DailyRateSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRateSupplier from a JSON string
daily_rate_supplier_instance = DailyRateSupplier.from_json(json)
# print the JSON string representation of the object
print(DailyRateSupplier.to_json())

# convert the object into a dict
daily_rate_supplier_dict = daily_rate_supplier_instance.to_dict()
# create an instance of DailyRateSupplier from a dict
daily_rate_supplier_from_dict = DailyRateSupplier.from_dict(daily_rate_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


