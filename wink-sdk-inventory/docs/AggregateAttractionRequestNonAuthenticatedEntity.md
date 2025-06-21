# AggregateAttractionRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | User session containing itinerary and other data by the user | 
**customization_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.aggregate_attraction_request_non_authenticated_entity import AggregateAttractionRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateAttractionRequestNonAuthenticatedEntity from a JSON string
aggregate_attraction_request_non_authenticated_entity_instance = AggregateAttractionRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateAttractionRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_attraction_request_non_authenticated_entity_dict = aggregate_attraction_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateAttractionRequestNonAuthenticatedEntity from a dict
aggregate_attraction_request_non_authenticated_entity_from_dict = AggregateAttractionRequestNonAuthenticatedEntity.from_dict(aggregate_attraction_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


