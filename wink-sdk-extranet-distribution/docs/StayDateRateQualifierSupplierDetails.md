# StayDateRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | The effective (start) date of the stay date rate qualifier | 
**expire_date** | **date** | The expiration (end) date of the stay date rate qualifier | 

## Example

```python
from wink_sdk_extranet_distribution.models.stay_date_rate_qualifier_supplier_details import StayDateRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StayDateRateQualifierSupplierDetails from a JSON string
stay_date_rate_qualifier_supplier_details_instance = StayDateRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(StayDateRateQualifierSupplierDetails.to_json())

# convert the object into a dict
stay_date_rate_qualifier_supplier_details_dict = stay_date_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of StayDateRateQualifierSupplierDetails from a dict
stay_date_rate_qualifier_supplier_details_from_dict = StayDateRateQualifierSupplierDetails.from_dict(stay_date_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


