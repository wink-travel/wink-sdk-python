# ChangePropertyNameRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_name** | **str** | Doing business as name. | 
**legal_name** | **str** | Hotel chain name if property is part of that chain. | 
**local_name** | **str** | Name of the hotel in its local language. | 

## Example

```python
from wink_sdk_extranet_property.models.change_property_name_request_supplier import ChangePropertyNameRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePropertyNameRequestSupplier from a JSON string
change_property_name_request_supplier_instance = ChangePropertyNameRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(ChangePropertyNameRequestSupplier.to_json())

# convert the object into a dict
change_property_name_request_supplier_dict = change_property_name_request_supplier_instance.to_dict()
# create an instance of ChangePropertyNameRequestSupplier from a dict
change_property_name_request_supplier_from_dict = ChangePropertyNameRequestSupplier.from_dict(change_property_name_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


