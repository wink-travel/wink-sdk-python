# BedroomConfigurationBooker

Desired bedroom layout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomBooker]**](BedroomBooker.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_booking.models.bedroom_configuration_booker import BedroomConfigurationBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationBooker from a JSON string
bedroom_configuration_booker_instance = BedroomConfigurationBooker.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationBooker.to_json())

# convert the object into a dict
bedroom_configuration_booker_dict = bedroom_configuration_booker_instance.to_dict()
# create an instance of BedroomConfigurationBooker from a dict
bedroom_configuration_booker_from_dict = BedroomConfigurationBooker.from_dict(bedroom_configuration_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


