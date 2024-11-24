# QuoteSupplier

The quote used to create totalCapturePrice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_extranet_booking.models.quote_supplier import QuoteSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSupplier from a JSON string
quote_supplier_instance = QuoteSupplier.from_json(json)
# print the JSON string representation of the object
print(QuoteSupplier.to_json())

# convert the object into a dict
quote_supplier_dict = quote_supplier_instance.to_dict()
# create an instance of QuoteSupplier from a dict
quote_supplier_from_dict = QuoteSupplier.from_dict(quote_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


