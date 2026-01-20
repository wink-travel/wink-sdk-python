# BooleanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether call to endpoint was successful or not. | [optional] 
**message** | **str** | A message indicating more textual information. Mostly used to convey an error message. | [optional] 

## Example

```python
from wink_sdk_user_settings.models.boolean_response import BooleanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponse from a JSON string
boolean_response_instance = BooleanResponse.from_json(json)
# print the JSON string representation of the object
print(BooleanResponse.to_json())

# convert the object into a dict
boolean_response_dict = boolean_response_instance.to_dict()
# create an instance of BooleanResponse from a dict
boolean_response_from_dict = BooleanResponse.from_dict(boolean_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


