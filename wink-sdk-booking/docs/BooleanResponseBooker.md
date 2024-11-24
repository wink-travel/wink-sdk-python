# BooleanResponseBooker

Boolean response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether call to endpoint was successful or not. | [optional] 
**message** | **str** | A message indicating more textual information. Mostly used to convey an error message. | [optional] 

## Example

```python
from wink_sdk_booking.models.boolean_response_booker import BooleanResponseBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponseBooker from a JSON string
boolean_response_booker_instance = BooleanResponseBooker.from_json(json)
# print the JSON string representation of the object
print(BooleanResponseBooker.to_json())

# convert the object into a dict
boolean_response_booker_dict = boolean_response_booker_instance.to_dict()
# create an instance of BooleanResponseBooker from a dict
boolean_response_booker_from_dict = BooleanResponseBooker.from_dict(boolean_response_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


