# AdvanceBookingRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_advance_booking_offset** | **int** | Minimum advance booking offset qualifier | [optional] 
**max_advance_booking_offset** | **int** | Maximum advance booking offset qualifier | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.advance_booking_rate_qualifier_supplier_details import AdvanceBookingRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceBookingRateQualifierSupplierDetails from a JSON string
advance_booking_rate_qualifier_supplier_details_instance = AdvanceBookingRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(AdvanceBookingRateQualifierSupplierDetails.to_json())

# convert the object into a dict
advance_booking_rate_qualifier_supplier_details_dict = advance_booking_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of AdvanceBookingRateQualifierSupplierDetails from a dict
advance_booking_rate_qualifier_supplier_details_from_dict = AdvanceBookingRateQualifierSupplierDetails.from_dict(advance_booking_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


