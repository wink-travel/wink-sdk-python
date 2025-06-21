# RoomConfigurationSupplierDetails

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[ChildSupplierDetails]**](ChildSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.room_configuration_supplier_details import RoomConfigurationSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationSupplierDetails from a JSON string
room_configuration_supplier_details_instance = RoomConfigurationSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationSupplierDetails.to_json())

# convert the object into a dict
room_configuration_supplier_details_dict = room_configuration_supplier_details_instance.to_dict()
# create an instance of RoomConfigurationSupplierDetails from a dict
room_configuration_supplier_details_from_dict = RoomConfigurationSupplierDetails.from_dict(room_configuration_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


