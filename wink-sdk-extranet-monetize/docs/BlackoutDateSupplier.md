# BlackoutDateSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | Blackout start date. | 
**expire_date** | **date** | Blackout end date. | 

## Example

```python
from wink_sdk_extranet_monetize.models.blackout_date_supplier import BlackoutDateSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDateSupplier from a JSON string
blackout_date_supplier_instance = BlackoutDateSupplier.from_json(json)
# print the JSON string representation of the object
print(BlackoutDateSupplier.to_json())

# convert the object into a dict
blackout_date_supplier_dict = blackout_date_supplier_instance.to_dict()
# create an instance of BlackoutDateSupplier from a dict
blackout_date_supplier_from_dict = BlackoutDateSupplier.from_dict(blackout_date_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


