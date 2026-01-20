# RoomConfigurationAffiliate

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildAffiliate]**](ChildAffiliate.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.room_configuration_affiliate import RoomConfigurationAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationAffiliate from a JSON string
room_configuration_affiliate_instance = RoomConfigurationAffiliate.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationAffiliate.to_json())

# convert the object into a dict
room_configuration_affiliate_dict = room_configuration_affiliate_instance.to_dict()
# create an instance of RoomConfigurationAffiliate from a dict
room_configuration_affiliate_from_dict = RoomConfigurationAffiliate.from_dict(room_configuration_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


