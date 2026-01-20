# BooleanResponseAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether call to endpoint was successful or not. | [optional] 
**message** | **str** | A message indicating more textual information. Mostly used to convey an error message. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.boolean_response_agent import BooleanResponseAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponseAgent from a JSON string
boolean_response_agent_instance = BooleanResponseAgent.from_json(json)
# print the JSON string representation of the object
print(BooleanResponseAgent.to_json())

# convert the object into a dict
boolean_response_agent_dict = boolean_response_agent_instance.to_dict()
# create an instance of BooleanResponseAgent from a dict
boolean_response_agent_from_dict = BooleanResponseAgent.from_dict(boolean_response_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


