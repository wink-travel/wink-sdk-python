# BlackoutDateSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | Blackout start date. | 
**expire_date** | **date** | Blackout end date. | 

## Example

```python
from wink_sdk_extranet_distribution.models.blackout_date_supplier_details import BlackoutDateSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BlackoutDateSupplierDetails from a JSON string
blackout_date_supplier_details_instance = BlackoutDateSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BlackoutDateSupplierDetails.to_json())

# convert the object into a dict
blackout_date_supplier_details_dict = blackout_date_supplier_details_instance.to_dict()
# create an instance of BlackoutDateSupplierDetails from a dict
blackout_date_supplier_details_from_dict = BlackoutDateSupplierDetails.from_dict(blackout_date_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


