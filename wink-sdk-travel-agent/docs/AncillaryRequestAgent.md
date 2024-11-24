# AncillaryRequestAgent

Extra reservations of spas, meeting rooms etc that should accompany the room type booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_identifier** | **str** | Travel blocking identifier | 
**channel_inventory_identifier** | **str** | Channel blocking identifier | 
**transactional_travel_inventory_identifier** | **str** | Travel blocking identifier | 
**start_date** | **datetime** | Date start time when reservation was made for. | 
**end_date** | **datetime** | Date end time when reservation was made for. | 
**quantity** | **int** | Quantity of the ancillary requested. | [default to 1]
**identifier** | **str** | Ancillary identifier | [optional] 
**type** | **str** | Inventory type | 

## Example

```python
from wink_sdk_travel_agent.models.ancillary_request_agent import AncillaryRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryRequestAgent from a JSON string
ancillary_request_agent_instance = AncillaryRequestAgent.from_json(json)
# print the JSON string representation of the object
print(AncillaryRequestAgent.to_json())

# convert the object into a dict
ancillary_request_agent_dict = ancillary_request_agent_instance.to_dict()
# create an instance of AncillaryRequestAgent from a dict
ancillary_request_agent_from_dict = AncillaryRequestAgent.from_dict(ancillary_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


