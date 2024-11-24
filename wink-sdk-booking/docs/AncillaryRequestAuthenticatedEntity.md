# AncillaryRequestAuthenticatedEntity

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
from wink_sdk_booking.models.ancillary_request_authenticated_entity import AncillaryRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryRequestAuthenticatedEntity from a JSON string
ancillary_request_authenticated_entity_instance = AncillaryRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AncillaryRequestAuthenticatedEntity.to_json())

# convert the object into a dict
ancillary_request_authenticated_entity_dict = ancillary_request_authenticated_entity_instance.to_dict()
# create an instance of AncillaryRequestAuthenticatedEntity from a dict
ancillary_request_authenticated_entity_from_dict = AncillaryRequestAuthenticatedEntity.from_dict(ancillary_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


