# SellDateRateQualifierSupplier

Restrict promotion to specific dates the booking is made.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | The effective (start) date of the sell date rate qualifier | 
**expire_date** | **date** | The expiration (end) date of the sell date rate qualifier | 

## Example

```python
from wink_sdk_extranet_monetize.models.sell_date_rate_qualifier_supplier import SellDateRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SellDateRateQualifierSupplier from a JSON string
sell_date_rate_qualifier_supplier_instance = SellDateRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(SellDateRateQualifierSupplier.to_json())

# convert the object into a dict
sell_date_rate_qualifier_supplier_dict = sell_date_rate_qualifier_supplier_instance.to_dict()
# create an instance of SellDateRateQualifierSupplier from a dict
sell_date_rate_qualifier_supplier_from_dict = SellDateRateQualifierSupplier.from_dict(sell_date_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


