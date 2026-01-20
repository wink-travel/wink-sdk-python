# BedroomSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedSupplierDetails]**](BedSupplierDetails.md) | A bedroom can have more than one bed type. | 

## Example

```python
from wink_sdk_extranet_booking.models.bedroom_supplier_details import BedroomSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomSupplierDetails from a JSON string
bedroom_supplier_details_instance = BedroomSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BedroomSupplierDetails.to_json())

# convert the object into a dict
bedroom_supplier_details_dict = bedroom_supplier_details_instance.to_dict()
# create an instance of BedroomSupplierDetails from a dict
bedroom_supplier_details_from_dict = BedroomSupplierDetails.from_dict(bedroom_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


