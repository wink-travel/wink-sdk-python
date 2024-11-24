# PrepayRateQualifierSupplierDetails

Restrict promotion to either prepaid / non-prepaid rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prepay** | **bool** | Whether prepay is required or not | 

## Example

```python
from wink_sdk_extranet_distribution.models.prepay_rate_qualifier_supplier_details import PrepayRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PrepayRateQualifierSupplierDetails from a JSON string
prepay_rate_qualifier_supplier_details_instance = PrepayRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PrepayRateQualifierSupplierDetails.to_json())

# convert the object into a dict
prepay_rate_qualifier_supplier_details_dict = prepay_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of PrepayRateQualifierSupplierDetails from a dict
prepay_rate_qualifier_supplier_details_from_dict = PrepayRateQualifierSupplierDetails.from_dict(prepay_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


