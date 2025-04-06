# SimpleDescriptionBooker

Localized description for this perk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | [optional] 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_booking.models.simple_description_booker import SimpleDescriptionBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionBooker from a JSON string
simple_description_booker_instance = SimpleDescriptionBooker.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionBooker.to_json())

# convert the object into a dict
simple_description_booker_dict = simple_description_booker_instance.to_dict()
# create an instance of SimpleDescriptionBooker from a dict
simple_description_booker_from_dict = SimpleDescriptionBooker.from_dict(simple_description_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


