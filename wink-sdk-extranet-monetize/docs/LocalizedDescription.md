# LocalizedDescription

List of localized descriptions for this fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_monetize.models.localized_description import LocalizedDescription

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedDescription from a JSON string
localized_description_instance = LocalizedDescription.from_json(json)
# print the JSON string representation of the object
print(LocalizedDescription.to_json())

# convert the object into a dict
localized_description_dict = localized_description_instance.to_dict()
# create an instance of LocalizedDescription from a dict
localized_description_from_dict = LocalizedDescription.from_dict(localized_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


