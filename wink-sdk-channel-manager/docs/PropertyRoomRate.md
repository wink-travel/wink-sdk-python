# PropertyRoomRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**property_identifier** | **str** |  | 
**name** | **str** |  | 
**room_type_identifier** | **str** |  | 
**rate_plan_identifier** | **str** |  | 
**guest_room_name** | **str** |  | 
**rate_plan_name** | **str** |  | 
**min_occupancy** | **int** |  | 
**max_occupancy** | **int** |  | 
**max_adult_occupancy** | **int** |  | 
**max_child_occupancy** | **int** |  | 
**included_adult_occupancy** | **int** |  | 
**included_child_occupancy** | **int** |  | 
**base_rate** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**single_occupancy_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | 
**extra_pax_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | 
**extra_child_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | 

## Example

```python
from wink_sdk_channel_manager.models.property_room_rate import PropertyRoomRate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRoomRate from a JSON string
property_room_rate_instance = PropertyRoomRate.from_json(json)
# print the JSON string representation of the object
print(PropertyRoomRate.to_json())

# convert the object into a dict
property_room_rate_dict = property_room_rate_instance.to_dict()
# create an instance of PropertyRoomRate from a dict
property_room_rate_from_dict = PropertyRoomRate.from_dict(property_room_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


