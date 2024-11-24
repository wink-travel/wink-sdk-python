# BedroomConfigurationSupplier

Desired bedroom layout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomSupplier]**](BedroomSupplier.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_extranet_booking.models.bedroom_configuration_supplier import BedroomConfigurationSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationSupplier from a JSON string
bedroom_configuration_supplier_instance = BedroomConfigurationSupplier.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationSupplier.to_json())

# convert the object into a dict
bedroom_configuration_supplier_dict = bedroom_configuration_supplier_instance.to_dict()
# create an instance of BedroomConfigurationSupplier from a dict
bedroom_configuration_supplier_from_dict = BedroomConfigurationSupplier.from_dict(bedroom_configuration_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


