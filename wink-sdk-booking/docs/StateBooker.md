# StateBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorBooker]**](SortDescriptorBooker.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorBooker**](CompositeFilterDescriptorBooker.md) | Descriptors used for filtering result set | [optional] 
**group** | [**List[GroupDescriptorBooker]**](GroupDescriptorBooker.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_booking.models.state_booker import StateBooker

# TODO update the JSON string below
json = "{}"
# create an instance of StateBooker from a JSON string
state_booker_instance = StateBooker.from_json(json)
# print the JSON string representation of the object
print(StateBooker.to_json())

# convert the object into a dict
state_booker_dict = state_booker_instance.to_dict()
# create an instance of StateBooker from a dict
state_booker_from_dict = StateBooker.from_dict(state_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


