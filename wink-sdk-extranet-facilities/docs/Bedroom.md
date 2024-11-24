# Bedroom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[Bed]**](Bed.md) | A bedroom can have more than one bed type. | 

## Example

```python
from wink_sdk_extranet_facilities.models.bedroom import Bedroom

# TODO update the JSON string below
json = "{}"
# create an instance of Bedroom from a JSON string
bedroom_instance = Bedroom.from_json(json)
# print the JSON string representation of the object
print(Bedroom.to_json())

# convert the object into a dict
bedroom_dict = bedroom_instance.to_dict()
# create an instance of Bedroom from a dict
bedroom_from_dict = Bedroom.from_dict(bedroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


