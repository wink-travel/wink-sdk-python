# PageableObjectBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**sort** | [**SortObjectBooker**](SortObjectBooker.md) |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.pageable_object_booker import PageableObjectBooker

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectBooker from a JSON string
pageable_object_booker_instance = PageableObjectBooker.from_json(json)
# print the JSON string representation of the object
print(PageableObjectBooker.to_json())

# convert the object into a dict
pageable_object_booker_dict = pageable_object_booker_instance.to_dict()
# create an instance of PageableObjectBooker from a dict
pageable_object_booker_from_dict = PageableObjectBooker.from_dict(pageable_object_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


