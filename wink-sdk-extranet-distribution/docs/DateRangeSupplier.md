# DateRangeSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Retrieve data range starting with and including this start date | 
**end_date** | **date** | Retrieve data range ending with and including this end date | 

## Example

```python
from wink_sdk_extranet_distribution.models.date_range_supplier import DateRangeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeSupplier from a JSON string
date_range_supplier_instance = DateRangeSupplier.from_json(json)
# print the JSON string representation of the object
print(DateRangeSupplier.to_json())

# convert the object into a dict
date_range_supplier_dict = date_range_supplier_instance.to_dict()
# create an instance of DateRangeSupplier from a dict
date_range_supplier_from_dict = DateRangeSupplier.from_dict(date_range_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


