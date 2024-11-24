# ChildBooker

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_booking.models.child_booker import ChildBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ChildBooker from a JSON string
child_booker_instance = ChildBooker.from_json(json)
# print the JSON string representation of the object
print(ChildBooker.to_json())

# convert the object into a dict
child_booker_dict = child_booker_instance.to_dict()
# create an instance of ChildBooker from a dict
child_booker_from_dict = ChildBooker.from_dict(child_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


