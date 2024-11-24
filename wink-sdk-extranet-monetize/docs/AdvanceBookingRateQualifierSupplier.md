# AdvanceBookingRateQualifierSupplier

Restrict promotion to users who want to book in advance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_advance_booking_offset** | **int** | Minimum advance booking offset qualifier | [optional] 
**max_advance_booking_offset** | **int** | Maximum advance booking offset qualifier | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.advance_booking_rate_qualifier_supplier import AdvanceBookingRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceBookingRateQualifierSupplier from a JSON string
advance_booking_rate_qualifier_supplier_instance = AdvanceBookingRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(AdvanceBookingRateQualifierSupplier.to_json())

# convert the object into a dict
advance_booking_rate_qualifier_supplier_dict = advance_booking_rate_qualifier_supplier_instance.to_dict()
# create an instance of AdvanceBookingRateQualifierSupplier from a dict
advance_booking_rate_qualifier_supplier_from_dict = AdvanceBookingRateQualifierSupplier.from_dict(advance_booking_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


