# AggregateAddOnRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | User session containing itinerary and other data by the user | 
**customization_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.aggregate_add_on_request_non_authenticated_entity import AggregateAddOnRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateAddOnRequestNonAuthenticatedEntity from a JSON string
aggregate_add_on_request_non_authenticated_entity_instance = AggregateAddOnRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateAddOnRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_add_on_request_non_authenticated_entity_dict = aggregate_add_on_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateAddOnRequestNonAuthenticatedEntity from a dict
aggregate_add_on_request_non_authenticated_entity_from_dict = AggregateAddOnRequestNonAuthenticatedEntity.from_dict(aggregate_add_on_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


