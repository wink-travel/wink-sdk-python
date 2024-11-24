# RoomRangeRateQualifierSupplier

Restrict promotion by restricting to how many rooms the user wants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_rooms** | **int** | Minimum number of rooms | 
**max_rooms** | **int** | Maximum number of rooms | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.room_range_rate_qualifier_supplier import RoomRangeRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RoomRangeRateQualifierSupplier from a JSON string
room_range_rate_qualifier_supplier_instance = RoomRangeRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(RoomRangeRateQualifierSupplier.to_json())

# convert the object into a dict
room_range_rate_qualifier_supplier_dict = room_range_rate_qualifier_supplier_instance.to_dict()
# create an instance of RoomRangeRateQualifierSupplier from a dict
room_range_rate_qualifier_supplier_from_dict = RoomRangeRateQualifierSupplier.from_dict(room_range_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


