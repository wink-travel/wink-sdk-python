# SimpleDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | [optional] 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_monetize.models.simple_description import SimpleDescription

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescription from a JSON string
simple_description_instance = SimpleDescription.from_json(json)
# print the JSON string representation of the object
print(SimpleDescription.to_json())

# convert the object into a dict
simple_description_dict = simple_description_instance.to_dict()
# create an instance of SimpleDescription from a dict
simple_description_from_dict = SimpleDescription.from_dict(simple_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


