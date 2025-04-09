# Social

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 

## Example

```python
from wink_sdk_extranet_experiences.models.social import Social

# TODO update the JSON string below
json = "{}"
# create an instance of Social from a JSON string
social_instance = Social.from_json(json)
# print the JSON string representation of the object
print(Social.to_json())

# convert the object into a dict
social_dict = social_instance.to_dict()
# create an instance of Social from a dict
social_from_dict = Social.from_dict(social_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


