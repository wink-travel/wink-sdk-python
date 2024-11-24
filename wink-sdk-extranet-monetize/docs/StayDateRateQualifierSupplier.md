# StayDateRateQualifierSupplier

Restrict promotion to specific stay dates the user wants to arrive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | The effective (start) date of the stay date rate qualifier | 
**expire_date** | **date** | The expiration (end) date of the stay date rate qualifier | 

## Example

```python
from wink_sdk_extranet_monetize.models.stay_date_rate_qualifier_supplier import StayDateRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of StayDateRateQualifierSupplier from a JSON string
stay_date_rate_qualifier_supplier_instance = StayDateRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(StayDateRateQualifierSupplier.to_json())

# convert the object into a dict
stay_date_rate_qualifier_supplier_dict = stay_date_rate_qualifier_supplier_instance.to_dict()
# create an instance of StayDateRateQualifierSupplier from a dict
stay_date_rate_qualifier_supplier_from_dict = StayDateRateQualifierSupplier.from_dict(stay_date_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


