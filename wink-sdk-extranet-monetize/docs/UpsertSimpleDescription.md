# UpsertSimpleDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_simple_description import UpsertSimpleDescription

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSimpleDescription from a JSON string
upsert_simple_description_instance = UpsertSimpleDescription.from_json(json)
# print the JSON string representation of the object
print(UpsertSimpleDescription.to_json())

# convert the object into a dict
upsert_simple_description_dict = upsert_simple_description_instance.to_dict()
# create an instance of UpsertSimpleDescription from a dict
upsert_simple_description_from_dict = UpsertSimpleDescription.from_dict(upsert_simple_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


