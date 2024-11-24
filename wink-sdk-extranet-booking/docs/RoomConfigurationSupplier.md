# RoomConfigurationSupplier

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildSupplier]**](ChildSupplier.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.room_configuration_supplier import RoomConfigurationSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationSupplier from a JSON string
room_configuration_supplier_instance = RoomConfigurationSupplier.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationSupplier.to_json())

# convert the object into a dict
room_configuration_supplier_dict = room_configuration_supplier_instance.to_dict()
# create an instance of RoomConfigurationSupplier from a dict
room_configuration_supplier_from_dict = RoomConfigurationSupplier.from_dict(room_configuration_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


