# PropertyRateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** |  | 
**end_date** | **date** |  | 
**amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**master** | **bool** |  | [optional] 
**closed_on_arrival** | **bool** |  | [optional] 
**closed_on_departure** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**min_length_of_stay** | **int** |  | [optional] 
**max_length_of_stay** | **int** |  | [optional] 
**min_occupancy** | **int** |  | [optional] 
**max_occupancy** | **int** |  | [optional] 
**single_occupancy_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_pax_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 
**extra_child_rate_modifier** | [**VariableCharge**](VariableCharge.md) |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.property_rate_update_request import PropertyRateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRateUpdateRequest from a JSON string
property_rate_update_request_instance = PropertyRateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PropertyRateUpdateRequest.to_json())

# convert the object into a dict
property_rate_update_request_dict = property_rate_update_request_instance.to_dict()
# create an instance of PropertyRateUpdateRequest from a dict
property_rate_update_request_from_dict = PropertyRateUpdateRequest.from_dict(property_rate_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


