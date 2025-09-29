# GenericErrorMessage

Generic error message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.generic_error_message import GenericErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GenericErrorMessage from a JSON string
generic_error_message_instance = GenericErrorMessage.from_json(json)
# print the JSON string representation of the object
print(GenericErrorMessage.to_json())

# convert the object into a dict
generic_error_message_dict = generic_error_message_instance.to_dict()
# create an instance of GenericErrorMessage from a dict
generic_error_message_from_dict = GenericErrorMessage.from_dict(generic_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


