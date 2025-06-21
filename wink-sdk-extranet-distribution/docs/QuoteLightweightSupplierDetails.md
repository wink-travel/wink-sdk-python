# QuoteLightweightSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from wink_sdk_extranet_distribution.models.quote_lightweight_supplier_details import QuoteLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLightweightSupplierDetails from a JSON string
quote_lightweight_supplier_details_instance = QuoteLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteLightweightSupplierDetails.to_json())

# convert the object into a dict
quote_lightweight_supplier_details_dict = quote_lightweight_supplier_details_instance.to_dict()
# create an instance of QuoteLightweightSupplierDetails from a dict
quote_lightweight_supplier_details_from_dict = QuoteLightweightSupplierDetails.from_dict(quote_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


