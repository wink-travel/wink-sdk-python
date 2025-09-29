# RegisterPropertyManually400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.register_property_manually400_response import RegisterPropertyManually400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterPropertyManually400Response from a JSON string
register_property_manually400_response_instance = RegisterPropertyManually400Response.from_json(json)
# print the JSON string representation of the object
print(RegisterPropertyManually400Response.to_json())

# convert the object into a dict
register_property_manually400_response_dict = register_property_manually400_response_instance.to_dict()
# create an instance of RegisterPropertyManually400Response from a dict
register_property_manually400_response_from_dict = RegisterPropertyManually400Response.from_dict(register_property_manually400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


