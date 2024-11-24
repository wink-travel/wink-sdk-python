# PropertyRoomRateWithRateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**PropertyRoomRate**](PropertyRoomRate.md) |  | 
**rates** | [**List[PropertyRate]**](PropertyRate.md) |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.property_room_rate_with_rate_list import PropertyRoomRateWithRateList

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRoomRateWithRateList from a JSON string
property_room_rate_with_rate_list_instance = PropertyRoomRateWithRateList.from_json(json)
# print the JSON string representation of the object
print(PropertyRoomRateWithRateList.to_json())

# convert the object into a dict
property_room_rate_with_rate_list_dict = property_room_rate_with_rate_list_instance.to_dict()
# create an instance of PropertyRoomRateWithRateList from a dict
property_room_rate_with_rate_list_from_dict = PropertyRoomRateWithRateList.from_dict(property_room_rate_with_rate_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


