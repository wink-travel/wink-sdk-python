# AggregateHotelRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**engine_configuration_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.aggregate_hotel_request_non_authenticated_entity import AggregateHotelRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateHotelRequestNonAuthenticatedEntity from a JSON string
aggregate_hotel_request_non_authenticated_entity_instance = AggregateHotelRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateHotelRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_hotel_request_non_authenticated_entity_dict = aggregate_hotel_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateHotelRequestNonAuthenticatedEntity from a dict
aggregate_hotel_request_non_authenticated_entity_from_dict = AggregateHotelRequestNonAuthenticatedEntity.from_dict(aggregate_hotel_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


