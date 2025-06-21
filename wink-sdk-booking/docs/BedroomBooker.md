# BedroomBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedBooker]**](BedBooker.md) |  | 

## Example

```python
from wink_sdk_booking.models.bedroom_booker import BedroomBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomBooker from a JSON string
bedroom_booker_instance = BedroomBooker.from_json(json)
# print the JSON string representation of the object
print(BedroomBooker.to_json())

# convert the object into a dict
bedroom_booker_dict = bedroom_booker_instance.to_dict()
# create an instance of BedroomBooker from a dict
bedroom_booker_from_dict = BedroomBooker.from_dict(bedroom_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


