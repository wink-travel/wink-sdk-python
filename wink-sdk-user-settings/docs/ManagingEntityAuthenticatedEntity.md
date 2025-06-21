# ManagingEntityAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The value that should be persisted. | 
**name** | **str** | Text representation of the value. | 
**type** | **str** | Type of entity. | 
**sub_type** | **str** | This is for Wink entities only. Does not apply to TripPay. | 
**price_lookup_key** | **str** | price lookup key | [optional] 

## Example

```python
from wink_sdk_user_settings.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityAuthenticatedEntity from a JSON string
managing_entity_authenticated_entity_instance = ManagingEntityAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityAuthenticatedEntity.to_json())

# convert the object into a dict
managing_entity_authenticated_entity_dict = managing_entity_authenticated_entity_instance.to_dict()
# create an instance of ManagingEntityAuthenticatedEntity from a dict
managing_entity_authenticated_entity_from_dict = ManagingEntityAuthenticatedEntity.from_dict(managing_entity_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


