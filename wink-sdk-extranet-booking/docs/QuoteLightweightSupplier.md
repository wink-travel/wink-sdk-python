# QuoteLightweightSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_extranet_booking.models.quote_lightweight_supplier import QuoteLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLightweightSupplier from a JSON string
quote_lightweight_supplier_instance = QuoteLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(QuoteLightweightSupplier.to_json())

# convert the object into a dict
quote_lightweight_supplier_dict = quote_lightweight_supplier_instance.to_dict()
# create an instance of QuoteLightweightSupplier from a dict
quote_lightweight_supplier_from_dict = QuoteLightweightSupplier.from_dict(quote_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


