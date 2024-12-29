# QuoteSupplierDetails

FX quote for this transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_extranet_booking.models.quote_supplier_details import QuoteSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSupplierDetails from a JSON string
quote_supplier_details_instance = QuoteSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteSupplierDetails.to_json())

# convert the object into a dict
quote_supplier_details_dict = quote_supplier_details_instance.to_dict()
# create an instance of QuoteSupplierDetails from a dict
quote_supplier_details_from_dict = QuoteSupplierDetails.from_dict(quote_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


