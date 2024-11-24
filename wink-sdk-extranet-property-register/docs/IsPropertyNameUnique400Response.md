# IsPropertyNameUnique400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.is_property_name_unique400_response import IsPropertyNameUnique400Response

# TODO update the JSON string below
json = "{}"
# create an instance of IsPropertyNameUnique400Response from a JSON string
is_property_name_unique400_response_instance = IsPropertyNameUnique400Response.from_json(json)
# print the JSON string representation of the object
print(IsPropertyNameUnique400Response.to_json())

# convert the object into a dict
is_property_name_unique400_response_dict = is_property_name_unique400_response_instance.to_dict()
# create an instance of IsPropertyNameUnique400Response from a dict
is_property_name_unique400_response_from_dict = IsPropertyNameUnique400Response.from_dict(is_property_name_unique400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


