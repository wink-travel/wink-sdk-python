# CompositeFilterDescriptorBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorBooker]**](FilterDescriptorBooker.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_booking.models.composite_filter_descriptor_booker import CompositeFilterDescriptorBooker

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorBooker from a JSON string
composite_filter_descriptor_booker_instance = CompositeFilterDescriptorBooker.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorBooker.to_json())

# convert the object into a dict
composite_filter_descriptor_booker_dict = composite_filter_descriptor_booker_instance.to_dict()
# create an instance of CompositeFilterDescriptorBooker from a dict
composite_filter_descriptor_booker_from_dict = CompositeFilterDescriptorBooker.from_dict(composite_filter_descriptor_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


