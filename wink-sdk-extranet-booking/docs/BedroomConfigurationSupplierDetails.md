# BedroomConfigurationSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomSupplierDetails]**](BedroomSupplierDetails.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_extranet_booking.models.bedroom_configuration_supplier_details import BedroomConfigurationSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationSupplierDetails from a JSON string
bedroom_configuration_supplier_details_instance = BedroomConfigurationSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationSupplierDetails.to_json())

# convert the object into a dict
bedroom_configuration_supplier_details_dict = bedroom_configuration_supplier_details_instance.to_dict()
# create an instance of BedroomConfigurationSupplierDetails from a dict
bedroom_configuration_supplier_details_from_dict = BedroomConfigurationSupplierDetails.from_dict(bedroom_configuration_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


