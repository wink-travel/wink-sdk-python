# SellDateRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | The effective (start) date of the sell date rate qualifier | 
**expire_date** | **date** | The expiration (end) date of the sell date rate qualifier | 

## Example

```python
from wink_sdk_extranet_distribution.models.sell_date_rate_qualifier_supplier_details import SellDateRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SellDateRateQualifierSupplierDetails from a JSON string
sell_date_rate_qualifier_supplier_details_instance = SellDateRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SellDateRateQualifierSupplierDetails.to_json())

# convert the object into a dict
sell_date_rate_qualifier_supplier_details_dict = sell_date_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of SellDateRateQualifierSupplierDetails from a dict
sell_date_rate_qualifier_supplier_details_from_dict = SellDateRateQualifierSupplierDetails.from_dict(sell_date_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


