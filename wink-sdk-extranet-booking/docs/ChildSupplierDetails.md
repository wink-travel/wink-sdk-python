# ChildSupplierDetails

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_extranet_booking.models.child_supplier_details import ChildSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChildSupplierDetails from a JSON string
child_supplier_details_instance = ChildSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ChildSupplierDetails.to_json())

# convert the object into a dict
child_supplier_details_dict = child_supplier_details_instance.to_dict()
# create an instance of ChildSupplierDetails from a dict
child_supplier_details_from_dict = ChildSupplierDetails.from_dict(child_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


