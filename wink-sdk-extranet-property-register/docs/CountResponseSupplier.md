# CountResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if count query worked. | 
**count** | **int** | Number of reviews for this property. | 

## Example

```python
from wink_sdk_extranet_property_register.models.count_response_supplier import CountResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CountResponseSupplier from a JSON string
count_response_supplier_instance = CountResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(CountResponseSupplier.to_json())

# convert the object into a dict
count_response_supplier_dict = count_response_supplier_instance.to_dict()
# create an instance of CountResponseSupplier from a dict
count_response_supplier_from_dict = CountResponseSupplier.from_dict(count_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


