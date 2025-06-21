# UpdateLocationRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) | New location for property. | 

## Example

```python
from wink_sdk_extranet_property.models.update_location_request_supplier import UpdateLocationRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLocationRequestSupplier from a JSON string
update_location_request_supplier_instance = UpdateLocationRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpdateLocationRequestSupplier.to_json())

# convert the object into a dict
update_location_request_supplier_dict = update_location_request_supplier_instance.to_dict()
# create an instance of UpdateLocationRequestSupplier from a dict
update_location_request_supplier_from_dict = UpdateLocationRequestSupplier.from_dict(update_location_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


