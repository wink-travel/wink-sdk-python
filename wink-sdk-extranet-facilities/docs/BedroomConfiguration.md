# BedroomConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[Bedroom]**](Bedroom.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_extranet_facilities.models.bedroom_configuration import BedroomConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfiguration from a JSON string
bedroom_configuration_instance = BedroomConfiguration.from_json(json)
# print the JSON string representation of the object
print(BedroomConfiguration.to_json())

# convert the object into a dict
bedroom_configuration_dict = bedroom_configuration_instance.to_dict()
# create an instance of BedroomConfiguration from a dict
bedroom_configuration_from_dict = BedroomConfiguration.from_dict(bedroom_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


