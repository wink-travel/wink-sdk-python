# MinutesBeforeBookingStartDateRateQualifierSupplierDetails

Restrict promotion to users who want to book a room close to the date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Seconds before day of arrival occurs | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.minutes_before_booking_start_date_rate_qualifier_supplier_details import MinutesBeforeBookingStartDateRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MinutesBeforeBookingStartDateRateQualifierSupplierDetails from a JSON string
minutes_before_booking_start_date_rate_qualifier_supplier_details_instance = MinutesBeforeBookingStartDateRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(MinutesBeforeBookingStartDateRateQualifierSupplierDetails.to_json())

# convert the object into a dict
minutes_before_booking_start_date_rate_qualifier_supplier_details_dict = minutes_before_booking_start_date_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of MinutesBeforeBookingStartDateRateQualifierSupplierDetails from a dict
minutes_before_booking_start_date_rate_qualifier_supplier_details_from_dict = MinutesBeforeBookingStartDateRateQualifierSupplierDetails.from_dict(minutes_before_booking_start_date_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


