# ChildSupplier

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_extranet_booking.models.child_supplier import ChildSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ChildSupplier from a JSON string
child_supplier_instance = ChildSupplier.from_json(json)
# print the JSON string representation of the object
print(ChildSupplier.to_json())

# convert the object into a dict
child_supplier_dict = child_supplier_instance.to_dict()
# create an instance of ChildSupplier from a dict
child_supplier_from_dict = ChildSupplier.from_dict(child_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


