# BooleanResponseAffiliate

Boolean response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether call to endpoint was successful or not. | [optional] 
**message** | **str** | A message indicating more textual information. Mostly used to convey an error message. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.boolean_response_affiliate import BooleanResponseAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponseAffiliate from a JSON string
boolean_response_affiliate_instance = BooleanResponseAffiliate.from_json(json)
# print the JSON string representation of the object
print(BooleanResponseAffiliate.to_json())

# convert the object into a dict
boolean_response_affiliate_dict = boolean_response_affiliate_instance.to_dict()
# create an instance of BooleanResponseAffiliate from a dict
boolean_response_affiliate_from_dict = BooleanResponseAffiliate.from_dict(boolean_response_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


