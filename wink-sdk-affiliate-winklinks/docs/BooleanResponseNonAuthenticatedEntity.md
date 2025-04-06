# BooleanResponseNonAuthenticatedEntity

Boolean response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether call to endpoint was successful or not. | [optional] 
**message** | **str** | A message indicating more textual information. Mostly used to convey an error message. | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.boolean_response_non_authenticated_entity import BooleanResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponseNonAuthenticatedEntity from a JSON string
boolean_response_non_authenticated_entity_instance = BooleanResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BooleanResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
boolean_response_non_authenticated_entity_dict = boolean_response_non_authenticated_entity_instance.to_dict()
# create an instance of BooleanResponseNonAuthenticatedEntity from a dict
boolean_response_non_authenticated_entity_from_dict = BooleanResponseNonAuthenticatedEntity.from_dict(boolean_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


