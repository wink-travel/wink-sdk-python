# PropertyRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**property_identifier** | **str** |  | 
**room_rate_identifier** | **str** |  | 
**guest_room_identifier** | **str** |  | 
**rate_plan_identifier** | **str** |  | 
**amount** | **float** |  | 
**currency_code** | **str** |  | 
**master** | **bool** |  | 
**closed_on_arrival** | **bool** |  | 
**closed_on_departure** | **bool** |  | 
**var_date** | **date** |  | 
**quantity** | **int** |  | [optional] 
**min_occupancy** | **int** |  | [optional] 
**max_occupancy** | **int** |  | [optional] 
**min_length_of_stay** | **int** |  | [optional] 
**max_length_of_stay** | **int** |  | [optional] 
**single_occupancy_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.property_rate import PropertyRate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRate from a JSON string
property_rate_instance = PropertyRate.from_json(json)
# print the JSON string representation of the object
print(PropertyRate.to_json())

# convert the object into a dict
property_rate_dict = property_rate_instance.to_dict()
# create an instance of PropertyRate from a dict
property_rate_from_dict = PropertyRate.from_dict(property_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


