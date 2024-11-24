# PropertyWithRoomRateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**ModelProperty**](ModelProperty.md) |  | 
**list** | [**List[PropertyRoomRate]**](PropertyRoomRate.md) |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.property_with_room_rate_list import PropertyWithRoomRateList

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyWithRoomRateList from a JSON string
property_with_room_rate_list_instance = PropertyWithRoomRateList.from_json(json)
# print the JSON string representation of the object
print(PropertyWithRoomRateList.to_json())

# convert the object into a dict
property_with_room_rate_list_dict = property_with_room_rate_list_instance.to_dict()
# create an instance of PropertyWithRoomRateList from a dict
property_with_room_rate_list_from_dict = PropertyWithRoomRateList.from_dict(property_with_room_rate_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


